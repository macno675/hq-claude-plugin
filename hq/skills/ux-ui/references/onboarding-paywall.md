# Onboarding i paywall (dla `ux-designer`, `ui-designer`, `hq:product-management`)

Liczby z materiałów wideo (RevenueCat, Adapty, wtórne) = kierunek do testu, `[ZAŁOŻENIE]` dla Twojego produktu.

## Onboarding: domyślnie najkrótszy
Przyczyna odpływu (wg źródła ~77% użytkowników w 3 dni): onboarding jak urzędowy formularz (rejestracja, zgody, samouczek) zamiast pokazania wartości. **Zasada: jak najszybciej do głównej wartości.** Wzór: Granola - 2 ekrany (logowanie, zgoda na mikrofon), bez kreatorów celów i wycieczek, po dwóch kliknięciach gotowa do pracy. Zgody prosić w momencie użycia, nie z góry.

### Kiedy wydłużać (oba warunki rozważ osobno)
1. **Hiperpersonalizacja pierwszego wrażenia**: odpowiedzi realnie zmieniają ekran startowy (plan, cel, dieta). Bez tego pytanie jest ceremonią.
2. **Filtr motywacji**: długi quiz (20+ pytań, skrajnie ~100 ekranów) odsiewa przypadkowych i zostawia osoby z silną potrzebą i intencją zakupu.
Test pytania: czy odpowiedź zmieni to, co użytkownik zobaczy zaraz potem? Nie = usuń. Długi onboarding ma pasek postępu, pozwala wrócić i kończy się wartością (spersonalizowany wynik), nie ścianą.

## Paywall: wzorce do testowania
1. **Plany tygodniowe**: rosnący udział w przychodach, konwertują lepiej niż roczne (niska bariera "cena kawy"); sprawdź retencję i zwroty, nie tylko konwersję.
2. **Zasada jednej sesji**: ok. 82-89% startów trialu następuje w dniu instalacji, duża część rezygnacji też; paywall i wyjaśnienie trialu muszą działać w pierwszej sesji.
3. **Struktura ponad cenę**: największe efekty dają liczba planów, lokalna waluta i język, struktura trialu; sama zmiana ceny najmniej. Plan bez trialu vs z trialem: największy skok LTV w przykładzie źródła.
4. **Uczciwość**: nagłówek i oś czasu "dziś / dzień X przypomnienie / dzień Y pierwsza opłata", jasne "nic nie płacisz teraz" (Cal AI, Lose It!, Blinkist: wyższa konwersja i mniej reklamacji bez wzrostu rezygnacji). Brak ukrytego druku, łatwa rezygnacja. Dotyczy też zgodności z prawem konsumenckim (`hq:legal-safety`).
5. **Wyższa cena = często wyższa konwersja** (przyciąga wysoką intencję; wojna cenowa obniża postrzeganą wartość). Testuj, nie zakładaj.
6. **Eksperymentowanie**: różnica przychodów wynika z liczby testów (liderzy 15-50+ eksperymentów rocznie na paywallu). Paywall to ekran żywy: hipoteza, test A/B (`hq:data-analysis`: `marketing/scripts/abtest.py`, `samplesize.py`), decyzja zapisana w `decisions.md`.

Zgoda człowieka przed zmianą cen, uruchomieniem testu na prawdziwych użytkownikach i tekstem o opłatach.
