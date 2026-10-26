# Checklisty backendu

## BE1 Wymagania
Funkcjonalne: kto używa, co robi, przypadki brzegowe, kryteria akceptacji. Niefunkcjonalne **z liczbami lub `[ZAŁOŻENIE]`**: obciążenie (rps, użytkownicy, wolumen danych i wzrost), opóźnienia (p95/p99), dostępność, RPO/RTO, bezpieczeństwo i zgodność (RODO/prywatność, dane wrażliwe), koszt, retencja. Dane: źródło, właściciel, jakość, cykl życia, usuwanie. Ograniczenia: zespół, termin, stos. Miara sukcesu.

## BE2 Projekt techniczny (`design.md`)
Komponenty i odpowiedzialności · przechowywane dane · interfejsy · przepływy (sekwencje głównych scenariuszy) · zależności (usługi, zewnętrzne API) · **co jeśli zawiedzie każda zależność** · testowanie · monitoring · skalowanie (gdzie wąskie gardło) · bezpieczeństwo (model zagrożeń: aktorzy, zasoby, granice zaufania) · migracja/wdrożenie · alternatywy odrzucone z powodem · otwarte pytania.
Styl: monolit (mały zespół, spójny produkt) -> modularny monolit (separacja bez kosztu rozproszenia) -> mikroserwisy (niezależne skalowanie, osobne zespoły, różne cykle wydań) -> zdarzeniowa (wiele zdarzeń asynchronicznych). Każda usługa dodaje koszt komunikacji, debugowania, monitoringu, utrzymania.

## BE3 Model danych
Encje i relacje · integralność (klucze, ograniczenia) · transakcje i granice · indeksy pod realne zapytania (sprawdź plan zapytań) · historia zmian/audyt · **migracje**: małe, odwracalne, kompatybilne wstecz z działającą wersją kodu (rozwiń-przełącz-zwiń), test na kopii danych · prywatność, retencja, usuwanie · zgodność danych między usługami. Spójność: silna (błąd nieakceptowalny), ostateczna (opóźnienie ok), transakcje (razem albo wcale), idempotencja (powtórzenie bez skutków).

## BE4 API
Spójne nazwy zasobów · właściwe metody i kody odpowiedzi · walidacja wejścia · **jednolity format błędów** (kod, komunikat, szczegóły, id śledzenia) · paginacja, filtrowanie, sortowanie · wersjonowanie i polityka zgodności wstecznej (zmiana łamiąca = nowa wersja + okres przejściowy) · authn/authz na każdym zasobie · limity zapytań · idempotency key dla operacji tworzących/płatności · dokumentacja (OpenAPI) · testy kontraktowe. Uzgodnij z klientem: format danych, błędy, paginację, stany ładowania, uprawnienia.

## BE5 Implementacja
Czytelność, prostota, spójność ze standardami zespołu, separacja odpowiedzialności, brak duplikacji, ograniczona złożoność, sensowne nazwy, obsługa błędów, logika biznesowa niezależna od szczegółów technicznych, testowalność. Kod pisany tak, jakby utrzymywała go inna osoba latami.

## Odporność na awarie
Timeouty na każdym połączeniu wychodzącym · ponawianie z backoffem i jitterem **tylko operacji bezpiecznych/idempotentnych** · circuit breaker/bulkhead tam, gdzie zależność może przeciągać awarię · limity i obsługa przeciążenia (load shedding, kolejki z limitem) · ścieżki awaryjne (degradacja) · rollback wdrożenia · izolacja awarii · zdrowie/gotowość (health/readiness) · brak stanu w instancji (łatwe replikowanie) · bezpieczne zamykanie (graceful shutdown).

## Bezpieczeństwo
Walidacja i oczyszczanie wejścia (w tym ochrona przed iniekcjami) · najmniejsze uprawnienia · poprawne uwierzytelnianie i **autoryzacja na poziomie zasobu** (sprawdzaj własność obiektu) · szyfrowanie w tranzycie i spoczynku · sekrety w menedżerze sekretów, nie w repo ani logach · logowanie bez danych wrażliwych · ochrona przed nadużyciami (rate limiting, enumeracja) · aktualizacje i skan zależności · brak własnej kryptografii · testy bezpieczeństwa · audyt dostępu.

## BE5 Testy
Jednostkowe (logika) · integracyjne (baza, kolejka, zależności, np. w kontenerach) · kontraktowe (API) · end-to-end (kluczowe scenariusze) · wydajnościowe (obciążenie normalne i szczytowe, wartości z BE1) · bezpieczeństwa (authz, wejścia) · odporności (zawiedzione zależności, timeouty, duplikaty żądań, wyścigi). Testuj błędy, limity, dane niepoprawne, równoległość.

## BE6 Wdrożenie
CI: build + testy + lint + skan przed scaleniem · wersjonowanie kodu i artefaktów · infrastruktura jako kod · konfiguracja środowisk (bez sekretów w kodzie) · migracje w procesie wdrożenia · wdrożenie stopniowe (canary/blue-green/flagi) · **szybki rollback** (sprawdzony) · kontrola zmian.

## BE7 Obserwowalność
Logi strukturalne z id żądania · metryki techniczne i biznesowe (RED/USE: tempo, błędy, czas; nasycenie) · tracing rozproszony przy wielu usługach · dashboardy · alerty na realny wpływ na użytkowników (nie na każde zdarzenie), z właścicielem i runbookiem · SLO/SLI jeśli wymagane.

## BE8 Awaria i utrzymanie
1. Przywróć działanie (rollback/przełączenie) i ogranicz wpływ. 2. Zbierz logi, metryki, ślady. 3. Ustal przyczynę źródłową. 4. Napraw przyczynę, nie objaw. 5. Dodaj test regresji. 6. Zaktualizuj dokumentację i runbook. 7. Wnioski dla zespołu (postmortem bez szukania winnych: oś czasu, wpływ, przyczyny, co zadziałało, działania z właścicielami). Dług techniczny: rejestr, regularne spłacanie.

## Dokumentacja
Architektura i diagramy przepływu danych · kontrakty API · model danych · decyzje (ADR) · procedury wdrożeniowe · runbooki awaryjne · ograniczenia i znane ryzyka · lokalne uruchomienie.

## Współpraca
PM: koszt techniczny, warianty, ryzyka, kolejność (nie samo "nie da się"). Frontend/mobile: kontrakt, błędy, paginacja, wersjonowanie. UX/UI: dostępne dane, ograniczenia, realne stany (ładowanie, brak wyników, błąd, brak uprawnień). DevOps/SRE: infrastruktura, wdrożenia, backup, odtwarzanie, pojemność. Bezpieczeństwo: model zagrożeń, authz, audyty.
