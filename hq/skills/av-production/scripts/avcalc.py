#!/usr/bin/env python3
"""Kalkulator dźwięku i światła (liczy skrypt, nie model). Użycie: avcalc.py <polecenie> ... | --test
  modes L W H [--c 343]            osiowe tryby własne pomieszczenia [m] -> częstotliwości [Hz]
  rt60 V S:alfa [S:alfa ...]       czas pogłosu (Sabine) V [m3], powierzchnie S [m2] ze współczynnikiem pochłaniania alfa
  spl SPL_1m ODLEGŁOŚĆ_m           spadek poziomu ze źródła punktowego w polu swobodnym (-6 dB na podwojenie odległości)
  lumen N STRUMIEŃ_lm UF MF POW_m2 średnie natężenie [lx] metodą strumienia: E = N*Phi*UF*MF/A
  dmx nazwa:kanały:ilość ...       adresacja DMX (512 kanałów/uniwersum, oprawa nie jest dzielona między uniwersa)
  load NAPIĘCIE nazwa:W:ilość ...  [--pf 0.95]  moc i prąd (jednofazowo; dla kontroli uprawniony elektryk)
Wyniki orientacyjne: rzeczywiste pomieszczenia i instalacje wymagają pomiarów i oceny uprawnionej osoby."""
import math
import sys


def modes(L, W, H, c=343.0):
    rows = [(n * c / (2 * d), name, n) for name, d in (("długość", L), ("szerokość", W), ("wysokość", H)) for n in range(1, 5)]
    return sorted(rows)


def rt60(V, parts):
    A = sum(s * a for s, a in parts)
    if A <= 0:
        raise ValueError("pochłanianie A = 0")
    return 0.161 * V / A, A


def spl(ref, d):
    return ref - 20 * math.log10(d)


def lumen(n, phi, uf, mf, area):
    return n * phi * uf * mf / area


def dmx(items):
    rows, uni, addr = [], 1, 1
    for name, ch, cnt in items:
        if ch > 512:
            raise ValueError(f"{name}: {ch} kanałów > 512")
        for i in range(1, cnt + 1):
            if addr + ch - 1 > 512:
                uni, addr = uni + 1, 1
            rows.append((f"{name}#{i}", uni, addr, addr + ch - 1))
            addr += ch
    return rows


def load(volt, items, pf=1.0):
    w = sum(p * n for _, p, n in items)
    return w, w / (volt * pf)


def pairs(args, ty):
    out = []
    for a in args:
        p = a.split(":")
        out.append(tuple([p[0]] + [ty(x) for x in p[1:]]) if ty is not float else tuple(float(x) for x in p))
    return out


def selftest():
    m = modes(4.0, 3.0, 2.5)
    assert abs(m[0][0] - 42.875) < 1e-9 and m[0][1] == "długość", m[:2]
    t, A = rt60(60, [(30, 0.2), (30, 0.2), (20, 0.4)])  # A = 6+6+8 = 20
    assert abs(A - 20) < 1e-9 and abs(t - 0.161 * 60 / 20) < 1e-9
    assert abs(spl(100, 2) - 93.9794) < 1e-3
    assert abs(lumen(10, 1000, 0.5, 0.8, 20) - 200) < 1e-9
    rows = dmx([("Par", 8, 30), ("Spot", 30, 10)])
    spots = [r for r in rows if r[0].startswith("Spot")]
    assert spots[0][1:] == (1, 241, 270) and spots[8][3] == 510 and spots[9][1:] == (2, 1, 30), spots
    w, a = load(230, [("Par", 150, 10), ("Spot", 300, 4)], 1.0)
    assert w == 2700 and abs(a - 2700 / 230) < 1e-9
    print("OK")


def main(a):
    cmd, r = a[0], a[1:]
    opt = lambda n, d: float(r[r.index(n) + 1]) if n in r else d
    if cmd == "modes":
        L, W, H = map(float, r[:3])
        print("f_Hz\twymiar\trząd")
        for f, name, n in modes(L, W, H, opt("--c", 343.0)):
            print(f"{f:.1f}\t{name}\t{n}")
    elif cmd == "rt60":
        t, A = rt60(float(r[0]), pairs(r[1:], float))
        print(f"RT60={t:.2f} s (Sabine; A={A:.1f} m2 sabin) - szacunek, zmierz pomieszczenie")
    elif cmd == "spl":
        print(f"{spl(float(r[0]), float(r[1])):.1f} dB SPL")
    elif cmd == "lumen":
        print(f"E={lumen(*map(float, r[:5])):.0f} lx (średnie, bez rozkładu i olśnienia)")
    elif cmd == "dmx":
        print("oprawa\tuniwersum\tstart\tkoniec")
        for row in dmx([(p[0], int(p[1]), int(p[2])) for p in (x.split(":") for x in r)]):
            print("\t".join(map(str, row)))
    elif cmd == "load":
        items = [(p[0], float(p[1]), int(p[2])) for p in (x.split(":") for x in r[1:] if not x.startswith("--") and ":" in x)]
        w, i = load(float(r[0]), items, opt("--pf", 1.0))
        print(f"moc={w:.0f} W, prąd={i:.1f} A (zapas i dobór zabezpieczeń: uprawniony elektryk)")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--test":
        selftest()
    else:
        main(sys.argv[1:])
