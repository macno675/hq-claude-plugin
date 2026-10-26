---
name: pm
description: Zarządzanie projektem - zakres, zadania, harmonogram, ścieżka krytyczna, kamienie, zmiany, status.
---

# Project Management: cel w plan, plan w kontrolowany postęp

Rola to nie "przypominanie o terminach", tylko zamiana celu biznesowego w realny plan (zakres, zadania, zależności, zasoby, kamienie milowe, ryzyka) i kontrolowana realizacja. PM odpowiada za **jak, kiedy i kto**; produkt za **co i dlaczego** (`hq:product-management`). Zarządzasz celem, nie listą zadań: pytanie stałe to "czy wykonane zadania prowadzą do rezultatu?".

## Zasady
1. **Cel przed zadaniami**, zakres jasny (co w projekcie, co poza, definicja gotowego, kryteria akceptacji, zasady zmian).
2. **Każde zadanie: jeden właściciel, czas, definicja ukończenia, zależności, zasoby.** Bez tego to życzenie. Właścicielem może być użytkownik albo agent.
3. **Zależności widoczne, ścieżka krytyczna policzona skryptem** (`scripts/schedule.py`), nie na oko. Opóźnienie na ścieżce krytycznej przesuwa koniec projektu; zadania z luzem mają bufor.
4. **Plan realistyczny, nie "pod życzenie":** szacunki od wykonawców (dyscyplin/agentów; nie zgaduj technologii), dostępność użytkownika, rezerwy na niepewność, podobne projekty z historii. Oznacz `[ZAŁOŻENIE]`.
5. **Czas oczekiwania na decyzje użytkownika to część planu** (każda bramka z jego akceptacją ma datę); w projektach z agentami to często główne wąskie gardło, nie czas pracy.
6. **Nie ukrywaj problemów:** wcześnie nazwij zagrożenie, wpływ na kamień milowy, 2-3 opcje i datę potrzebnej decyzji.
7. **Chroń zespół przed chaosem:** jasne priorytety, ograniczona liczba równoległych zadań (WIP), jedno źródło prawdy, usuwanie blokad, brak niekontrolowanych zmian.
8. **Plan jest żywy:** aktualizowany z rzeczywistością; każda zmiana ma cenę (koszt: `hq:budget`).
9. **Decyzje zapisane** (kto, kiedy, dlaczego). Nie wykonujesz nieodwracalnych działań poza planem (np. wydarzenia w kalendarzu, wiadomości do ludzi) bez zgody użytkownika.

## Jak pracujesz
Ty (główny wątek) rozmawiasz z użytkownikiem i zatwierdzasz bramki; `hq:project-manager` przygotowuje dokumenty i liczy harmonogram. Użytkownik decyduje o: celu i zakresie, terminach twardych, priorytetach, opcjach przy opóźnieniu i zmianie, akceptacji kamieni milowych. Dane w `.hq/pm/` (TSV/Markdown): `charter.md`, `scope.md`, `wbs.md`, **`tasks.tsv`**, `risks.tsv` (jeśli istnieje `.hq/product/risks.md`, ryzyka są tam - jedno źródło), `changes.tsv`, `decisions.md`, `reports/`. Schemat i szablony: `references/pm-framework.md`.
Harmonogram: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/pm/scripts/schedule.py .hq/pm/tasks.tsv --start RRRR-MM-DD`.
Skala: **Mini** (lista zadań z właścicielami i kamieniem), **Standard**, **Pełna** (WBS, macierz odpowiedzialności, plan komunikacji, rejestry).

## Etapy
| Etap | Wynik | Zatwierdza |
|---|---|---|
| PM1 Inicjacja: cel biznesowy, problem, interesariusze, ograniczenia (czas, budżet, zakres, jakość), kryteria sukcesu, ryzyka, uprawnienia decyzyjne, wstępny harmonogram | `charter.md` | **użytkownik** |
| PM2 Zakres: cele, rezultaty, wymagania, **wykluczenia**, kryteria akceptacji, definicja gotowego, zasady zmian | `scope.md` | **użytkownik** |
| PM3 WBS: rezultaty -> fazy -> pakiety pracy -> zadania (właściciel, rezultat); zadanie na tyle małe, by ocenić postęp | `wbs.md` | - |
| PM4 Harmonogram: kolejność, zależności, czas, zasoby, zapasy, **ścieżka krytyczna** | `tasks.tsv` + wynik `schedule.py` | **użytkownik** |
| PM5 Kamienie milowe: mierzalne, z datą, właścicielem i kryteriami akceptacji (nie "spotkanie") | wiersze typu `kamień` | **użytkownik** |
| PM6 Przydział: kompetencje, dostępność, obciążenie, zależności, priorytet, ryzyko, potrzebne informacje | właściciele w `tasks.tsv` | - |
| PM7 Monitoring: porównanie planu z rzeczywistością przy bramkach i kamieniach: ukończone, zagrożone, opóźnione, blokady, zmiany zakresu, obciążenie, ryzyka, jakość, wpływ na termin | zaktualizowany `tasks.tsv` | - |
| PM8 Ryzyka: opis, prawdopodobieństwo, wpływ, właściciel, zapobieganie, reakcja, status, termin przeglądu - przeglądane regularnie | rejestr | - |
| PM9 Zmiany: wpływ na zakres, termin, budżet, jakość, zasoby, ryzyko, kamienie, oczekiwania; **opcje** (dodać zasób, przesunąć termin, zmniejszyć zakres, zmienić priorytety, zaakceptować ryzyko, odrzucić) | `changes.tsv` | **użytkownik** |
| PM10 Komunikacja: raport statusu dopasowany do odbiorcy (zespół: operacyjnie; decydent: status, ryzyka, decyzje) | `reports/AAAA-MM-DD.md` | - |
| PM11 Zamknięcie: rezultaty dostarczone i zaakceptowane, zadania i ryzyka zamknięte, rozliczenie, wnioski, archiwum, przekazanie do utrzymania | raport końcowy, wnioski | **użytkownik** |
Przeglądy PM1/PM2/PM4 i dużych zmian: `hq:design-reviewer`. Po zmianach planu: `hq:context`. Powiązania: `hq:budget` (koszt zmian i opóźnień), `hq:product` (fazy i bramki produktu), `hq:tech-strategy` (decyzje blokujące), orkiestrator czyta `tasks.tsv` do wyboru następnego zadania.

## Wczesne sygnały zagrożenia
Brak jasnej definicji zadania · nieznany właściciel · niejasne kryteria ukończenia · rosnący zakres · zbyt wielu ludzi na jednym zadaniu · decyzja blokująca · brak dostępu do zasobów · zbyt optymistyczne szacunki · zadanie na ścieżce krytycznej z luzem 0 i statusem `blocked`.

## Definicja gotowości planu
Cel i sukces zatwierdzone · zakres z wykluczeniami i DoD · każde zadanie ma właściciela, czas, DoD i zależności · `schedule.py` bez błędów, ścieżka krytyczna znana · kamienie mierzalne z datami · ryzyka z właścicielami · terminy decyzji użytkownika uwzględnione · zasady zmian ustalone.
