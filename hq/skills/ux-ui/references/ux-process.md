# UX: proces i szablony (dla `ux-designer`)

## U1 Discovery - źródła i synteza
Źródła: wywiady, ankiety, analityka, zgłoszenia i reklamacje, obsługa klienta, konkurencja, warsztaty, audyt obecnego produktu. Bez dostępu do nich: desk research (WebSearch, ze źródłami), przegląd konkurencji, a luki zapisz jako `[ZAŁOŻENIE]` + plan sprawdzenia.
Pytania wyjściowe: jaki problem rozwiązuje użytkownik? co robi dziś? gdzie traci czas, myli się, rezygnuje? co uznaje za sukces? jakie ograniczenia mają biznes, technologia, prawo? skąd poznamy, że działa?
Synteza: potrzeby, bariery, persony/archetypy (krótkie: cel, kontekst, ograniczenia, dostępność), mapa podróży, user stories, hipotezy, priorytety. Każdy wniosek z tagiem `[DOWÓD: źródło]` lub `[ZAŁOŻENIE]`.

## U2 Definicja problemu (`problem.md`)
Użytkownik · Potrzeba · Problem · Kontekst (kiedy, gdzie, urządzenie, stres/pośpiech) · Efekt · Miara sukcesu (liczbowa: czas zadania, odsetek ukończeń, błędy) · Poza zakresem.

## U3 Widoki
Architektura informacji, ścieżki, spis bloków i szare makiety: skill `hq:views` (`views/references/process.md`), artefakty w `.hq/views/`. Przegląd heurystyczny niżej stosuj na makietach i prototypie.

## Przegląd heurystyczny (gdy brak ludzi do testu) - 10 heurystyk Nielsena
Widoczność stanu systemu · zgodność z językiem i światem użytkownika · kontrola i swoboda (cofnij/anuluj) · spójność i standardy · zapobieganie błędom · rozpoznawanie zamiast pamiętania · elastyczność i wydajność (skróty) · estetyka i minimalizm · pomoc w rozpoznaniu, diagnozie i naprawie błędów · pomoc i dokumentacja. Wynik: lista problemów z ważnością (blokujący/duży/mały), nie "podoba mi się".

## Komunikat błędu
Co się stało · dlaczego (jeśli wiadomo) · co użytkownik może zrobić dalej. Nigdy samo "wystąpił błąd". Bez winienia. Przy ryzyku: możliwość cofnięcia.

## U5 Testy użyteczności
Plan: cel i hipotezy · uczestnicy (różnorodni: poziom doświadczenia, potrzeby dostępności; ok. 5 na rundę wystarcza do wykrycia głównych problemów) · zadania realistyczne bez podpowiadania · metryki (ukończenie, czas, błędy, rezygnacje, zadowolenie) · skrypt prowadzącego (bez sugerowania). Obserwuj zachowanie, nie opinie. Raport: wynik na zadanie, gdzie się zatrzymali, błędy, cytaty, przyczyny, rekomendacje z ważnością.

## U6 Iteracja
Obserwacja -> analiza przyczyny (nie kosmetyka, zmiana struktury, jeśli to ona zawiodła) -> nowa hipoteza -> zmiana -> ponowny test -> potwierdzenie poprawy metryką. Zapis w `decisions.md`.

## Kontekst projektowy (dopasuj, nie narzucaj)
Początkujący vs ekspert · pośpiech · stres · mały ekran · dużo danych · wysokie bezpieczeństwo · wiele języków (długość tekstów) · słabe łącze · ekran urządzenia bez myszy (fokus, kierunki, przyciski fizyczne).

## Współpraca
Produkt (priorytety, zakres, kompromisy, miary) · UI (struktura, ścieżki, stany, wyniki testów, intencje) · Developerzy (wykonalność, wydajność, obsługa błędów, dane, ograniczenia platformy, testowanie) · Badacz (jeśli jest). Dokumentuj "dlaczego", nie tylko "co".
