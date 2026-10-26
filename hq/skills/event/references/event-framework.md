# Szablony wydarzenia

## Brief (`brief.md`)
Cel biznesowy · grupa docelowa · oczekiwany rezultat · miary sukcesu (liczby: frekwencja, ocena, przychód, zasięg) · forma (stacjonarne/online/hybryda) · liczba uczestników (min/plan/max) · termin i miejsce (lub kryteria) · budżet (limit i priorytet: koszt/jakość/zakres) · marka i ton · główne wymagania · ograniczenia prawne i bezpieczeństwa (`DO WERYFIKACJI`) · co uczestnik ma zapamiętać · założenia `[ZAŁOŻENIE]`.

## Podróż uczestnika (tabela)
Etap | punkt kontaktu | komunikat/kanał | właściciel | co może pójść nie tak.
Etapy: informacja -> rejestracja -> komunikacja przed -> dojazd -> powitanie -> wejście/orientacja -> program -> przerwy/posiłki/rozmowy -> obsługa problemów -> zakończenie -> komunikacja po -> materiały/nagrania.

## Budżet (struktura dla `hq:budget`)
Stałe: miejsce, produkcja techniczna, honoraria, obsługa, organizacja, ubezpieczenie, bezpieczeństwo, marketing. Zmienne (zależne od liczby uczestników): catering, materiały, transport, pakiety, nagrody. Zawsze: **rezerwa na nieprzewidziane**, harmonogram płatności (zaliczki, terminy), limity per obszar, procedura zatwierdzania dodatkowych kosztów (kto, do jakiej kwoty), rozliczenie po wydarzeniu. Wrażliwość: koszt przy -/+ 20% uczestników.

## Kamienie milowe (typowe)
Zatwierdzenie briefu i budżetu · wybór daty i miejsca · podpisanie kluczowych umów · zatwierdzenie koncepcji wizualnej · potwierdzenie programu i gości · zakończenie produkcji materiałów · gotowość techniczna · próba generalna · dzień wydarzenia · demontaż i rozliczenie · podsumowanie i raport. Każdy: właściciel, termin, zależności, definicja ukończenia (do `hq:pm`).

## Miejsce (`venue.md`) i dostawcy (`vendors.tsv`)
Kryteria miejsca: pojemność, dostępność (także dla osób z niepełnosprawnościami), dojazd/parking, wejścia i przepływ, zasilanie, sieć, nagłośnienie/światło, szatnie/toalety/zaplecze, zasady (hałas, godziny, catering), ubezpieczenie, wyjścia ewakuacyjne i wymagania formalne, koszt całkowity, plan B.
`vendors.tsv`: `dostawca | usługa | oferta/cena (data) | doświadczenie/opinie | termin realizacji | warunki anulowania | ubezpieczenie | kontakt w dniu | plan awaryjny | ocena | status`. Nie wybieraj tylko po cenie. Lista kontrolna umowy: zakres, terminy, płatności, warunki anulowania, ubezpieczenie, odpowiedzialność, kontakt i dostępność w dniu, zasady zmian. Podpisuje użytkownik.

## Logistyka (checklista)
Dojazd, parking, oznakowanie · wejścia, rejestracja, przepływ osób · catering i woda · toalety, strefy odpoczynku · transport sprzętu, rozładunek · montaż/demontaż (okna czasowe) · zasilanie, sieć, światło, nagłośnienie, obsługa techniczna · sprzątanie i odpady · ochrona i pierwsza pomoc · składowanie rzeczy · dostępność. Każdy punkt: właściciel, termin, status.

## Scenariusz / run of show (`ros.tsv`)
`start (HH:MM) | min | element | odpowiedzialny | sygnał/przejście | plan_awaryjny`. Element krytyczny oznacz `*` (wymaga odpowiedzialnego i planu awaryjnego). Uwzględnij czas na zmiany sceny/boiska, przerwy, komunikaty, materiały, dźwięk i światło. Walidacja: `python3 <katalog skilla>/scripts/runofshow.py .hq/event/ros.tsv`. Dokument zna każda kluczowa osoba przed wydarzeniem.

