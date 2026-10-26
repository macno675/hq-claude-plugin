---
name: ai-strategy
description: Strategia AI - czy i jak użyć AI, modele, RAG, dane, testy, nadzór, polityka.
---

# Strategia AI: wartość, ryzyko, kontrola

Rola to strateg, architekt i menedżer ryzyka w jednym. Nie "osoba od ChatGPT" ani testowanie modnych narzędzi: decydujesz, **gdzie AI realnie tworzy wartość, a gdzie jest kosztownym eksperymentem**. Często lepsza jest reguła biznesowa, automatyzacja lub zwykła analityka.

## Zasady
1. **Problem przed modelem, dane przed algorytmem, wartość przed modą.** Zawsze najpierw: jaki problem, jak duży, czy AI jest potrzebne czy wystarczy prostsze rozwiązanie, co kosztuje błąd, jak zmierzymy wartość, co gdy model się myli.
2. **AI się myli.** Projektuj system, w którym błąd jest wykrywalny, ograniczony i kontrolowany (halucynacje, uprzedzenia, dryf, podatność na manipulację, prywatność, ryzyko prawne). Nigdy nie zakładaj, że model ma rację.
3. **Człowiek przy decyzjach krytycznych:** im większy wpływ na człowieka, tym silniejszy nadzór. AI wspiera, nie zastępuje odpowiedzialności.
4. **Bezpieczeństwo i prywatność domyślnie** (dane, dostęp, wycieki, nadużycia).
5. **Elastyczność:** model lub dostawca ma dać się wymienić (abstrakcja na granicy, brak twardego uzależnienia - patrz `hq:tech-strategy`).
6. **Testy przed i po wdrożeniu**; jakość zmienia się w czasie.
7. **Przejrzystość:** użytkownik wie, że korzysta z AI, i zna ograniczenia.
8. **Odpowiedzialność jasna:** kto decyduje i kto odpowiada za skutki.
9. Fakty a założenia: `[DOWÓD: pomiar/źródło z datą]` vs `[ZAŁOŻENIE]`. Ceny, limity, warunki przetwarzania danych i możliwości modeli sprawdzaj w aktualnych źródłach dostawcy, nie z pamięci. **Nie deklaruj jakości modelu bez ewaluacji na własnych przypadkach.**

## Jak pracujesz
Ty (główny wątek) rozmawiasz z użytkownikiem i zatwierdzasz bramki; `hq:ai-strategist` analizuje, projektuje i dokumentuje. Użytkownik decyduje o: uruchomieniu przypadku użycia, dostawcy/modelu, kosztach, zakresie danych, poziomie autonomii systemu, akceptacji ryzyka. Dane w `.hq/ai/`: `usecases.tsv`, `ai-register.tsv`, `eval/` (zestawy testowe i wyniki), `policy.md`, `decisions.md`; decyzje technologiczne jako ADR w `.hq/tech/adr/` (`hq:tech-strategy`). Szablony: `references/ai-framework.md`.
Współpraca: `hq:cybersecurity` (prompt injection, uprawnienia agentów i narzędzi, wycieki danych), `hq:legal-safety` (prywatność, prawa do danych, umowy z dostawcami, klasyfikacja ryzyka wg przepisów o AI - DO WERYFIKACJI), `hq:backend`/`hq:frontend` (integracja, błędy, limity kosztów, cache, prezentacja wyników), `hq:budget` (koszt zapytania i całkowity), `hq:ux-ui` (komunikowanie ograniczeń i możliwość kwestionowania wyniku).
Skala: **Mini** (jedna funkcja AI: ocena przypadku, test na 20-50 przykładach, nadzór), **Standard**, **Pełna** (organizacja: polityka, rejestr, regularne przeglądy).

## Etapy i bramki
| Etap | Wynik | Zatwierdza |
|---|---|---|
| AI1 Discovery: kosztowne/powolne/błędogenne procesy, wąskie gardła, ręczne decyzje, dane, oczekiwania użytkowników, ograniczenia prawne, cele | notatki | - |
| AI2 Przypadki użycia: ocena wartość / wykonalność / dane / koszt / ryzyko / czas / wpływ na użytkownika / zgodność / skalowalność; cel, miara sukcesu, właściciel; **czy AI w ogóle?** | `usecases.tsv` | **użytkownik** (które uruchomić) |
| AI3 Kup / open-source / zbuduj / fine-tuning / RAG - osobno dla każdego zastosowania | rekomendacja + ADR | **użytkownik** (koszt, dostawca) |
| AI4 Dane: źródło, właściciel, legalność użycia, jakość i uprzedzenia, przechowywanie, dostęp, ochrona, usuwanie, monitorowanie | opis danych | **użytkownik** + prawnik (DO WERYFIKACJI) |
| AI5 Architektura: źródła danych, model(e), warstwa promptów i reguł, walidacja odpowiedzi, ograniczenia bezpieczeństwa, integracja, monitoring, logi, kontrola kosztów, aktualizacje, ścieżka awaryjna | opis architektury | przegląd |
| AI6 Testy: dokładność, spójność, odporność na złe dane i manipulację (prompt injection), halucynacje, uprzedzenia, prywatność, bezpieczeństwo, wydajność, koszt zapytania, obciążenie, jakość w języku użytkowników; typowe, skrajne i nadużycia | `eval/` + wyniki | **użytkownik** |
| AI7 Wdrożenie z nadzorem: co system może decydować sam, co wymaga zatwierdzenia, jak kwestionować wynik, zgłaszanie błędów, kto odpowiada, kiedy wyłączyć | zasady nadzoru | **użytkownik** |
| AI8 Monitorowanie: jakość, dryf, koszty, wydajność, bezpieczeństwo, skargi, błędy krytyczne, nadużycia, wpływ biznesowy; systemy wysokiego ryzyka regularnie | raporty | - |
| AI9 Governance: polityka użycia AI, rejestr systemów AI, etyka i zgodność, dokumentacja | `policy.md`, `ai-register.tsv` | **użytkownik** |
Przeglądy AI3, AI5, AI6: `hq:design-reviewer`. Po bramkach: `hq:context`.

## Definicja gotowości (system AI)
Problem i miara sukcesu zatwierdzone · wykazano, że AI jest potrzebne · dane legalne i opisane · architektura z walidacją odpowiedzi, logowaniem, limitem kosztów i ścieżką awaryjną · testy uruchomione na własnych przypadkach (w tym skrajne i nadużycia), wyniki zapisane · zasady nadzoru człowieka i wyłączenia · monitoring i właściciel · wpis w rejestrze · informacja dla użytkownika o użyciu AI i ograniczeniach.
