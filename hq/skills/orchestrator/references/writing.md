# Pisanie dla ludzi (wszystkie teksty: UI, strona, raport, dokument, odpowiedź w czacie)

Czytelnik jest bystry i zajęty. Każde zdanie ma mu coś dać: fakt, decyzję albo krok. Zdanie, które tego nie robi, usuwasz. Przed oddaniem tekstu skróć go o 20-30%.

## Jak pracujesz
1. Zanim napiszesz: kto czyta, w jakim miejscu (pole formularza, pusty stan, raport, czat), czego mu brakuje i co ma zrobić potem. Bez tego nie piszesz, tylko pytasz albo zakładasz `[ZAŁOŻENIE]`.
2. Piszesz roboczo, potem **osobny przebieg redakcji** wg tej listy: usuń ogólniki, trójki, kontrasty, meta i podsumowania; sprawdź zwłaszcza pierwsze i ostatnie zdanie każdego akapitu, bo tam najczęściej siedzi wata. Redakcja nie uzupełni brakujących faktów, więc fakty sprawdzasz wcześniej.
3. Lista zakazanych słów to kontrola, nie metoda: podmiana „kluczowy” na „istotny” niczego nie naprawia. Przepisz zdanie tak, żeby niosło konkret.

## Trzy pytania do każdego zdania
1. Czy czytelnik już to wie albo właśnie to widzi? Usuń. („Twój kod zobaczą gospodarze”, „Ten przycisk zapisuje zmiany”, „W tej sekcji znajdziesz...”).
2. Czy to zdanie pasuje do dowolnego produktu lub tematu? Zamień na konkret: liczbę, nazwę, przykład, skutek.
3. Czy człowiek z branży powiedziałby to na głos koledze? Jeśli nie, napisz tak, jak by powiedział.
Test usunięcia: jeśli bez tego zdania nie wzrośnie liczba błędów, pytań do wsparcia ani czas wykonania zadania, usuń je. Wyjątek: ostrzeżenia o bezpieczeństwie, danych, pieniądzach i działaniach nieodwracalnych zostają.

## Usuń
- **Wstępy i zakończenia:** „Świetne pytanie”, „Poniżej przedstawiam”, „Mam nadzieję, że pomogłem”, „Daj znać, jeśli...”, „Podsumowując” po trzech akapitach, powtórzenie prośby użytkownika.
- **Meta i oczywistości:** opis tego, co widać na ekranie; „Warto zauważyć, że”, „Należy pamiętać, że”, „Ważne jest, aby”, „Z przyjemnością informujemy”, „Prosimy o uwzględnienie”; tłumaczenie, po co jest pole, którego cel wynika z etykiety.
- **Puste słowa:** kompleksowy, innowacyjny, intuicyjny, wyjątkowy, nowoczesny, płynny, bezproblemowy, kluczowy, niezwykle, odkryj, zanurz się, „na wyższy poziom”, „w dzisiejszym dynamicznym świecie”, „w erze/dobie AI”, „szyte na miarę”, holistyczny, niezrównany, „szeroki wachlarz”, „kluczowa rola”, „istotny aspekt”, „najlepsze praktyki”, „stworzony z myślą o”, „ciesz się..., a my zajmiemy się resztą”; EN: seamless, robust, leverage, delve, elevate, unlock, streamline, cutting-edge, game-changer, tapestry, „in today's fast-paced world”.
- **Rytm z szablonu:** trójki przymiotników („szybko, prosto i bezpiecznie”), „nie tylko X, ale też Y”, „to nie X, to Y”, pytanie retoryczne z odpowiedzią, myślnik jako dramatyczna pauza w co drugim zdaniu, wszystkie zdania tej samej długości.
- **Forma bez treści:** lista, gdzie wystarczy zdanie; każdy punkt z pogrubionym wstępem i dwukropkiem; nagłówki w tekście na 5 zdań; emoji jako ozdoba; „Ups!” i wykrzykniki w komunikatach.
- **Asekuracja bez powodu:** „może”, „potencjalnie”, „w pewnym stopniu”, „warto rozważyć”. Niepewność podawaj raz, wprost, z powodem.
- **Fałszywa równowaga:** „zarówno A, jak i B mają zalety” zamiast kryterium i rekomendacji („Wybierz A, jeśli liczy się koszt”).
- **Wyróżnienia bez powodu:** pogrubienie zwykłych słów, „**Ważne:**” przed zwykłą informacją, nagłówki-wytrychy („Wprowadzenie”, „Korzyści”, „Wnioski”) zamiast nazwy tematu, sekcje równej długości mimo różnej ilości treści.
- **Kalki i urzędowy styl (PL):** „dokonać weryfikacji” -> sprawdzić, „w oparciu o” -> na podstawie, „dedykowany” -> przeznaczony/własny, „adresować problem” -> rozwiązać, „na koniec dnia” -> w końcu, „zrobić różnicę” -> zmienić coś, „upewnij się, że” -> sprawdź, „w celu” -> żeby, „wygląda na to, że” -> wprost, anglicyzmy (leverage, onboardować, insight) -> polskie słowo. Strona bierna i rzeczowniki odczasownikowe zamieniaj na czasowniki. Wielkie litery tylko na początku nagłówka (nie Title Case). „Twój/Ty” małą literą w interfejsie i nie w każdym zdaniu.

