# <Projekt>

## Cel
<1-2 zdania: co budujemy, dla kogo>

## Struktura
- <ścieżka> - <rola>

## Zasady
- Najpierw plan (max 8 punktów) przy zadaniach powyżej 3 kroków; małe, zamknięte zadania.
- Czytaj fragmenty plików (grep, offset/limit), nie całe pliki ani całe repozytorium bez potrzeby.
- Ograniczaj wyniki poleceń: testy tylko zmienionego modułu, pokaż błędy i ostatnie linie.
- Nie dodawaj zależności bez zgody. Nie zmieniaj publicznego API bez zgody.
- Stan pracy: `.hq/context.md` i `.hq/handoff.md`; zadania: `.hq/pm/tasks.tsv`.
- Zadania wieloetapowe/domenowe: zacznij od skilla `hq:orchestrator`.

## Polecenia
- Testy: <polecenie> · Testy modułu: <polecenie> · Build: <polecenie>

## Szczegóły (wczytuj na żądanie)
- Architektura: docs/architecture.md · API: docs/api.md · Testy: docs/testing.md

# Compact instructions
Przy kompaktowaniu zachowaj: cel zadania, zmienione pliki, decyzje z powodem, nieudane testy, otwarte problemy, ograniczenia, następny krok. Usuń: logi i pełne wyniki poleceń, nieaktualne plany, martwe ścieżki, powtórzone treści plików.
