#!/usr/bin/env python3
"""Audyt marki w kodzie i plikach (liczy skrypt, nie model).
Użycie: brandscan.py KATALOG --brand PLIK [--brand PLIK ...] [--fonts "Inter,Lora"] [--top 40] | --test
  --brand  pliki z paletą (brandbook.md, profil projektu, tokens.css); bierze z nich wszystkie kolory HEX.
  --fonts  dozwolone rodziny fontów; bez tej opcji bierze nazwy z linii `--font...:` w plikach --brand.
Wynik TSV: rodzaj, wartość, wystąpienia, najbliższy_kolor_marki, deltaE, status, przykład (plik:linia).
Status: MARKA (dokładnie kolor marki) | DRYF (dE<6, prawie marka: zamień na token) | OBCY (dE>=6) | FONT_OK | FONT_OBCY.
"""
import os, re, sys

EXT = {".css", ".scss", ".sass", ".less", ".html", ".htm", ".js", ".jsx", ".ts", ".tsx", ".vue",
       ".svelte", ".svg", ".astro", ".json", ".xml", ".kt", ".swift", ".dart"}
SKIP = {"node_modules", ".git", "dist", "build", ".next", "out", "vendor", "coverage", ".hq", ".venv", "venv", "__pycache__"}
HEX = re.compile(r"(?<![\w&])#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b")
RGB = re.compile(r"rgba?\(\s*(\d{1,3})[\s,]+(\d{1,3})[\s,]+(\d{1,3})")
FONT = re.compile(r"font-family\s*[:=]\s*['\"]?([^;'\"}\n]+)", re.I)
GENERIC = {"serif", "sans-serif", "monospace", "system-ui", "inherit", "initial", "cursive", "ui-sans-serif",
           "ui-serif", "ui-monospace", "-apple-system", "blinkmacsystemfont", "emoji", "math", "fantasy", "unset"}


def norm(h):
    h = h.lower()
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h[:3])
    return "#" + h[:6]


def lab(h):
    rgb = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    rgb = [((c + 0.055) / 1.055) ** 2.4 if c > 0.04045 else c / 12.92 for c in rgb]
    x = (rgb[0] * 0.4124 + rgb[1] * 0.3576 + rgb[2] * 0.1805) / 0.95047
    y = rgb[0] * 0.2126 + rgb[1] * 0.7152 + rgb[2] * 0.0722
    z = (rgb[0] * 0.0193 + rgb[1] * 0.1192 + rgb[2] * 0.9505) / 1.08883
    f = [t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116 for t in (x, y, z)]
    return 116 * f[1] - 16, 500 * (f[0] - f[1]), 200 * (f[1] - f[2])


def de(a, b):  # shortcut: CIE76, wystarcza do wykrycia dryfu; CIEDE2000 gdy potrzebna precyzja druku
    return sum((p - q) ** 2 for p, q in zip(lab(a), lab(b))) ** 0.5


def palette(files):
    cols, fonts = [], []
    for f in files:
        t = open(f, encoding="utf-8", errors="ignore").read()
        cols += [norm(m) for m in HEX.findall(t)]
        fonts += [v.strip().strip("'\"") for v in re.findall(r"--font[\w-]*\s*:\s*([^;\n]+)", t)]
    fam = {x.strip().strip("'\"").lower() for v in fonts for x in v.split(",")} - GENERIC
    return sorted(set(cols)), fam


def scan(root):
    seen = {}
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP and not x.startswith(".")]
        for fn in files:
            if os.path.splitext(fn)[1].lower() not in EXT or fn.endswith(".min.js") or fn.endswith(".min.css"):
                continue
            p = os.path.join(d, fn)
            try:
                lines = open(p, encoding="utf-8", errors="ignore").read().splitlines()
            except OSError:
                continue
            for i, line in enumerate(lines, 1):
                if len(line) > 2000:  # zminifikowane / dane binarne
                    continue
                where = f"{os.path.relpath(p, root)}:{i}"
                vals = [("kolor", norm(h)) for h in HEX.findall(line)]
                vals += [("kolor", "#%02x%02x%02x" % tuple(min(255, int(c)) for c in m)) for m in RGB.findall(line)]
                for v in FONT.findall(line):
                    vals += [("font", x.strip().strip("'\"")) for x in v.split(",") if x.strip()]
                for k in vals:
                    n, ex = seen.get(k, (0, where))
                    seen[k] = (n + 1, ex)
    return seen


