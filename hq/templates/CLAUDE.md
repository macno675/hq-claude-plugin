# <Projekt>

<!-- hq-begin (blok zarządzany przez hq:init; edytuj poza znacznikami) -->
## hq (obowiązuje w całej rozmowie, także po /compact i /clear)
- Zadanie wieloetapowe lub domenowe (kod, marka, elektronika, PM, produkt, finanse, marketing, bezpieczeństwo, research...): najpierw skill `hq:orchestrator`, potem tylko wybrany skill/agent `hq:*`. Nie rób sam tego, co ma agent hq.
- Marka i organizacja: linie `[hq] Marka/Organizacja` ze startu sesji; nowe materiały wizualne i teksty zgodne z brandbookiem (`hq:brand`).
- Stan: czytaj `.hq/context.md` i `.hq/handoff.md`; po ważnej zmianie aktualizuj (`hq:context`). Zadania: `.hq/pm/tasks.tsv`.
- Długa rozmowa lub zmiana zadania: `hq:context` (handoff, nowy czat), nie ciągnij historii.
<!-- hq-end -->

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
