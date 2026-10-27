---
name: context
description: Utrzymuje .hq/context.md, szablon /compact, podpowiada nowy czat; dyscyplina tokenów.
---

# Kontekst projektu

`.hq/context.md` = jedyne, co nowy czat musi wczytać, żeby kontynuować pracę. Szablon: `${CLAUDE_PLUGIN_ROOT}/templates/context.md`; brak pliku w projekcie = zaproponuj `/hq:init`.

## Równoległe czaty (wątki)
Kilka czatów w jednym projekcie = kilka wątków. `context.md` jest **wspólny** (cel, stan projektu, decyzje, pułapki, klucz); to, czym zajmuje się dany czat, jest w **jego** pliku `.hq/threads/<slug>.md` (szablon `${CLAUDE_PLUGIN_ROOT}/templates/thread.md`; slug = krótka nazwa tematu, ustal go z użytkownikiem, gdy czat zaczyna temat).
- Czat zapisuje fokus, następne kroki, blokery i handoff **tylko w swoim** pliku wątku; cudzych nie rusza.
- Przed edycją `context.md` wczytaj go ponownie (inny czat mógł go zmienić), edytuj punktowo (Edit), nie przepisuj całości (Write), i nie usuwaj wpisów, których nie rozpoznajesz: mogą pochodzić z innego wątku.
- Decyzja dotycząca tylko jednego wątku idzie do jego pliku; do `context.md` tylko to, co obowiązuje cały projekt.
- Hook SessionStart wczytuje `context.md` i wszystkie wątki; nowy czat dostaje slug wątku, który ma kontynuować, w linii startowej. Zakończony wątek: usuń jego plik.
- Stary `.hq/handoff.md` jest nadal wczytywany (zgodność wsteczna); nowe handoffy piszesz do wątku.

## Kiedy aktualizować
Po: decyzji, ukończonym zadaniu, zmianie kierunku, odkrytej pułapce, ostrzeżeniu hooka `[hq]`, prośbie o nowy czat. Nie po każdej wiadomości.

## Jak (tanio)
1. Przeczytaj plik, edytuj punktowo (Edit), nie przepisuj całości.
2. **Nadpisuj, nie dopisuj**: stan zastępuje stary stan; zrobione zadania znikają z wątku.
3. Limit ~40 linii. Przekroczysz = skompresuj najstarsze/najmniej ważne.
4. Telegraficznie, bez historii rozmowy. Piszesz wniosek, nie przebieg.

## Co zachować, co wyrzucić
Zachowaj: cel, aktualny stan, fokus i następne kroki, decyzje **z powodem**, pułapki i wymagania użytkownika, ścieżki kluczowych plików.
Wyrzuć: dyskusję i odrzucone opcje (zostaw tylko "odrzucone: X, bo Y", jeśli ktoś mógłby do tego wrócić), logi, kod który jest w plikach, rzeczy wynikające z kodu lub gita, kroki już wykonane.

## Kiedy zaproponować nowy czat
Zaproponuj, gdy zajdzie którekolwiek:
- hook `[hq]` zgłosił dużą rozmowę,
- skończony etap/kamień milowy i następne zadanie nie potrzebuje historii,
- zmiana tematu na niezwiązany,
- zaczynasz się powtarzać, gubić szczegóły lub poprawiać własne błędy z wcześniejszych tur.

Procedura: (1) zaktualizuj `context.md`, (2) nadpisz swój `.hq/threads/<slug>.md` (zrobione / fokus / następne / blokery, ≤15 linii), (3) powiedz użytkownikowi w 2 liniach, dlaczego warto, i podaj gotową linię startową dla nowego czatu:
`Kontynuuj projekt, wątek <slug>. Przeczytaj .hq/context.md i .hq/threads/<slug>.md, potem: <następny krok>.`
Nie rób tego częściej niż raz na etap; jeśli użytkownik odmówi, nie ponawiaj bez nowego powodu.

