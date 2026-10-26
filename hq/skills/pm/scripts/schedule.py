#!/usr/bin/env python3
"""Harmonogram i ścieżka krytyczna (CPM) z tasks.tsv. Użycie: schedule.py [plik=.hq/pm/tasks.tsv] [--start RRRR-MM-DD] [--kal 5|7] | --test
Kolumny TSV (nagłówek opcjonalny): id | tytuł | właściciel | dni | zależy_od (po przecinku) | status (todo/doing/blocked/done) | definicja_ukończenia | typ (zadanie/kamień) | termin (RRRR-MM-DD, opcjonalnie)
Dni = dni robocze (--kal 5, domyślnie) lub kalendarzowe (--kal 7). Zadanie done liczy się jako 0 dni; doing liczy pełne dni (zachowawczo).
Dzień 'koniec' = ostatni dzień pracy zadania; kamień = dzień ostatniego poprzednika."""
import sys, tempfile
from datetime import date, timedelta
from pathlib import Path


def load(text):
    tasks, errs = {}, []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        c = (line.split("\t") + [""] * 9)[:9]
        if not c[3].strip().isdigit():
            if n == 1:
                continue  # nagłówek
            errs.append(f"linia {n}: dni nie jest liczbą: {c[3]!r}")
            continue
        if c[0] in tasks:
            errs.append(f"linia {n}: zdublowane id {c[0]}")
        tasks[c[0]] = dict(id=c[0], title=c[1], owner=c[2].strip(), d=int(c[3]),
                           deps=[x.strip() for x in c[4].split(",") if x.strip()],
                           status=(c[5].strip() or "todo"), dod=c[6].strip(),
                           ms=c[7].strip().startswith("kam"), due=c[8].strip())
    for t in tasks.values():
        for p in t["deps"]:
            if p not in tasks:
                errs.append(f"{t['id']}: nieznana zależność {p}")
    return tasks, errs


def order(tasks):
    indeg = {k: len([p for p in t["deps"] if p in tasks]) for k, t in tasks.items()}
    ready = [k for k, v in indeg.items() if v == 0]
    out = []
    while ready:
        k = ready.pop(0)
        out.append(k)
        for j, t in tasks.items():
            if k in t["deps"]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    ready.append(j)
    if len(out) != len(tasks):
        raise ValueError("cykl w zależnościach: " + ",".join(sorted(set(tasks) - set(out))))
    return out


def wd(start, n, cal):
    d = start
    while cal == 5 and d.weekday() >= 5:
        d += timedelta(1)
    for _ in range(n):
        d += timedelta(1)
        while cal == 5 and d.weekday() >= 5:
            d += timedelta(1)
    return d


def plan(tasks, start, cal=5):
    seq = order(tasks)
    eff = {k: (0 if t["status"] == "done" else t["d"]) for k, t in tasks.items()}
    es, ef = {}, {}
    for k in seq:
        es[k] = max([ef[p] for p in tasks[k]["deps"]], default=0)
        ef[k] = es[k] + eff[k]
    end = max(ef.values(), default=0)
    lf, ls = {}, {}
    for k in reversed(seq):
        succ = [j for j, t in tasks.items() if k in t["deps"]]
        lf[k] = min([ls[j] for j in succ], default=end)
        ls[k] = lf[k] - eff[k]
    rows = []
    for k in seq:
        t, fl = tasks[k], ls[k] - es[k]
        last = wd(start, max(ef[k] - 1, 0), cal)
        first = last if t["d"] == 0 or t["ms"] else wd(start, es[k], cal)
        notes = []
        if t["status"] != "done":
            if not t["ms"] and not t["owner"]:
                notes.append("BRAK WŁAŚCICIELA")
            if not t["ms"] and not t["dod"]:
                notes.append("BRAK DEFINICJI UKOŃCZENIA")
            if t["status"] == "blocked":
                notes.append("ZABLOKOWANE")
            if t["due"]:
                late = (last - date.fromisoformat(t["due"])).days
                if late > 0:
                    notes.append(f"ZAGROŻONY TERMIN +{late}d")
        rows.append(dict(id=k, title=t["title"], owner=t["owner"], d=t["d"], es=es[k], ef=ef[k], float=fl,
                         crit=fl == 0 and t["status"] != "done", first=first, last=last, status=t["status"], notes=notes))
    # przeciążenie: ten sam właściciel, nakładające się zadania
    for o in {r["owner"] for r in rows if r["owner"]}:
        iv = [(r["es"], r["ef"], r["id"]) for r in rows if r["owner"] == o and r["status"] != "done" and r["ef"] > r["es"]]
        for day in sorted({a for a, _, _ in iv}):
            ids = [i for a, b, i in iv if a <= day < b]
            if len(ids) > 1:
                for r in rows:
                    if r["id"] in ids:
                        r["notes"].append(f"PRZECIĄŻENIE {o}: równolegle {','.join(ids)}")
                break
    return rows, end


def render(rows, end, start, cal):
    out = ["id\ttytuł\twłaściciel\tdni\tES\tEF\tluz\tkryt\tstart\tkoniec\tstatus\tuwagi"]
    for r in rows:
        out.append("\t".join(str(x) for x in (r["id"], r["title"], r["owner"], r["d"], r["es"], r["ef"], r["float"],
                                              "*" if r["crit"] else "", r["first"], r["last"], r["status"], "; ".join(dict.fromkeys(r["notes"])))))
    crit = [r["id"] for r in rows if r["crit"]]
    out.append(f"# długość={end} dni, koniec={wd(start, max(end - 1, 0), cal)}, ścieżka krytyczna={' -> '.join(crit)}")
    return "\n".join(out)


def selftest():
    txt = "A\ta\tu\t3\t\ttodo\tx\tzadanie\t\nB\tb\tu\t2\tA\ttodo\tx\tzadanie\t\nC\tc\tw\t4\tA\ttodo\tx\tzadanie\t\nM\tm\t\t0\tB,C\ttodo\t\tkamień\t2026-01-01\n"
    tasks, errs = load(txt)
    assert not errs, errs
    rows, end = plan(tasks, date(2026, 1, 5))  # poniedziałek
    r = {x["id"]: x for x in rows}
    assert end == 7 and r["B"]["float"] == 2 and [x["id"] for x in rows if x["crit"]] == ["A", "C", "M"], (end, rows)
    assert any("PRZECIĄŻENIE u" in n for n in r["A"]["notes"]) is False  # A sama, B i C mają różnych właścicieli? B:u, A:u nie nakładają się
    assert any("ZAGROŻONY TERMIN" in n for n in r["M"]["notes"]), r["M"]["notes"]
    try:
        order(load("X\tx\to\t1\tY\ttodo\td\tzadanie\t\nY\ty\to\t1\tX\ttodo\td\tzadanie\t\n")[0])
        raise SystemExit("cykl nie wykryty")
    except ValueError:
        pass
    print("OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--test" in a:
        selftest()
        sys.exit()
    opt = lambda n, d: a[a.index(n) + 1] if n in a else d
    path = next((x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or not a[i - 1].startswith("--"))), ".hq/pm/tasks.tsv")
    start, cal = date.fromisoformat(opt("--start", date.today().isoformat())), int(opt("--kal", "5"))
    tasks, errs = load(Path(path).read_text())
    if errs:
        sys.exit("BŁĘDY:\n" + "\n".join(errs))
    try:
        rows, end = plan(tasks, start, cal)
    except ValueError as e:
        sys.exit(f"BŁĄD: {e}")
    print(render(rows, end, start, cal))
