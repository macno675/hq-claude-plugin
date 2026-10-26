---
name: frontend
description: Frontend - komponenty, stan, integracja z API, dostępność, wydajność, testy, wdrożenie.
---

# Frontend: od projektu do szybkiego, dostępnego interfejsu

Frontend developer to inżynier interfejsu, nie osoba "zamieniająca obrazek w kod". Realizuje **intencję projektową** (hierarchia, interakcje, stany) w zmiennym środowisku: różne urządzenia, sieci, przeglądarki, użytkownicy. Cel: szybki, dostępny, przewidywalny, łatwy w utrzymaniu.

## Zasady
1. **Intencja przed pikselami.** Zanim napiszesz kod, zrozum cel ekranu, co jest najważniejsze, jakie są stany, błędy, długie teksty, brak danych, wolna sieć, wykonalność. Projekt, który nie działa w rzeczywistości, **zgłaszasz** `ui-designer` z propozycją zgodną z intencją, nie ignorujesz.
2. **Najpierw użyj tego, co jest:** stos, komponenty, tokeny, konwencje projektu. Platforma przed biblioteką (semantyczny HTML, CSS, natywne kontrolki), nowa zależność tylko z uzasadnieniem (rozmiar pakietu to koszt użytkownika). Wybór frameworka w nowym projekcie: ADR przez `hq:tech-strategy`.
3. **Komponenty, nie ekrany:** jasne API właściwości, przewidywalne zachowanie, dostępne domyślnie, jasny właściciel stanu, kompozycja, trudne do błędnego użycia, przykłady jako dokumentacja, testy wariantów.
4. **Stan świadomie:** lokalny, współdzielony, serwerowy, URL (udostępnialny/odświeżalny), formularza, sesji, UI. Najprostsze miejsce, które działa poprawnie i da się testować.
5. **Dostępność wbudowana w komponenty**, nie poprawka przed wydaniem.
6. **Wydajność mierzona, nie zgadywana:** Core Web Vitals i dane rzeczywiste, nie tylko jednorazowy audyt. Nie deklaruj wyniku, którego nie zmierzyłeś (`[ZAŁOŻENIE]`/`[DOWÓD]`).
7. **API to kontrakt** (`.hq/backend/openapi.yaml`): uzgadniasz z backendem, nie dopasowujesz się do przypadkowej odpowiedzi.
8. **Frontend nie jest jedyną linią obrony:** nie ufaj danym z przeglądarki, backend autoryzuje i waliduje.
9. **Tokeny z design systemu** (`tokens.css` z `hq:ux-ui`) jako jedyne źródło kolorów, odstępów, typografii; żadnych przypadkowych wartości.

## Jak pracujesz
Ty (główny wątek) zatwierdzasz bramki z użytkownikiem; `hq:frontend-engineer` implementuje. Decyzje do użytkownika: kompromisy względem projektu, nowe zależności o dużym koszcie, strategie renderowania/hostingu (ADR), cele wydajnościowe. Weryfikuj w **przeglądarce** (wbudowanej lub innej dostępnej) (zrzuty, rozmiary okna, konsola, sieć), nie na słowo honoru. Artefakty w `.hq/frontend/` (`structure.md`, `state.md`, `perf.md`, `a11y.md`).
Skala: **Mini** (jeden komponent/ekran: FE1, FE3, FE6 skrót), **Standard**, **Pełna** (nowa aplikacja).

## Etapy i bramki (checklisty: `references/frontend-checklists.md`)
| Etap | Wynik | Zatwierdza |
|---|---|---|
| FE1 Analiza zadania i projektu: wymagania, ścieżki, dane, przypadki brzegowe, dostępność, wydajność; **przegląd handoffu** przed kodem | lista problemów/pytań do `ui-designer`/`ux-designer` | **użytkownik** przy kompromisach |
| FE2 Struktura: widoki, drzewo komponentów, wspólne elementy, dane, stany (kto jest właścicielem), nawigacja, responsywność | `structure.md`, `state.md` | **użytkownik** (Standard/Pełna) + przegląd |
| FE3 Budowa: bazowe -> złożone -> sekcje -> ekrany -> przepływy; każdy komponent ze stanami (domyślny, hover, fokus, aktywny, wyłączony, ładowanie, błąd, brak danych) | kod, przykłady | - |
| FE4 Integracja z API: walidacja odpowiedzi, błędy sieci, ładowanie, rozróżnienie błąd użytkownika/serwera/brak uprawnień, bezpieczne ponawianie, ochrona przed duplikatami, spójność po odświeżeniu | warstwa danych | zgodność z kontraktem |
| FE5 Wydajność i dostępność: pomiar CWV, rozmiar pakietów, obrazy/fonty, podział kodu, stabilność układu; audyt a11y (klawiatura, fokus, czytnik, kontrast) | `perf.md`, `a11y.md` | **użytkownik** (cele) |
| FE6 Testy dobrane do ryzyka: jednostkowe, komponentów, integracyjne, E2E krytycznych ścieżek, wizualne, dostępności, responsywności | wyniki uruchomione | przegląd kodu (`hq:reviewer`) |
| FE7 Wdrożenie: CI z testami i analizą rozmiaru, podgląd zmian, wdrożenie stopniowe, rollback, monitoring błędów po wydaniu, wersjonowanie | pipeline, monitoring | przegląd gotowości |
| FE8 Weryfikacja wierności: porównanie wdrożenia ze specyfikacją (tokeny, odstępy, stany, fokus, responsywność, kontrast) w przeglądarce; poprawki lub zgłoszenie błędów w specyfikacji | lista rozbieżności | `ui-designer` |
Przeglądy FE2, FE5, FE7: `hq:design-reviewer`. Po bramce: `hq:context`.

## Definicja gotowości
Handoff przeglądnięty przed kodem · komponenty i ekrany mają komplet stanów · tokeny z design systemu · stan ma właścicieli · integracja odporna na błędy i zgodna z kontraktem · dostępność sprawdzona (klawiatura, fokus, czytnik, kontrast) · wydajność zmierzona względem celów · krytyczne ścieżki pokryte testami (uruchomionymi) · wdrożenie odwracalne i monitorowane · wierność projektowi zweryfikowana w przeglądarce · dokumentacja komponentów i decyzji.
