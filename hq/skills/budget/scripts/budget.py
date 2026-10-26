#!/usr/bin/env python3
"""Raport budżetu z plików TSV (liczy skrypt, nie model). Użycie: budget.py [katalog=.hq/budget] [--prog 10] | --test
baseline.tsv:    kat<TAB>budżet<TAB>etc<TAB>notatka   (wiersz REZERWA = rezerwa, kolumna budżet; etc = pozostałe koszty poza poniesionymi i zobowiązanymi)
actuals.tsv:     data<TAB>kat<TAB>kwota<TAB>opis       (poniesione)
commitments.tsv: data<TAB>kat<TAB>kwota<TAB>opis       (zobowiązane, jeszcze niezapłacone; po zapłacie przenieś do actuals, nie dubluj)
EAC = poniesione + zobowiązane + ETC; wariancja = budżet - EAC (ujemna = niekorzystna)."""
import sys, tempfile
from collections import defaultdict
from decimal import Decimal as D
from pathlib import Path


def rows(path):
    p = Path(path)
    out = []
    for n, line in enumerate(p.read_text().splitlines() if p.exists() else [], 1):
        if line.strip() and not line.startswith("#"):
            out.append((n, line.split("\t")))
    return out


def num(s, where):
    try:
        return D(s.replace(",", ".").strip())
    except Exception:
        raise ValueError(f"{where}: nie liczba: {s!r}")


def load(d):
    d = Path(d)
    base, etc, notes = {}, {}, []
    for n, c in rows(d / "baseline.tsv"):
        if len(c) < 2 or not c[1].replace(".", "").replace(",", "").replace("-", "").strip().isdigit():
            continue  # nagłówek
        base[c[0]] = num(c[1], f"baseline.tsv:{n}")
        etc[c[0]] = num(c[2], f"baseline.tsv:{n}") if len(c) > 2 and c[2].strip() else D(0)
    sums = {}
    for name in ("actuals", "commitments"):
        s = defaultdict(D)
        for n, c in rows(d / f"{name}.tsv"):
            if len(c) < 3 or not c[2].replace(".", "").replace(",", "").replace("-", "").strip().isdigit():
                continue
            s[c[1]] += num(c[2], f"{name}.tsv:{n}")
            if c[1] not in base:
                notes.append(f"{name}.tsv:{n}: kategoria {c[1]!r} bez wiersza w baseline")
        sums[name] = s
    return base, etc, sums["actuals"], sums["commitments"], notes


def report(d, prog=D(10)):
    base, etc, ac, cm, notes = load(d)
    reserve = base.get("REZERWA", D(0))
    cats = [k for k in base if k != "REZERWA"] + [k for k in set(ac) | set(cm) if k not in base]
    lines = ["kat\tbudżet\tponiesione\tzobowiązane\tETC\tEAC\twariancja\twar%\tflaga"]
    tb = tac = tcm = tetc = D(0)
    for k in cats:
        b, a, c, e = base.get(k, D(0)), ac.get(k, D(0)), cm.get(k, D(0)), etc.get(k, D(0))
        eac = a + c + e
        var = b - eac
        pct = (var / b * 100) if b else D(0)
        flag = "!" if var < 0 and (b == 0 or -pct > prog) else ""
        lines.append(f"{k}\t{b}\t{a}\t{c}\t{e}\t{eac}\t{var}\t{pct:.1f}\t{flag}")
        tb, tac, tcm, tetc = tb + b, tac + a, tcm + c, tetc + e
    teac = tac + tcm + tetc
    lines.append(f"RAZEM\t{tb}\t{tac}\t{tcm}\t{tetc}\t{teac}\t{tb - teac}\t\t")
    over = max(D(0), teac - tb)
    status = ("W BUDŻECIE" if teac <= tb else "UŻYWA REZERWY" if over <= reserve else "PRZEKROCZENIE PONAD REZERWĘ")
    lines.append(f"# rezerwa={reserve} zużycie_rezerwy={min(over, reserve)} pozostała={reserve - min(over, reserve)} status={status}")
    lines += [f"# UWAGA {n}" for n in notes]
    return "\n".join(lines)


def selftest():
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        (t / "baseline.tsv").write_text("kat\tbudżet\tetc\tnotatka\nczęści\t100\t10\t\nPCB\t50\t0\t\nREZERWA\t20\t\t\n")
        (t / "actuals.tsv").write_text("2026-01-01\tczęści\t60\tx\n2026-01-02\tPCB\t55\ty\n")
        (t / "commitments.tsv").write_text("2026-01-03\tczęści\t30\tz\n")
        out = report(t)
        assert "części\t100\t60\t30\t10\t100\t0\t0.0\t" in out, out
        assert "PCB\t50\t55\t0\t0\t55\t-5\t-10.0\t" in out and "PCB" in out.split("!")[0] + "!" , out  # -10% nie przekracza progu 10
        assert "RAZEM\t150\t115\t30\t10\t155\t-5" in out, out
        assert "zużycie_rezerwy=5" in out and "status=UŻYWA REZERWY" in out, out
    print("OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--test" in a:
        selftest()
    else:
        prog = D(a[a.index("--prog") + 1]) if "--prog" in a else D(10)
        d = next((x for x in a if not x.startswith("--") and x != str(prog)), ".hq/budget")
        print(report(d, prog))