def analyze(root, brand_files, fonts=None):
    pal, fam = palette(brand_files)
    if fonts:
        fam = {f.strip().lower() for f in fonts.split(",") if f.strip()}
    rows = []
    for (kind, val), (n, ex) in scan(root).items():
        if kind == "kolor":
            if pal:
                near = min(pal, key=lambda c: de(val, c))
                d = de(val, near)
                st = "MARKA" if val == near else "DRYF" if d < 6 else "OBCY"
            else:
                near, d, st = "-", 0.0, "BRAK_PALETY"
            rows.append(("kolor", val, n, near, round(d, 1), st, ex))
        else:
            low = val.lower()
            if low in GENERIC or low.startswith("var("):
                continue
            rows.append(("font", val, n, "-", 0.0, "FONT_OK" if not fam or low in fam else "FONT_OBCY", ex))
    order = {"OBCY": 0, "FONT_OBCY": 0, "DRYF": 1, "BRAK_PALETY": 2, "MARKA": 3, "FONT_OK": 3}
    rows.sort(key=lambda r: (order[r[5]], -r[2]))
    return rows, pal, fam


def main(a):
    if not a or a[0] in ("-h", "--help"):
        sys.exit(__doc__)
    root, brand, fonts, top = a[0], [], None, 40
    i = 1
    while i < len(a):
        if a[i] == "--brand":
            brand.append(a[i + 1]); i += 2
        elif a[i] == "--fonts":
            fonts = a[i + 1]; i += 2
        elif a[i] == "--top":
            top = int(a[i + 1]); i += 2
        else:
            sys.exit(f"Nieznana opcja: {a[i]}")
    for f in brand:
        if not os.path.isfile(f):
            sys.exit(f"Brak pliku marki: {f}")
    rows, pal, fam = analyze(root, brand, fonts)
    print("rodzaj\twartość\twystąpienia\tnajbliższy\tdeltaE\tstatus\tprzykład")
    for r in rows[:top]:
        print("\t".join(map(str, r)))
    cnt = {}
    for r in rows:
        cnt[r[5]] = cnt.get(r[5], 0) + r[2]
    print(f"# paleta marki: {len(pal)} kolorów, fonty: {', '.join(sorted(fam)) or 'brak (podaj --fonts)'}"
          f" | unikalnych wartości: {len(rows)} (pokazano {min(top, len(rows))}) | wystąpienia: "
          + ", ".join(f"{k}={v}" for k, v in sorted(cnt.items())))


def selftest():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "src")); os.makedirs(os.path.join(d, "node_modules"))
        b = os.path.join(d, "brand.md")
        open(b, "w").write("| primary | #1A73E8 |\n| ink | #111111 |\n--font-sans: 'Inter', sans-serif;\n")
        open(os.path.join(d, "src", "a.css"), "w").write(
            ".a{color:#1a73e8;background:#1b74e9}\n.b{color:#ff0000;font-family:'Comic Sans MS',sans-serif}\n"
            ".c{color:rgb(17,17,17);font-family:Inter}\n")
        open(os.path.join(d, "node_modules", "x.css"), "w").write(".z{color:#00ff00}")
        rows, pal, fam = analyze(d, [b])
        st = {r[1]: r[5] for r in rows}
        assert pal == ["#111111", "#1a73e8"] and fam == {"inter"}, (pal, fam)
        assert st["#1a73e8"] == "MARKA" and st["#111111"] == "MARKA", st
        assert st["#1b74e9"] == "DRYF" and st["#ff0000"] == "OBCY", st
        assert st["Comic Sans MS"] == "FONT_OBCY" and st["Inter"] == "FONT_OK", st
        assert "#00ff00" not in st and rows[0][5] in ("OBCY", "FONT_OBCY"), rows
        assert dict((r[1], r[6]) for r in rows)["#ff0000"] == "src/a.css:2"
    print("OK")


if __name__ == "__main__":
    selftest() if "--test" in sys.argv else main(sys.argv[1:])
