# Kontrola makiet przed pokazaniem człowiekowi

AI nie udowodni, że makieta jest idealna; może znaleźć błędy, zanim zobaczy je człowiek. Kolejność: automat -> świeże oczy -> ścieżki -> pre-mortem -> rubryka -> recenzent. Wyniki w `qa.md`.

## 1. Automat (`wirecheck.mjs`)
`node <katalog skilla>/scripts/wirecheck.mjs .hq/views/wireframes/<VIEW>.html --out .hq/views/wireframes/png` (aplikacja: `--app`). TSV `szerokość poziom reguła element`; FAIL blokuje, WARN wymaga powodu w `qa.md`. Reguły: przewijanie w bok, kolor spoza szarości, cel dotykowy <24 px (FAIL) / <44 px na mobile (WARN), liczba `h1`, przeskok nagłówków, `main`/`nav`, pole bez etykiety, `data-nav` nie jako `<a href>`, blok bez `data-p`/`data-why`, główne CTA: brak / kilka różnych akcji / poza pierwszym ekranem bez paska przyklejonego, blok P3 większy od największego P1, placeholder obrazu bez etykiety. Potem otwórz PNG (Read) i oceń hierarchię okiem.

## 2. Test świeżych oczu (symulowany test 5 sekund)
Osobny agent (`hq:design-reviewer`, bez `brief.md` i specyfikacji, tylko zrzut mobile pierwszego ekranu i całego widoku) odpowiada: czym jest produkt? co tu można zrobić? jaka jest główna akcja? gdzie jest najważniejsza informacja? czego brakuje do decyzji? Porównaj z celem widoku. Próg (wewnętrzny, nie norma): cel i główna akcja rozpoznane trafnie na każdym widoku krytycznym. To nie badanie z ludźmi - oznacz `[ZAŁOŻENIE]`.

## 3. Przejście ścieżek (cognitive walkthrough)
Każdy `FLOW` krok po kroku na makietach: czy użytkownik chce tu tej akcji? czy zauważy element? czy rozumie, co zrobi? czy dostaje jasny wynik? Wynik: `kroki przechodzące / wszystkie`, martwe końce, brakujące stany. Plus ścieżka alternatywna i wejście z wyszukiwarki na podstronę (bez strony startowej). Opcjonalnie (skala Pełna) 3-5 profili użytkowników z `brief.md` przechodzi to samo; wynik `[ZAŁOŻENIE]`.

## 4. Pre-mortem
„Strona działa od miesiąca i nikt nie rezerwuje / użytkownicy się gubią - co poszło nie tak?” 5-8 przyczyn (nie zauważył formularza, nie widzi ceny, nie ufa, nie wie, czy rezerwacja przeszła, nie znalazł warunków anulowania). Przy każdej: ważność (blokujący/duży/mały) i czy makieta już temu zapobiega; jeśli nie - poprawka albo jawne ryzyko.

## 5. Rubryka (100 pkt; ≥90 = do recenzji, 75-89 = poprawki, <75 = przeprojektuj)
| Obszar | Pkt | Co sprawdzasz |
|---|---|---|
| Realizacja zadań | 25 | każdy top task od wejścia do końca, błędy z wyjściem, potwierdzenia |
| Architektura | 15 | mapa kompletna, nazwy w języku użytkownika, miejsce zawsze widoczne, rozbudowa bez przebudowy |
| Widoki i stany | 15 | cel, główna akcja, bloki z powodem i danymi, stany widoku i elementów |
| Hierarchia i ergonomia | 15 | ≤3 poziomy, główna akcja dominuje, kciuk, grupowanie, desktop nie rozciąga mobile |
| Dostępność struktury | 15 | landmarki, nagłówki, etykiety, fokus, cele dotykowe |
| SEO | 10 | intencja na stronę, URL, linki `<a href>`, nagłówki, schema w `seo.md` (aplikacje bez publicznych stron: punkty do „Realizacja zadań”) |
| Spójność | 5 | te same wzorce w tych samych sytuacjach, wspólne prymitywy |
**Warunki bezwzględne** (niezależnie od punktów): zero FAIL, zero martwych końców, wszystkie widoki krytyczne istnieją, każdy blok ma powód i źródło danych, brak funkcji spoza fundamentu bez zgody, zero dark patterns.

## 6. Wykrywanie generyczności
- **„Hero + 3 karty + opinie + CTA”** bez związku z mapą pytań: przepisz kolejność z mapy pytań.
- **Ta sama sekwencja na różnych typach widoków**: spójność wzorców tak, kopia struktury nie.
- **Karty zamiast tabeli/listy**, gdy użytkownik porównuje lub skanuje.
- **Sekcja bez zadania** (np. „Nasza misja” na stronie rezerwacji): test konieczności.
- **Marketingowy hero w aplikacji**: pierwszy ekran = status i główna operacja.
- **Podstrony pod frazy bez osobnej potrzeby**: połącz.
- **Brak wariantu alternatywnego** dla widoku krytycznego: dorób jeden i porównaj.

## 7. Paczka dla `hq:design-reviewer` (V7)
Pliki: `brief.md`, `flows.md`, `views.tsv`, `seo.md`, `specs/`, PNG, `qa.md`, ten plik. Zadanie: niezależnie oceń rubrykę i warunki bezwzględne, wskaż ≤10 problemów z ważnością i dowodem (plik, blok, zrzut). Zwrot ≤300 tokenów. Rozbieżność ocen >10 pkt: pokaż użytkownikowi obie.
