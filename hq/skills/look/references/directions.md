# Kierunki i wybór (Y2-Y4) - dla `ui-designer`

## Y2 Dywergencja (szeroko, potem ostro)
1. **8-12 idei** wewnętrznie, każda: idea w zdaniu + forma w zdaniu + soczewka (`dna.md`). Tanio, tekstem.
2. **Selekcja do 3**: różne idee lub wartości, nie warianty tej samej. Zakaz „Złotowłosej” (bezpieczny/środkowy/odważny) i wariantów różniących się tylko tokenami (kolor, font, promień).
3. **≥4 różnice** między każdą parą z: kompozycja w bloku · hierarchia typografii · gospodarka przestrzenią · sygnatura · materiał i głębia · osobowość ruchu.
4. **Jeden odważny ruch na kierunek**, nazwany (np. „cyfry cennika 4x większe niż nagłówek”); im mocniejszy, tym spokojniej wokół.
5. **Paleta ograniczeń startowych** `[ZAŁOŻENIE z praktyki]`: 1-2 rodziny pisma (z puli `brand/references/typography.md`, licencja i polskie znaki), 2-3 kolory poza neutralnymi, 3-4 wyraźnie różne poziomy hierarchii.

## Stylescape (jeden plik HTML na kierunek: `directions/<A|B|C>.html`)
Na tej samej makiecie, prawdziwej treści i jednej szerokości (zwykle 1280 lub 390 - wg głównej platformy), jasny motyw:
- **fragment otwierający** krytycznego widoku,
- **jeden trudny fragment**: formularz, lista/tabela, pusty stan lub błąd (kierunku nie zatwierdza się na pięknym hero),
- **próbka typografii**: wszystkie role (display, nagłówek, tekst, etykieta, liczby) na realnych tekstach,
- **próbka interakcji**: przycisk i karta/link w stanach spoczynek, hover, fokus, naciśnięty, wyłączony (statycznie obok siebie + działające w HTML).
Nagłówek planszy: nazwa, idea w zdaniu, soczewka, odważny ruch, sygnatura, **ryzyko banału** (co tu najłatwiej zepsuć w stronę przeciętności). Każdy plik przechodzi `stylecheck` bez FAIL kontrastu, zrzut otwierasz przed pokazaniem.

## Prezentacja użytkownikowi
3 zrzuty obok siebie + po 3 linie (idea, odważny ruch, czego nie robi) + **lista odrzuconych** (jedno zdanie każdy, dlaczego odpadł - pokazuje, czym projekt nie jest). Bez rekomendacji przed pytaniem; rekomendacja z uzasadnieniem z DNA dopiero, gdy użytkownik zapyta lub się waha.

## Y3 Wybór (G2)
Kierunek -> **intensywność** wewnątrz kierunku: spokojna (sygnatura tylko w funkcji, momenty 1) vs ekspresyjna (sygnatura szerzej, momenty 2-3). Dwie wersje tego samego fragmentu. Przy wątpliwości między 2 kierunkami: obie responsywnie (360 + 1280) zamiast nowej rundy. Mieszanie kierunków („to z A, to z B”) = jedna dominująca idea + max 1 cecha z drugiego, zapisane w `decisions.md`; inaczej poziom 3 „Frankenstein”. Po 2 rundach bez wyboru: pytanie o kryterium, nie nowe warianty.

## Y4 Widok referencyjny (G3)
Najtrudniejszy krytyczny widok (nie strona główna, jeśli inny ma formularz/listę): pełny styl, wszystkie stany z `.hq/views/specs/` (pusty, ładowanie, błąd, sukces, długie teksty, brak zdjęcia), mobile 360 i desktop 1280, ciemny gdy wymagany. Najpierw widok, potem komponenty (curate, don't create): w Y5 wyciągasz z niego skalę, tokeny i komponenty. `stylecheck` bez FAIL, zrzuty w `reference/`.
