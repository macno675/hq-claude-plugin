# Dobór komponentów

Cel: najlepsza część za tę cenę, potwierdzona danymi. Format wyniku: tabela TSV (patrz niżej), nie opowieść.

## Źródło główne: API LCSC
Skrypt: `<katalog skilla>/scripts/lcsc.py` (klucze w zmiennych środowiskowych `LCSC_APP_KEY`, `LCSC_SECRET`; nigdy w plikach ani w czacie).
- `python3 lcsc.py search "<słowa>" [--in-stock] [--limit 20]` - wyszukiwanie po słowach, MPN, numerze LCSC
- `python3 lcsc.py detail C25804` - szczegóły, progi cenowe, parametry
Limit zapytań: ok. 60/min i 1000/dzień na wyszukiwanie. Zapytań nie marnuj: zawężaj słowa, filtruj `--in-stock`, nie szukaj w pętli.
Brak kluczy: powiedz użytkownikowi, że wniosek składa się na lcsc.com/agent/apply (darmowy, po weryfikacji), a w międzyczasie używaj wyszukiwarki EasyEDA (`easyeda_schematic_search_device`, `easyeda_catalog_*`) i stron produktów LCSC.

## Tryb bez API (domyślny, dopóki brak kluczy) - drabina od najtańszej
Skrypt zwrócił "Brak LCSC_APP_KEY" = ten tryb. Schodź w dół drabiny tylko tak daleko, jak trzeba.
0. **Cache:** `.hq/electronics/parts-cache.tsv` (projekt) i `~/.hq/parts-cache.tsv` (wszystkie projekty). Trafienie = użyj bez szukania (stan/cena kluczowych części ważne ~30 dni, pasywa bez limitu). Format: `lcsc mpn opis pakiet jlc_typ cena@ilość stan data źródło uwagi`. Każdą zweryfikowaną część dopisz.
1. **Biblioteka EasyEDA** (bez klucza, lokalnie przez most): `easyeda_schematic_search_device` zwraca numer LCSC, `JLCPCB Part Class` (Basic/Extended), parametry i link do datasheetu. Pełna odpowiedź to ok. 700 tokenów na część, więc: konkretne słowa (typ, wartość, pakiet, np. "10k 0603 1%"), `itemsOfPage` <= 5, wyłącznie w agencie. `minimal:true` dopiero przy wyborze deviceItem do wstawienia. Brak stanu i ceny w tej odpowiedzi.
2. **Stan i cena zbiorczo:** wpisz wybrane części do BOM projektu i wywołaj raz `easyeda_bom_sourcing` dla całości (zamiast pojedynczych zapytań). Gdy niedostępne: strona `https://www.lcsc.com/product-detail/<Cxxxx>.html` jest renderowana skryptem (WebFetch zwraca puste - sprawdzone), więc użyj przeglądarki (jeśli dostępna) i jej narzędzia do JS, zwracając tylko kilka pól (wymaga zgody użytkownika na witrynę). Gdy i to zawiedzie: oznacz `stan=NIEZNANY` i poproś użytkownika **jednym komunikatem** o sprawdzenie zbiorczej listy numerów C.
3. **Datasheet:** WebFetch na adres z pola `Datasheet`, z promptem wyciągającym tylko potrzebne parametry. Nie czytaj całych dokumentów.
4. **Opinie:** tylko dla części kluczowych (MCU, zasilanie, czujniki, złącza, moduły), 1-2 WebSearch na część. Pasywa i standardowa drobnica: bez opinii.
5. **Opcjonalny upgrade:** lokalna baza projektu jlcparts (SQLite, ok. 11 GB, licencja MIT) daje zapytania SQL po parametrach bez żadnych tokenów. Duże pobieranie - tylko za zgodą użytkownika.

**Pasywa i drobnica** (R, C, LED, diody, tranzystory uniwersalne): standardowe wartości i pakiety, wybór z JLC Basic, jedno zapytanie na typ/pakiet, wynik do cache. Bez porównywania alternatyw i opinii. Uwaga na parametry krytyczne (napięcie MLCC, moc rezystora, tolerancja w torach pomiarowych).

**Oszczędność tokenów:** zawężaj parametrami zamiast przeglądać listy; <= 5 wyników; grupuj wiele części w jednym zleceniu dla agenta; dla pasywów zatrzymaj się na "wystarczająco dobre"; pełne rozumowanie i alternatywy tylko tam, gdzie część decyduje o działaniu lub kosztach.

## Procedura dla każdej części
1. **Wymagania z planu** zamień na liczby (napięcie, prąd, tolerancja, pakiet, temperatura, interfejs).
2. **Kandydaci** (3-5): z API; uwzględnij JLC Basic/Extended (opłata za Extended, jeśli montaż w JLC).
3. **Specyfikacja z datasheetu**, nie z opisu: pobierz i sprawdź parametry krytyczne, absolute max vs praca, zalecany schemat aplikacyjny, footprint, piny. Zapas (derating): napięcia i prądy co najmniej 20-50% marginesu, kondensatory MLCC uwzględnij spadek pojemności pod napięciem DC, temperatury z marginesem.
4. **Dostępność:** stan magazynu >= (ilość × liczba płytek × 1.1 + zapas), MOQ i krok zamówienia, cykl życia (nowa/aktywna/NRND/EOL), czas dostawy.
5. **Cena:** realny próg dla Twojej ilości (`standardPricing`), nie cena za 1 szt.; koszt z montażem (Extended = dopłata).
6. **Lepsza alternatywa:** zawsze sprawdź, czy istnieje część równoważna za tę samą lub niższą cenę, o lepszych/równych parametrach, zgodna footprintem lub z niewielką zmianą schematu. Wynik: "zostaje X, bo…" albo "zamiana na Y, oszczędność Z".
7. **Opinie i wiarygodność:** WebSearch: problemy, erraty, podróbki, fora (EEVblog, Reddit r/electronics, GitHub issues bibliotek), opinie o producencie. Preferuj uznanych producentów; tanie klony tylko gdy są dowody, że działają. Zapisz źródła.
8. **Decyzja:** wybierz sam, jeśli różnica jasna. **Zapytaj użytkownika**, gdy: wybór zmienia funkcję/koszt >10%, brak dobrej części, ryzyko podróbek/EOL, kompromis jakość-cena nie ma oczywistego zwycięzcy.

## Poza LCSC
Tylko gdy LCSC nie ma części lub wyraźnie przepłaca. Sprawdź tanie, wiarygodne sklepy (np. Mouser, Digi-Key, TME, inne autoryzowane lub znane dystrybutory). Unikaj anonimowych sprzedawców marketplace dla części krytycznych (podróbki). Policz **koszt dostarczony** (wysyłka, cło/VAT, czas). Uwaga: montaż SMT w JLCPCB wymaga części z ich zapasów lub konsygnacji - części spoza LCSC oznacz w BOM jako "ręcznie/konsygnacja" i podaj konsekwencje użytkownikowi.

## Format wyniku (`bom.tsv`)
`ref<TAB>wartość/opis<TAB>MPN<TAB>producent<TAB>LCSC<TAB>pakiet<TAB>JLC_typ<TAB>ilość<TAB>cena_jedn@ilość<TAB>stan<TAB>datasheet_ok<TAB>uwagi/alt`

Dla wyboru kluczowej części dodaj 3 linie uzasadnienia: dlaczego ta, czym wygrała z alternatywą, ryzyka i źródła opinii.
