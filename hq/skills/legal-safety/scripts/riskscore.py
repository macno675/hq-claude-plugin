#!/usr/bin/env python3
"""Macierz ryzyka z rejestru TSV. Użycie: riskscore.py [plik=.hq/legal/risks.tsv] | --test
Kolumny (nagłówek opcjonalny): id | ryzyko | kategoria | prawdop (1-5) | wpływ (1-5) | właściciel | środek | status | przegląd_do (RRRR-MM-DD)
Wynik = prawdopodobieństwo x wpływ. Poziomy (konwencja robocza, dostosuj): 1-4 niskie, 5-9 średnie, 10-14 wysokie, 15-25 krytyczne.
Ostrzeżenia: wysokie/krytyczne bez środka lub właściciela, przeterminowany przegląd, wartości poza 1-5. Kod wyjścia 1 gdy są ostrzeżenia."""
import sys
from datetime import date
from pathlib import Path


def level(s):
    return "krytyczne" if s >= 15 else "wysokie" if s >= 10 else "średnie" if s >= 5 else "niskie"


def check(text, today=None):
    today = today or date.today()
    rows, warns = [], []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        c = (line.split("\t") + [""] * 9)[:9]
        if not (c[3].strip().isdigit() and c[4].strip().isdigit()):
            if n == 1:
                continue  # nagłówek
            warns.append(f"linia {n}: prawdopodobieństwo/wpływ nie są liczbami")
            continue
        p, i = int(c[3]), int(c[4])
        if not (1 <= p <= 5 and 1 <= i <= 5):
            warns.append(f"linia {n} ({c[0]}): wartości poza skalą 1-5")
            continue
        s, closed = p * i, c[7].strip().lower() in ("zamknięte", "zamkniete", "closed", "done")
        lv, w = level(s), []
        if not closed:
            if s >= 10 and not c[6].strip():
                w.append("BRAK ŚRODKA")
            if s >= 10 and not c[5].strip():
                w.append("BRAK WŁAŚCICIELA")
            if c[8].strip():
                try:
                    if date.fromisoformat(c[8].strip()) < today:
                        w.append("PRZEGLĄD PRZETERMINOWANY")
                except ValueError:
                    w.append("ZŁA DATA PRZEGLĄDU")
        rows.append((s, c[0], c[1], c[2], p, i, lv, c[5].strip(), c[7].strip(), "; ".join(w)))
        warns += [f"{c[0]}: {x}" for x in w]
    rows.sort(key=lambda r: -r[0])
    return rows, warns


def render(rows, warns):
    out = ["wynik\tpoziom\tid\tryzyko\tkategoria\tP\tW\twłaściciel\tstatus\tuwagi"]
    out += [f"{s}\t{lv}\t{i}\t{t}\t{cat}\t{p}\t{im}\t{o}\t{st}\t{w}" for s, i, t, cat, p, im, lv, o, st, w in rows]
    out.append("# " + ", ".join(f"{k}={sum(1 for r in rows if r[6] == k)}" for k in ("krytyczne", "wysokie", "średnie", "niskie")))
    return "\n".join(out + [f"# OSTRZEŻENIE {w}" for w in warns if "linia" in w])


def selftest():
    t = ("R1\tupadek oprawy\tbezpieczeństwo\t2\t5\tOla\tlinki, kontrola riggera\totwarte\t2099-01-01\n"
         "R2\twyciek danych\tdane\t3\t5\t\t\totwarte\t2020-01-01\n"
         "R3\tdeszcz\tpogoda\t2\t2\tTom\tnamiot\totwarte\t\n")
    rows, warns = check(t, date(2026, 1, 1))
    assert [r[1] for r in rows] == ["R2", "R1", "R3"], rows
    assert rows[0][6] == "krytyczne" and rows[1][6] == "wysokie" and rows[2][6] == "niskie"
    assert any("R2: BRAK ŚRODKA" in w for w in warns) and any("R2: BRAK WŁAŚCICIELA" in w for w in warns)
    assert any("R2: PRZEGLĄD PRZETERMINOWANY" in w for w in warns) and not any(w.startswith("R1") for w in warns)
    print("OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest()
        sys.exit()
    path = next((x for x in sys.argv[1:] if not x.startswith("--")), ".hq/legal/risks.tsv")
    rows, warns = check(Path(path).read_text())
    print(render(rows, warns))
    sys.exit(1 if warns else 0)
