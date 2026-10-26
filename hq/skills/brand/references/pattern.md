# Motyw i wzory marki: proces (B3)

Wzór to rozszerzenie DNA marki, nie ozdoba: ma czynić markę rozpoznawalną bez logo. Wynik to **system**, nie jeden plik. Pytanie wyjściowe nie brzmi "jaki będzie ładny", tylko: co marka znaczy i jaki kształt lub rytm to wyraża.

## Pojęcia
- **Motyw** = atom (pojedynczy kształt: kropka, linia, łuk, kąt, fragment logo).
- **Wzór** = powtarzalny układ motywów.
- **Tekstura** = subtelna struktura powierzchni (papier, ziarno).
- **System** = zasady: kiedy, gdzie, w jakiej skali i kolorze.

## Proces W1-W8
1. **Wejście z B1:** wartości (3-5), osobowość, emocja, historia, produkt i proces marki, miejsca użycia (ekran, druk, opakowanie, produkt, wideo). Brak B1 = stop.
2. **Słowa-klucze i metafora:** 10-20 słów o marce, każde zamień na kształt lub mechanizm. Szukaj metafory, nie dosłownej ikony: połączenie = linie schodzące się w jeden kształt · rozwój = rosnący rytm · precyzja = siatka, moduł · ruch = skos, przesunięcie, fala · równowaga = symetria, odbicie · ochrona = warstwy, obwódka · energia = kontrast, kąt, powtórzenie · naturalność = organiczna krzywa · rzemiosło = tekstura, nieregularność · technologia = moduł, sygnał.
3. **Źródło motywu** (kolejność): logo (fragment litery, łuk, kąt, kropka, negatyw, rytm liter, geometria monogramu) → produkt lub proces (sygnał, struktura danych, materiał, przepływ) → wartość lub historia (miejsce, architektura, natura). Motyw z logo daje wzór będący przedłużeniem identyfikacji. Konkurenci: wzór nie może przypominać ich wzorów (agent `researcher`).
4. **Typ wzoru** wg marki: geometryczny (precyzja, technologia: SaaS, inżynieria) · organiczny (natura, ciepło: wellness, żywność) · editorial (linie, siatka, typografia: media, kultura) · teksturalny (rzemiosło, premium: kawa, kosmetyki, moda) · danych i sygnałów (AI, fintech, analityka) · narracyjny (marki z historią) · kinetic (animowany: www, aplikacja, wideo). Zwykle jeden typ wiodący.
5. **Moduł i rytm:** zacznij od jednego prostego modułu, 2-3 kształty, spójne proporcje. Rytm steruje emocją: równy = spokój, zaufanie · nierówny = energia, ruch · gęsty = bogactwo, intensywność · luźny = lekkość, natura. Kontroluj odstęp, rozmiar, kierunek, rotację, naprzemienność, gęstość. Płytka musi układać się **bezszwowo** (poziomo, pionowo, po przekątnej, po przesunięciu, bez przypadkowych "dziur"). Warianty 2-4 w Figmie (`figma.md`), wybór wg kryteriów, zapis w `decisions.md`.
6. **System wzorów (5 warstw):** główny (rozpoznawalny, kampanie, opakowania, duże formaty) · pomocniczy (spokojniejszy: tła, dokumenty, e-mail, prezentacje, www) · akcentowy (wyrazisty: social, merch, wydarzenia) · teksturalny (bardzo subtelny: tło zdjęcia lub sekcji, druk) · ruchomy (animacja motywu: www, wideo, intro, ekrany wydarzeń). Każdy w skalach: **mikro** (tło), **średnia** (marketing), **makro** (plakat, opakowanie, baner).
7. **Kolor wzoru** (z `color.md`): najpierw jeden kolor (czerń, biel, kolor marki), potem dodawaj. Paleta ograniczona: kolor główny, pomocniczy, akcent, neutralne tło; role i proporcje z `color.md` (60/30/10), z tym że we wzorze dominuje neutralne tło, a kolor główny i akcent są dodatkiem. Nie używaj całej palety naraz, często najlepszy jest wzór dwukolorowy. Wzór ma wersje: jeden kolor, czarna, biała, jasne i ciemne tło, negatyw.
8. **Testy i zapis:** 
   - skala: 16, 64, 256, 1024 px, baner, opakowanie;
   - powtarzalność: szwy, rytm, dziury, przesunięcie;
   - czytelność: tekst, logo (pole ochronne), przycisk CTA, zdjęcie, nagłówek na wzorze; kontrast tekstu `scripts/contrast.py` liczony na najciemniejszym i najjaśniejszym polu wzoru;
   - mono: czerń, biel, jeden kolor, negatyw;
   - kontekst: www, aplikacja, e-mail, slajdy, druk, opakowanie, social, merch, wideo.
   Zapis w sekcji 6 brandbooka wg szablonu poniżej; pliki jako SVG (płytka bezszwowa) + PNG podglądowe, w bibliotece zasobów.

## Szablon zapisu (sekcja 6 brandbooka)
```
Motyw główny: pochodzenie (logo/wartość/proces) · kształt · znaczenie
Wzór główny / pomocniczy / akcentowy / teksturalny / ruchomy: zastosowanie · skala (mikro/średnia/makro) · kolory · plik
Zasady: nie zasłania logo · tekst zawsze czytelny · druk w mono · nie pod ważnym CTA · testy skali i kontrastu
Poprawne i błędne użycia (przykłady)
```

## Zasady
- Motyw musi mieć znaczenie, nie jest przypadkową dekoracją.
- Prostota daje skalowalność; rytm ważniejszy niż liczba elementów.
- Wzór wspiera treść i nie konkuruje z logo ani CTA; nie wszędzie w tej samej intensywności.
- Wzór musi działać w jednym kolorze (inaczej nie jest uniwersalny).
- Kolory wzoru tylko z tokenów; `brandscan.py` łapie dryf.

## Błędy do wyłapania
Wzór bez związku z marką · zbyt wiele elementów lub zbyt gęsty · konkuruje z tekstem · brak wersji mono i małoskalowej · brak płytki bezszwowej · kopia trendu lub konkurenta · brak zasad użycia · ta sama intensywność wszędzie · jeden plik zamiast systemu.