## Zespół (`raci.tsv`)
`obszar | odpowiada | decyduje | konsultowany | informowany | zastępca | kontakt`. Obszary: produkcja, logistyka, technika, goście/uczestnicy, komunikacja, wolontariusze, bezpieczeństwo, budżet i rozliczenia. Producent nie może być jedyną osobą, która wie wszystko.

## Ryzyka i plany awaryjne (`contingency.tsv`)
`ryzyko | prawdopodobieństwo | wpływ | właściciel | próg decyzyjny (kiedy uruchamiamy) | alternatywa | kto decyduje | kto komunikuje | koszt | kontakt awaryjny | kroki zespołu | status`. Typowe: pogoda, choroba kluczowej osoby, opóźnienie dostawy, awaria techniczna, problem z miejscem, zmiana liczby uczestników, awaria zasilania/sieci, incydent bezpieczeństwa. Ryzyko ma plan reakcji, nie tylko wpis. Wspólny rejestr z `hq:pm`, jeśli istnieje.

## Bezpieczeństwo i zgodność (`safety.md`, `DO WERYFIKACJI`)
Ocena ryzyka · plan ewakuacji (wyjścia, miejsca zbiórki, osoby odpowiedzialne) · procedury medyczne (pierwsza pomoc, kontakt z pogotowiem, AED jeśli wymagane) · ochrona uczestników (w tym małoletnich, jeśli są) · plan komunikacji kryzysowej (kto, co, kanał, komunikaty wzorcowe) · wymagania formalne (zgłoszenia, zezwolenia, zasady imprez masowych i hałasu zależne od kraju i skali) · ubezpieczenie · lista osób decyzyjnych w sytuacji zagrożenia. To projekty dokumentów; zatwierdza je organizator i właściwy specjalista/organ.

## Komunikacja (`comms.md`)
Plan: odbiorca | komunikat | kanał | termin | właściciel. Przed (zaproszenie, rejestracja, przypomnienia, dojazd, program), w dniu (powitanie, oznakowanie, komunikaty), po (podziękowanie, materiały, ankieta). Ton z brandbooka. Wysyłkę akceptuje użytkownik.

## Próba generalna (protokół)
Technika (dźwięk, obraz, zasilanie, sieć) · przejścia między punktami · komunikacja (radia/komunikator, sygnały) · strefy i oznakowanie · scenariusze awaryjne (min. 2 zagrywki) · kontakty i uprawnienia decyzyjne potwierdzone. Wynik: lista poprawek z właścicielami i terminami.

## Dzień wydarzenia (protokół dowodzenia)
Odprawa zespołu (scenariusz, role, kontakty, plan B) · jeden kanał komunikacji i jedna osoba dowodząca · log zdarzeń (czas, zdarzenie, decyzja, kto) · zasada: decyzje szybkie według planu, zmiana programu zgłaszana wszystkim kluczowym osobom · monitorowanie samopoczucia uczestników, jakości i bezpieczeństwa.

## Raport po wydarzeniu (`report.md`)
Cel osiągnięty? (miary z briefu) · frekwencja plan/rzeczywista · koszty plan vs rzeczywiste (z `hq:budget`) · dostawcy (ocena, ponowna współpraca?) · problemy i przyczyny · oceny uczestników (ankieta) · co zmienić w kolejnej edycji · materiały do ponownego użycia · wnioski do `~/.hq/event-lessons.md`.

## Dokumenty wydarzenia (komplet)
Brief · cele i miary · budżet i płatności · harmonogram · kamienie · dostawcy i umowy · plan miejsca · scenariusz · zadania i właściciele · plan komunikacji · rejestr ryzyk · plan awaryjny · kontakty · raport.

## Moduł turniejowy (rozszerzenie na życzenie)
Dla zawodów sportowych dodaj: format (grupy/puchar/liga, liczba drużyn), czas meczu i przerwy, liczba boisk, sędziowie i zaplecze, odpoczynek drużyn między meczami, zasady punktacji i tie-breakerów, protokół wyników, nagrody. Harmonogram meczów pod ograniczenia (boiska, odpoczynek) może wymagać osobnego narzędzia - zaproponuj je użytkownikowi, nie zakładaj.
