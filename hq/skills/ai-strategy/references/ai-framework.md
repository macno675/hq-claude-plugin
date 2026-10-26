# Ramy strategii AI

## Przypadki użycia (`usecases.tsv`)
`id | przypadek | problem i skala | wartość (miara) | wykonalność | dane (dostępne/legalne/jakość) | koszt | ryzyko (koszt błędu) | czas | wpływ na użytkownika | zgodność | alternatywa bez AI | decyzja | właściciel`
Pytania: czy problem istnieje i jak duży? czy wystarczy reguła/automatyzacja/analityka? co się stanie, gdy model się pomyli (kto ucierpi, jak wykryjemy)? jak zmierzymy wartość (przed/po, na prawdziwych danych)? Każdy przypadek ma cel, miarę sukcesu i właściciela. Zasada: najprostsze rozwiązanie, które działa.

## Kup / open-source / zbuduj / fine-tuning / RAG (osobno dla zastosowania)
| Opcja | Kiedy | Główne ryzyko |
|---|---|---|
| Gotowe API | szybkie wdrożenie, standardowy problem, brak potrzeby pełnej kontroli | uzależnienie od dostawcy, koszty, warunki przetwarzania danych |
| Model open-source | potrzebna kontrola i elastyczność | utrzymanie, bezpieczeństwo, jakość, odpowiedzialność |
| Własny model | unikalne dane, przewaga, wymagania specjalistyczne | koszt, czas, zespół i dane |
| Fine-tuning | model ogólny blisko celu, wymaga dostosowania | jakość danych, koszt, przetrenowanie |
| RAG (wiedza firmy) | odpowiedzi na podstawie aktualnej wiedzy | jakość bazy wiedzy, kontrola dostępu, aktualność |
Zacznij od najprostszego (prompt + dobre dane/RAG) i przechodź wyżej tylko z dowodem, że za mało. Dla decyzji strategicznych: ADR (`hq:tech-strategy`, TCO, plan wyjścia). Własne trenowanie bez wyraźnej przewagi = kosztowne ego projektu.

## Dane
Skąd pochodzą · właściciel · czy legalnie można je użyć (licencje, zgody, dane osobowe - `hq:legal-safety`) · kompletność, aktualność, błędy, uprzedzenia · przechowywanie · kto ma dostęp · ochrona · usuwanie · monitorowanie w czasie. Jakość danych i jasne uprawnienia ważniejsze niż wybór modelu. Nie wprowadzaj do zewnętrznych narzędzi AI danych, do których nie masz prawa lub które są wrażliwe, bez decyzji użytkownika.

## Architektura systemu AI (nie tylko prompt)
Źródła i cykl życia danych · model(e) (z routingiem według zadania i kosztu) · warstwa promptów i reguł (wersjonowana) · **walidacja odpowiedzi** (schemat, reguły, weryfikacja źródeł, odmowa gdy brak pewności) · ograniczenia bezpieczeństwa (najmniejsze uprawnienia narzędzi, brak ufania treści z wejścia - prompt injection, filtrowanie wyjścia) · integracja z produktem · monitoring i logi (bez zbędnych danych wrażliwych) · kontrola kosztów (limity, cache, krótszy kontekst, tańszy model do prostych zadań) · możliwość aktualizacji/wymiany modelu · ścieżka awaryjna (degradacja do reguł/człowieka). System testowalny, obserwowalny, odwracalny.

## Testy (zestaw własny `eval/`)
Zbiór przykładów reprezentatywnych + skrajnych + nadużyć (20-50 na start; rośnie z incydentów) z oczekiwanym wynikiem · metryki dopasowane do zadania (poprawność, kompletność, format, spójność między uruchomieniami, odmowy) · odporność na błędne dane i manipulację (prompt injection, jailbreak) · halucynacje (czy twierdzenia mają źródło) · uprzedzenia (różne grupy/języki) · prywatność (wycieki danych) · bezpieczeństwo · wydajność i koszt zapytania · obciążenie · jakość w języku użytkowników. Wyniki zapisane i porównywane między wersjami modeli/promptów. Zmiana modelu/promptu = ponowny test. Nie ufaj ocenie "na oko" ani jednej próbie.

## Nadzór człowieka
Ustal: które decyzje system może podejmować sam · które wymagają zatwierdzenia · jak użytkownik może zakwestionować wynik i jak wygląda odwołanie · jak zgłaszać błędy · kto odpowiada za decyzję · kiedy system trzeba wyłączyć (kryteria + wyłącznik). Decyzje o dużym wpływie na człowieka: zawsze kontrola człowieka. Systemy działające autonomicznie (agenci z narzędziami): minimalne uprawnienia, potwierdzenie akcji nieodwracalnych i zewnętrznych (płatności, wiadomości, usuwanie), log działań.

## Monitorowanie
Jakość odpowiedzi (próbkowanie i metryki) · dryf danych i zachowania · koszty · wydajność · bezpieczeństwo i nadużycia · skargi i zgłoszenia · błędy krytyczne · wpływ na procesy. Przeglądy okresowe (wysokie ryzyko częściej). Alerty z właścicielem i procedurą.

## Governance
- **Polityka użycia AI** (`policy.md`): jakie dane wolno i nie wolno wprowadzać · jak weryfikować wyniki · kto odpowiada za decyzję · zgłaszanie błędów · dokumentowanie użycia · zatwierdzone narzędzia · zastosowania wymagające zgody.
- **Rejestr systemów AI** (`ai-register.tsv`): `system | cel | właściciel | dostawca/model (wersja) | dane (kategorie) | poziom ryzyka | nadzór | ostatni test | następny przegląd | status`. Wpisz też własne narzędzia pracy (np. agenci i modele tego pluginu).
- **Etyka i zgodność:** prywatność, przejrzystość, sprawiedliwość, ograniczanie uprzedzeń, bezpieczeństwo, możliwość wyjaśnienia, zgodność z przepisami (w UE rozporządzenie o AI opiera się na klasyfikacji ryzyka - **ustalenie kategorii i obowiązków DO WERYFIKACJI z prawnikiem**), odpowiedzialność za skutki.

## Dokumentacja
Cele zastosowań · dane i pochodzenie · modele i dostawcy (wersje) · ograniczenia · testy i wyniki · ryzyka · zasady nadzoru · procedury awaryjne · koszty · decyzje architektoniczne (ADR) · zmiany wersji modeli · wyniki monitorowania.

## Edukacja zespołu
Krótkie szkolenie: co AI potrafi i czego nie, jak weryfikować, jakie dane chronić, jak zgłaszać błędy.
