#!/usr/bin/env python3
"""Priorytetyzacja backlogu metodą RICE z backlog.tsv. Użycie: prioritize.py [plik=.hq/product/backlog.tsv] | --test
Kolumny (nagłówek opcjonalny): id | pozycja | zasięg | wpływ | pewność_% | nakład | status | notatki
RICE = zasięg * wpływ * (pewność/100) / nakład. Zasięg: ile osób/zdarzeń w okresie; wpływ: np. 0.25 minimalny, 0.5 mały, 1 średni, 2 duży, 3 ogromny; nakład: osobo-dni lub tygodnie (spójnie).
Flagi: pewność < 50% (najpierw zbadaj hipotezę), nakład <= 0, brak liczb. Pozycje done/odrzucone pomijane. To pomoc w rozmowie, nie wyrok: sprawdź zależności, ryzyko i strategię."""
import sys
from decimal import Decimal as D
from pathlib import Path


def score(text):
    rows, flags = [], []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        c = (line.split("\t") + [""] * 8)[:8]
        try:
            reach, imp, conf, eff = (D(c[i].replace(",", ".").strip()) for i in (2, 3, 4, 5))
        except Exception:
            if n == 1:
                continue  # nagłówek
            flags.append(f"linia {n}: brak liczb w zasięgu/wpływie/pewności/nakładzie")
            continue
        if c[6].strip().lower() in ("done", "odrzucone", "zrobione"):
            continue
        w = []
        if eff <= 0:
            flags.append(f"{c[0]} {c[1]}: nakład <= 0")
            continue
        if not (0 <= conf <= 100):
            w.append("PEWNOŚĆ POZA 0-100")
        elif conf < 50:
            w.append("NISKA PEWNOŚĆ - zbadaj hipotezę")
        rice = reach * imp * conf / 100 / eff
        rows.append((rice, c[0], c[1], reach, imp, conf, eff, "; ".join(w)))
        flags += [f"{c[0]} {c[1]}: {x}" for x in w]
    rows.sort(key=lambda r: -r[0])
    return rows, flags


def render(rows, flags):
    out = ["rank\tRICE\tid\tpozycja\tzasięg\twpływ\tpewność_%\tnakład\tuwagi"]
    out += [f"{i}\t{r[0]:.1f}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[6]}\t{r[7]}" for i, r in enumerate(rows, 1)]
    return "\n".join(out + [f"# FLAGA {f}" for f in flags if "linia" in f or "nakład <= 0" in f])


def selftest():
    t = ("F1\trejestracja online\t1000\t2\t80\t4\ttodo\t\n"
         "F2\tpanel wyników\t300\t1\t50\t2\ttodo\t\n"
         "F3\tstatystyki zawodników\t200\t3\t30\t5\ttodo\t\n"
         "F4\tzrobione\t100\t1\t100\t1\tdone\t\n"
         "F5\tzły nakład\t10\t1\t100\t0\ttodo\t\n")
    rows, flags = score(t)
    assert [r[1] for r in rows] == ["F1", "F2", "F3"], rows
    assert abs(float(rows[0][0]) - 400.0) < 1e-9 and abs(float(rows[1][0]) - 75.0) < 1e-9 and abs(float(rows[2][0]) - 36.0) < 1e-9, rows
    assert any("F3" in f and "NISKA PEWNOŚĆ" in f for f in flags) and any("F5" in f and "nakład <= 0" in f for f in flags), flags
    print("OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest()
        sys.exit()
    path = next((x for x in sys.argv[1:] if not x.startswith("--")), ".hq/product/backlog.tsv")
    rows, flags = score(Path(path).read_text())
    print(render(rows, flags))
