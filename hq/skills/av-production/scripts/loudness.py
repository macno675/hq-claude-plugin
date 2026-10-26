#!/usr/bin/env python3
"""Pomiar głośności pliku audio/wideo (EBU R128) przez ffmpeg. Użycie: loudness.py plik [--target LUFS] [--tp dBTP] | --test
Wypisuje TSV: plik, LUFS zintegrowane, LRA, true peak. Opcje --target/--tp porównują z wymaganiem dostawy,
które musisz podać z aktualnej specyfikacji platformy (skrypt nie zgaduje celów). Wymaga ffmpeg."""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def measure(path):
    if not shutil.which("ffmpeg"):
        sys.exit("Brak ffmpeg w PATH")
    p = subprocess.run(["ffmpeg", "-nostats", "-hide_banner", "-i", str(path), "-filter_complex", "ebur128=peak=true",
                        "-f", "null", "-"], capture_output=True, text=True)
    s = p.stderr
    summary = s[s.rfind("Summary:"):] if "Summary:" in s else ""
    g = lambda pat: (re.findall(pat, summary) or [None])[-1]
    i, lra, tp = g(r"I:\s+(-?[\d.]+|-inf) LUFS"), g(r"LRA:\s+([\d.]+) LU"), g(r"Peak:\s+(-?[\d.]+|-inf) dBFS")
    if i is None:
        sys.exit("Nie udało się odczytać pomiaru:\n" + s[-500:])
    return float(i), float(lra), float(tp)


def selftest():
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "t.wav"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "lavfi", "-i", "sine=frequency=1000:duration=5",
                        "-af", "volume=-6dB", str(f)], check=True)
        i, lra, tp = measure(f)
        assert -60 < i < 0 and 0 <= lra < 5 and -40 < tp < 0, (i, lra, tp)
    print("OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "--test":
        selftest()
        sys.exit()
    opt = lambda n: float(a[a.index(n) + 1]) if n in a else None
    i, lra, tp = measure(a[0])
    print("plik\tLUFS\tLRA\ttrue_peak_dBTP")
    print(f"{a[0]}\t{i}\t{lra}\t{tp}")
    t, ceiling = opt("--target"), opt("--tp")
    if t is not None:
        print(f"# głośność {'OK' if abs(i - t) <= 1.0 else 'POZA'} względem {t} LUFS (tolerancja +/-1 LU, dostosuj do specyfikacji)")
    if ceiling is not None:
        print(f"# true peak {'OK' if tp <= ceiling else 'PRZEKROCZONY'} względem {ceiling} dBTP")