## Nowy czat
Kontekst wczytuje hook SessionStart. Nie czytaj niczego poza `context.md`, swoim wątkiem i plikami potrzebnymi do kroku; resztę dociągaj na żądanie.

## Dyscyplina tokenów
Koszt = rozmiar kontekstu x liczba zapytań (instrukcje, historia, odczytane pliki, wyniki poleceń, opisy narzędzi i skilli). Oszczędzaj widocznością, nie lakonicznością. Komendy poniżej zweryfikowane w dokumentacji Claude Code (strona o kosztach).

**Użytkownik (komendy):** `/clear` przy zmianie zadania (wcześniej `/rename`, później `/resume`; `/clear` nic nie kosztuje) · `/compact <instrukcje>` w długim zadaniu (sam `/compact` czyta całą rozmowę, więc robi się go przed ogromnym kontekstem, nie po) · `/usage` (zużycie i udział skilli, pluginów, subagentów i MCP z rekomendacjami) · `/context` (co zajmuje okno) · `/model` (Sonnet do większości, Opus do złożonych decyzji) · `/effort` (niższy poziom do prostych zadań) · `/mcp` (wyłącz nieużywane serwery) · Shift+Tab plan mode przed dużą zmianą · Esc i `/rewind` przy złym kierunku. Notatka użytkownika wspomina `/autocompact N`: w dokumentacji jest ustawienie "auto-compact window" (strona model-config), nazwę komendy sprawdź w swojej wersji.

**Plugin (zachowania):** stan trzymaj w `.hq/context.md`, `.hq/threads/`, `.hq/pm/tasks.tsv`, nie w rozmowie · nowy czat startuje z `context.md` (hook) · po długiej przerwie cache wygasa i pierwsza wiadomość przetwarza cały kontekst, więc **po przerwie tańszy jest nowy czat z `context.md` niż wznawianie dużej sesji** · hook ostrzega o rozmiarze dwustopniowo (patrz niżej) · duże odczyty, badania i uruchamianie testów idą do subagentów (zwracają podsumowanie) · nie zmieniaj zestawu pluginów i MCP w trakcie sesji (zmiana definicji narzędzi unieważnia cache; wniosek z opisu przyczyn pudeł cache).

**Dwa progi hooka:** hook czyta rzeczywiste tokeny z `usage` ostatniej odpowiedzi (to samo co `/context`) i liczy **przyrost od pierwszej odpowiedzi**, bo stały narzut (narzędzia, skille, MCP) bywa ~90k i nie jest winą rozmowy. Przyrost ≥60k (`HQ_CTX_COMPACT`): podpowiedz `/compact` z szablonem, jeśli to wciąż to samo zadanie; ≥110k (`HQ_CTX_TOKENS`): zaktualizuj `context.md` i swój wątek i zaproponuj nowy czat; kolejne ostrzeżenie dopiero po +50k (`HQ_CTX_STEP`). Brak odpowiedzi w rozmowie = brak pomiaru, brak ostrzeżenia. Po `/compact` licznik spada sam. Duży stały narzut zmniejszysz w `/mcp` i przez wyłączenie nieużywanych pluginów.

**Szablon `/compact`** (wklej, dostosuj):
```
/compact Zachowaj: cel zadania, zmienione pliki, przyjęte decyzje z powodem, nieudane testy, otwarte problemy, ograniczenia użytkownika, następny krok. Usuń: pełne wyniki poleceń i logi, nieaktualne plany, martwe ścieżki, powtórzone treści plików, szczegóły zakończonych kroków.
```
Można go też zapisać na stałe w `CLAUDE.md` w sekcji `# Compact instructions` (dokumentacja potwierdza ten mechanizm; patrz `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE.md`).

**`CLAUDE.md` projektu:** krótki (poniżej 200 linii wg dokumentacji): struktura, zasady, komendy, ograniczenia, ścieżki do szczegółów; specjalistyczne instrukcje przenoś do skilli lub plików wczytywanych na żądanie (`.hq/`, `docs/`). Szablon: `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE.md`.
