# Szablon planu urządzenia (`.hq/electronics/plan.md`)

Wypełnij razem z użytkownikiem. Pytaj grupami (max 4 pytania naraz), z domyślnymi propozycjami. Luki = zadaj pytanie, nie zakładaj.

## 1. Cel i funkcje
- Do czego służy, kto używa, gdzie (wewnątrz/na zewnątrz, wilgoć, wibracje, temperatura)
- Funkcje: MUST / SHOULD / NICE, każda z kryterium "działa gdy…"
- Czego urządzenie świadomie NIE robi

## 2. Specyfikacja
- Zasilanie: źródło, zakres napięć, prąd szczytowy i średni, bateria (czas pracy), ładowanie, ochrona (polaryzacja, przepięcia, zwarcie)
- Interfejsy: wejścia/wyjścia, komunikacja (USB, UART, I2C, SPI, CAN, BLE/Wi-Fi…), złącza, poziomy logiczne
- Sterowanie: MCU/FPGA, pamięć, taktowanie; firmware (kto pisze, jak programować/debugować)
- Czujniki i aktuatory: zakres, dokładność, prędkość
- UI: przyciski, LED, wyświetlacz
- Wymiary i mechanika: max gabaryty, mocowanie, obudowa (jest/będzie?), złącza dostępne z zewnątrz
- Środowisko i normy: temperatura, IP, CE/FCC/RoHS, bezpieczeństwo (jeśli sieć 230 V - wyraźnie zaznacz i ustal zasady)

## 3. Produkcja
- Ilości: prototypy (np. 5) i seria; czy montaż SMT w JLCPCB (zalecane) czy ręczny
- Liczba warstw, grubość, wykończenie, kolor maski (wpływa na styl i cenę)
- Strategia części: preferuj JLC Basic (brak opłaty za załadunek), Extended tylko gdy trzeba; części poza zapasami JLC = konsygnacja/ręcznie (koszt i czas)
- Termin i miejsce dostawy (wysyłka, cło/VAT)

## 3b. Zgodność i bezpieczeństwo produktu
Rynek docelowy, zasilanie sieciowe/bateria Li-ion/radio (Wi-Fi, BLE) i wymagane oznakowanie (CE, EMC, RoHS, baterie, recykling) wyjaśnij wcześnie z `hq:legal-safety` (lista LS4, wszystko DO WERYFIKACJI): wpływa na architekturę, koszt testów i czas.

## 4. Często pomijane (sprawdź każde, zapisz "tak/nie/n.d.")
Ochrona ESD i przepięć na złączach · odsprzęganie i filtry zasilania · bezpieczeństwo baterii Li-ion (zabezpieczenia, ładowarka, termistor) · pobór prądu w uśpieniu · reset, watchdog, tryb bootloadera · złącze programowania i debug · punkty testowe · diody statusu · rezerwa GPIO · otwory montażowe · fiducjały · odporność na odwrotne podłączenie · ciepło (moc strat, radiator) · zgodność EMC · drugie źródło dla kluczowych części i cykl życia (EOL) · wersja płytki w silkscreenie · dokumentacja i plan testów uruchomienia

## 5. Architektura
Schemat blokowy w tekście: bloki, sygnały, napięcia. Bilans mocy (tabela źródła -> odbiorniki, sprawność, straty).

## 6. Budżet (zaproponuj, użytkownik akceptuje)
Zasady, rezerwy i późniejsze śledzenie (poniesione/zobowiązane/EAC) prowadzi skill `hq:budget`; tabela poniżej jest jego baseline dla elektroniki (dane z `bom.tsv`, wycen JLCPCB, wysyłki), a kwoty wpisz do `.hq/budget/baseline.tsv`.
Użytkownik nie zna cen - podaj widełki z realnych danych (API LCSC, wycena JLCPCB), nie z głowy.

| Pozycja | Min | Zalecany | Premium | Uwagi |
|---|---|---|---|---|
| Części (BOM × ilość) | | | | z zapasem na straty |
| PCB | | | | rozmiar, warstwy, ilość |
| Montaż SMT (setup + załadunek Extended + lutowanie) | | | | |
| Stencil / opcje | | | | |
| Wysyłka + cło/VAT | | | | |
| Zapas 10-15% | | | | |
| **Razem** | | | | |

Wypisz co różni warianty (jakość/ryzyko/funkcje). Zapytaj: który wariant i jaki limit.

## 7. Akceptacja (G1)
`Zaakceptowano: <wariant>, budżet <kwota>, <data>` - dopisz do `gates.md` dopiero po jawnej zgodzie użytkownika.
