---
name: ux-ui
description: UX i UI - badania, ścieżki, wireframe, design system, stany, dostępność, handoff.
---

# UX i UI: od problemu do wdrożonego interfejsu

UX odpowiada za **logikę doświadczenia** (czy użytkownik osiąga cel szybko i bez frustracji). UI nadaje jej **formę** (hierarchia, system, dostępność, spójność). Cel: czytelny, spójny, przewidywalny, dostępny i możliwy do wdrożenia interfejs - nie "ładne ekrany". Najpierw problem, potem struktura, na końcu detal.

## Zasady
1. **Fakty a założenia.** Nie masz dostępu do prawdziwych użytkowników. Każdy wniosek oznacz `[DOWÓD]` (dane, wywiad, test, źródło) albo `[ZAŁOŻENIE]` (do sprawdzenia). Nie podawaj założeń jako wyników badań. Badania z ludźmi robi użytkownik (Ty przygotowujesz skrypt, zadania, metryki i analizujesz wyniki); do tego czasu działasz na desk research, danych, przeglądzie eksperckim (heurystyki) i hipotezach.
2. **Projektuj całą ścieżkę i wszystkie stany**, nie tylko idealny ekran.
3. **System, nie pojedyncze ekrany**: tokeny + komponenty z wariantami.
4. **Dostępność od początku**, nie przed publikacją.
5. **Marka jest wejściem**: marka efektywna (linia `Marka:` z hooka, zasady w `hq:brand`) daje styl, rdzeń organizacji nienaruszalny; UI adaptuje go do czytelności, dostępności i responsywności, nie kopiuje mechanicznie. Brak brandbooka = zaproponuj `hq:brand` Mini.
6. **Dodawaj tylko to, co poprawia zrozumienie.** Pytanie kontrolne: co mogę usunąć, żeby było jaśniej?
7. **Projektuj w Figmie.** Wireframe'y, ekrany, komponenty i tokeny powstają w Figmie (`${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/figma.md`: podłączenie Figma MCP, link do pliku); HTML tylko jako prototyp lub za zgodą użytkownika.
8. **Poziom 4, nie średnia.** Jedna wizja i motyw przewodni przed ekranami; AI wykonuje, człowiek kieruje (`direction-and-patterns.md`). Nie generuj ekranów bez systemu designu z referencji (`anti-slop.md`). Ładne bez statusu, cofnięcia i wyjścia z błędu to teatr designu (`premium-craft.md`).
9. **Programiści wcześnie** (wykonalność, wydajność, gotowe komponenty), nie dopiero przy handoffie.

## Jak pracujesz
Ty (główny wątek) zadajesz użytkownikowi pytania (`AskUserQuestion`, paczki ≤4, z opcjami i rekomendacją) i **pokazujesz przykłady do wyboru** (widżet wizualny, jeśli dostępny, albo plik HTML do otwarcia w przeglądarce: wireframe'y, 2 warianty wizualne, prototyp). Agenci (`ux-designer`, `ui-designer`) przygotowują artefakty i nie pytają użytkownika. Artefakty w `.hq/ux-ui/`; decyzje i powody w `decisions.md` (wspólne z `.hq/product/` jeśli istnieje).

**Skala:** Mini (1-3 ekrany, skrót U1 do pytań + U3-U6), Standard (pełne), Pełna (+ badania z użytkownikami, testy dostępności z technologiami asystującymi). Zapytaj na początku i o platformę (web, mobile, desktop, ekran urządzenia/embedded - wtedy dochodzą ograniczenia rozdzielczości, wejścia, pamięci).

## Etapy i bramki
| Etap | Kto | Wynik | Zatwierdza |
|---|---|---|---|
| U1 Discovery i synteza: użytkownicy, cele, kontekst, konkurencja, dane, ograniczenia; potrzeby, bariery, persony/archetypy, user stories, hipotezy | `ux-designer` | `research.md` | - |
| U2 **Definicja problemu**: użytkownik, potrzeba, problem, kontekst, efekt, miara sukcesu | `ux-designer` | `problem.md` | **użytkownik** |
| U3 Architektura informacji, ścieżki (z błędami, rozgałęzieniami, punktami rezygnacji), wireframe'y, przegląd heurystyczny | `ux-designer` | `ia.md`, `flows.md`, `wireframes/` | **użytkownik** |
| U4 UI: brief, analiza treści, **dwa warianty kierunku wizualnego**, tokeny, komponenty ze stanami, ekrany ze wszystkimi stanami, dostępność | `ui-designer` | `tokens.css`, `design-system.md`, `screens/` | **użytkownik** (wybór wariantu) |
| U5 Prototyp klikalny i testy użyteczności (skrypt, zadania, metryki; ludzi dostarcza użytkownik) | `ux-designer` + `ui-designer` | `prototype/`, `test-results.md` | - |
| U6 Iteracja: obserwacja -> przyczyna -> hipoteza -> zmiana -> ponowny test | oba | zaktualizowane artefakty | **użytkownik** przy zmianach strukturalnych |
| U7 Handoff i weryfikacja wdrożenia: paczka dla developerów (`hq:frontend`, przegląd handoffu przed kodem), współpraca w trakcie, porównanie wdrożenia ze specyfikacją | `ui-designer` | `handoff.md` | - |
Przeglądy bramek U3, U4, U7: `hq:design-reviewer`. Nie przechodź dalej bez zatwierdzenia bramki.

## Reużywaj, co już jest
Dane ilościowe o zachowaniach i wyniki ankiet: `hq:data-analysis`; research użytkowników i konkurencji: `hq:research`.
Jeśli dostępne, korzystaj z istniejących skilli zamiast pisać od zera: `design:accessibility-review`, `design:design-critique`, `design:ux-copy`, `design:design-handoff`, `frontend-design`. Szczegóły procesu: `references/ux-process.md`, `references/ui-system.md`. Na żądanie: `references/premium-craft.md` (status/cofnięcie/błędy, testy długiej sesji i psucia, emocje), `references/direction-and-patterns.md` (poziomy 1-4, rubryka 15 pkt, wzorce list i filtrów), `references/onboarding-paywall.md` (długość onboardingu, paywall), `references/anti-slop.md` (przepływ spec -> referencja -> system -> ekrany, lista wykrywania generyczności). Kontrast: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/brand/scripts/contrast.py`.

## Definicja gotowości
Problem i miara sukcesu zatwierdzone · ścieżki obejmują błędy i wyjątki · każdy krok mówi: co zrobiono, jak cofnąć, co dalej · test długiej sesji i celowego psucia (sieć, płatność, limit) · ten sam przypadek wygląda tak samo na wszystkich ekranach · każdy komponent ma stany · każdy ekran ma stany (pusty, ładowanie, błąd, offline, brak uprawnień, długa treść, brak danych, sukces, nieaktywny) · kontrasty i cele dotykowe sprawdzone · wyniki testów lub jawnie oznaczone luki `[ZAŁOŻENIE]` · tokeny i komponenty w pliku wspólnym z kodem · handoff z intencjami · decyzje zapisane. Po zakończeniu: `hq:context`.
