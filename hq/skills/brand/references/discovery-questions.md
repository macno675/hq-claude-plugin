# Wywiad o marce: przewodnik rozmowy (rundy ≤4 pytań, z propozycjami)

Cel: użytkownik odpowiada krótko i z przyjemnością, a Ty wiesz wszystko, co potrzebne. Z ~200 pytań zostają **cztery rundy rdzenia (16 pytań)** + rundy dodatkowe tylko na żądanie lub gdy brak danych.

## Zasady prowadzenia
1. **Najpierw sam, potem pytaj.** Przed pierwszym pytaniem skanuj: brandbook org (`~/.hq/orgs/<slug>/brand/`), `.hq/brand/`, `.hq/context.md`, README, opisy w `package.json`/stronie/kodzie, `scripts/brandscan.py` (kolory i fonty w użyciu). Wynik wpisz do `discovery.md` z tagiem `[WYWNIOSKOWANE]`.
2. **Potwierdzaj zamiast pytać od zera:** "Z materiałów rozumiem: [3-5 punktów]. Zgadza się?" (opcje: tak / popraw: ... ). Pytaj tylko o luki i sprzeczności.
3. **Każde pytanie ma gotowe opcje** (2-4, Twoja hipoteza pierwsza z "(Rekomendacja)", plus "Inne" i "Nie wiem - zaproponuj"). Nigdy gołe "jaki styl lubisz?" - najpierw przykład.
4. **Jedna runda = jeden temat**, ≤4 pytania (`AskUserQuestion`), nagłówek rundy z postępem ("Runda 2/4: klient"). Po rundzie jedno zdanie: co zapisałeś i co dalej.
5. **Pytaj "dlaczego" tylko tam, gdzie to zmienia decyzję** (wartości, przewaga, granice). Gust (kolory, fonty) sprawdzaj pokazem, nie rozmową.
6. **Nie wiem = Twoja robota:** zaproponuj 2-3 wersje z uzasadnieniem, zapisz wybraną jako `[ZAŁOŻENIE]` do potwierdzenia.
7. **Pokazuj, nie opisuj** (Figma wg `figma.md`; bez niej widżet/HTML): skale osobowości jako suwaki, palety z próbkami i kontrastem, pary fontów jako specimeny, komunikat błędu w 3 tonach obok siebie, 2-4 moodboardy. Rund wizualnych nie mieszaj z rundami słownymi.
8. **Zapis** w `discovery.md`: tabela `pole | odpowiedź | źródło (użytkownik/wywnioskowane/założenie)`; decyzje z powodem do `decisions.md`.

## Tryb (zapytaj w pierwszej paczce razem z skalą)
- **Szybki:** R0 + R1 + R3 (+ palety/fonty pokazem) ≈ 8 pytań. Mini i małe projekty.
- **Standard:** R0-R5, runda wizualna R6 w B2-B3.
- **Pełny:** + rundy dodatkowe D1-D5.

## R0 Start (0-1 paczka, głównie skan)
Czyja marka (org/projekt), skala, punkt wyjścia (nowa / odświeżenie / rebranding), **co musi zostać** (nazwa, logo, kolor), termin i kto zatwierdza. Resztę weź ze skanu.

## R1 Fundament (B0)
1. Co robi marka - jednym zdaniem dla osoby spoza branży? (pokaż Twoją wersję z materiałów)
2. Jaki problem rozwiązuje i dla kogo? (opcje z hipotez)
3. Po co istnieje poza zarabianiem / jakiej zmiany chce? → misja; gdzie za 3-5 lat? → wizja (2 wersje do wyboru)
4. Czym jest lepsza od alternatyw i czym to udowodni (wyniki, opinie, doświadczenie, dane)? → przewaga + dowód

## R2 Klient i rynek (B0)
1. Kto jest idealnym klientem (i kto płaci, jeśli ktoś inny)? Pokaż 2-3 typy, zaznacz główny.
2. Co go blokuje przed wyborem i co przeważa na korzyść? (lista typowych obiekcji do zaznaczenia)
3. 3 główne marki konkurencyjne/sąsiednie: co robią dobrze, co źle? (propozycje z WebSearch do potwierdzenia)
4. Gdzie jest wolna przestrzeń? 2-3 pozycjonowania do wyboru: "Dla [kto], która potrzebuje [co], [marka] jest [kategoria], która [korzyść], bo [dowód]."

