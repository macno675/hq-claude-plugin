# UI: system, jakość, handoff (dla `ui-designer`)

## Przed projektem
Brief: problem (`problem.md`), użytkownik, cel użytkownika i biznesowy, dane dostępne, ograniczenia techniczne, priorytety, ryzyka. Za mało kontekstu = zgłoś PYTANIA, nie projektuj z jednego zdania.
Analiza treści: informacje konieczne/pomocnicze/ukrywane, dane zmienne, **maksymalne długości tekstów**, jednostki i formaty, tłumaczenia (PL potrafi być dłuższy), skrajne dane (długi tytuł, brak wartości, setki elementów).
Styl marki: z `brandbook.md` (minimalistyczny/ekspresyjny, techniczny/przyjazny, itp.); zmienia się język wizualny, nie zasady: hierarchia, główna akcja, nawigacja, spójność, kontrast, stany, czytelność, rozsądna ilość informacji. Trend tylko gdy pasuje do marki, nie psuje czytelności/dostępności/wydajności i da się spójnie zastosować.

## Hierarchia (nie dekoracje)
Najważniejsze najmocniejsze: rozmiar, grubość, kontrast, kolor, odstępy, wyrównanie, grupowanie, powtarzalne wzorce. Drugorzędne nie konkuruje o uwagę. Test: zmróż oczy / odwróć o skali szarości - czy nadal widać, gdzie patrzeć i co jest główną akcją?

## Ograniczenia zamiast przypadkowości (tokeny, `tokens.css`)
Kolory: 1 główny, akcenty, neutralne (skala), stany (sukces/ostrzeżenie/błąd/info), tryb jasny i ciemny jeśli potrzebny · Typografia: 1-2 rodziny, skala (np. 12/14/16/20/24/32), interlinia, długość wiersza ok. 45-75 znaków · Odstępy: skala wielokrotności (np. 4/8) · Promienie, cienie, obramowania: 2-3 stałe wartości · Ikony: jeden styl · Ruch: czas i easing, `prefers-reduced-motion`.
Wartości pochodzą z brandbooka; plik tokenów jest wspólnym źródłem prawdy z kodem (zmienne CSS / odpowiednik platformy). Nazewnictwo semantyczne (`color-action-primary`), nie opisowe (`blue-500` jako jedyny poziom).

## Komponenty (z wariantami i stanami)
Min. zestaw: przycisk, pole tekstowe, wybór (select/radio/checkbox/switch), karta, lista/tabela, nawigacja, komunikat/toast, modal, ładowanie (skeleton/spinner), pusty stan, błąd.
Przycisk: główny, wtórny, tekstowy, niszczący, z ikoną, ładowanie, nieaktywny. **Stany każdego**: domyślny, hover, naciśnięty, fokus (widoczny), wyłączony, ładowanie, błąd/sukces gdzie dotyczy.
Dokumentacja komponentu: cel, warianty, stany, zachowanie, zasady użycia (kiedy tak/nie), dostępność (rola, etykieta, klawiatura), responsywność, nazwa w kodzie.

## Ekrany - stany obowiązkowe
Idealny · pusty · ładowanie · błąd (z naprawą) · offline/brak połączenia · brak uprawnień · zbyt długa treść · brak danych · po sukcesie/potwierdzenie · nieaktywny · hover/naciśnięcie/fokus. Układ nie "skacze" (rezerwuj miejsce na komunikaty błędu). Responsywność: punkty przełamania i zachowanie układu opisane.

## Dostępność (zawsze)
Kontrast tekstu co najmniej 4,5:1 (duży tekst 3:1; sprawdź `contrast.py`) · informacja nie tylko kolorem · widoczny fokus i pełna obsługa klawiatury · etykiety pól (nie sam placeholder) · komunikaty błędów zrozumiałe i powiązane z polem · cele dotykowe wygodne (zalecenia platform ok. 44 pt iOS / 48 dp Android; minimum WCAG 2.2 AA to 24 px) · logiczna kolejność i struktura nagłówków · obsługa czytników ekranu (role, nazwy, kolejność) · skalowanie tekstu · ograniczenie ruchu · tryb jasny/ciemny działa. Pełny audyt: `design:accessibility-review` jeśli dostępny.

## Detal
Tekst nie dotyka krawędzi karty · ikona optycznie wyśrodkowana · cień nie za mocny · animacja nie opóźnia pracy · pole błędu nie przesuwa układu · przejścia naturalne · spójność jasny/ciemny.

## Prototyp
HTML w `prototype/` (przeglądarka, jeśli dostępna), pozwalający przejść ścieżki testowe; dowodzi hipotez, nie jest prezentacją. Animacje wspierają zrozumienie.

## Handoff (`handoff.md`) - proces, nie wysłanie pliku
Paczka: ekrany i stany · komponenty z wariantami i dokumentacją · tokeny (`tokens.css`) i specyfikacja typografii · zasady responsywności · animacje (czas, easing, kiedy) · przypadki brzegowe · **intencje** ("dlaczego tak") · mapowanie komponent -> nazwa w kodzie · kryteria akceptacji. Wspólne źródło prawdy: biblioteka komponentów + dokumentacja + prototyp. Porządek: logiczne warstwy, czytelne nazwy, wersjonowanie, decyzje opisane.
Weryfikacja wdrożenia: uruchom zaimplementowany interfejs w przeglądarce (wbudowanej lub innej dostępnej), porównaj ze specyfikacją (tokeny, odstępy, stany, fokus, responsywność, kontrasty), zgłoś rozbieżności jako listę poprawek `miejsce - jest - powinno być`. Poprawiaj projekt, jeśli rzeczywistość pokazuje błąd w specyfikacji.
