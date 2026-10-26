#!/usr/bin/env python3
"""Prognoza przepływów pieniężnych z cashflow.tsv (liczy skrypt, nie model). Użycie:
  cashflow.py PLIK --cash STAN_POCZĄTKOWY [--min PRÓG_GOTÓWKI] | --test
  cashflow.py ccc DSO DIO DPO                       cykl konwersji gotówki = DSO + DIO - DPO (dni)
Kolumny TSV (nagłówek opcjonalny): data (RRRR-MM-DD) | typ (wpływ/wydatek) | kategoria | kwota | pewność_% | opis
Scenariusze: realistyczny = wpływy x pewność%, wydatki 100%; pesymistyczny = tylko wpływy z pewnością >= 90%, wydatki 100%;
optymistyczny = wpływy 100%, wydatki 100%. Wyjście: stan gotówki na koniec każdego miesiąca w 3 scenariuszach; flagi: pierwszy miesiąc poniżej progu i poniżej zera.
To scenariusze z podanych założeń, nie prognoza; pewność% wpływów to Twoja ocena, nie fakt."""
import sys
from collections import defaultdict
from decimal import Decimal as D
from pathlib import Path


def load(text):
    items, errs = [], []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        c = (line.split("\t") + [""] * 6)[:6]
        try:
            amount, conf = D(c[3].replace(",", ".").strip()), D(c[4].strip() or "100")
        except Exception:
            if n == 1:
                continue  # nagłówek
            errs.append(f"linia {n}: kwota/pewność nie są liczbami")
            continue
        kind = c[1].strip().lower()
        if kind not in ("wpływ", "wplyw", "wydatek") or len(c[0].strip()) < 7:
            errs.append(f"linia {n}: zły typ lub data ({c[0]!r}, {c[1]!r})")
            continue
        items.append((c[0].strip()[:7], "in" if kind.startswith("wp") else "out", amount, conf))
    return items, errs


def forecast(items, cash, minimum=D(0)):
    months = sorted({m for m, *_ in items})
    res = {}
    for name, f_in in (("realistyczny", lambda a, p: a * p / 100), ("pesymistyczny", lambda a, p: a if p >= 90 else D(0)), ("optymistyczny", lambda a, p: a)):
        bal, rows, below, neg = D(cash), [], None, None
        net = defaultdict(D)
        for m, k, a, p in items:
            net[m] += f_in(a, p) if k == "in" else -a
        for m in months:
            bal += net[m]
            rows.append((m, bal))
            if below is None and bal < minimum:
                below = m
            if neg is None and bal < 0:
                neg = m
        res[name] = (rows, below, neg)
    return months, res


def selftest():
    t = ("2026-01-10\twydatek\tpłace\t6000\t100\t\n2026-01-15\twpływ\tfaktura A\t5000\t100\t\n"
         "2026-02-10\twydatek\tpłace\t6000\t100\t\n2026-02-20\twpływ\tfaktura B\t10000\t50\t\n"
         "2026-03-10\twydatek\tpłace\t6000\t100\t\n")
    items, errs = load(t)
    assert not errs, errs
    months, r = forecast(items, 4000, D(1000))
    real = dict(r["realistyczny"][0])
    assert real["2026-01"] == 3000 and real["2026-02"] == 2000 and real["2026-03"] == -4000, real
    pes = dict(r["pesymistyczny"][0])
    assert pes["2026-02"] == -3000 and r["pesymistyczny"][1] == "2026-02" and r["pesymistyczny"][2] == "2026-02"
    assert r["realistyczny"][1] == "2026-03" and r["realistyczny"][2] == "2026-03"
    assert dict(r["optymistyczny"][0])["2026-03"] == 4000 + (5000 - 6000) + (10000 - 6000) - 6000  # 1000
    print("OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "--test":
        selftest()
    elif a[0] == "ccc":
        dso, dio, dpo = map(float, a[1:4])
        print(f"cykl konwersji gotówki = {dso + dio - dpo:.0f} dni (DSO {dso:.0f} + DIO {dio:.0f} - DPO {dpo:.0f})")
    else:
        cash = D(a[a.index("--cash") + 1])
        minimum = D(a[a.index("--min") + 1]) if "--min" in a else D(0)
        items, errs = load(Path(a[0]).read_text())
        if errs:
            sys.exit("BŁĘDY:\n" + "\n".join(errs))
        months, res = forecast(items, cash, minimum)
        print("miesiąc\t" + "\t".join(res))
        for i, m in enumerate(months):
            print(m + "\t" + "\t".join(f"{res[s][0][i][1]:.0f}" for s in res))
        for s, (_, below, neg) in res.items():
            if neg:
                print(f"# UWAGA {s}: gotówka poniżej zera w {neg}")
            elif below:
                print(f"# UWAGA {s}: poniżej progu {minimum} w {below}")
        sys.exit(1 if any(v[1] or v[2] for v in res.values()) else 0)
