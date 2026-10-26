#!/usr/bin/env python3
"""Lejek partnerstw i sponsoringu z pipeline.tsv. Użycie: pipeline.py [plik=.hq/partners/pipeline.tsv] | --test
Kolumny (nagłówek opcjonalny): id | organizacja | kontakt_rola | etap | wartość | prawdop_% | następny_krok | termin_kroku (RRRR-MM-DD) | właściciel | notatki
Etapy: lead, rozmowa, oferta, negocjacje (otwarte), wygrana, przegrana. Prognoza ważona = suma wartość*prawdop% dla otwartych.
Flagi: otwarta szansa bez następnego kroku lub terminu, termin kroku przeterminowany, brak roli kontaktu (decydent?), brak właściciela, prawdop% poza 0-100.
Kod wyjścia 1 przy flagach."""
import sys
from datetime import date
from decimal import Decimal as D
from pathlib import Path

OPEN = ("lead", "rozmowa", "oferta", "negocjacje")


def analyze(text, today=None):
    today = today or date.today()
    deals, flags = [], []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        c = (line.split("\t") + [""] * 10)[:10]
        try:
            val, pr = D(c[4].replace(",", ".").strip()), D(c[5].strip() or "0")
        except Exception:
            if n == 1:
                continue  # nagłówek
            flags.append(f"linia {n}: wartość/prawdopodobieństwo nie są liczbami")
            continue
        stage, w = c[3].strip().lower(), []
        if not (0 <= pr <= 100):
            w.append("PRAWDOP. POZA 0-100")
        if stage in OPEN:
            if not c[6].strip() or not c[7].strip():
                w.append("BRAK NASTĘPNEGO KROKU LUB TERMINU")
            else:
                try:
                    if date.fromisoformat(c[7].strip()) < today:
                        w.append("TERMIN KROKU PRZETERMINOWANY")
                except ValueError:
                    w.append("ZŁA DATA")
            if not c[2].strip():
                w.append("BRAK ROLI KONTAKTU")
            if not c[8].strip():
                w.append("BRAK WŁAŚCICIELA")
        elif stage not in ("wygrana", "przegrana"):
            w.append(f"NIEZNANY ETAP {stage!r}")
        deals.append((c[0], c[1], stage, val, pr, "; ".join(w)))
        flags += [f"{c[0]} {c[1]}: {x}" for x in w]
    return deals, flags


def render(deals, flags):
    out = ["etap\tilość\twartość\tważona"]
    for st in OPEN + ("wygrana", "przegrana"):
        ds = [d for d in deals if d[2] == st]
        out.append(f"{st}\t{len(ds)}\t{sum(d[3] for d in ds)}\t{sum(d[3] * d[4] / 100 for d in ds) if st in OPEN else ''}")
    out.append(f"# prognoza ważona (otwarte) = {sum(d[3] * d[4] / 100 for d in deals if d[2] in OPEN):.2f}; wygrane = {sum(d[3] for d in deals if d[2] == 'wygrana')}")
    out += [f"# FLAGA {f}" for f in flags]
    return "\n".join(out)


def selftest():
    t = ("A1\tFirma X\tdyrektor marketingu\toferta\t10000\t50\twysłać ofertę\t2099-01-01\tOla\t\n"
         "A2\tFirma Y\t\trozmowa\t4000\t20\t\t\t\t\n"
         "A3\tFirma Z\tprezes\twygrana\t5000\t100\t\t\tTom\t\n"
         "A4\tFirma W\tCEO\tnegocjacje\t8000\t75\tpodpis\t2020-01-01\tOla\t\n")
    deals, flags = analyze(t, date(2026, 1, 1))
    out = render(deals, flags)
    assert "prognoza ważona (otwarte) = 11800.00" in out, out  # 800 + 5000 + 6000
    assert any("A2" in f and "BRAK NASTĘPNEGO KROKU" in f for f in flags), flags
    assert any("A4" in f and "PRZETERMINOWANY" in f for f in flags), flags
    assert not any(f.startswith("A1") or f.startswith("A3") for f in flags), flags
    print("OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        selftest()
        sys.exit()
    path = next((x for x in sys.argv[1:] if not x.startswith("--")), ".hq/partners/pipeline.tsv")
    deals, flags = analyze(Path(path).read_text())
    print(render(deals, flags))
    sys.exit(1 if flags else 0)
