# Szablony i reguły zarządzania projektem

## Karta projektu (`charter.md`)
Cel biznesowy · problem, który rozwiązuje · jak poznamy sukces (mierzalnie) · interesariusze (rola, czego oczekuje, wpływ) · ograniczenia: czas / budżet / zakres / jakość (**priorytet: co jest sztywne, co elastyczne**) · główne ryzyka · uprawnienia decyzyjne (kto zatwierdza co) · wstępny harmonogram i kamienie · założenia `[ZAŁOŻENIE]`.

## Zakres (`scope.md`)
Cele · rezultaty (konkretne) · funkcje i wymagania · **wykluczenia (czego nie robimy)** · kryteria akceptacji dla każdego rezultatu · definicja "gotowego" · zasady zgłaszania i oceny zmian. Zakres chroni przed pełzaniem: nowe wymaganie bez oceny wpływu nie wchodzi.

## WBS (`wbs.md`)
Drzewo: rezultat -> faza -> pakiet pracy -> zadanie; przy każdym: właściciel i oczekiwany rezultat. Rozmiar zadania: da się ocenić postęp (typowo 1-5 dni), nie tworzy zbędnej administracji.

## Zadania (`tasks.tsv`, kolumny rozdzielone tabulatorem)
`id | tytuł | właściciel | dni | zależy_od | status | definicja_ukończenia | typ | termin`
- `dni`: dni robocze (dla kamienia 0). Dla zadań agentowych uwzględnij czas na decyzje i akceptacje użytkownika.
- `zależy_od`: id po przecinku. `status`: todo / doing / blocked / done. `typ`: zadanie / kamień. `termin`: twardy termin (RRRR-MM-DD), opcjonalnie.
- Orkiestrator dobiera następne zadanie z tego pliku: najpierw na ścieżce krytycznej i odblokowujące innych, potem największa wartość, potem równoległe, na końcu odkładane.

Kolejność priorytetów: 1) co blokuje innych, 2) co wpływa na kamień milowy, 3) co ma największą wartość biznesową, 4) co można robić równolegle, 5) co można odłożyć.

## Kamień milowy
Jasna definicja ukończenia · data · właściciel · kryteria akceptacji · znaczenie dla dalszej części. Przykłady: zatwierdzone wymagania, zakończona architektura, gotowy prototyp, zakończone testy, projekt zatwierdzony do produkcji, start produkcji, premiera. Nie: "spotkanie", "prezentacja".

## Przydział
Jeden właściciel na zadanie. Uwzględnij: kompetencje, dostępność, obecne obciążenie (`schedule.py` zgłasza nakładanie się zadań jednego właściciela), zależności, priorytet, ryzyko, potrzebne informacje i narzędzia. Ogranicz równoległość (WIP).

## Monitoring
Przy każdej bramce, kamieniu i zmianie: zaktualizuj statusy, uruchom `schedule.py`, porównaj koniec z terminami, wypisz zagrożone/opóźnione/zablokowane, zmiany zakresu, obciążenie, ryzyka. Opóźnienie na ścieżce krytycznej = natychmiast opcje. Postęp realny (kryterium ukończenia spełnione), nie deklarowany.

## Ryzyka
`ryzyko | prawdopodobieństwo | wpływ | właściciel | zapobieganie | reakcja | status | przegląd do`. Ryzyko to zdarzenie, które może wystąpić; problem to ryzyko zmaterializowane (przenieś do blokad i zadań naprawczych). Przegląd regularny, działanie zanim stanie się problemem. Wpływy finansowe: `hq:budget`.

## Zmiana (`changes.tsv`)
`id | opis | wpływ: zakres / termin / budżet / jakość / zasoby / ryzyko / kamienie | opcje | rekomendacja | decyzja (kto, kiedy) | status`.
Opcje do rozważenia: dodać zasób · przesunąć termin · zmniejszyć zakres · zmienić priorytety · zaakceptować ryzyko · odrzucić zmianę. Zmiana nie jest przyjmowana bez świadomej decyzji o koszcie (liczy `hq:budget`) i źródle środków.

## Raport statusu (`reports/AAAA-MM-DD.md`, jedna strona)
Status (ZIELONY/ŻÓŁTY/CZERWONY z jednym zdaniem dlaczego) · cel i kamień najbliższy (data, prognoza) · ścieżka krytyczna i koniec projektu (z `schedule.py`) · zrobione od ostatniego raportu · zagrożone/zablokowane z opcjami · top ryzyka · zmiany · **decyzje potrzebne od użytkownika z datą**. Zespół: szczegóły operacyjne; decydent: status, ryzyka, decyzje. Raport jest krótki i rzetelny, nie obrona przeszłości.

## Zamknięcie
Rezultaty dostarczone i spełniają kryteria akceptacji · zadania i ryzyka zamknięte · budżet i zasoby rozliczone (`hq:budget`) · wnioski (co zadziałało, co nie, szacunki vs rzeczywistość) do `~/.hq/pm-lessons.md` · dokumentacja zarchiwizowana · przekazanie do utrzymania lub następnego etapu.

## Dokumentacja (jedno źródło prawdy)
Karta · interesariusze · zakres · WBS · harmonogram · kamienie · macierz odpowiedzialności · ryzyka · zmiany · plan komunikacji · raporty · decyzje · wnioski. Dokumentacja nie jest biurokracją, tylko utrzymaniem wspólnej wersji prawdy.

## Kalendarz
Po wyraźnej zgodzie użytkownika można utworzyć wydarzenia dla kamieni milowych i decyzji w jego kalendarzu (dostępne konektory). Nie rób tego z własnej inicjatywy; wydarzenia z zaproszeniami dla innych osób wymagają osobnej zgody.
