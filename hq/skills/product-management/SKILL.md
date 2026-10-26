---
name: product-management
description: Product Management - problem, wizja, strategia, roadmapa, backlog RICE, wymagania.
---

# Product Management: właściwy problem, właściwe rzeczy, mierzalna wartość

Product Manager odpowiada za to, żeby produkt **rozwiązywał realny problem, miał sens biznesowy, był wykonalny i dostarczał mierzalną wartość** (użytkownik + cele firmy + możliwości zespołu + ograniczenia rynku). Nie "wymyśla funkcje". PM odpowiada za **co i dlaczego** (strategia, rynek, wartość), Product Owner za **przełożenie tego na kolejność pracy zespołu** (backlog, wymagania); w małych projektach to jedna osoba. **Jak, kiedy i kto** to `hq:pm`.

## Zasady
1. **Problem przed funkcją:** jaki problem, kto go ma, jak często, jak duży wpływ, jak użytkownik radzi sobie dziś, dlaczego to nie wystarcza, co znaczy sukces, czy ta funkcja jest najlepszym sposobem. Jesteś rzecznikiem problemu użytkownika, nie listy życzeń interesariuszy.
2. **Wartość przed ilością funkcji:** mniej, ale naprawdę użyteczne.
3. **Priorytety to decyzja:** co teraz, co później, czego nie robić wcale. Mów "nie" dobrym pomysłom, żeby skupić zespół. Oceniaj: wartość dla użytkownika i biznesu, koszt, czas, ryzyko, wykonalność, wpływ na strategię i inne funkcje, pilność. RICE liczy skrypt.
4. **Roadmapa to kierunek, nie lista obietnic:** cel, obszary, problemy do rozwiązania, oczekiwane rezultaty, zależności, ryzyka, kolejność, **poziom pewności** (format Teraz / Następne / Później); aktualizowana wraz z danymi.
5. **Dane przed opinią, funkcja to hipoteza** dopóki wartość nie jest potwierdzona (`hq:data-analysis`, `hq:research`).
6. **Wymagania wyjaśniają intencję**, nie tylko wygląd: problem, użytkownik, rezultat, przypadki brzegowe, ograniczenia, miary, zakres w/poza.
7. **Komunikuj kompromisy** interesariuszom; oddzielaj wymagania od rozwiązań; chroń zespół przed chaosem.
8. **Mierz po wdrożeniu;** sukces nie kończy się na premierze.
9. Fakty a założenia: `[DOWÓD]` / `[ZAŁOŻENIE]`.

## Jak pracujesz
Ty (główny wątek) uzgadniasz z użytkownikiem problem, priorytety i kompromisy; `hq:product-strategist` (działa jako Product Manager) przygotowuje analizy, dokumenty i oceny. Użytkownik decyduje o: wizji, strategii, co wchodzi do roadmapy, zakresie, premierze. Dane w `.hq/product/`: `vision.md`, `strategy.md`, `roadmap.md`, `backlog.tsv` (id | pozycja | zasięg | wpływ | pewność_% | nakład | status | notatki), `requirements.md`, `decisions.md`. Priorytety: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/product-management/scripts/prioritize.py .hq/product/backlog.tsv`. Szablony: `references/product-framework.md`.
Powiązania: `hq:product` (fazy i bramki wielodyscyplinarne), `hq:pm` (plan realizacji), `hq:research` i `hq:data-analysis` (rynek, użytkownicy, wyniki), `hq:ux-ui` (rozwiązania), `hq:marketing` i `hq:partnerships` (premiera, rynek), `hq:budget`, `hq:executive` (strategia firmy), `hq:legal-safety`.
Skala: **Mini** (jedna funkcja: problem, hipoteza, miara, RICE), **Standard**, **Pełna** (strategia, roadmapa, system metryk).

## Etapy
| Etap | Wynik | Zatwierdza |
|---|---|---|
| PD1 Discovery: wywiady, ankiety, dane produktu, zgłoszenia supportu, sprzedaż, konkurencja, trendy, opinie -> problemy, potrzeby, możliwości | notatki, lista problemów | - |
| PD2 Wizja: jaki świat ma stworzyć produkt i dlaczego (prosta, ambitna, realna, spójna z firmą, o użytkowniku) | `vision.md` | **użytkownik** |
| PD3 Strategia: dla kogo, jaki problem, czym różni się od konkurencji, model biznesowy, priorytety, miary sukcesu, ryzyka | `strategy.md` | **użytkownik** |
| PD4 Roadmapa: inicjatywy, kolejność, zależności, kamienie, założenia, ryzyka, miary, pewność | `roadmap.md` | **użytkownik** |
| PD5 Priorytetyzacja backlogu: RICE + ocena strategii, ryzyka i zależności | `backlog.tsv` + wynik skryptu | **użytkownik** (top pozycje) |
| PD6 Wymagania: kontekst, użytkownik, rezultat, przypadki brzegowe, ograniczenia, miary, w/poza zakresem | `requirements.md` | **użytkownik** |
| PD7 Hipotezy: "jeśli wprowadzimy X, oczekujemy Y"; co mierzymy, wynik potwierdzający, wynik wymuszający zmianę, czas, ryzyka zafałszowania (z `hq:data-analysis`) | wpis w `experiments.tsv` | **użytkownik** |
| PD8 Launch: gotowość, jakość, dokumentacja, komunikacja, marketing, szkolenia, obsługa, plan reakcji, pomiar | lista gotowości | **użytkownik** |
| PD9 Pomiar i iteracja: czy używana, czy rozwiązuje problem, czy poprawia KPI, czy nie szkodzi innym obszarom, koszt utrzymania, co poprawić, czy kontynuować | raport | **użytkownik** |
Przeglądy PD3, PD4, PD6: `hq:design-reviewer`. Po bramkach: `hq:context`.

## Definicja gotowości (funkcja/produkt)
Problem i użytkownik opisani dowodami · miara sukcesu liczbowa · hipoteza i sposób weryfikacji · pozycja w backlogu z RICE i uzasadnieniem · wymagania z zakresem w/poza · wykonalność i koszt uzgodnione z dyscyplinami · ryzyka znane · plan pomiaru po wdrożeniu.
