# Rzemiosło i tokeny (Y4-Y6) - dla `ui-designer`, `frontend-engineer`

Liczby to punkty startu zbieżne w 2+ źródłach (`[ZAŁOŻENIE]` z praktyki, nie norma), poza WCAG. Wartości z wzoru koryguj okiem (np. 22 -> 20 px).

## Tokeny: struktura i rozmiar
Źródło: format DTCG 2025.10 (stabilny raport Community Group, nie Rekomendacja W3C) w `tokens.json` lub od razu `tokens.css`; jedyny eksport do kodu: `tokens.css` (szablon: `<katalog skilla>/assets/tokens.css`). Nazwy semantyczne (`--color-text`, `--color-accent`), nie wyglądowe (`--blue-500` tylko w warstwie prymitywnej).
| Skala | Odstępy | Role typografii | Promienie | Głębia | Ruch | Poziomy |
|---|---|---|---|---|---|---|
| Mini | 5-7 | 5-7 (display, heading, body, label, overline, liczby) | 2-3 | 2-3 | 2-3 konfiguracje | prymitywne + semantyczne |
| Standard+ | 8-12 | 7-10 | 2-3 | 3 | 3-4 | + komponentowe |
Rytm sekcji (duże odstępy między blokami) ≠ odstępy w komponentach; to dwie osobne skale.

## Typografia
Tracking: display 0 do -0,02em · body 0 do +0,01em · wersaliki i małe etykiety +0,04 do +0,08em; nigdy dodatni na tekście ciągłym, nigdy ujemny na małym. Duże rozmiary = odmiana display lub oś `opsz`, nie powiększony krój tekstowy. Wagi dobrane świadomie (kontrast wag zamiast domyślnego 400/500/700). Interlinia body 1,4-1,6, nagłówki 1,1-1,3; 45-75 znaków w linii. Skala płynna `clamp()` dla display i nagłówków, body stałe. Liczby w tabelach i cenach: `font-variant-numeric: tabular-nums`. Wersaliki na linkach = slop. Polskie znaki sprawdź na realnych słowach (ąęłńóśźż w nagłówku display).

## Kolor
Rampa neutralnych z odcieniem marki (nie czysty szary), w OKLCH; stany (sukces, ostrzeżenie, błąd, info) wyprowadzone, nie domyślne zielony/czerwony z biblioteki. Nasycony akcent tylko dla **jednej** głównej akcji na widok (zgodne z `brand` K7). Kolor nigdy jedynym nośnikiem informacji. Ciemny motyw wyprowadzony (nie odwrócony): powierzchnie podnoszą się jasnością, akcent ciszej. Kontrast: tekst 4,5:1 (duży 3:1), elementy UI 3:1, liczony na najgorszym tle pod spodem.

## Kształt i głębia
Promienie: 1-2 + reguła; nie mieszaj 0 i małego promienia w sąsiednich elementach; koncentryczność: promień wewnętrzny = zewnętrzny - padding. Głębia: 2-3 poziomy, cień barwiony tłem (nie czarny o niskim kryciu), w ciemnym motywie głębia jasnością powierzchni zamiast cienia. Ramka domyślnie zbędna (kontrast tła i odstęp zamiast obrysu); dozwolona jako świadomy element DNA.

## Kompozycja i rytm
Rytm proporcji: sekcje przeplatają proporcje obraz/tekst (np. 80/20, 40/60, pełna szerokość) zamiast 50/50 wszędzie. ≤50% sekcji tej samej konstrukcji. Test miniatury: po zmniejszeniu zrzutu części strony są rozróżnialne. Jedna dominanta na widok.

## Ikony i obraz
Bez emoji jako ikon · jeden zestaw ikon, rozmiar podporządkowany tekstowi, wyrównany do pierwszej linii · bez ikon w kółkach jako dekoracji · bez karty w karcie · bez gradientowego tekstu na H1 i liczbach · prawdziwe zdjęcia lub spójny styl ilustracji zamiast stockowych SVG; kadrowanie jako element DNA.

## System ogranicza błędy (Y5)
Mało wariantów: przycisk 2-3, karta 1-2, układy sekcji 3-5. `design-system.md`: każdy komponent ze stanami (spoczynek, hover, fokus, naciśnięty, wyłączony, ładowanie, błąd), regułą użycia i **przykładem dobrym i złym** (jak `brand` S6). Wyjątek od systemu = `data-style-exception` w HTML + wpis w `decisions.md`.
