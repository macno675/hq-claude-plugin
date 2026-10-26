#!/usr/bin/env python3
"""Zdrowie kont i terminy odnowień z accounts.tsv (heurystyka, liczy skrypt). Użycie: health.py [plik=.hq/cs/accounts.tsv] [--today RRRR-MM-DD] | --test
Kolumny (nagłówek opcjonalny): id | klient | właściciel | trend_użycia_% | kluczowe_funkcje_% | zgłoszenia_otwarte | satysfakcja_0-10 | odnowienie (RRRR-MM-DD) | zmiana_decydenta (tak/nie) | pierwsza_wartość (tak/nie) | notatki
Wynik 0-100 = 30% adopcja (kluczowe funkcje) + 25% trend użycia + 20% satysfakcja + 15% zgłoszenia + 10% pierwsza wartość; -15 przy zmianie decydenta.
Trend: +10% lub więcej = 100, 0% = 70, -10% = 40, -30% lub mniej = 0 (liniowo). Satysfakcja brak = 60 (neutralnie, flaga). Zgłoszenia otwarte: 0=100, 1=80, 2=60, 3=40, 4=20, 5+=0.
Poziomy: >= 75 zdrowe, 50-74 uwaga, < 50 zagrożone. Wagi i progi to konwencja robocza; dostosuj do swojego produktu i sprawdzaj na historii odejść.
Odnowienie: flaga przy <= 90, 60, 30 dni i po terminie. Kod wyjścia 1 gdy są konta zagrożone lub flagi odnowień."""
import sys
from datetime import date
from pathlib import Path


def clamp(x, lo=0.0, hi=100.0):
    return max(lo, min(hi, x))


def trend_score(t):
    if t >= 10:
        return 100.0
    if t >= 0:
        return 70 + 30 * t / 10
    if t >= -10:
        return 40 + 30 * (t + 10) / 10
    return clamp(40 * (t + 30) / 20)


def analyze(text, today):
    rows, flags = [], []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        c = (line.split("\t") + [""] * 11)[:11]
        try:
            trend, feat, tickets = float(c[3]), float(c[4]), int(float(c[5]))
        except Exception:
            if n == 1:
                continue  # nagłówek
            flags.append(f"linia {n}: trend/funkcje/zgłoszenia nie są liczbami")
            continue
        w = []
        if c[6].strip():
            sat = clamp(float(c[6]) * 10)
        else:
            sat = 60.0
            w.append("BRAK ANKIETY")
        first = 100.0 if c[9].strip().lower() == "tak" else 30.0
        if first < 100:
            w.append("BRAK PIERWSZEJ WARTOŚCI")
        score = 0.30 * clamp(feat) + 0.25 * trend_score(trend) + 0.20 * sat + 0.15 * clamp(100 - 20 * tickets) + 0.10 * first
        if c[8].strip().lower() == "tak":
            score -= 15
            w.append("ZMIANA DECYDENTA")
        score = clamp(score)
        level = "zdrowe" if score >= 75 else "uwaga" if score >= 50 else "zagrożone"
        if c[7].strip():
            try:
                d = (date.fromisoformat(c[7].strip()) - today).days
                if d < 0:
                    w.append(f"ODNOWIENIE PO TERMINIE ({-d}d)")
                elif d <= 90:
                    w.append(f"ODNOWIENIE za {d}d" + (" - PRIORYTET" if level != "zdrowe" and d <= 60 else ""))
            except ValueError:
                w.append("ZŁA DATA ODNOWIENIA")
        else:
            w.append("BRAK DATY ODNOWIENIA")
        rows.append((score, c[0], c[1], c[2], level, "; ".join(w)))
        if level == "zagrożone" or any(x.startswith("ODNOWIENIE") for x in w):
            flags.append(f"{c[0]} {c[1]}: {level}; {'; '.join(w)}")
    rows.sort(key=lambda r: r[0])
    return rows, flags


def selftest():
    t = ("K1\tFirma A\tOla\t12\t90\t0\t9\t2026-06-01\tnie\ttak\t\n"
         "K2\tFirma B\tTom\t-30\t20\t5\t3\t2026-02-15\ttak\tnie\t\n"
         "K3\tFirma C\tOla\t0\t60\t1\t\t2026-01-20\tnie\ttak\t\n")
    rows, flags = analyze(t, date(2026, 1, 1))
    by = {r[1]: r for r in rows}
    assert by["K1"][4] == "zdrowe" and by["K1"][0] > 90, by["K1"]
    assert by["K2"][4] == "zagrożone" and "ZMIANA DECYDENTA" in by["K2"][5] and "PRIORYTET" in by["K2"][5], by["K2"]
    assert "BRAK ANKIETY" in by["K3"][5] and "ODNOWIENIE za 19d" in by["K3"][5], by["K3"]
    assert [r[1] for r in rows][0] == "K2"  # najgorsze pierwsze
    assert not any(f.startswith("K1") for f in flags)
    print("OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--test" in a:
        selftest()
        sys.exit()
    today = date.fromisoformat(a[a.index("--today") + 1]) if "--today" in a else date.today()
    path = next((x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or a[i - 1] != "--today")), ".hq/cs/accounts.tsv")
    rows, flags = analyze(Path(path).read_text(), today)
    print("wynik\tpoziom\tid\tklient\twłaściciel\tuwagi")
    for s, i, k, o, lv, w in rows:
        print(f"{s:.0f}\t{lv}\t{i}\t{k}\t{o}\t{w}")
    for f in flags:
        print(f"# FLAGA {f}")
    sys.exit(1 if flags else 0)
