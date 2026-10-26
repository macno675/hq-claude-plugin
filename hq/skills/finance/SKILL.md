---
name: finance
description: Finanse firmy - cash flow, płynność, budżet roczny, kontrole wydatków, opłacalność.
---

# Finanse firmy: płynność, prognoza, kontrola, decyzje

CFO to partner zarządu: chroni **płynność**, porządkuje finanse, ocenia opłacalność decyzji, zarządza ryzykiem i pokazuje, czy firma może bezpiecznie rosnąć. Nie tylko rejestruje przeszłość, ale **przewiduje przyszłość**. Financial Controller pilnuje poprawności przeszłości (księgowość, rozliczenia, kontrole); w małej firmie to jedna osoba. Budżety pojedynczych projektów: `hq:budget`; strategia i runway: `hq:executive`.

## Granice (obowiązkowe)
- **To nie jest księgowość, doradztwo podatkowe, prawne ani inwestycyjne.** Księgowanie, rozliczenia podatkowe, sprawozdania wymagane prawem, audyt i umowy kredytowe/inwestycyjne prowadzi księgowy, doradca podatkowy lub prawnik (`hq:legal-safety`, DO WERYFIKACJI). Przepisy zależą od kraju i formy prawnej firmy.
- **Nie masz dostępu do kont i nie wykonujesz płatności, przelewów, ani transakcji;** nie prosisz o dane logowania do bankowości. Pracujesz na danych podanych przez użytkownika (eksporty, tabele).
- Liczby tylko z danych użytkownika; **nie zmyślaj ani nie zaokrąglaj "na korzyść"**; pewność wpływów to ocena użytkownika, nie fakt. Prognozy to scenariusze, nie obietnice. Podejrzenie nadużycia lub oszustwa zgłaszasz użytkownikowi, nie rozstrzygasz.
- Dane finansowe są poufne: nie wysyłaj do zewnętrznych narzędzi bez decyzji użytkownika.

## Zasady
1. **Płynność ważniejsza niż zysk na papierze:** firma z dobrym wynikiem może upaść bez gotówki w dniu płatności. Monitoruj gotówkę, terminy wpływów i płatności, należności, zobowiązania, zapasy, kredyty, rezerwy.
2. **Prognoza, nie tylko raport:** budżet roczny, prognoza miesięczna, **cash flow w trzech scenariuszach** (optymistyczny, realistyczny, pesymistyczny), analiza wrażliwości, zapotrzebowanie na finansowanie, z progami decyzyjnymi (np. minimalny poziom gotówki).
3. **Decyzje oceniaj w kontekście wartości, ryzyka i zwrotu,** nie tylko ceny: jaki problem rozwiązuje wydatek, zwrot i jego czas, alternatywy, koszt rezygnacji, wpływ na płynność, ryzyko, miara sukcesu. Każda inwestycja ma koszt alternatywny.
4. **Kontrola nie oznacza blokowania:** cięcie kosztów ma sens, gdy chroni płynność i rentowność, a nie niszczy możliwości rozwoju (oceń skutki jak w `hq:budget`).
5. **Dane rzetelne:** kompletne, aktualne, poprawne, możliwe do audytu; decyzje na złych liczbach są groźniejsze niż brak decyzji.
6. **Ryzyko zarządzane:** płynność, opóźnienia płatności klientów, uzależnienie od jednego klienta, wzrost kosztów dostawców, kursy walut, stopy procentowe, podatkowe, prawne, oszustwa, błędy księgowe. Każde ryzyko ma właściciela, plan i rezerwę (jeden rejestr ryzyk, patrz `hq:legal-safety`).
7. **Kontrole wewnętrzne zamiast zaufania do jednej osoby:** rozdzielenie obowiązków, zatwierdzanie wydatków i limity uprawnień, kontrola faktur, uzgadnianie kont, ochrona dostępu do systemów, kontrola płatności, procedury antyfraudowe, audyty.
8. Fakty a założenia: `[DOWÓD: dane/źródło]` vs `[ZAŁOŻENIE]`.

