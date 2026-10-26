#!/usr/bin/env python3
"""Kalkulator marketingowy (liczy skrypt, nie model). Użycie: mkcalc.py <polecenie> ... | --test
  kpi KOSZT WYŚWIETLENIA KLIKNIĘCIA KONWERSJE [PRZYCHÓD]   CTR, CPC, CPM, współczynnik konwersji, koszt konwersji (CPA), ROAS, ROI
  abtest N_A KONW_A N_B KONW_B                              test dwóch proporcji (przybliżenie normalne): różnica, lift, z, p
  samplesize ODSETEK_BAZOWY MDE_BEZWZGL [--alpha 0.05] [--power 0.8]   minimalna liczba obserwacji na wariant (np. samplesize 0.10 0.02)
Wnioski z A/B: p < 0,05 to wskazówka, nie dowód; potrzebna odpowiednia liczba obserwacji i test zaplanowany z góry (bez zaglądania i zatrzymywania po drodze)."""
import math
import sys
from statistics import NormalDist


def kpi(cost, imp, clicks, conv, revenue=None):
    r = {"CTR_%": 100 * clicks / imp if imp else None, "CPC": cost / clicks if clicks else None,
         "CPM": 1000 * cost / imp if imp else None, "CVR_%": 100 * conv / clicks if clicks else None,
         "CPA": cost / conv if conv else None}
    if revenue is not None:
        r["ROAS"] = revenue / cost if cost else None
        r["ROI_%"] = 100 * (revenue - cost) / cost if cost else None
    return r


def abtest(na, ca, nb, cb):
    pa, pb = ca / na, cb / nb
    pool = (ca + cb) / (na + nb)
    se = math.sqrt(pool * (1 - pool) * (1 / na + 1 / nb))
    z = (pb - pa) / se if se else 0.0
    p = math.erfc(abs(z) / math.sqrt(2))
    return pa, pb, (pb - pa) / pa * 100 if pa else None, z, p


def samplesize(base, mde_abs, alpha=0.05, power=0.8):
    """Obserwacje na wariant, test dwustronny dwóch proporcji; base = bazowy odsetek (0-1), mde_abs = minimalna wykrywalna różnica bezwzględna."""
    nd = NormalDist()
    p1, p2 = base, base + mde_abs
    pbar = (p1 + p2) / 2
    za, zb = nd.inv_cdf(1 - alpha / 2), nd.inv_cdf(power)
    num = (za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / mde_abs ** 2)


def selftest():
    assert 3700 < samplesize(0.10, 0.02) < 4000, samplesize(0.10, 0.02)
    assert samplesize(0.10, 0.01) > 3 * samplesize(0.10, 0.02)
    r = kpi(500, 100000, 2000, 100, 2000)
    assert abs(r["CTR_%"] - 2.0) < 1e-9 and abs(r["CPC"] - 0.25) < 1e-9 and abs(r["CPA"] - 5.0) < 1e-9
    assert abs(r["ROAS"] - 4.0) < 1e-9 and abs(r["ROI_%"] - 300.0) < 1e-9 and abs(r["CPM"] - 5.0) < 1e-9
    pa, pb, lift, z, p = abtest(1000, 100, 1000, 130)
    assert 2.0 < z < 2.2 and 0.03 < p < 0.04 and abs(lift - 30.0) < 1e-9, (z, p)
    assert abtest(1000, 100, 1000, 101)[4] > 0.5
    print("OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "--test":
        selftest()
    elif a[0] == "kpi":
        v = list(map(float, a[1:]))
        for k, x in kpi(*v).items():
            print(f"{k}\t{'-' if x is None else round(x, 2)}")
    elif a[0] == "abtest":
        na, ca, nb, cb = map(float, a[1:5])
        pa, pb, lift, z, p = abtest(na, ca, nb, cb)
        print(f"A={pa * 100:.2f}% B={pb * 100:.2f}% lift={'-' if lift is None else f'{lift:.1f}%'} z={z:.2f} p={p:.4f}")
        print("# p < 0,05: wskazówka różnicy; sprawdź wielkość próby i czy test był zaplanowany z góry" if p < 0.05 else "# brak istotnej różnicy przy tej próbie (nie znaczy, że różnicy nie ma)")
    elif a[0] == "samplesize":
        base, mde = float(a[1]), float(a[2])
        alpha = float(a[a.index("--alpha") + 1]) if "--alpha" in a else 0.05
        power = float(a[a.index("--power") + 1]) if "--power" in a else 0.8
        n = samplesize(base, mde, alpha, power)
        print(f"{n} obserwacji na wariant ({2 * n} łącznie); bazowo {base * 100:.1f}% -> {(base + mde) * 100:.1f}%, alfa={alpha}, moc={power}")
    else:
        sys.exit(__doc__)
