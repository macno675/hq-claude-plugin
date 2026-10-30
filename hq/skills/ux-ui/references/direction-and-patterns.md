# Kierunek, poziomy dojrzałości i wzorce (dla `ui-designer`, `hq:design-reviewer`)

## 4 poziomy pracy z AI
| Poziom | Jak powstaje | Skutek |
|---|---|---|
| 1 Przeciętność | goły prompt "zaprojektuj X" | poprawnie, bezosobowo, jak setki innych |
| 2 Nakierowanie | słownictwo, reguły typografii, system designu | staranniej, ale bez charakteru |
| 3 Przeładowanie | wszystkie referencje i style naraz, bez hierarchii | rozjeżdżanie: marginesy, komponenty, kierunki znoszą się (gorzej niż 1) |
| 4 Dyrekcja artystyczna | człowiek wybiera motyw przewodni, tnie, projektuje zachowanie pod realnego człowieka | spójnie i z intencją |
**Cel: poziom 4.** AI to silnik, człowiek kapitan. Konsekwencje dla pracy: (a) zanim zaczniesz, ustal **jeden motyw przewodni i jedno zdanie wizji** (z marki lub od użytkownika); (b) referencje z hierarchią: 1 główna, reszta tylko do wybranych cech; nie wrzucaj wszystkiego; (c) tnij: co usunąć, by cel produktu był lepiej spełniony; (d) zadaj pytanie "czego AI nie wie o stanie człowieka w tym momencie" (przykład: budzik z drzemką pozwala zasnąć znowu; zastąpiony potrząsaniem telefonu 15 s z paskiem postępu spełnia prawdziwy cel). Nie pytaj użytkownika o to ogólnikami: pokaż 2 kierunki (zasada U4).

## Rubryka oceny (15 pkt) - dla recenzenta i autoprzeglądu
Wizja 1-5 (charakter i tożsamość vs nijakość) · Spójność 1-5 (jeden system vs losowe ekrany) · Wykonanie 1-5 (logika uwzględnia realne zachowania, stany, awarie). Ocena <9/15 = poziom 1-3: wskaż, którego wymiaru brakuje i co dodać. Ocena jest opinią; uzasadnij konkretem z ekranu.

## Wzorce wg dojrzałości (lista kontrolna do przeglądu; źródło: analiza junior/mid/senior/staff)
**Lista kart (np. restauracje, produkty):** zdjęcie jako bohater karty (pełna szerokość, nie miniatura upychana "above the fold") · hierarchia typografii (nazwa większa, ocena wyróżniona) · jeden promień zaokrągleń w całym ekranie · filtry widoczne jako chipy, nie schowane w menu · jeden własny zestaw ikon kategorii zamiast fotografii (nie konkurują ze zdjęciami) · przycisk filtrów z licznikiem wyników · przełącznik widoku (karty/lista) · nazwa i ocena pod zdjęciem, gdy zdjęcia są od osób trzecich (czytelność niezależna od kompozycji) · wyszukiwarka podpowiadająca kategorie, "najlepsze dopasowanie" z historii.
**Filtry (np. nieruchomości):** jeden przewijany arkusz (bottom sheet) nad wynikami, kontekst zachowany, nie osobna podstrona na parametr (7 kliknięć na 2 parametry) · przycisk akcji z liczbą wyników na żywo ("Pokaż 41") · histogram rozkładu za suwakiem ceny · przyciski opcji z dolną granicą ("3+") zamiast stepperów +/- · przedziały gdzie sensowne · liczba wyników widoczna **przed** kliknięciem opcji (informacja wyprzedzająca) · parametr wejściowy zgodny z myśleniem użytkownika (wkład własny, rata zamiast maksymalnej ceny; system przelicza i nanosi na histogram).
Zasada ogólna: pokaż konsekwencję decyzji zanim zostanie podjęta; nie rozbijaj powiązanych decyzji na osobne ekrany; ukrywane = utracone.

## Wzorce z rynku (research)
Przed projektem przeglądnij realne ekrany podobnych aplikacji (Mobbin; jeśli podłączony serwer MCP, przeszukaj go zamiast zbierać zrzuty ręcznie) i zapisz w `research.md`: co robią wspólnie (konwencja, której nie łam bez powodu), czym się różnią, co przyjmujesz i dlaczego. Kopiowanie bez powodu = poziom 1.