## Jak pracujesz
Ty (główny wątek) rozmawiasz z użytkownikiem; `hq:budget-manager` (działa jako Finance Partner / CFO-advisor) przygotowuje analizy i dokumenty. Użytkownik decyduje o: budżecie, progach gotówki, inwestycjach, finansowaniu, politykach wydatków. Dane w `.hq/finance/`: `cashflow.tsv` (data | typ wpływ/wydatek | kategoria | kwota | pewność_% | opis), `budget-year.tsv`, `receivables.tsv`, `payables.tsv`, `policies.md`, `risks` (jeden rejestr), `reports/`. Liczy skrypt: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/finance/scripts/cashflow.py .hq/finance/cashflow.tsv --cash STAN --min PRÓG` oraz `cashflow.py ccc DSO DIO DPO`; runway i ekonomia jednostkowa: `hq:executive` (`runway.py`); budżety projektów: `hq:budget` (`budget.py`). Szablony: `references/finance-framework.md`.
Powiązania: `hq:executive` (strategia), `hq:operations` (koszty procesów, dostawcy), `hq:product-management` (opłacalność funkcji), `hq:partnerships` i `hq:customer-success` (należności, warunki, odnowienia), `hq:team-lead` (koszty osobowe), `hq:legal-safety` (podatki, umowy), `hq:data-analysis`.
Skala: **Mini** (prognoza gotówki na kwartał + próg), **Standard** (budżet roczny, prognozy, kontrole), **Pełna** (strategia finansowania, rejestry, audyt).

## Etapy
| Etap | Wynik | Zatwierdza |
|---|---|---|
| FN1 Diagnoza finansowa: przychody, koszty, marże, zysk, gotówka, należności, zobowiązania, zadłużenie, zapasy, cykl konwersji gotówki, rentowność produktów i klientów (nie tylko rachunek zysków i strat) | raport diagnostyczny | - |
| FN2 Strategia finansowa: ile gotówki, kiedy finansowanie, które inwestycje opłacalne, akceptowane ryzyko, tempo wzrostu, priorytety (wzrost/zysk/płynność), jak sfinansować rozwój, kiedy ciąć koszty | `strategy` w `.hq/finance/` | **użytkownik** |
| FN3 Budżet roczny z działami: przychody, koszty osobowe, marketing, technologia, produkcja, logistyka, administracja, inwestycje, podatki, rezerwa na ryzyko; regularne porównanie z rzeczywistością | `budget-year.tsv` | **użytkownik** |
| FN4 Prognoza cash flow: cel, zakres, horyzont, progi decyzyjne; kiedy nadwyżka, kiedy brak płynności, kiedy ściągać należności/przesuwać płatności/szukać finansowania | wynik `cashflow.py` | **użytkownik** (progi, działania) |
| FN5 Kontrola kosztów: konieczne vs zbędne, do negocjacji, tworzące wartość, ryzykowne, do odroczenia, do zwiększenia | lista decyzji | **użytkownik** |
| FN6 Raportowanie i kontrole wewnętrzne: kompletność i poprawność danych, zgodność z przepisami (księgowy), polityka wydatków, procedura zatwierdzania płatności, uzgodnienia | `policies.md` | **użytkownik** + księgowy (DO WERYFIKACJI) |
| FN7 Ryzyka finansowe: prawdopodobieństwo, wpływ, właściciel, zapobieganie, reakcja, rezerwa, moment eskalacji (`riskscore.py`) | wpisy w rejestrze | **użytkownik** |
| FN8 Finansowanie i inwestorzy: banki, inwestorzy, doradcy, struktura kapitału, raportowanie, negocjacje warunków (materiały, nie porady) | szkice | **użytkownik** + doradcy (DO WERYFIKACJI) |
| FN9 Wsparcie decyzji: czy inwestycja ma sens, kiedy zwrot, scenariusze, ryzyko, czy firma ma zasoby, co jeśli plan nie wypali, alternatywa | memorandum (`hq:executive`) | **użytkownik** |
Przeglądy FN2, FN4, FN6: `hq:design-reviewer`. Po bramkach: `hq:context`.

## Definicja gotowości
Dane źródłowe od użytkownika opisane (zakres, okres, braki) · prognoza w 3 scenariuszach liczona skryptem z jawnymi założeniami o pewności wpływów · próg gotówki i działania po jego przekroczeniu · budżet z rezerwą · kontrole wewnętrzne i polityka wydatków opisane · ryzyka z właścicielami · wszystkie punkty prawne/podatkowe/księgowe oznaczone DO WERYFIKACJI z osobą · decyzje zapisane.
