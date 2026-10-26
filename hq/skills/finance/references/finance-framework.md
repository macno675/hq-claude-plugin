# Ramy finansów firmy

## Diagnoza (jedna strona)
Przychody (źródła, sezonowość) · koszty (stałe/zmienne) · marże brutto i operacyjna · zysk · gotówka · należności (struktura wiekowa, koncentracja klientów) · zobowiązania (terminy) · zadłużenie i koszt finansowania · zapasy · cykl konwersji gotówki (`cashflow.py ccc DSO DIO DPO`: DSO = dni do zapłaty od klientów, DIO = dni zapasów, DPO = dni do zapłaty dostawcom) · rentowność produktów i klientów. Analizuj także przepływy, nie tylko rachunek zysków i strat.

## Strategia finansowa
Pytania: ile gotówki potrzeba, kiedy finansowanie, które inwestycje są opłacalne, jakie ryzyko akceptujemy, jak szybko chcemy rosnąć, co ma priorytet (wzrost, zysk, płynność), jak sfinansować rozwój, kiedy ciąć koszty. Wynik: zasady (np. minimalny poziom gotówki w miesiącach kosztów), dopuszczalne zadłużenie, kolejność inwestycji, progi uruchamiające działania.

## Budżet roczny (`budget-year.tsv`)
`kategoria | dział | miesiąc | plan | rzeczywiste | odchylenie | uwagi`. Kategorie: przychody, koszty osobowe, marketing, technologia, produkcja, logistyka, administracja, inwestycje, podatki, **rezerwa na ryzyko**. Regularne porównanie z rzeczywistością i aktualizacja (żywy plan). Koszty projektów: `hq:budget`.

## Prognoza cash flow (`cashflow.tsv`)
Wpływy (faktury: termin zapłaty klienta, nie data wystawienia) i wydatki (płace, podatki, dostawcy, czynsze, raty) z datą, kwotą i **pewnością %** wpływów (ocena na podstawie historii płatności klienta). `cashflow.py PLIK --cash STAN --min PRÓG` daje stan na koniec miesięcy w trzech scenariuszach (realistyczny: wpływy x pewność, pesymistyczny: tylko wpływy >= 90%, optymistyczny: wszystkie) i flagi: pierwszy miesiąc poniżej progu i poniżej zera. Horyzont: tygodnie dla krótkiej płynności, miesiące dla planu. Co zrobić: ściągać należności, przesunąć płatności (w ramach umów), negocjować terminy, uruchomić finansowanie z wyprzedzeniem, wstrzymać wydatki odroczone.

## Ocena inwestycji / wydatku (memorandum, patrz `hq:executive`)
Problem, który rozwiązuje · oczekiwany zwrot i kiedy (okres zwrotu, wartość bieżąca netto gdy potrzebne) · alternatywy i koszt alternatywny · koszt rezygnacji · wpływ na płynność w scenariuszach · ryzyko · miara sukcesu i termin weryfikacji · plan wyjścia. Proste obliczenia kodem, nie z głowy.

## Kontrola kosztów
Kategorie: konieczne / zbędne / do negocjacji / tworzące wartość / ryzykowne / do odroczenia / do zwiększenia (przyspieszą rozwój). Cięcie tylko po ocenie skutków (jakość, termin, ryzyko techniczne, przeniesienie kosztu, utrata przewagi).

## Kontrole wewnętrzne (`policies.md`)
Rozdzielenie obowiązków (kto zamawia, kto zatwierdza, kto płaci, kto księguje) · limity zatwierdzania wydatków per rola · kontrola faktur (zamówienie, odbiór, cena, VAT) · uzgadnianie kont i sald · ochrona dostępu do bankowości i systemów (MFA, najmniejsze uprawnienia, `hq:cybersecurity`) · kontrola płatności (podwójne zatwierdzenie dla dużych kwot i zmian numerów kont) · procedury antyfraudowe (sprawdzanie próśb o zmianę rachunku, phishing) · audyty okresowe. W małej firmie: minimum to dwie osoby przy płatnościach powyżej progu.

## Ryzyka finansowe
Płynność · opóźnienia płatności klientów · uzależnienie od jednego klienta · wzrost kosztów dostawców · kursy walut · stopy procentowe · podatkowe · prawne · oszustwo · błędy księgowe · utrata kontroli nad zobowiązaniami. Rejestr: `ryzyko | P | W | właściciel | zapobieganie | reakcja | rezerwa | eskalacja od` (`riskscore.py`).

## Finansowanie i inwestorzy (materiały, nie porady)
Cel finansowania i użycie środków · potrzebna kwota i runway po rundzie · źródła (własne, kredyt, inwestorzy, dotacje) i koszt · wymagane dane i raportowanie · negocjowane warunki do przeglądu prawnika i doradcy. Materiały tylko z prawdziwych liczb użytkownika.

## Miary
| Obszar | Przykłady |
|---|---|
| Płynność | gotówka, runway, prognoza cash flow |
| Rentowność | marża brutto, marża operacyjna, zysk netto |
| Efektywność | koszt operacyjny, koszt pozyskania klienta, cykl konwersji gotówki |
| Zadłużenie | poziom długu, koszt finansowania, zobowiązania |
| Jakość finansów | terminowość raportów, liczba błędów, wynik audytu |
| Wzrost | przychód, przychody rentowne, zwrot z inwestycji |

## Raport dla zarządu (jedna strona)
Gotówka i runway (scenariusze) · wynik vs budżet (odchylenia i przyczyny) · należności i zobowiązania (terminy) · ryzyka finansowe (top 3) · decyzje wymagane z opcjami, kosztem i rekomendacją · zmiany założeń.

## Dokumentacja
Sprawozdania (księgowy) · budżet · prognoza cash flow i P&L · rejestr należności i zobowiązań · rejestr ryzyk · polityki wydatków · procedury zatwierdzania płatności · dokumentacja podatkowa (księgowy) · umowy finansowania · raporty dla zarządu i inwestorów · wyniki audytów.
