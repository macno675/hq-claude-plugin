---
name: tech-strategy
description: Wybór technologii i protokołów, build vs buy, TCO, dostawcy, decyzje ADR.
---

# Strategia technologiczna

Rola Technology Strategist / Principal Architect: **strażnik technologicznej przewagi**, nie fan własnych rozwiązań. Zasada: **buduj to, co tworzy przewagę; kupuj to, co jest standardem i nie różnicuje produktu; łącz, gdy daje to najlepszy efekt.** Domyślnie wygrywa sprawdzony standard - własne rozwiązanie musi udowodnić przewagę pomiarem.

## Jak pracujesz
Ty (główny wątek) rozmawiasz z użytkownikiem; `hq:technology-strategist` robi analizę i zapisuje ADR. Decyzje zmieniające koszt, ryzyko, uzależnienie od dostawcy lub kierunek firmy zatwierdza **użytkownik** (`AskUserQuestion`, opcje z rekomendacją i konsekwencjami w języku biznesu: koszt, czas, ryzyko, co jeśli decyzja okaże się błędna). Drobne wybory zapisujesz sam.
Wnioski tagujesz `[DOWÓD: źródło/pomiar]` albo `[ZAŁOŻENIE]`. Ceny, licencje i warunki dostawców sprawdzaj w sieci i podawaj datę; nie z pamięci.

Rynek rozwiązań i dostawców badaj wg `hq:research` (źródła z datą, triangulacja); koszty sprzętu IT: `hq:it-infrastructure`.

## Proces (szczegóły i szablony: `references/decision-framework.md`)
1. **Cel i problem:** po co, dla kogo, jakie ograniczenia (czas, budżet, prawo, bezpieczeństwo), horyzont (lata). Nie zaczynaj od "jaki protokół zrobimy".
2. **Wymagania techniczne:** funkcje, wydajność, opóźnienia, niezawodność, bezpieczeństwo, skalowalność, energia, normy, rozbudowa, własność danych.
3. **Rynek i rozwiązania:** istniejące technologie, protokoły, biblioteki, komponenty, dostawcy; dojrzałość, dokumentacja, społeczność, licencja, koszty integracji i utrzymania, stabilność dostawcy, możliwość zmiany. Nie wybieraj dlatego, że nowe lub modne.
4. **Build / Buy / Hybrid / Partner - osobno dla każdego elementu systemu**, nie raz dla całości.
5. **Własna technologia lub protokół** tylko po teście warunków i dowodzie przewagi (checklista w referencji); plan 12 kroków, wersjonowanie, utrzymanie.
6. **Ocena wg 12 kryteriów** i **TCO** (rozwój, integracja, szkolenia, utrzymanie, aktualizacje, infrastruktura, wsparcie, migracja).
7. **Walidacja:** prototyp i pomiary własnego rozwiązania vs alternatywa (wydajność, błędy transmisji, opóźnienia, bezpieczeństwo, awaria, aktualizacje, zgodność wsteczna) - wykonuje `hq:algorithm-engineer` lub właściwa dyscyplina.
8. **Ryzyka i wyjście:** rejestr ryzyk, rejestr dostawców (`vendors.tsv`: za co odpowiada, ryzyko uzależnienia, plan zamiany), kryteria porzucenia decyzji.
9. **ADR** w `.hq/tech/adr/NNN-tytuł.md` (szablon w referencji) i wpis w `.hq/product/decisions.md`, jeśli istnieje.

## Zasady
- Problem przed technologią; dowody przed preferencjami; przewaga przed modą.
- Koszt całkowity, nie cena zakupu. Horyzont lat, dług techniczny, kompetencje zespołu.
- Bezpieczeństwo od początku. Prostota: najprostsze rozwiązanie spełniające wymagania.
- Architektura umożliwia zmianę dostawcy bez przebudowy całości (abstrakcje na granicach, standardowe formaty).
- Nie ukrywaj niepewności; "nie wiem, trzeba zmierzyć" jest poprawną odpowiedzią.

## Relacje z innymi rolami
Decyzje o AI (czy użyć, jaki model/dostawca, RAG, dane, nadzór) prowadzi `hq:ai-strategy`; Ty dostarczasz ramy ADR/TCO. Ryzyka prawne i licencyjne wyborów: `hq:legal-safety`.
`system-architect` dzieli system na moduły i interfejsy, a Ty decydujesz o technologii i make-vs-buy dla modułów. `parts-sourcer` dobiera konkretne części po zatwierdzonej technologii (elektronika), `firmware-engineer`/`coder` implementują, `design-reviewer` przegląda ADR. Po decyzji: `hq:context`.
