#!/usr/bin/env python3
"""Kalkulator IT (liczy skrypt, nie model). Użycie: itcalc.py <polecenie> ... | --test
  tco nazwa:zakup:koszt_roczny:lata[:odsprzedaż[:waty:godz_dzień]] ... [--kwh CENA_ZA_kWh]
      koszt całkowity posiadania i na rok; koszt roczny = serwis, licencje, naprawy; energia z watów i godzin pracy dziennie
  inventory PLIK [--today RRRR-MM-DD] [--warn 90] [--eos 180]
      kontrola ewidencji; kolumny TSV (nagłówek opcjonalny): id | urządzenie | użytkownik | model | zakup | gwarancja_do | koniec_wsparcia | lokalizacja | status | uwagi
      flagi: gwarancja wygasła/wygasa (<= --warn dni), koniec wsparcia producenta minął/zbliża się (<= --eos dni), brak dat; status 'wycofane' pomijany. Kod wyjścia 1 przy flagach."""
import sys
from datetime import date
from pathlib import Path


def tco(items, kwh=0.0):
    out = []
    for name, buy, yearly, years, resale, watts, hours in items:
        energy = watts / 1000 * hours * 365 * kwh
        total = buy + years * (yearly + energy) - resale
        out.append((name, buy, yearly, energy, years, resale, total, total / years))
    return out


def inventory(text, today, warn=90, eos=180):
    rows, flags = [], []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        c = (line.split("\t") + [""] * 10)[:10]
        if n == 1 and not c[5][:1].isdigit() and not c[6][:1].isdigit() and c[5] != "":
            continue  # nagłówek
        if c[8].strip().lower() == "wycofane":
            continue
        w = []
        for label, val, limit in (("GWARANCJA", c[5], warn), ("WSPARCIE PRODUCENTA", c[6], eos)):
            if not val.strip():
                w.append(f"BRAK DATY: {label}")
                continue
            try:
                d = (date.fromisoformat(val.strip()) - today).days
            except ValueError:
                w.append(f"ZŁA DATA: {label}")
                continue
            if d < 0:
                w.append(f"{label} WYGASŁA/KONIEC {-d}d temu")
            elif d <= limit:
                w.append(f"{label} wygasa za {d}d")
        rows.append((c[0], c[1], c[2], c[3], "; ".join(w)))
        flags += [f"{c[0]} {c[1]}: {x}" for x in w]
    return rows, flags


def selftest():
    r = tco([("A", 1000, 100, 4, 200, 100, 8), ("B", 1500, 50, 4, 300, 0, 0)], kwh=1.0)
    assert abs(r[0][3] - 292.0) < 1e-9 and abs(r[0][6] - (1000 + 4 * (100 + 292) - 200)) < 1e-9 and abs(r[1][6] - 1400) < 1e-9, r
    t = ("L1\tlaptop\tOla\tX1\t2023-01-01\t2026-01-20\t2030-01-01\tbiuro\taktywne\t\n"
         "L2\trouter\t\tR\t2019-01-01\t2022-01-01\t2026-02-15\tsala\taktywne\t\n"
         "L3\tstary\t\tS\t2015-01-01\t2016-01-01\t2017-01-01\t\twycofane\t\n"
         "L4\tkamera\tTom\tK\t2025-01-01\t2030-01-01\t\tmagazyn\taktywne\t\n")
    rows, flags = inventory(t, date(2026, 1, 1))
    assert any("L1" in f and "GWARANCJA wygasa za 19d" in f for f in flags), flags
    assert any("L2" in f and "GWARANCJA WYGASŁA" in f for f in flags) and any("L2" in f and "WSPARCIE PRODUCENTA wygasa za 45d" in f for f in flags), flags
    assert not any("L3" in f for f in flags) and any("L4" in f and "BRAK DATY: WSPARCIE" in f for f in flags), flags
    print("OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    opt = lambda n, d: a[a.index(n) + 1] if n in a else d
    if a[0] == "--test":
        selftest()
    elif a[0] == "tco":
        items = []
        for s in (x for x in a[1:] if ":" in x):
            p = s.split(":")
            nums = [float(x) for x in p[1:]] + [0.0] * 6
            items.append((p[0], nums[0], nums[1], nums[2] or 1.0, nums[3], nums[4], nums[5]))
        print("nazwa\tzakup\tkoszt_rocz\tenergia_rocz\tlata\todsprzedaż\tTCO\tTCO_na_rok")
        for r in tco(items, float(opt("--kwh", 0))):
            print("\t".join([r[0]] + [f"{x:.2f}" for x in r[1:4]] + [f"{r[4]:.0f}"] + [f"{x:.2f}" for x in r[5:]]))
    elif a[0] == "inventory":
        today = date.fromisoformat(opt("--today", date.today().isoformat()))
        rows, flags = inventory(Path(a[1]).read_text(), today, int(opt("--warn", 90)), int(opt("--eos", 180)))
        print("id\turządzenie\tużytkownik\tmodel\tuwagi")
        print("\n".join("\t".join(r) for r in rows))
        for f in flags:
            print(f"# FLAGA {f}")
        sys.exit(1 if flags else 0)
    else:
        sys.exit(__doc__)
