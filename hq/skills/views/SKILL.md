---
name: views
description: Plan widoków przed kodem - mapa podstron/ekranów, spis bloków z uzasadnieniem, szare makiety mobile-first, SEO, bramka akceptacji.
---

# Widoki: co gdzie i dlaczego, zanim powstanie wygląd i kod

Po ustaleniu fundamentu (problem, funkcje, architektura), a przed wyglądem (`hq:ux-ui` U4) i kodem (`hq:frontend`), planujesz **wszystkie widoki**: jakie podstrony/ekrany, co na nich jest, w jakiej kolejności i po co. Wynik to specyfikacja widoków + szare makiety HTML (szare pola z etykietą typu, bez kolorów, fontów marki i copywritingu). Makieta to kontrakt dla UI i kodu, nie obrazek. Wykonuje agent `ux-designer`; Ty pytasz użytkownika i pokazujesz zrzuty.

## Zasady
1. **Najpierw specyfikacja, potem HTML.** Decyzje zapadają w spisie bloków, makieta je tylko pokazuje; HTML niezgodny ze specyfikacją to błąd.
2. **Każdy blok ma powód**: zadanie użytkownika lub obawę, którą rozwiązuje, priorytet P1-P3, źródło danych z fundamentu, co się stanie po usunięciu. Brak powodu = usuń. Brak źródła danych (cena, dostępność, opinie) = pytanie, nie zmyślona funkcja.
3. **Kolejność = kolejność decyzji użytkownika** (np. co to i gdzie -> czy dla mnie -> ile i kiedy -> czy można ufać -> jak zarezerwować), nie szablon „hero + 3 karty”.
4. **Mobile-first to priorytet treści**: najpierw 360-390 px, jeden główny cel na widok; tablet i desktop wykorzystują miejsce (kolumny, porównania), nie rozciągają mobile.
5. **Najpierw ścieżki, potem makiety**: kluczowe zadania jako wireflow z błędami i powrotami, bo zmieniają zestaw widoków.
6. **SEO w architekturze, nie w makiecie**: osobny `seo.md` (intencja, URL, nagłówki, linki, schema); struktura gotowa na rozbudowę (oferty, blog, języki) bez martwych pustych sekcji.
7. **Najpierw widoki krytyczne** (5-8), zatwierdzenie wzorca, potem reszta na tych samych prymitywach (`assets/wire.css`).
8. **Psychologia bez manipulacji**: zasady z dowodem i znanym nadużyciem (`references/principles.md`); zero dark patterns (fałszywa pilność, ukryte koszty, wabiki cenowe).
9. **AI nie zatwierdza sama.** Najwyżej `ready_for_review`; `approved` nadaje tylko użytkownik. Zmiana zatwierdzonego widoku = nowa wersja do akceptacji.

## Etapy (szczegóły i szablony: `references/process.md`)
| Etap | Wynik w `.hq/views/` | Warunek przejścia |
|---|---|---|
| V0 Wejście: fundament, typ projektu i profil (`references/profiles.md`), platformy, ograniczenia, dane o ruchu mobile/desktop | `brief.md` | fundament zatwierdzony; brak = `blocked` i pytania |
| V1 Cele: zadania użytkownika (top tasks), cel biznesowy i miara, pytania i obawy w kolejności, intencje wyszukiwania | `brief.md` | cele i miara zatwierdzone przez użytkownika |
| V2 Ścieżki: wireflow kluczowych zadań (kroki, decyzje, błędy, powrót, potwierdzenie) | `flows.md` | każde zadanie ma koniec i wyjście z błędu |
| V3 Architektura: mapa widoków z ID, URL, typem, nawigacją, relacjami; model treści; `seo.md` | `views.tsv`, `seo.md` | każde zadanie osiągalne od wejścia; **akceptacja użytkownika** |
| V4 Spis bloków każdego widoku z uzasadnieniem i stanami | `specs/<VIEW-ID>.md` | każdy blok ma powód i dane |
| V5 Szare makiety: mobile -> tablet -> desktop, zrzuty | `wireframes/` | wszystkie widoki krytyczne wyrenderowane |
| V6 Kontrola automatyczna + test „świeżych oczu” + przejście ścieżek + pre-mortem (`references/quality.md`) | `qa.md` | zero FAIL, rubryka ≥90/100, warunki bezwzględne |
| V7 Przegląd niezależny: `hq:design-reviewer` | `qa.md` | brak blokujących uwag -> `ready_for_review` |
| V8 Akceptacja: zrzuty mobile i desktop, uwagi, iteracje (max 2 rundy na uwagę, potem decyzja użytkownika) | `status.md` | **użytkownik**: `approved` + wersja |

Skala: **Mini** (landing, 1-3 widoki: V0-V1 razem, V3 skrót, V5-V8), **Standard** (wszystko), **Pełna** (+ test z ludźmi: 5 osób, zadania z `flows.md`; przygotowujesz skrypt, ludzi daje użytkownik). Zapytaj o skalę na początku.

## Narzędzia
- Makiety z prymitywów `${CLAUDE_PLUGIN_ROOT}/skills/views/assets/wire.css`; wzór: `${CLAUDE_PLUGIN_ROOT}/skills/views/assets/example.html` (skopiuj css do `.hq/views/wireframes/`).
- Kontrola i zrzuty: `node ${CLAUDE_PLUGIN_ROOT}/skills/views/scripts/wirecheck.mjs <plik.html> [--app] [--out <katalog>]` z katalogu projektu (Playwright z projektu wg `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/visual.md`). Sprawdza szerokości 360/768/1280: przewijanie w bok, kolory, cele dotykowe, H1 i nagłówki, landmarki, etykiety pól, linki nawigacji jako `<a href>`, główne CTA i strefę kciuka, priorytety bloków; zapisuje PNG. Zrzut otwórz (Read), zanim napiszesz, że wygląda dobrze.
- CLI/TUI: zamiast HTML zapis sesji terminala (polecenie -> wynik -> błąd -> pomoc) w `wireframes/*.txt`.

## Gdzie w procesie
Wejście: `hq:product-management` (wymagania), `hq:system-architect` (moduły, dane). Wyjście: `hq:ux-ui` U4 (kierunek wizualny na zatwierdzonych makietach), `hq:frontend` (nie buduje nowego widoku bez `approved`), `hq:marketing` (treści i SEO na podstawie `seo.md`). Teksty na koniec: `design:ux-copy` lub `hq:brand` (język marki). Wiedza z zewnątrz o wzorcach branży: `hq:external-ai` (Perplexity).

## Definicja gotowości
`status.md` = `approved` z wersją i datą · każdy top task przechodzi ścieżkę bez martwych końców · każdy widok: cel, główna akcja (lub powód braku), bloki z powodem i danymi, stany · `wirecheck` bez FAIL na 360/768/1280 · `seo.md` dla stron publicznych · decyzje i odrzucone warianty w `decisions.md`. Potem `hq:context`.
