# Fazy: wejście, praca, wyjście

| Faza | Kto pracuje (równolegle gdzie `||`) | Wyjście (dowód) | Przegląd |
|---|---|---|---|
| 1 Koncepcja | strateg; architekt (wstępne ryzyka) | `requirements.md` (funkcje MUST/SHOULD/NICE, kryteria sukcesu, koszt docelowy, ograniczenia), lista niepewności, zatwierdzenie użytkownika | wymagań |
| 2 Prototyp koncepcyjny | dyscypliny wg ryzyk `||` | wyniki eksperymentów: założenie -> pomiar -> wniosek; zaktualizowane `risks.md` | ryzyk |
| 3 Architektura i projekt | architekt (najpierw), potem elektronika `||` firmware `||` algorytmy `||` mechanika `||` design `||` QA (plan testów) | `architecture.md`, `interfaces.md`, plany dyscyplin, plan testów, make-vs-buy | architektury, interfejsów |
| 4 Integracja | integrator (Ty) + dotknięte dyscypliny | działający system na prototypie, lista rozbieżności interfejsów (zamknięta) | prototypu |
| 5 Walidacja | QA; dyscypliny poprawiają | raport testów po poziomach, RCA usterek, decyzje o zmianach | wyników testów |
| 6 Finalizacja | produkcja, QA, elektronika, mechanika | zamrożony projekt, zatwierdzony BOM, instrukcje montażu, stanowiska testowe, partia pilotażowa, dokumentacja serwisowa | gotowości produkcyjnej |
| 7 Produkcja i rozwój | produkcja, QA, strateg | pętla: dane z serwisu/reklamacji -> backlog wersji | gotowości rynkowej |

## Etapy walidacji sprzętu (typowe nazwy)
- **EVT** (potwierdzenie koncepcji inżynierskiej): działa funkcjonalnie, rozwiązuje ryzyka techniczne.
- **DVT** (potwierdzenie pełnego designu): projekt kompletny, testy niezawodności i zgodności, zbliżony do finalnego.
- **PVT** (potwierdzenie produkcyjne): z linii/procesu docelowego, powtarzalność i wydajność.
Zakres dopasuj do skali: pojedynczy egzemplarz dla siebie = uproszczone EVT/DVT; seria = pełne.

## Zasady przejścia
Nie wchodzisz w fazę, jeśli poprzednia nie ma wpisu w `gates.md` z dowodem. Największe ryzyka (top 3) wypisujesz na każdym przeglądzie razem ze sposobem sprawdzenia. Niezamknięte ryzyko krytyczne = blokada.
