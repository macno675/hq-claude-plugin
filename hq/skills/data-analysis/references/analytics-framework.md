# Ramy analityki

## Pytanie analityczne (`questions.md`)
Decyzja do podjęcia · odbiorca · pytanie konkretne (grupa, okres, miara, porównanie) · hipoteza główna i przeciwne · potrzebne dane · co zmieniłoby decyzję · termin. Przykład: nie "dlaczego produkt nie działa", tylko "dlaczego w ostatnich 30 dniach spadł odsetek użytkowników kończących rejestrację na wydarzenie?".

## Słownik metryk (`metrics.md`)
`metryka | definicja (wzór, jednostka, okno czasu) | źródło | właściciel | wersja | uwagi`. Zmiana definicji = nowa wersja i zapis (porównania historyczne!). Typowe: konwersja, retencja, frekwencja (zarejestrowani vs obecni), CAC/CPA, ROAS, NPS/CSAT, czas zadania, odsetek błędów.

## Jakość danych (`data-quality.md`)
Źródło i sposób zbierania · zakres (okres, populacja, braki systematyczne) · liczba rekordów przed/po · duplikaty · braki (jak obsłużone) · formaty i strefy czasowe · odstające (usunięte/zostawione i dlaczego) · definicje spójne między źródłami · zmiany w śledzeniu w czasie (przerwy, wdrożenia). Każda transformacja w kodzie, nie ręcznie.

## Analiza eksploracyjna (przepisy)
- **Trend w czasie:** zmiana vs sezonowość, dni tygodnia, wydarzenia/kampanie/wdrożenia w osi czasu.
- **Segmenty:** rozbij po kanale, urządzeniu, grupie, nowy vs powracający; sprawdź, czy wynik zbiorczy nie ukrywa przeciwnych trendów (paradoks Simpsona).
- **Lejek:** kroki, odsetek przejścia, punkty największego porzucenia; porównaj segmenty i okresy.
- **Retencja i kohorty:** grupy wg daty pierwszego kontaktu, odsetek powracających w kolejnych okresach.
- **Zmiana po wdrożeniu:** przed/po z grupą porównawczą, jeśli się da; uwaga na inne zdarzenia w tym samym czasie.
- **Korelacje:** tylko jako hipotezy przyczynowe do sprawdzenia; zmienne zakłócające.
- **Odstające:** zbadaj przyczynę zanim usuniesz.
Narzędzia: Python (stdlib/pandas jeśli zainstalowany), SQL na lokalnym SQLite; kod i wynik zapisane w `analyses/<nazwa>.*`.

## Feedback (opinie, ankiety, rozmowy, zgłoszenia, recenzje, testy użyteczności)
Zbierz -> zakoduj tematy (jedna wypowiedź może mieć kilka) -> policz częstotliwość -> oceń wpływ na użytkownika i biznes -> możliwe rozwiązanie -> priorytet. Tabela: `temat | przykłady (anonimowe cytaty) | liczba | segmenty | wpływ | rozwiązanie | priorytet`. Liczby mówią "co", opinie "dlaczego"; łącz. Próbka ankiet to nie populacja: zaznacz odchylenia (kto odpowiada).

## Eksperymenty A/B (`experiments.tsv`)
`id | hipoteza | zmiana | kontrola/test | miara główna | miary ochronne | MDE | próba (samplesize) | czas | kryteria sukcesu | zasady zakończenia | status | wynik | decyzja`. Zaplanuj z góry; nie zaglądaj i nie kończ po drodze; jedna zmiana naraz lub korekta; unikaj nakładania eksperymentów na tych samych użytkowników; weryfikuj równość grup. Obliczenia: `mkcalc.py samplesize BAZA MDE` i `mkcalc.py abtest ...`. Wynik istotny statystycznie nie zawsze jest istotny biznesowo (oceń wielkość efektu i koszt). Mała grupa (np. lokalny turniej) często nie pozwala na A/B: użyj porównań przed/po i feedbacku, z zastrzeżeniami.

## Dashboard
Pokaż to, co pomaga decydować: najważniejsze KPI, trendy, cel, segmenty, alerty, kontekst i wyjaśnienie zmian, link do szczegółów. Bez dekoracji; liczby z definicją i okresem; źródło i data odświeżenia. Wykresy według skilla `dataviz`.

## Wnioski i rekomendacja (szablon raportu)
Pytanie i decyzja · odpowiedź w 2-3 zdaniach · dowody (wykres/tabela) · jak pewne (poziom, próba, ograniczenia) · przyczyna (hipotezy i co je potwierdza/odrzuca) · wpływ (skala) · rekomendacja (działanie, oczekiwany efekt, koszt, ryzyko, pomiar, właściciel, termin weryfikacji) · alternatywy · czego nie wiemy / kolejne pytania.

## Dokumentacja
Pytanie biznesowe · hipoteza · źródła · definicje metryk · metoda · ograniczenia · wyniki · wnioski · rekomendacje · decyzje podjęte · wyniki eksperymentów · zmiany w KPI. Chroni przed powtarzaniem analiz i błędnymi interpretacjami.