## R3 Wartości i granice (B1)
1. Wybierz 3 wartości z 12-15 kandydatów (precyzja, otwartość, wytrzymałość, radość, uczciwość, prostota, odwaga, troska...) + po jednym zachowaniu, które je pokazuje.
2. Jak klient ma opisać markę w 3-5 słowach? (lista przymiotników do wyboru)
3. Czego marka **nigdy** nie zrobi / nie chce przypominać (skojarzenia, słowa, marki, kolory)?
4. Co jest dla marki najważniejsze: cena / jakość / szybkość / zaufanie / innowacja / relacja (wybierz 2).

## R4 Osobowość i głos (B1/B4)
1. Skale 1-5 (widżet, 6 suwaków): formalna↔swobodna · ekspercka↔przystępna · emocjonalna↔rzeczowa · poważna↔zabawna · nowoczesna↔klasyczna · luksusowa↔dostępna.
2. Komunikat błędu w 3 tonach obok siebie (sucho / ciepło / z humorem): który to Wy?
3. Forma: Ty / Pan-Pani; żargon: tak / tylko z objaśnieniem / nie.
4. Słowa preferowane i zakazane (zaproponuj po 5, użytkownik poprawia).

## R5 Inspiracje i kontekst użycia (B0/B2)
1. 3-5 lubianych marek/produktów/stron (dowolna branża) + powód jednym zdaniem; linki lub obrazy mile widziane.
2. 1-2 nielubiane + powód.
3. Gdzie marka będzie żyć: www / aplikacja / sklep / druk / opakowanie / produkt fizyczny / event / merch / wideo (zaznacz; testujesz tylko te).
4. Języki i kraje; przyszłość: nowe produkty, submarki, ekspansja (tak/nie/możliwe) - ile elastyczności musi mieć system.

## R6 Runda wizualna (B2-B3, tylko pokazem)
Kolejność, każdy krok = 2-4 warianty obok siebie, wybór + uwaga, zapis w `decisions.md`:
1. **Kierunek:** moodboardy (nazwa, idea, paleta 4-6, para fontów, forma, mockup, ryzyko) - różnicuj mocno.
2. **Logo:** typ (słowny / sygnet / monogram / emblemat), szkice SVG, test małego rozmiaru i mono (`logo.md`).
3. **Kolor:** 2-3 palety z próbkami i kontrastem, tryb ciemny, druk (`color.md`).
4. **Fonty:** 2-3 specimeny z polskimi znakami i licencją (`typography.md`).
5. **Zdjęcia/ilustracje/ikony/wzory:** tablice stylu, "tak / nie" (`imagery.md`, `pattern.md`).
Kryteria oceny (1-5): zgodność z pozycjonowaniem · czytelność dla odbiorcy · wyróżnienie · wielokanałowość · trwałość · koszt wdrożenia.

## Rundy dodatkowe (tylko na żądanie lub gdy brakuje danych)
- **D1 Historia:** start, przełomowy moment, pierwszy klient, co niezmienne, co opowiadać a czego nie (materiał na narrację).
- **D2 Dowody:** liczby, opinie, case studies, certyfikaty, nagrody, co klienci chwalą i krytykują.
- **D3 Percepcja klientów:** jak obecnie postrzegają markę, jak opisaliby ją koledze, co by im brakowało, czy polecą (propozycja: krótka ankieta/wywiady 5-8 osób; bez danych nie zgaduj).
- **D4 Spójność (audyt):** gdzie marka jest niespójna, kto za nią odpowiada (z `brandscan.py` i przeglądu materiałów, nie z pamięci użytkownika).
- **D5 Ryzyko prawne:** dostępność nazwy, domeny, znaku towarowego, podobne marki - **DO WERYFIKACJI** u specjalisty.

## Po etapach (B4-B8)
- B4: nazwa (kryteria + 5-10 propozycji z wstępnym sprawdzeniem), hasło (3-5 wariantów), zasady zapisu.
- B5: mockupy tylko wybranych kanałów; pytania: co działa, co nie, co poprawić. Produkt: oznaczenia, ekran startowy, LED/dźwięk (`design-feel.md` w `hq:product`), opakowanie, instrukcja.
- B6-B8: właściciel marki i zatwierdzający, miejsce zasobów, rytm przeglądu (6-12 mies.), dostępy.