## Rób
- Najważniejsze na początku. Jedna myśl w zdaniu. Czasowniki zamiast rzeczowników.
- Konkret zamiast przymiotnika: „rezerwacja w 3 krokach” zamiast „szybka rezerwacja”.
- Zdania zwykle do 20 słów, różnej długości. Zwykłe słowa. Ton jak człowiek z branży do kolegi, zgodny z głosem marki (`hq:brand`, sekcja Język).
- Liczby, nazwy i twierdzenia tylko prawdziwe; brak danych = pytanie, nie wymyślona treść.

## Interfejs (mikrocopy)
- Etykieta przycisku mówi, co się stanie: „Zapisz zmiany”, „Usuń rezerwację”, „Utwórz projekt”, nie „OK”, „Zatwierdź”, „Rozpocznij”, „Dowiedz się więcej”.
- Tekst pomocniczy tylko, gdy użytkownik może się pomylić albo nie wie, co dalej (format, limit, skutek nieodwracalny). Inaczej brak. Instrukcji nie chowaj w placeholderze, bo znika po wpisaniu. Tooltip tylko dla rzadkiego terminu.
- Walidacja mówi, czego brakuje: „Podaj nazwę firmy i NIP”, nie „Uzupełnij wymagane pola”.
- Błąd: co się stało i co zrobić, bez winienia i bez „Ups”: „Nie zapisano. Brak połączenia - spróbuj za chwilę.”
- Pusty stan: co tu będzie i jedna akcja: „Brak rezerwacji. Dodaj pierwszą.”
- Jedno słowo na jedną rzecz w całym produkcie (np. zawsze „rezerwacja”, nie raz „booking”, raz „zamówienie”).

## Odpowiedzi w czacie i raporty
- Zaczynaj od wyniku albo odpowiedzi. Rekomendacja z danymi, nie przegląd opcji bez wyboru. Bez streszczania tego, co użytkownik napisał, i bez podsumowania na końcu, jeśli nic nie dodaje.
- Raport: wynik, dowód, co niepewne, następny krok. Tabela tylko dla porównania wielu rzeczy.

## Przed i po (wzorzec, nie do kopiowania)
| Przed | Po |
|---|---|
| Twój kod zobaczą gospodarze. Upewnij się, że wpisujesz go poprawnie, aby dołączyć do rozgrywki. | (brak podpowiedzi; etykieta „Kod gry”, a przy błędzie: „Nie ma gry o tym kodzie. Sprawdź 6 znaków od gospodarza.”) |
| Wygląda na to, że nie masz jeszcze żadnych rezerwacji! Zacznij swoją przygodę już dziś. | Brak rezerwacji. Wybierz salę i termin. |
| Odkryj Nowy Wymiar Zarządzania Rezerwacjami — Szybko, Prosto i Bezpiecznie | Rezerwacja sali w 3 krokach |
| Ups! Coś poszło nie tak. Spróbuj ponownie później. | Nie zapisano: brak połączenia. Zmiany są w przeglądarce, ponów za chwilę. |
| Twoje dane są bezpieczne dzięki zaawansowanym zabezpieczeniom. | Dane są szyfrowane przy przesyłaniu i przechowywaniu. |
| Warto zauważyć, że analiza pozwoliła na zidentyfikowanie kluczowych obszarów. Podsumowując, wyniki są obiecujące. | Dwa obszary do poprawy: eksport (12 zgłoszeń) i logowanie (8). Reszta bez zmian. |
| Zespół może rozważyć różne podejścia, uwzględniając korzyści i ryzyka. | Rekomenduję B: 12 tys. zł, 2 tygodnie; ryzyko: potrzebna zgoda prawnika. |
| Świetne pytanie! Poniżej przedstawiam kompleksowe omówienie. Mam nadzieję, że pomoże! | (od razu odpowiedź) |

## Kontrola
`python3 <katalog skilla orchestrator>/scripts/textcheck.py <plik...>` (albo tekst na stdin) wskazuje typowe zwroty AI z linią i podpowiedzią. Trafienie to sygnał do przepisania zdania, nie do podmiany słowa na synonim. Wynik 0 nie znaczy, że tekst jest dobry: na koniec przeczytaj go na głos.
