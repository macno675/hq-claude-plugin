#!/usr/bin/env python3
"""Płynność i ekonomia jednostkowa (liczy skrypt, nie model). Użycie: runway.py <polecenie> ... | --test
  runway GOTÓWKA KOSZTY_MIES PRZYCHÓD_MIES [--growth % miesięcznie] [--months 36]
      miesięczne spalanie netto i długość runway: bez wzrostu oraz z założonym wzrostem przychodu
  unit CENA KOSZT_ZMIENNY CAC [--months LICZBA_MIESIĘCY_KLIENTA]
      marża na jednostkę, zwrot CAC (w jednostkach/miesiącach sprzedaży), LTV i LTV/CAC gdy podano czas życia klienta
Wyniki to scenariusze z podanych założeń, nie prognoza; ostrożnie z założeniem wzrostu."""
import sys


def runway(cash, costs, revenue, growth=0.0, horizon=36):
    net = costs - revenue
    flat = None if net <= 0 else cash / net
    c, rev, m = cash, revenue, 0
    while m < horizon and c > 0:
        c += rev - costs
        rev *= 1 + growth / 100
        m += 1
        if c <= 0:
            break
    with_growth = None if c > 0 else m
    return net, flat, with_growth, c


def unit(price, var, cac, months=None):
    margin = price - var
    pay = None if margin <= 0 else cac / margin
    ltv = margin * months if months else None
    return margin, margin / price * 100 if price else None, pay, ltv, (ltv / cac if ltv is not None and cac else None)


def selftest():
    net, flat, wg, _ = runway(120000, 20000, 10000)
    assert net == 10000 and abs(flat - 12.0) < 1e-9 and wg == 12, (net, flat, wg)
    net, flat, wg, c = runway(1000, 5000, 6000)
    assert flat is None and wg is None and c > 1000
    _, _, wg2, _ = runway(120000, 20000, 10000, growth=10)
    assert wg2 is None or wg2 > 12, wg2
    m, pct, pay, ltv, r = unit(100, 40, 120, 6)
    assert m == 60 and abs(pct - 60) < 1e-9 and abs(pay - 2) < 1e-9 and ltv == 360 and abs(r - 3) < 1e-9
    print("OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    opt = lambda n, d: float(a[a.index(n) + 1]) if n in a else d
    if a[0] == "--test":
        selftest()
    elif a[0] == "runway":
        cash, costs, rev = map(float, a[1:4])
        net, flat, wg, c = runway(cash, costs, rev, opt("--growth", 0.0), int(opt("--months", 36)))
        print(f"spalanie netto/mies = {net:.0f}")
        print("runway bez wzrostu = " + ("brak (przepływ dodatni)" if flat is None else f"{flat:.1f} mies."))
        g = opt("--growth", 0.0)
        if g:
            print(f"runway ze wzrostem {g}%/mies. = " + (f"powyżej {int(opt('--months', 36))} mies. (gotówka po horyzoncie {c:.0f})" if wg is None else f"{wg} mies."))
    elif a[0] == "unit":
        m, pct, pay, ltv, r = unit(float(a[1]), float(a[2]), float(a[3]), opt("--months", None))
        print(f"marża/jedn.={m:.2f} ({'-' if pct is None else f'{pct:.0f}%'}) zwrot CAC po {'nigdy (marża <= 0)' if pay is None else f'{pay:.1f} jedn.'}")
        if ltv is not None:
            print(f"LTV={ltv:.2f} LTV/CAC={'-' if r is None else f'{r:.1f}'}")
    else:
        sys.exit(__doc__)
