# Ramy: prawo, zgodność, bezpieczeństwo

Wszystko poniżej to **listy kontrolne i szkielety do weryfikacji** przez właściwych specjalistów, nie porada prawna. Najpierw ustal jurysdykcję.

## Rejestr obowiązków (`obligations.tsv`)
`id | obowiązek | źródło (akt/norma/umowa/licencja, data sprawdzenia) | dotyczy (projekt/produkt/wydarzenie) | właściciel | termin | priorytet | status | DO WERYFIKACJI przez`
Źródła do mapowania: prawo krajowe i unijne · wymagania branżowe · normy techniczne · warunki licencji (w tym open source zależności) · umowy z klientami i dostawcami · ochrona danych · BHP · wymagania produktu · wymagania wydarzeń · zobowiązania wobec inwestorów i partnerów.

## Ocena ryzyka
Dla każdego: opis · kategoria (prawo/BHP/dane/produkt/wydarzenie/cyber/reputacja/finanse) · prawdopodobieństwo 1-5 · wpływ 1-5 · kto może ucierpieć · skutki finansowe/prawne/reputacyjne · środki · właściciel · status · termin przeglądu. Tabela do `riskscore.py` (kolumny w nagłówku skryptu).
Hierarchia środków ochronnych: 1) usunąć zagrożenie, 2) zastąpić mniej groźnym, 3) środki techniczne (osłony, blokady, zabezpieczenia), 4) organizacyjne (procedury, szkolenia, strefy, oznakowanie), 5) środki ochrony indywidualnej. Zacznij od góry.
Typowe zagrożenia: elektryczne, mechaniczne, praca na wysokości, pożar, tłum i panika, pogoda, awaria sprzętu, nieuprawniony dostęp, zagrożenia cyber i dla danych, hałas, potknięcia, transport i montaż.

## Polityki i procedury (krótkie, per rola)
Bezpieczeństwo i BHP · procedury pracy i instrukcje stanowiskowe · ochrona danych · zgłaszanie incydentów · ocena dostawców · zasady podpisywania umów (kto, do jakiej kwoty) · postępowanie z danymi · reagowanie kryzysowe · ewakuacja · badanie wypadków · użycie AI (`hq:ai-strategy`). Każda: cel, zakres, rola odpowiedzialna, kroki, wersja, data przeglądu.

## Umowy (lista kontrolna do przeglądu prawnika)
Strony i uprawnienia · przedmiot i zakres · terminy i odbiory · wynagrodzenie i płatności · gwarancja i odpowiedzialność za wady · ograniczenie odpowiedzialności · poufność (NDA) · prawa autorskie i licencje (przeniesienie praw, pola eksploatacji) · dane osobowe (powierzenie przetwarzania) · ubezpieczenie · zmiany i rozwiązanie · kary umowne · prawo właściwe i spory · siła wyższa. Umowy: pracownicze/B2B/zlecenie, klient, dostawca, licencyjne, wynajem miejsca i sprzętu. Podpisuje użytkownik po przeglądzie.

## Własność intelektualna
Nazwa firmy i produktu · znaki towarowe (wstępne sprawdzenie baz, np. EUIPO, UPRP; rejestracja i ocena ryzyka kolizji: rzecznik patentowy) · wzory przemysłowe · prawa autorskie (kto jest autorem, umowy z twórcami i freelancerami, licencje na zdjęcia, muzykę, fonty) · know-how i tajemnica przedsiębiorstwa · oprogramowanie i **licencje zależności open source (zgodność licencji z modelem dystrybucji)** · dokumentacja techniczna.

## Ochrona danych (RODO/GDPR i prawo krajowe - DO WERYFIKACJI)
Jakie dane, po co (cel), podstawa prawna, zgody (gdy wymagane), minimalizacja, bezpieczeństwo (kontrola dostępu, szyfrowanie, kopie), czas przechowywania i usuwanie, udostępnianie, **umowy powierzenia z podmiotami przetwarzającymi**, prawa osób (dostęp, sprostowanie, usunięcie, sprzeciw, przenoszenie), rejestr czynności przetwarzania (gdy wymagany), ocena skutków (DPIA) przy wysokim ryzyku, procedura naruszeń (zgłoszenie do organu nadzorczego co do zasady w ciągu 72 godzin od stwierdzenia, o ile wymagane - zweryfikuj), potrzeba inspektora ochrony danych. Dane małoletnich i wrażliwe: podwyższona ostrożność. Uczestnicy wydarzeń, wizerunek (zgody na zdjęcia/nagrania).

