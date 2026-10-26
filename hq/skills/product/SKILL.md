---
name: product
description: Produkt wielodyscyplinarny od pomysłu do produkcji - fazy, interfejsy, zespół agentów, przeglądy.
---

# Produkt jako jeden system

Dyscypliny nie pracują po kolei ("elektronika, potem program, potem obudowa"). Pracują **równolegle na wspólnej architekturze, wspólnych wymaganiach i uzgodnionych interfejsach**. Ty (główny wątek) jesteś właścicielem produktu i architektem-integratorem; użytkownik zatwierdza cel, budżet i większe kompromisy. Agenci wykonują prace dyscyplin; pytania do użytkownika zadajesz sam.

## Skala (oszczędność tokenów)
Uruchamiaj tylko dyscypliny, których produkt potrzebuje. Mały moduł PCB = strateg (lekko) + `electronics`. Aplikacja bez sprzętu = strateg + architekt + coder/firmware + QA. Pełna ekipa tylko dla produktu z elektroniką, kodem, obudową i interfejsem. Każdy agent dostaje paczkę zadaniową (cel, jego sekcja architektury, interfejsy, które go dotyczą), nie całą dokumentację.

## Zespół = agenci
| Obszar | Agent | Model |
|---|---|---|
| Wizja, strategia produktu, roadmapa, backlog (RICE), wymagania, koszt docelowy | skill `hq:product-management` (`hq:product-strategist` jako Product Manager) | sonnet |
| Plan realizacji: zakres, zadania, harmonogram, ścieżka krytyczna, kamienie, zmiany, status | skill `hq:pm` (`project-manager`) | sonnet |
| Budżet, rezerwy, prognoza kosztu (EAC), odchylenia, koszt zmian | skill `hq:budget` (`budget-manager`) | sonnet |
| Architektura, interfejsy, ryzyka, plan testowania modułów | `hq:system-architect` | opus |
| Wybór technologii i protokołów, build vs buy vs partner, TCO, dostawcy, ADR | skill `hq:tech-strategy` (`technology-strategist`) | opus |
| Elektronika (części, schemat, PCB) | skill `hq:electronics` + `parts-sourcer`, `eda-engineer` | - |
| Firmware i oprogramowanie urządzenia | `hq:firmware-engineer` | sonnet |
| Backend, API, dane, integracje, wdrożenie i utrzymanie usług | skill `hq:backend` (`backend-engineer`) | sonnet |
| Implementacja interfejsu w kodzie (komponenty, stan, integracja, wydajność, dostępność) | skill `hq:frontend` (`frontend-engineer`) | sonnet |
| Algorytmy i własne technologie | `hq:algorithm-engineer` | opus |
| Mechanika, obudowa, termika | `hq:mechanical-engineer` | sonnet |
| Marka i brandbook (strategia, identyfikacja, język) - **przed designem produktu** | skill `hq:brand` (`brand-strategist`, `brand-designer`, `brand-copywriter`) | - |
| Design produktu fizycznego, feeling i feedback sprzętowy (dziedziczy markę) | `hq:industrial-designer` | sonnet |
| Doświadczenie i interfejs cyfrowy (aplikacja, strona, panel, ekran urządzenia) | skill `hq:ux-ui` (`ux-designer`, `ui-designer`) | sonnet |
| Testy, walidacja, jakość, przyczyny źródłowe | `hq:qa-engineer` | sonnet |
| Produkcja, łańcuch dostaw, serwis | `hq:manufacturing-engineer` | sonnet |
| Niezależny przegląd każdej bramki | `hq:design-reviewer` | opus |
Aplikacje i kod ogólny: `hq:coder`, `hq:planner`, `hq:reviewer`.

## Wspólne źródło prawdy: `.hq/product/`
`requirements.md` · `architecture.md` · `interfaces.md` (właściciel: architekt) · `decisions.md` · `risks.md` · `changes.tsv` · `gates.md`. Każdy agent pisze **tylko do własnego pliku/sekcji** (brak konfliktów przy pracy równoległej); wspólne pliki aktualizujesz Ty lub architekt. Gdy istnieje `.hq/product/`, `decisions.md` i `risks.md` są wspólne dla elektroniki.

## Fazy i bramki (szczegóły: `references/phases.md`)
0. **Marka (jeśli brak brandbooka):** uruchom skill `hq:brand` (skala Mini wystarcza dla małych projektów). Produkt organizacji: tryb marki z `hq:org` (domyślnie dziedziczy; produkt wymagający innego designu: `rozszerza` lub `odrębna-zgodna`, nigdy łamanie rdzenia).
1. **Koncepcja:** problem, użytkownik, cel, wymagania, kryteria sukcesu, największe niepewności. Strateg -> Ty -> użytkownik zatwierdza.
2. **Prototyp koncepcyjny:** tanie eksperymenty rozstrzygające najgroźniejsze ryzyka (nie "ładny prototyp").
3. **Architektura i projekt:** architekt dzieli na moduły i **specyfikację interfejsów** (`references/interfaces-and-change.md`); po zatwierdzeniu dyscypliny pracują równolegle, ciągle uzgadniając interfejsy.
4. **Integracja:** łączenie podsystemów (elektronika + firmware, mechanika + elektronika, UI + funkcje, algorytmy + prawdziwe dane).
5. **Walidacja:** testy na wszystkich poziomach, prototypy wcześnie i często; kontrolowane poprawki.
6. **Finalizacja:** zamrożenie projektu, BOM, instrukcje, stanowiska testowe, partia pilotażowa.
7. **Produkcja i rozwój:** dane z serwisu i testów -> kolejne wersje.
Przejście do kolejnej fazy = przegląd `design-reviewer` + zapis w `gates.md`. **Produkt kończy się przy powtarzalnej produkcji, nie gdy prototyp działa.**

## Zasady
- Jeden cel, wspólna architektura, jasne interfejsy, właściciel każdego obszaru.
- Recenzja każdej ważnej decyzji; decyzje i ryzyka zapisane (z uzasadnieniem i sposobem sprawdzenia).
- Testy planowane razem z architekturą, nie po awarii.
- **Własna technologia tylko z mierzalną przewagą** (wydajność, koszt, niezawodność, UX, niezależność): decyzję prowadzi `hq:tech-strategy` (porównanie z gotowym, prototyp, pomiar, ADR).
- Każda zmiana przez kontrolę zmian (analiza wpływu na wszystkie dyscypliny, koszt (liczy `hq:budget`), ryzyko, decyzja, aktualizacja dokumentów, test).
- Po bramce: `hq:context` aktualizuje `.hq/context.md`.
