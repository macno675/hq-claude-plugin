# Ramy budżetowe

## Kategorie kosztów (dobierz, nie wszystkie)
Wynagrodzenia/czas zespołu · zewnętrzni specjaliści · licencje i narzędzia (w tym subskrypcje AI) · infrastruktura i usługi (hosting, chmura, domeny) · komponenty i materiały · prototypy · testy i certyfikacja · produkcja (PCB, montaż, formy) · logistyka (wysyłka, cło, VAT) · marketing · prawne i administracyjne · **rezerwa**. Każda kategoria: właściciel, podstawa wyceny, sposób aktualizacji.

## Pliki (TSV, kolumny rozdzielone tabulatorem)
- `baseline.tsv`: `kat | budżet | etc | notatka`. `etc` = bieżące oszacowanie **pozostałych** kosztów poza poniesionymi i zobowiązanymi. Wiersz `REZERWA` = kwota rezerwy w kolumnie budżet.
- `actuals.tsv`: `data | kat | kwota | opis` (poniesione).
- `commitments.tsv`: `data | kat | kwota | opis` (zobowiązane: zamówienia, umowy niezapłacone). **Po zapłacie przenieś wiersz do actuals i usuń z commitments** (inaczej podwójne liczenie).
- `changes.tsv`: `id | data | opis | wpływ koszt | wpływ termin | ryzyko | źródło środków | decyzja | status`.
- `risks.tsv`: `ryzyko | wpływ finansowy (min-max) | prawdopodobieństwo | rezerwa przypisana | działanie | status`.
- `assumptions.md`: założenia wyceny, źródła z datą, poziom niepewności.

## Pojęcia
Koszty poniesione (AC) · zobowiązane (C) · ETC (pozostałe) · **EAC = AC + C + ETC** · wariancja = budżet − EAC (ujemna niekorzystna) · rezerwa na znane ryzyka (przypisana do ryzyk, wydawana wg zasad) i na nieznane (zarządcza, użycie za zgodą użytkownika). Wyniki liczy `scripts/budget.py`.
Opcjonalnie, gdy mierzony jest postęp (wartość wykonana): EAC wg wskaźnika efektywności kosztowej = budżet / CPI; użyj tylko z rzetelnym pomiarem postępu, nie zgaduj.

## Szacowanie
Metody: analogie do podobnych projektów (`~/.hq/cost-history.tsv`) · oddolnie od dyscyplin (agenci dają godziny/koszty z uzasadnieniem) · parametrycznie (wskaźniki, np. koszt na sztukę, cena za cm² PCB) · 3 scenariusze · wrażliwość (które 3 zmienne najbardziej ruszają koszt końcowy; co jeśli x2). Każde oszacowanie: założenia, źródło z datą, niepewność (zakres). Ceny rynkowe weryfikuj w sieci lub u dostawcy, nie z pamięci.
Rezerwa: zacznij od ryzyk (suma oczekiwanych skutków z `risks.tsv`) + procent na nieznane zależny od niepewności (im wcześniejszy etap i nowsza technologia, tym więcej); podaj użytkownikowi uzasadnienie, nie tylko procent.

## Analiza odchyleń (każda istotna różnica)
Wielkość i znak · próg istotności (domyślnie 10% kategorii lub kwota ustalona przez użytkownika) · przyczyna: błąd szacunku / zmiana zakresu / zmiana ceny / wydajność zespołu / zdarzone ryzyko · jednorazowe czy powtarzalne · trend (rośnie?) · wpływ na dalszą część i EAC · opcje działania (koszt, korzyść, ryzyko każdej) · rekomendacja.

## Ocena zmiany (przed zatwierdzeniem)
Koszt (jednorazowy i cykliczny) · termin · zasoby · jakość · ryzyko · dostawcy · wartość biznesowa/rentowność · **skąd środki** (rezerwa, inna kategoria, zwiększenie budżetu). Bez wiedzy o koszcie i źródle zmiana nie jest zatwierdzana.

## Ocena cięcia kosztów
Czy obniży jakość? opóźni wdrożenie? zwiększy ryzyko techniczne? przeniesie koszt na przyszłość (dług)? zniszczy przewagę? czy oszczędność jest realna po uwzględnieniu skutków? Porównaj z alternatywą: tańszy sposób osiągnięcia celu, zmiana zakresu, przesunięcie terminu.

## Raport (jedna strona, `reports/AAAA-MM-DD.md`)
Status (W BUDŻECIE / UŻYWA REZERWY / PRZEKROCZENIE) · budżet zatwierdzony · poniesione · zobowiązane · **EAC** · odchylenia i przyczyny (top 3) · rezerwa (użyta/pozostała) · ryzyka finansowe (top 3) · rekomendacje · **decyzje wymagane od użytkownika** (kontynuować / zmienić zakres / przesunąć termin / zwiększyć budżet / zatrzymać) z kosztem, korzyścią i ryzykiem każdej opcji. Tabela z `budget.py` dołączona, nie przepisywana.

## Budżet osobisty (prosty tryb)
1. Cel (oszczędności, zakup, spłata). 2. Realny dochód, bez najlepszego scenariusza. 3. Koszty stałe (mieszkanie, media, abonamenty, zobowiązania). 4. Koszty zmienne (jedzenie, transport, rozrywka, zdrowie). 5. Rezerwa na nieprzewidziane. 6. Regularne monitorowanie. 7. Analiza odchyleń: co i dlaczego odbiega. 8. Aktualizacja planu - budżet to narzędzie, nie sztywny dokument. Te same pliki w `~/.hq/personal-budget/`. Zachowaj prywatność danych; **bez porad inwestycyjnych, podatkowych i prawnych**.

## Rejestry i historia
Budżet bazowy · rejestr kosztów, zobowiązań, zmian, ryzyk · prognozy · raporty · faktury i umowy (referencje, nie treść wrażliwa w repo) · decyzje · historia projektów jako baza przyszłych wycen (`~/.hq/cost-history.tsv`: `projekt | kat | plan | rzeczywisty | uwagi`).
