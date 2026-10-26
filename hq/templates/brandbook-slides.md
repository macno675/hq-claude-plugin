# Szablon slajdów brandbooka (układ wzorowany na stylu agencyjnym)

Jeden plik Figma, **15 slajdów tego samego układu**, powtarzalnych dla każdej marki. Zmienia się tylko marka (paleta, logo, font, zdjęcia), nigdy układ. Wzorzec to inspiracja układem, nie treścią: nie kopiuj cudzej marki ani zdjęć.

## Układ każdego slajdu (ramka 16:9, np. 1920x1080)
- Tło slajdu: prawie biały (neutralny z palety marki, np. `#FDFDFF`), marginesy ~60 px.
- Lewy górny róg: **tytuł na 2 linie**, cienka/regularna waga fontu głównego, duży (≈110-140 px), letter-spacing -3%, interlinia ciasna. Przykład: `Brand` / `Billboard`.
- Prawy górny róg: opis 1-2 zdania, szary, ≈14-16 px, szerokość ~1/3 slajdu, wyrównany do góry z tytułem. Wzór: "<Element> <robi co> w <jaki sposób>, zapewniając spójność i rozpoznawalność."
- Pusta przestrzeń oddycha między nagłówkiem a panelem (≈1/5 wysokości).
- **Panel treści**: jedna zaokrąglona ramka (promień ≈ 8-12 px) na całą szerokość i dolną ~60% wysokości; wewnątrz wyłącznie treść slajdu. Tło panelu: jasnoszare (typografia, logo clearspace), ciemne lub z palety (obrazy, mockupy). Gradient tła tylko w panelu mockupów.
- Bez dodatkowych ozdobników, ramek i numeracji na slajdzie; max 1 font (główny), 1 akcent kolorystyczny.

## Kolejność i zawartość (= obowiązkowy zestaw 15 z `hq:brand`)
| # | Slajd (tytuł) | Panel zawiera |
|---|---|---|
| 1 | Primary Logo | 2 pola obok siebie: jasne tło i czarne tło; logo wyśrodkowane |
| 2 | Logomark | 3 pola: czarne, jasne, kolor główny (znak odwrócony); znak wyśrodkowany |
| 3 | Logo Clearspace | szare pole, 2 diagramy (logo poziome, logomark): różowa ramka pola ochronnego, czarne kwadraty z opisem `1/4` (pole = ¼ wysokości logo) |
| 4 | Primary Typeface | nazwa fontu duża, warianty Bold/Medium/Regular/Light, pełny zestaw znaków (A-Z, a-z, 0-9, symbole, polskie znaki) |
| 5 | Typeface Hierarchy | tabela wierszy: Display, H1, H2, H3, H4, Paragraph, Caption; kolumny Size (px) i Letter Spacing; każdy wiersz renderowany w swoim rozmiarze |
| 6 | Color Palette | 4-5 pionowych pasów równej szerokości; nazwa (2 linie) u góry, RGB i HEX u dołu; role: ciemny, ciemny akcentowy, kolor główny, jasny |
| 7 | Brand Imagery (zasady: `imagery.md`) | mozaika 5 zdjęć/obrazów w jednym stylu (spójne światło, kadr, tonacja z palety) |
| 8 | Graphic Patterns (zasady: `pattern.md`) | wzór wyprowadzony z logomarka (linie, powtarzalny moduł) na ciemnym polu palety |
| 9 | Social Media Creatives | 4 posty w ramkach aplikacji na ciemnym tle w kolorze marki; różne typy: zdjęcie+hasło, dane, cytat, liczba |
| 10 | Social Media Page Banners | 2 profile (np. LinkedIn, X): baner z patternem, awatar logomark, hasło |
| 11 | Brand Mockups | 3 kolumny: ikona aplikacji, urządzenie/produkt, strona www |
| 12 | Business Card | awers ciemny z logo, rewers jasny z danymi; na gradiencie palety |
| 13 | Brand Billboard | billboard w realnym otoczeniu: logo, krótkie hasło, pattern, osoba/produkt |
| 14 | Brand Merch | 3 kadry: butelka, czapka, torba (logo/logomark na kolorze marki) |
| 15 | Conference Display | scena/ekran LED, ścianka lub roll-up: hasło, logo, nazwa wydarzenia |

## Realizacja
- Figma: jedna strona `Brandbook`, ramki `01 Primary Logo` ... `15 Conference Display`, komponent `Slide` (tytuł, opis, panel) z auto-layout; kolory, typografia i promienie jako zmienne/style z B3 (skill `figma:figma-generate-library`, slajdy `figma:figma-generate-design`; `figma:figma-use` przed każdym `use_figma`).
- Zdjęcia i mockupy (11-15): generator obrazów lub zdjęcia stockowe tylko jako **materiał poglądowy** (zaznacz w opisie; do wymiany przed publikacją, sprawdź licencje i prawa wizerunku). Logo na mockupach wstawiaj z wektora, nigdy z obrazu generatora.
- Teksty slajdów, hasła i opisy po języku użytkownika; nazwy slajdów po angielsku zostają (tytuły standardu), chyba że użytkownik zdecyduje inaczej.
- Po złożeniu: przegląd `hq:design-reviewer` (spójność układu między slajdami, kontrasty `contrast.py`, `logotest.py` dla logo), eksport PDF jako wersja do przekazania.
