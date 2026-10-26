#!/usr/bin/env python3
"""Kontrola scenariusza wydarzenia (run of show). Użycie: runofshow.py [plik=.hq/event/ros.tsv] | --test
Kolumny TSV (nagłówek opcjonalny): start (HH:MM) | min | element | odpowiedzialny | sygnał/przejście | plan_awaryjny
Element krytyczny oznacz gwiazdką na początku nazwy (*Otwarcie): wymaga odpowiedzialnego i planu awaryjnego.
Błędy: nakładanie elementów, brak odpowiedzialnego, krytyczny bez planu awaryjnego, zły format. Luki między elementami to informacja.
Kod wyjścia 1 przy błędach."""
import re
import sys
from pathlib import Path


def tm(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)


def hm(x):
    return f"{x // 60 % 24:02d}:{x % 60:02d}"


def check(text):
    out, errs, info, rows = [], [], [], []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        c = (line.split("\t") + [""] * 6)[:6]
        if not re.fullmatch(r"\d{1,2}:\d{2}", c[0].strip()):
            if n == 1:
                continue  # nagłówek
            errs.append(f"linia {n}: zły format startu {c[0]!r} (HH:MM)")
            continue
        if not c[1].strip().isdigit():
            errs.append(f"linia {n}: czas trwania nie jest liczbą: {c[1]!r}")
            continue
        rows.append((n, tm(c[0].strip()), int(c[1]), c[2].strip(), c[3].strip(), c[5].strip()))
    prev_end = None
    for n, s, d, el, owner, plan in rows:
        e = s + d
        notes = []
        if prev_end is not None:
            if s < prev_end:
                errs.append(f"linia {n}: '{el}' zaczyna się {hm(s)}, poprzedni element kończy się {hm(prev_end)} (nakładanie {prev_end - s} min)")
                notes.append("NAKŁADANIE")
            elif s > prev_end:
                info.append(f"luka {s - prev_end} min przed '{el}' ({hm(prev_end)}-{hm(s)})")
        if not owner:
            errs.append(f"linia {n}: '{el}' bez odpowiedzialnego")
            notes.append("BRAK ODPOWIEDZIALNEGO")
        if el.startswith("*") and not plan:
            errs.append(f"linia {n}: element krytyczny '{el}' bez planu awaryjnego")
            notes.append("BRAK PLANU AWARYJNEGO")
        out.append(f"{hm(s)}-{hm(e)}\t{d}\t{el}\t{owner}\t{'; '.join(notes)}")
        prev_end = max(prev_end or 0, e)
    if rows:
        info.append(f"całość: {hm(rows[0][1])}-{hm(prev_end)} ({prev_end - rows[0][1]} min)")
    return out, errs, info


def selftest():
    t = ("10:00\t30\t*Otwarcie\tOla\tgong\tplan B: bez mikrofonu\n"
         "10:30\t15\tPrzerwa\tTom\t\t\n"
         "10:50\t20\tMecz 1\t\t\t\n"
         "11:05\t10\tMecz 2\tAni\t\t\n"
         "11:15\t5\t*Finał\tTom\t\t\n")
    out, errs, info = check(t)
    assert any("luka 5 min" in i for i in info), info
    assert any("Mecz 1" in e and "bez odpowiedzialnego" in e for e in errs), errs
    assert any("nakładanie 5 min" in e for e in errs), errs
    assert any("Finał" in e and "planu awaryjnego" in e for e in errs), errs
    assert not any("Otwarcie" in e for e in errs), errs
    print("OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest()
        sys.exit()
    path = next((x for x in sys.argv[1:] if not x.startswith("--")), ".hq/event/ros.tsv")
    out, errs, info = check(Path(path).read_text())
    print("czas\tmin\telement\todpowiedzialny\tuwagi")
    print("\n".join(out))
    for i in info:
        print(f"# {i}")
    for e in errs:
        print(f"# BŁĄD {e}")
    sys.exit(1 if errs else 0)
