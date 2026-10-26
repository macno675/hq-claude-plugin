# Dźwięk (dla `audio-engineer`)

## Słuchanie krytyczne - nazywaj zjawiska
Rezonanse · odbicia i pogłos · maskowanie częstotliwości · problemy fazowe · szum · zniekształcenia · nierówna głośność · utrata czytelności · za wąska/za szeroka scena · problemy dynamiki. Mów: gdzie jest problem, co go powoduje, jak to sprawdzić (pomiar, A/B, test w innym miejscu). Decyzje na kalibrowanym odsłuchu i pomiarach; słuch i pomiary się uzupełniają.

## Akustyka pomieszczenia
Oceń: odbicia wczesne, czas pogłosu, rezonanse (tryby: `avcalc.py modes L W H`), szum tła, symetrię i pozycję odsłuchu, rozmieszczenie głośników, materiały i meble, izolację. Pogłos: `avcalc.py rt60 V S:alfa ...` (Sabine, szacunek). Środki: absorpcja, dyfuzja, pułapki basowe, przestawienie głośników i odsłuchu, ograniczenie szumów. Cel to przewidywalne i wiarygodne środowisko, nie płaska odpowiedź za wszelką cenę. Pomiar w kilku pozycjach słuchacza.

## Tor sygnałowy (zaprojektuj od źródła)
Źródło -> mikrofon/instrument -> przedwzmacniacz -> przetwornik -> konsola/interfejs -> procesory -> nagrywanie -> monitoring/odtwarzanie. Dbaj o: jakość źródła, dobór mikrofonu, odległość i kąt, poziom nagrania (bez przesterowania, z zapasem), zasilanie i uziemienie (brzęczenie), kable i złącza, zgodność impedancji, konwersję AD/DA. Nie ratuj złego nagrania efektami: usuń przyczynę. Zapisz schemat w `signal-flow.md`.

## Dobór sprzętu
Kryteria: przeznaczenie, charakter brzmienia, poziom szumu, dynamika, odporność na zakłócenia, niezawodność, zgodność z torem, serwis i części, koszt całkowity (zakup vs wynajem), możliwość rozbudowy. Droższy nie znaczy lepszy; uzasadnij każdy element. Parametry z datasheetu.

## Nagrywanie
Ustawienie mikrofonów, poziomy, brak przesterowania, kontrola szumu i zakłóceń, spójność ujęć, notatki i metadane, **kopie zapasowe**, natychmiastowa kontrola jakości materiału (odsłuch próbki).

## Edycja i czyszczenie
Wycinanie zbędnego, usuwanie szumów i trzasków, wyrównanie poziomów, timing, porządek sesji, kopie bezpieczeństwa. Minimum obróbki potrzebne dla czystego materiału; pracuj na kopiach.

## Projektowanie dźwięku (film, gry, reklamy, produkt)
Efekty, atmosfery, warstwowanie, synteza, przestrzeń, dopasowanie do obrazu, spójność świata. Dźwięk wspiera narrację/funkcję. Dźwięki produktu (kliknięcia, sygnały, alerty) zaprojektuj razem z `industrial-designer` (tabela stanów feedbacku w `hq:product`) i ograniczeniami sprzętowymi (głośnik, obudowa, przetwornik; `hq:electronics`).

## Miks
Balans, EQ, kompresja, bramki, panorama, pogłos i delay, automatyzacja, czytelność wokalu/narracji, separacja źródeł, dynamika, scena stereo, spójność. Cel: czytelność, równowaga, wpływ emocjonalny, nie maksymalna głośność.

## Mastering
Balans tonalny, kontrola rezonansów, obraz stereo, dynamika, głośność, ograniczenie true peak, dopasowanie do platformy, spójność między utworami, pliki do dystrybucji. Finalizacja dobrego miksu, nie naprawa złego. Zachowaj dynamikę tam, gdzie ważna.

## Głośność i standardy
Miary: LUFS (zintegrowana), LRA, true peak (dBTP). Wymagania różnią się między platformami i emitentami - **pobierz aktualną specyfikację dostawy z sieci/od odbiorcy i zapisz ją**; nie zgaduj. Przykłady do weryfikacji: radiofonia europejska wg EBU R128 (cel -23 LUFS, true peak maks. -1 dBTP); platformy streamingowe mają własne cele. Pomiar: `python3 <katalog skilla>/scripts/loudness.py plik --target <LUFS> --tp <dBTP>` (ffmpeg). Zostaw zapas na true peak; nie przesteruj.

## Nagłośnienie na żywo i instalacje
Test połączeń i polaryzacji, każdy tor osobno, kierunek i pokrycie głośników, dopasowanie subwooferów, korekcja odpowiedzi, opóźnienia, sprawdzenie w wielu miejscach widowni, ograniczenie sprzężeń, monitory sceniczne, komunikacja z zespołem, zapasowe tory, kontrola zasilania. Pokrycie i spadek poziomu: `avcalc.py spl SPL_1m odległość`. Cel strojenia: spójne brzmienie w całej widowni. **Limity głośności i ochrona słuchu:** wymagania zależą od kraju i miejsca - `DO WERYFIKACJI`; mierz SPL miernikiem, nie na oko.

## Próba i test przed wydarzeniem
Wszystkie wejścia i wyjścia, mikrofony, monitory, komunikacja, próba dźwięku, zapasowe tory (mikrofon, bezprzewodowe baterie/częstotliwości, nośnik), zasilanie, rozwiązania awaryjne, przejścia między punktami programu.

## Kontrola jakości przed dostawą
Czytelność dialogów/wokalu · brak przesterowania · szum · spójność głośności · wymagania platformy · odsłuch na kilku systemach (słuchawki, małe głośniki, telefon, samochód) · poprawność plików i metadanych · synchronizacja z obrazem · brak błędów montażowych i przerw. Raport QC z liczbami.

## Dokumentacja
Schemat toru, ustawienia mikrofonów, lista sprzętu, ustawienia konsoli i procesorów, wyniki pomiarów akustycznych, ustawienia systemu, parametry miksu i masteringu, wymagania platformy, lista plików dostawy, znane problemy i rozwiązania.

## Współpraca
Reżyser/producent: możliwości, kompromisy. Wykonawcy: komfort, monitoring, brak stresu. Montażysta/reżyser dźwięku: synchronizacja, dialogi, efekty, atmosfery. Światło/wydarzenie: montaż, zasilanie, miejsca pracy, próby, program (`hq:event`). Produkt: głośniki, mikrofony, przetworniki, akustyka obudowy (`hq:electronics`).
