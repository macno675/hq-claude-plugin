# Jakość premium: kunszt, stany, emocje (dla `ux-designer` i `ui-designer`)

Liczby poniżej pochodzą z materiałów wideo (wtórne, bez źródeł pierwotnych) - traktuj jako `[ZAŁOŻENIE]`/kierunek, nie cytuj jako fakt bez sprawdzenia.

## Sufit towarowy i teatr designu
AI robi czysty, poprawny, identyczny interfejs; to podłoga, nie przewaga. Brakuje jej najczęściej tego, co mało efektowne, a najważniejsze: **status systemu, cofnięcie, wyjście z błędu**. Ekran bez nich to "teatr designu": ładny, ale zostawia człowieka bez informacji (przykład: test mikrofonu kończący się samym "za krótko" - brak reakcji, porzucenie).

## Kontrola głównej ścieżki (każdy krok)
Na każdym kroku użytkownik wie: (1) co system właśnie zrobił, (2) jak to cofnąć, (3) jaki jest następny krok. Brakujące = luka do naprawy przed estetyką. Wynik zapisz w `flows.md` jako kolumny `zrobiono / cofnięcie / dalej`.

## Spójność w skali (ekran 80 po ekranie 1)
Oceniaj ścieżkę ciągiem, nie ekran po ekranie na wyidealizowanych danych. Ten sam przypadek = ten sam schemat wszędzie (np. wyczerpany limit: jeden ekran, dokładny licznik użyć, widoczna data odnowienia). Nie przenoś elementów nawigacji między ekranami (badanie z 2009: zmiana strony paska nawigacji >2x wydłużyła zadania); użytkownicy rzadko potrafią wskazać przyczynę, więc mierz czas i błędy, nie pytaj.

## Testy, które trzeba zrobić
- **Długa sesja**: korzystaj z produktu godzinę w realistycznych warunkach; notuj każdy moment, gdzie interfejs traci płynność lub przestaje być jedną całością.
- **Psucie celowo**: wyłącz sieć w połowie krytycznego procesu, wymuś odrzucenie płatności, wyczyść listy, przekrocz limit, wpisz skrajne dane. Dopracowane ścieżki negatywne to najtańszy sposób na efekt premium.

## Paradoks naprawy usługi
Dobrze obsłużona awaria (proaktywnie, z instrukcją i kontaktem) może dać wyższą satysfakcję niż brak awarii. Komunikat błędu = co się stało, czy dane/środki są bezpieczne, co zrobić teraz, jak szybko dotrzeć do pomocy (widoczny przycisk). Przykład z filmu: odrzucona płatność kartą z "sprawdź saldo" + przycisk kontaktu podniosła konwersję rejestracji i wpłaty (wg źródła +60% kont, +79% wpłat). Momenty błędu i pustki to okazja na charakter marki (Chrome: gra z dinozaurem na ekranie offline).

## Projektowanie emocjonalne (pętle, nie ozdoby)
Gdy funkcje stają się towarem, przewagą jest to, jak użytkownik się czuje. Dobór wg typu produktu:
- **Nawyk/rutyna** (nauka, dzienniki, trackery): natychmiastowa, ludzka informacja zwrotna, postać reagująca na sukces i błąd, animacje postępu (wzorzec Duolingo).
- **Wysokie ryzyko i brak zaufania** (finanse, zdrowie, ubezpieczenia, krypto): polish jest sygnałem zaufania; ciepły, prosty onboarding, przyjazne detale (wzorzec Phantom).
- **Premium** (fintech zamożny): perfekcyjne pierwsze wrażenie, płynne przejścia, fizyczność elementów (karta reagująca na ruch telefonu), bez nachalności (wzorzec Revolut).
Ruch i nagrody zawsze z `prefers-reduced-motion` i bez opóźniania zadania. Polish to inwestycja strategiczna, ale po fundamentach (status, cofnięcie, błędy), nie zamiast nich.
