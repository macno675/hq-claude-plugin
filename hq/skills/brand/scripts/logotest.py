#!/usr/bin/env python3
"""Test logo SVG. Użycie: logotest.py plik.svg [--sheet arkusz.html] | --test
Lint (TSV: poziom, reguła, uwaga) + opcjonalny arkusz HTML: 16/24/32/64/128 px, czarne/białe, jasne/ciemne tło."""
import re, sys

RULES = [  # (regex, poziom, reguła, uwaga)
    (r"<image\b|data:image", "BLAD", "raster", "obraz rastrowy w SVG - odtwórz jako wektor"),
    (r"<(linear|radial)Gradient|<pattern\b", "UWAGA", "gradient", "znak nie przeżyje druku jednokolorowego, grawerunku, haftu"),
    (r"<filter\b|filter=|<feDropShadow|<mask\b", "UWAGA", "efekt", "cień/filtr/maska - usuń z głównego znaku"),
    (r"<text\b", "UWAGA", "tekst", "tekst nieobrysowany - w finale zamień na krzywe, sprawdź licencję fontu"),
    (r"(?<![-\w])(fill|stroke)-opacity|(?<![-\w])opacity=", "UWAGA", "przezroczystość", "znaczenie nie może zależeć od przezroczystości"),
]


def lint(svg):
    out = []
    if not re.search(r"viewBox=", svg):
        out.append(("BLAD", "viewBox", "brak viewBox - znak się nie przeskaluje"))
    for rx, lvl, name, note in RULES:
        if re.search(rx, svg):
            out.append((lvl, name, note))
    cols = {c.lower() for c in re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b", svg)}
    if len(cols) > 3:
        out.append(("UWAGA", "kolory", f"{len(cols)} kolorów - nowoczesne logo: 1 główny + 1 pomocniczy + neutralne"))
    if len(svg) > 20000:
        out.append(("UWAGA", "rozmiar", f"{len(svg)} B - zbyt wiele punktów, uprość"))
    return out


def sheet(svg):
    cell = lambda bg, fg, px, mono: (
        f'<div style="background:{bg};padding:12px;display:inline-block;margin:4px">'
        f'<div style="width:{px}px;height:{px}px;{"filter:" + fg + ";" if mono else ""}">{svg}</div>'
        f'<small style="color:{"#888"}">{px}px</small></div>')
    rows = ""
    for title, bg, mono in (("kolor, jasne tło", "#fff", ""), ("kolor, ciemne tło", "#111", ""),
                            ("czarne na jasnym", "#fff", "brightness(0)"), ("białe na ciemnym", "#111", "brightness(0) invert(1)")):
        rows += f"<h3 style='font:600 14px sans-serif;margin:16px 4px 0'>{title}</h3>" + "".join(
            cell(bg, mono, px, bool(mono)) for px in (16, 24, 32, 64, 128))
    return f"<!doctype html><meta charset=utf-8><title>Test logo</title><style>svg{{width:100%;height:100%}}</style>{rows}"


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--test"]:
        assert [r[1] for r in lint("<svg><image href='x'/></svg>")][:2] == ["viewBox", "raster"]
        assert lint('<svg viewBox="0 0 1 1"><path fill="#000"/></svg>') == []
        assert "128px" in sheet("<svg/>")
        print("OK")
        sys.exit()
    if not a or not a[0].endswith(".svg"):
        sys.exit(__doc__)
    svg = open(a[0], encoding="utf-8").read()
    res = lint(svg)
    print("poziom\treguła\tuwaga")
    for r in res:
        print("\t".join(r))
    print("OK: brak uwag" if not res else f"{len(res)} uwag(i)")
    if "--sheet" in a:
        open(a[a.index("--sheet") + 1], "w", encoding="utf-8").write(sheet(svg))
    sys.exit(1 if any(r[0] == "BLAD" for r in res) else 0)
