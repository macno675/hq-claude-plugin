# Kontrola i krytyka (Y7) - dla `ui-designer` (autoprzegląd) i `hq:design-reviewer` (ślepy krytyk)

Kolejność: odejmowanie -> `stylecheck` -> testy wzrokowe -> krytyk -> naprawa. Rubryka porządkuje ocenę, nie zastępuje człowieka.

## 1. Odejmowanie (autor, przed kontrolą)
Wskaż 5 elementów do usunięcia lub uproszczenia; usuń te, które nie wzmacniają idei ani użyteczności. Zapisz w `qa.md` (co, dlaczego zostało lub odpadło).

## 2. Testy wzrokowe (zrzuty ze `stylecheck --out`)
- **Skala szarości:** hierarchia i główna akcja czytelne bez koloru.
- **Bez logo** (`[data-logo]` ukryte): czy widać, czyje to? Czy pasowałoby do dowolnej marki z branży?
- **Miniatura:** po zmniejszeniu sekcje są rozróżnialne, jest jedna dominanta.
- **Poza hero:** charakter widać w formularzu, liście, pustym stanie.

## 3. 12 pytań krytyka (każda odpowiedź z dowodem: zrzut + miejsce albo selektor CSS; „tak” bez dowodu = „nie”)
1. Jaka jest idea, odczytana tylko z ekranu? Zgodna z `dna.md`?
2. Czy idea konsekwentnie wpływa na typografię, kompozycję, obraz, ruch, kolor?
3. Co użytkownik zapamięta po 10 sekundach?
4. Czy to pasuje do dowolnej marki z branży? Co by trzeba zmienić, żeby pasowało do konkurenta?
5. Czy typografia ma hierarchię z wyraźnymi poziomami i świadomy tracking?
6. Czy jest rytm (proporcje, odstępy sekcji), czy wszystko ma tę samą konstrukcję?
7. Czy obraz i kadrowanie są częścią DNA, czy dekoracją?
8. Czy na każdym widoku jest jedna dominanta i jedna główna akcja?
9. Czy ruch tłumaczy zmianę, czy ozdabia? Czy działa bez animacji?
10. Czy są prawdziwa treść i wszystkie stany (pusty, błąd, ładowanie, długi tekst)?
11. Co można usunąć bez straty?
12. Czy przetrwa 2 lata (trend z warunkami, nie moda)?
**Obowiązkowo:** 3 najbardziej generyczne elementy (miejsce, dlaczego generyczne, kierunek naprawy z DNA).

## 4. Rubryka 15
Idea i trafność do briefu 3 · wyrazistość (test bez logo, „dowolna marka z branży”) 3 · hierarchia, kompozycja, rytm 3 · typografia i kolor 2 · ruch i interakcja 2 · kompletność (stany, realna treść, charakter poza hero) 2.
**Werdykt W/K/F:** Wyrazisty (idea czytelna i rozpoznawalna) · Kompletny (stany, treść, wszystkie widoki) · Funkcjonalny (WCAG 2.2 AA, rdzeń UX z `hq:views` nienaruszony, `stylecheck` bez FAIL). **F jest twardą bramką.**
Progi: <9 = powrót do Y2 (kierunek nie niesie) · 9-11 = poprawki wg 3 generycznych elementów · ≥12 i F = `ready_for_review`.

## 5. Ćwiczenia presji (naprawa, nie obowiązkowy etap)
| Objaw | Ćwiczenie |
|---|---|
| za dużo dekoracji | odejmij 30% elementów, zostaw tylko to, co niesie ideę |
| słaba typografia | wersja tylko typograficzna (bez obrazów, koloru, ikon), potem wróć |
| brak charakteru | przekład zasady z innej dziedziny (soczewki z `dna.md`), nie jej wyglądu |
| zależność od koloru | wersja w jednym kolorze + neutralne |
| generyczne otwarcie | otwarcie bez klasycznego hero, w granicach makiety (zmiana struktury = nowa wersja `hq:views`) |
Wynik ćwiczenia = propozycja zmiany tokenów lub widoku, nie nowy kierunek.
