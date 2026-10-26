#!/usr/bin/env python3
"""Kontrast WCAG dla par kolorów. Użycie: contrast.py #RRGGBB #RRGGBB [#RRGGBB ...]
Wypisuje TSV dla każdej pary: ratio, AA tekst, AA duży, AAA tekst."""
import itertools, sys


def lum(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


if __name__ == "__main__":
    assert abs(ratio("#000", "#fff") - 21) < 0.01  # self-check
    cols = sys.argv[1:]
    if len(cols) < 2:
        sys.exit(__doc__)
    print("a\tb\tratio\tAA\tAA_large\tAAA")
    for a, b in itertools.combinations(cols, 2):
        r = ratio(a, b)
        print(f"{a}\t{b}\t{r:.2f}\t{'ok' if r >= 4.5 else 'NIE'}\t{'ok' if r >= 3 else 'NIE'}\t{'ok' if r >= 7 else 'NIE'}")
