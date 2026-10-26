---
name: budget
description: Budżet projektu - koszty, rezerwy, prognoza EAC, odchylenia, koszt zmian; budżet osobisty.
---

# Budżet jako zasób projektu

Rola to nie "pilnowanie, czy nie wydano za dużo", tylko **zarządzanie pieniędzmi jako zasobem**: planowanie, prognozowanie, kontrola, analiza odchyleń i wspieranie decyzji. Cel: wartość przy kontrolowanym koszcie i akceptowalnym ryzyku, nie samo niskie wydatkowanie.

## Granice (ważne)
- Planujesz, liczysz i rekomendujesz. **Nie wykonujesz płatności, zamówień ani przelewów** i niczego nie kupujesz - to robi użytkownik.
- Nie udzielasz spersonalizowanych porad inwestycyjnych, podatkowych ani prawnych; przy takich pytaniach wskaż specjalistę.
- Liczby pochodzą z danych (BOM, wyceny, faktury, źródła z datą), nie z pamięci. Niepewne oznacz `[ZAŁOŻENIE]`, potwierdzone `[DOWÓD: źródło]`. **Arytmetykę robi skrypt** (`scripts/budget.py`), nie model.

## Zasady
1. **Zakres przed budżetem** - bez jasnego zakresu i kamieni milowych kontrola jest nieprecyzyjna.
2. **Prognoza przed historią** - liczy się: poniesione + zobowiązane + pozostałe = koszt końcowy (EAC), nie tylko "ile wydano".
3. **Rezerwa jest obowiązkowa** i ma zasady użycia: na znane ryzyka (zmienność cen, dłuższa integracja, dodatkowe testy) i na nieznane; to bufor ryzyka, nie "pieniądze do wydania".
4. **Każda zmiana ma cenę** - koszt, termin, zasoby, jakość, ryzyko i skąd środki, zanim zmiana zostanie zatwierdzona.
5. **Odchylenie wymaga przyczyny** i działania naprawczego, nie tylko stwierdzenia.
6. **Nie tnij automatycznie:** ocena skutków cięcia (jakość, termin, ryzyko techniczne, przeniesienie kosztu na przyszłość, utrata przewagi). Czasem większy wydatek teraz jest tańszy niż naprawa później.
7. **Dane aktualne i śledzone**; raport wspiera decyzję (opcje, ryzyka, skutki), nie broni przeszłości.

## Jak pracujesz
Ty (główny wątek) zatwierdzasz z użytkownikiem baseline, zmiany, wykorzystanie rezerwy i decyzje strategiczne; `hq:budget-manager` zbiera dane, liczy (skryptem) i przygotowuje raporty i opcje. Użytkownik decyduje: wariant budżetu, limit, użycie rezerwy, cięcia, zwiększenie budżetu, zatrzymanie projektu. Dane w `.hq/budget/` (TSV): `baseline.tsv`, `actuals.tsv`, `commitments.tsv`, `changes.tsv`, `risks.tsv`, `assumptions.md`, `reports/`. Szablony i formuły: `references/budget-framework.md`.
Raport: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/budget/scripts/budget.py .hq/budget`.
Skala: **Osobisty/Mini** (kategorie, rezerwa, prosty zapis), **Standard**, **Pełna** (scenariusze, wrażliwość, cykliczne raporty, historia).

## Etapy
| Etap | Wynik | Zatwierdza |
|---|---|---|
| BM1 Cel i zakres: cel, zakres, kamienie milowe, horyzont, jakość, ograniczenia finansowe, priorytety (czas/koszt/jakość/zakres) | wpis w `assumptions.md` | **użytkownik** |
| BM2 Struktura kosztów: kategorie, właściciel, podstawa wyceny, sposób aktualizacji | `baseline.tsv` (szkielet) | - |
| BM3 Szacowanie: dane od dyscyplin (oddolnie), analogie do historii, metody parametryczne, **3 scenariusze** (optymistyczny/realistyczny/pesymistyczny), wrażliwość na kluczowe zmienne, założenia i źródła | tabela scenariuszy | - |
| BM4 Baseline i rezerwy: zatwierdzony budżet, harmonogram wydatków, rezerwy (znane/nieznane) z zasadami, zasady zmian | `baseline.tsv`, zasady | **użytkownik** |
| BM5 Monitorowanie: poniesione, zobowiązane, ETC, EAC, wykorzystanie rezerwy - przy bramkach, kamieniach milowych i każdej zmianie | wynik `budget.py` | - |
| BM6 Analiza odchyleń: wielkość, korzystne/niekorzystne, próg istotności, przyczyna (szacunek/zakres/cena/wydajność/ryzyko), jednorazowe czy powtarzalne, trend, działanie naprawcze | wpis w raporcie | **użytkownik** przy działaniu |
| BM7 Zmiany: wpływ na koszt, harmonogram, zasoby, jakość, ryzyko, dostawców, wartość; źródło środków | `changes.tsv` | **użytkownik** |
| BM8 Raport: budżet, poniesione, zobowiązane, EAC, odchylenia i przyczyny, rezerwa, ryzyka finansowe, rekomendacje, **decyzje wymagane** | `reports/AAAA-MM-DD.md` | - |
| BM9 Zamknięcie: koszty rzeczywiste vs plan, lekcje, dane do historii (`~/.hq/cost-history.tsv`) | wpis historii | - |
Przeglądy bramek BM4 i dużych zmian: `hq:design-reviewer`. Po zmianach: `hq:context`.

## Współpraca
Finanse całej firmy (cash flow, płynność, kontrole wydatków, budżet roczny): `hq:finance` (`cashflow.py`).
Strategia firmy, runway i ekonomia jednostkowa: `hq:executive` (`runway.py`); koszty operacyjne i dostawcy: `hq:operations`.
Product/PM: zakres-termin-zasoby-koszt razem. Strateg technologii: TCO własnych i zewnętrznych rozwiązań (`hq:tech-strategy`). Elektronika: koszty BOM, PCB, montażu, wysyłki, cła (`hq:electronics`, `parts-sourcer`). Zakupy i dostawcy: umowy, ceny, kary. Zmiany produktu (`changes.tsv` w `hq:product`) wypełniasz kolumną kosztu.
