# Ramy zarządzania produktem

## Problem (karta)
Użytkownik (segment) · problem · częstotliwość · wpływ (ilościowo) · jak radzi sobie dziś · dlaczego obecne rozwiązania nie wystarczą · miara sukcesu · ograniczenia (biznes, technologia, prawo) · dowody `[DOWÓD: źródło]` i założenia `[ZAŁOŻENIE]`.

## Wizja (`vision.md`)
Jeden akapit: jaki świat tworzymy i dlaczego to ma znaczenie; dla kogo; co jest nienegocjowalne. Kryteria: prosta, zrozumiała, ambitna ale realna, spójna ze strategią firmy, ukierunkowana na użytkownika, da się ją opowiedzieć zespołowi. Wyznacza kierunek, nie plan zadań.

## Strategia (`strategy.md`)
Dla kogo · jaki problem · czym różnimy się od konkurencji (pozycjonowanie) · model biznesowy · priorytety (3-5) i **czego nie robimy** · miary sukcesu (nieliczne, powiązane z zachowaniem użytkownika) · ryzyka i jak je ograniczamy · zależności od zasobów. Łączy potrzeby klientów, cele firmy i możliwości techniczne.

## Roadmapa (`roadmap.md`)
Format Teraz / Następne / Później. Pozycja: problem do rozwiązania (nie lista funkcji), oczekiwany rezultat i miara, zależności, kamień milowy, ryzyka, założenia, **pewność** (wysoka/średnia/niska). Teraz = zobowiązane, Następne = prawdopodobne, Później = kierunek. Zmieniaj, gdy zmieniają się dane, rynek, priorytety lub zespół; komunikuj zmiany z powodem.

## Priorytetyzacja (`backlog.tsv`)
`id | pozycja | zasięg | wpływ | pewność_% | nakład | status | notatki`. RICE = zasięg x wpływ x pewność / nakład (`prioritize.py`). Wpływ w skali np. 0.25/0.5/1/2/3. Nakład spójnie (osobo-dni). Niska pewność (< 50%) = najpierw badanie lub eksperyment, nie budowa. Po RICE oceń: strategię, zależności, ryzyko, pilność (termin zewnętrzny), koszt opóźnienia. Backlog to uporządkowana lista pracy prowadząca do celu, nie wysypisko pomysłów; regularnie usuwaj nieaktualne.

## Wymagania (`requirements.md`)
Problem i dlaczego teraz · użytkownik · oczekiwany rezultat · historyjki/scenariusze · przypadki brzegowe i błędy · ograniczenia (techniczne, prawne, budżet) · miary sukcesu · w zakresie / poza zakresem · kryteria akceptacji · pytania otwarte. Intencja, nie wygląd.

## Hipotezy i eksperymenty
"Jeśli wprowadzimy [rozwiązanie], oczekujemy [rezultat] dla [segment]." Miara główna i ochronne, próg sukcesu, próg zmiany kierunku, czas, ryzyka zafałszowania. Szczegóły i obliczenia: `hq:data-analysis`. Małe grupy: porównania przed/po i feedback z zastrzeżeniami.

## Miary sukcesu (wybierz nieliczne)
| Obszar | Przykłady |
|---|---|
| Pozyskanie | rejestracje, koszt pozyskania, jakość leadów |
| Aktywacja | czas do pierwszej wartości, odsetek kończących kluczowe działanie |
| Zaangażowanie | częstotliwość, adopcja funkcji, powtarzalność |
| Retencja | powroty, utrzymanie, odejścia |
| Monetyzacja | konwersja, przychód, wartość klienta |
| Jakość | błędy, zgłoszenia, czas reakcji, satysfakcja |

## Launch (lista gotowości)
Gotowość produktu i jakość (`hq:qa-engineer`) · dokumentacja · komunikacja i marketing (`hq:marketing`) · szkolenia i obsługa klienta · prawo i bezpieczeństwo (`hq:legal-safety`, `hq:cybersecurity`) · plan reakcji na problemy (wyłącznik/rollback) · pomiar od dnia 1.

## Interesariusze
Zarząd (postęp, ryzyka, wyniki, decyzje), sprzedaż/marketing (wartość, grupa, przewagi; sygnały z rynku), support (realne problemy, częste pytania), inżynierowie (wykonalność, koszt, zależności, jakość), projektanci (problem i kontekst; weryfikacja z użytkownikami). Oddzielaj wymagania od rozwiązań, tłumacz kompromisy, nie wydawaj rozkazów: wspólny obraz celu i decyzje na argumentach.

## Dokumentacja
Wizja · strategia · roadmapa · backlog · wymagania · decyzje produktowe · persony i wnioski z badań · miary sukcesu · wyniki eksperymentów · raporty po wdrożeniu · rejestr ryzyk · zmiany.
