---
name: data-analysis
description: Analiza danych - KPI, lejki, ankiety, opinie, eksperymenty A/B, rekomendacje.
---

# Analityka: dane w decyzje

Nie "robienie wykresów": zamieniasz dane, opinie i obserwacje w rzetelne wnioski i rekomendacje. Łączysz liczby (co się dzieje) z kontekstem i feedbackiem (dlaczego), a analizę kończysz rekomendacją, nie opisem przeszłości.

## Zasady
1. **Pytanie przed danymi.** Jaką decyzję wspiera analiza, kto jest odbiorcą, jaka hipoteza, jakie dane, **jaki wynik zmieniłby decyzję**. Sformułuj konkretnie: grupa, okres, miara, porównanie, oczekiwany rezultat decyzji (np. "dlaczego w ostatnich 30 dniach spadł odsetek kończących rejestrację?").
2. **Jakość danych jest fundamentem.** Zapisz źródło, sposób zbierania, zakres i ograniczenia; sprawdź duplikaty, braki, formaty, porównywalność; jakość analizy nie przekroczy jakości danych.
3. **Rozdzielaj:** dane (zmierzone) -> obserwacja (co widać) -> hipoteza (możliwe wyjaśnienie) -> wniosek (potwierdzone) -> rekomendacja (co zrobić) -> ryzyko (czego nie wiemy). Tagi `[DOWÓD]` / `[ZAŁOŻENIE]`.
4. **Nie szukaj tylko potwierdzenia.** Sprawdź hipotezy przeciwne, alternatywne wyjaśnienia, powtarzalność na segmentach, wystarczalność próby. Pokaż wynik niezgodny z oczekiwaniami. Żadnego p-hackingu ani wybiórczego raportowania; wynik negatywny też jest wynikiem.
5. **Segmentuj.** Średnia może ukrywać różne zachowania grup (uwaga na paradoks Simpsona); korelacja to nie przyczyna; wielokrotne porównania zwiększają fałszywe alarmy.
6. **Testuj zamiast zakładać** (eksperyment lepszy niż pewność bez dowodu).
7. **Obliczenia robi kod, nie model:** analizy wykonuj skryptami (Python/SQL), zapisuj kod i wynik (powtarzalność), nie licz w głowie. `mkcalc.py` do KPI, testu A/B i wielkości próby.
8. **Tłumacz prostym językiem**, dopasuj do odbiorcy, pokaż ograniczenia i poziom pewności.
9. **Prywatność:** dane osobowe tylko w niezbędnym zakresie, zanonimizowane/zagregowane gdzie możliwe; nie wysyłaj danych do zewnętrznych usług bez decyzji użytkownika; zgodność `hq:legal-safety` (DO WERYFIKACJI).

## Jak pracujesz
Ty (główny wątek) uzgadniasz z użytkownikiem pytanie i zatwierdzasz wnioski; `hq:data-analyst` analizuje na lokalnych danych. Użytkownik decyduje o: pytaniu i priorytecie, dostępie do danych, wdrożeniu rekomendacji, uruchomieniu eksperymentu. Dane robocze lokalnie w `.hq/analytics/`: `questions.md`, `metrics.md` (słownik KPI: nazwa | definicja | źródło | właściciel | wersja), `data-quality.md`, `analyses/` (kod + wyniki), `experiments.tsv`, `reports/`. Przepisy i szablony: `references/analytics-framework.md`.
Obliczenia: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/marketing/scripts/mkcalc.py kpi|abtest|samplesize ...`. Wykresy: skill `dataviz`, jeśli dostępny (czytelne, dostępne, spójne w jasnym i ciemnym motywie).
Powiązania: `hq:research` (kontekst i źródła zewnętrzne), `hq:marketing` (kampanie, leady), `hq:partnerships` (źródła klientów), `hq:ux-ui` (zachowania w interfejsie, testy), `hq:backend`/`hq:frontend` (poprawne zbieranie zdarzeń i definicje metryk), `hq:event` (frekwencja, ankiety), `hq:budget` (koszt vs efekt).
Skala: **Mini** (jedno pytanie, jeden zbiór: wynik, pewność, rekomendacja), **Standard**, **Pełna** (system metryk, dashboard, eksperymenty).

## Etapy
| Etap | Wynik | Zatwierdza |
|---|---|---|
| DA1 Pytanie analityczne i hipoteza | `questions.md` | **użytkownik** |
| DA2 Zbieranie danych: źródła (bazy, analityka, CRM, narzędzia marketingowe, sprzedaż, ankiety, opinie, zgłoszenia, dane aplikacji i wydarzeń), pochodzenie, ograniczenia | opis źródeł | - |
| DA3 Czyszczenie i przygotowanie: duplikaty, niespójności, braki, formaty, porównywalność; dziennik zmian | `data-quality.md` | - |
| DA4 Analiza eksploracyjna: trendy, segmenty, zmiany po wdrożeniu, punkty krytyczne lejka, korelacje, odstające, sezonowość, wpływ kampanii | `analyses/` | - |
| DA5 Feedback: porządkowanie opinii, ankiet, rozmów, zgłoszeń w tematy wg problemu, częstotliwości, wpływu na użytkownika i biznes, rozwiązania, priorytetu | tabela tematów | - |
| DA6 Eksperyment A/B: hipoteza, kontrola/test, miara główna i ochronne, minimalna próba (`samplesize`), czas, kryteria sukcesu i zakończenia, ryzyka równoległych testów | `experiments.tsv` | **użytkownik** (start) |
| DA7 Raport i dashboard: KPI, trendy, porównanie z celem, segmenty, alerty, kontekst, wyjaśnienie zmian, link do szczegółów (pokazuje to, co pomaga decydować) | `reports/` | - |
| DA8 Wnioski: co się dzieje, dlaczego, jak duży wpływ, jak pewny wniosek, co zrobić, alternatywy, ryzyko decyzji | sekcja raportu | **użytkownik** |
| DA9 Rekomendacja: działanie, oczekiwany efekt, koszt/nakład, ryzyko, sposób pomiaru, właściciel, termin weryfikacji | rekomendacja | **użytkownik** |
Przed projektem: potencjał pomysłu, miary sukcesu, ryzyka, linia bazowa, plan pomiaru. W trakcie: postęp do celów, zachowania, jakość danych, kampanie, sygnały ostrzegawcze. Po projekcie: czy cel osiągnięty, co zadziałało i dlaczego, wnioski uniwersalne. Przeglądy DA1, DA6, DA8: `hq:design-reviewer`.

## Definicja gotowości
Decyzja i pytanie jasne · definicje metryk zapisane · jakość danych sprawdzona i opisana · kod i wyniki zapisane i powtarzalne · segmenty sprawdzone · hipotezy przeciwne rozważone · poziom pewności i ograniczenia jawne · rekomendacja z kosztem, ryzykiem, pomiarem i terminem weryfikacji.
