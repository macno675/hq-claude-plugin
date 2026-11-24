# Ruch i interakcja (Y1, Y5) - dla `ui-designer`, `frontend-engineer`

Zasada: **animuj zmianę, nie element.** Test: po wyłączeniu animacji nadal wiadomo, co się stało.

## Trzy kategorie
1. **Wejście** (pierwsze wczytanie, zmiana widoku): raz, krótko, nie blokuje czytania.
2. **Przewijanie** (odsłanianie, paralaksa): oszczędnie, nigdy na tekście obok ruchomego wideo; elementy konkurujące o wzrok bez animacji.
3. **Mikrointerakcje** (hover, naciśnięcie, przełącznik, walidacja, sukces): tu żyje osobowość interakcji.

## Czasy i krzywe (web) `[ZAŁOŻENIE z praktyki]`
| Token | Czas | Użycie |
|---|---|---|
| `--dur-fast` | 100-180 ms | reakcje: hover, naciśnięcie, fokus |
| `--dur-base` | 180-300 ms | przejścia: rozwinięcie, zmiana stanu, panel |
| `--dur-slow` | 300-500 ms | ekspresyjne: moment sukcesu, wejście |
Krzywe jako tokeny (`--ease-out`, `--ease-in-out`, sprężyna jako `linear()` lub biblioteka tylko gdy uzasadniona). Bez `linear` poza postępem i pętlami. Overshoot (y > 1 w `cubic-bezier`) tylko przy osobowości energicznej/organicznej zapisanej w `dna.md`. Wartości M3 Expressive (150/350/500/650 ms) dotyczą ruchu przestrzennego na mobile, nie hover. Liczby z filmów demo (sprężyny, 1000+ ms) to nie progi.
Osobowość -> start: precyzyjna `fast 120 / ease-out` · elegancka `base 260 / ease-in-out miękki` · energiczna `fast 150 / lekki overshoot` · techniczna `0-100 / zmiana stanu bez ruchu` · organiczna `sprężyna, base`.

## Przepisy interakcji (per typ, w `design-system.md`)
Nie każdy element ma hover; hover wynika z funkcji. **Zakaz jednego efektu dla wszystkiego** (`translateY(-4px)`, `scale(1.02)`, sama opacity). Biblioteka reakcji, dobierana do funkcji:
- **typograficzna** (link: podkreślenie rośnie, zmiana wagi przez oś zmienną),
- **kierunkowa** (strzałka/treść przesuwa się w stronę celu),
- **mechaniczna** (przycisk: ugięcie przy naciśnięciu, nie przy hover),
- **ujawnienie treści** (karta: pokazuje dodatkową informację, nie tylko się podnosi).
Każdy hover ma odpowiednik dla fokusu (widoczny, kontrast 3:1) i dotyku (stan naciśnięty; nic ważnego tylko pod hover). Tooltipy ikon z opóźnieniem 300-700 ms `[ZAŁOŻENIE]`.

## Dostępność ruchu
`@media (prefers-reduced-motion: reduce)`: osobny zestaw (krócej lub bez ruchu, bez paralaksy i overshoot), stan dalej czytelny. Pętle ciągłe >5 s = pauza (WCAG 2.2.2). Bez migania >3 razy/s. Nie animuj `backdrop-filter`, `width/height/top/left` (tylko `transform`, `opacity`).

## `motion.md` projektu (Y5)
Osobowość, tokeny czasu i krzywych, lista mikrointerakcji (element -> wyzwalacz -> reakcja -> czas -> wersja reduced-motion), 1-3 autorskie animacje z budżetu (cel, koszt, alternatywa).