## Zgodność produktu (elektronika, rynek UE - lista do weryfikacji; sprawdź aktualne akty i normy zharmonizowane)
Oznakowanie CE i deklaracja zgodności, dokumentacja techniczna · dyrektywy/rozporządzenia zależne od produktu, m.in. EMC, niskonapięciowa (LVD), radiowa (RED) dla urządzeń z radiem (Wi-Fi/BLE), RoHS (substancje), WEEE (zużyty sprzęt), baterie, ogólne bezpieczeństwo produktów, ekoprojekt · instrukcja i ostrzeżenia w języku rynku · oznakowanie (typ, numer partii, producent, adres) · gwarancja i odpowiedzialność producenta · recykling i środowisko · testy w akredytowanym laboratorium (EMC/bezpieczeństwo) · łańcuch dostaw (deklaracje komponentów). Zasilanie sieciowe, baterie Li-ion i radio podnoszą wymagania - ustal wcześnie (`hq:electronics` plan, projekt PCB a EMC).

## Bezpieczeństwo projektu i wydarzenia
Ocena ryzyka (jw.) · plan bezpieczeństwa: zasady pracy, środki ochrony, strefy ograniczonego dostępu, punkty medyczne, ewakuacja, komunikacja awaryjna, kontakty alarmowe, odpowiedzialni, procedury (pożar, awaria, zagrożenie zdrowia) · wymagania formalne wydarzenia (zgłoszenia, zezwolenia, zasady imprez masowych, hałas - zależne od kraju i skali) · ubezpieczenie · nadzór w trakcie (obserwacja warunków, nowe zagrożenia, korekta niebezpiecznych działań, komunikacja, dokumentowanie incydentów). **REKOMENDACJA ZATRZYMANIA** przy bezpośrednim zagrożeniu: pierwsza linia odpowiedzi, powód, kto ma zdecydować.

## Szkolenia (`training.tsv`: `szkolenie | grupa | termin | prowadzący | zakres | kto ukończył | następne`)
Grupy: pracownicy, kierownicy, zespoły techniczne, dostawcy, wolontariusze, obsługa klienta. Praktyczne, dopasowane do roli, powtarzane; sprawdzenie zrozumienia.

## Audyty (`audits/`)
Planowe, udokumentowane, zakończone działaniami naprawczymi z właścicielem i terminem. Zakres: dokumentacja, uprawnienia, stan sprzętu, procedury, bezpieczeństwo miejsca, ochrona danych, umowy, dostawcy, realizacja zaleceń.

## Incydenty (`incidents.tsv`) - 10 kroków
1) Zabezpiecz ludzi i mienie · 2) powstrzymaj dalszą szkodę · 3) zabezpiecz dowody · 4) powiadom właściwe osoby · 5) oceń skalę · 6) powiadom organy, jeśli wymagane (decyzja użytkownika + prawnik) · 7) analiza przyczyny źródłowej · 8) działania naprawcze · 9) aktualizacja procedur · 10) wnioski dla organizacji. Kolumny: `id | data | opis | skala | ludzie/dane dotknięte | działania | zgłoszono (komu, kiedy) | przyczyna | działania naprawcze | status`.

## Raport (jedna strona)
Główne ryzyka (z `riskscore.py`) · naruszenia · incydenty i trendy · wyniki audytów · działania naprawcze i skuteczność · zmiany przepisów · rekomendacje · **decyzje wymagane** (opcje z ryzykiem, kosztem, rekomendacją).

## Dokumentacja
Rejestr obowiązków, ryzyk, incydentów · polityki i procedury · umowy i załączniki · dokumentacja szkoleń · raporty audytów · plany bezpieczeństwa · oceny ryzyka · decyzje prawne · korespondencja z organami · wnioski po incydentach.
