# Ramy operacyjne

## Diagnoza (`process-map.md`)
Dla każdego procesu głównego: nazwa · cel · wejście · kroki (kto, ile trwa, co czeka) · wyjście · czas całkowity vs czas pracy (czas oczekiwania zwykle dominuje) · koszt · błędy i ponowienia · dokumenty i narzędzia · wąskie gardła · właściciel (lub jego brak). Źródła: obserwacja, dane (`hq:data-analysis`), rozmowy z wykonawcami, artefakty (maile, formularze), nie tylko deklaracje. Pytania: gdzie praca się zatrzymuje? kto czeka na decyzję? co robimy ręcznie wielokrotnie? gdzie powstają błędy? które narzędzia się dublują? które informacje są niedostępne? które zadania nie mają właściciela? Priorytet: procesy krytyczne i największe straty.

## Projekt procesu (`processes/<nazwa>.md`)
Cel · wejście · kroki (numerowane, każdy z wykonawcą) · właściciel i odpowiedzialni (RACI) · terminy/SLA wewnętrzne · dokumenty i szablony · kryteria jakości i ukończenia · eskalacja (kto, kiedy) · miernik sukcesu · wyjątki i procedura awaryjna · wersja i data przeglądu. Prosty, powtarzalny, możliwy do poprawy. Zasada: usuń krok, zanim go zautomatyzujesz.

## Skalowalność (test)
Co pęknie przy 3x obciążeniu? Które kroki zależą od jednej osoby? Co jest w głowie, a nie w dokumencie? Co da się zautomatyzować bez utraty jakości? Czy nowa osoba wykona proces z instrukcji?

## Narzędzia
Najpierw proces, potem narzędzie. Kryteria: upraszcza pracę, poprawia jakość danych, będzie używane, integruje się z resztą, koszt i ryzyko dostawcy (`hq:tech-strategy`, `hq:it-infrastructure`, `hq:cybersecurity`). Kategorie: zadania, CRM, dokumentacja, dostawcy, ewidencja majątku, automatyzacje, raportowanie, komunikacja wewnętrzna. Nie wdrażaj bez zatwierdzenia użytkownika.

## Zasoby (`resources.tsv`)
`zasób | typ (osoba/czas/budżet/sprzęt/przestrzeń/licencja/umowa) | przydział | dostępność | obciążenie % | okres | uwagi`. Wykrywaj: przeciążone osoby/działy obok niewykorzystanych zasobów, brak zastępstw, licencje bez użytkowników.

## Dostawcy (`vendors.tsv`)
`id | dostawca | kategoria | umowa/SLA (data) | koszt | terminowość % | jakość (reklamacje) | ryzyko dostaw | alternatywa | właściciel relacji | ocena | przegląd do`. Zakres: wybór, negocjacje, umowy, terminy, jakość, płatności, serwis, ryzyko, ocena współpracy. Kryteria wielokryterialne (nie tylko cena); ryzyko pojedynczego dostawcy; plan B dla krytycznych. Umowy: `hq:legal-safety`.

## Logistyka i łańcuch dostaw
Zamówienia materiałów (czasy dostaw, minimalne ilości) · magazyn i zapasy (poziom minimalny, rotacja, zabezpieczenie) · transport (koszt, czas, ubezpieczenie, cło/VAT dla importu) · pakowanie · dystrybucja · zwroty i reklamacje · dokumentacja przewozowa · ryzyko opóźnień (bufory, alternatywne trasy). Mierz: czas dostawy, koszt transportu, poziom zapasów. Produkty elektroniczne: `hq:electronics` (BOM, JLCPCB, wysyłka), wydarzenia: `hq:event`.

## KPI operacyjne (`kpi.tsv`)
| Obszar | Przykłady |
|---|---|
| Procesy | czas realizacji, liczba błędów, liczba ponowień |
| Zespół | obciążenie, rotacja, produktywność |
| Dostawcy | terminowość, jakość, koszt, reklamacje |
| Logistyka | czas dostawy, koszt transportu, poziom zapasów |
| Klienci | czas reakcji, satysfakcja, skargi |
| Finanse | koszt operacyjny, budżet, rentowność |
Definicje w słowniku metryk (`hq:data-analysis`); cel, bieżąca wartość, właściciel, okres.

## Ciągłe doskonalenie (`improvements.tsv`)
`id | problem | dowód | przyczyna | zmiana | oczekiwany efekt (miara) | właściciel | termin | wynik po teście | decyzja`. Cykl: pomiar -> analiza -> zmiana -> test -> ponowny pomiar. Regularny przegląd: co działa, co opóźnia, co generuje koszty, co wraca jako problem, co uprościć, co zautomatyzować, co zmienić w dokumentacji, co wymaga szkolenia.

## Kryzys operacyjny (protokół)
1) Oceń skalę wpływu · 2) wyznacz osobę odpowiedzialną · 3) ogranicz szkody · 4) skomunikuj interesariuszom · 5) uruchom procedurę awaryjną · 6) przywróć normalne działanie · 7) przyczyna źródłowa · 8) zaktualizuj proces i dokumentację. Incydenty bezpieczeństwa/prawne: `hq:cybersecurity`, `hq:legal-safety`.

## Dokumentacja
Mapa procesów · procedury operacyjne · macierz odpowiedzialności · KPI · plan zasobów · rejestr dostawców · umowy i SLA · plan logistyczny · rejestr ryzyk · procedury awaryjne · raporty operacyjne · wnioski po incydentach. Firma nie zależy od pamięci kilku osób.
