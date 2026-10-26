# Logo: profesjonalny proces (2026)

Logo to **system znaków** wynikający ze strategii, nie jeden ładny obrazek. Kolejność: strategia -> research -> kierunki -> szkice -> wybór -> wektor -> typografia -> kolor -> testy -> pliki + zasady. Nie zaczynaj od pliku wektorowego ani od generowania obrazów.

## L0 Brief (z B1 + wywiad; brak odpowiedzi = zapytaj)
Kim jest marka, dla kogo, jaki problem, wartości, postrzeganie (skale osobowości), różnica wobec konkurencji, **gdzie logo będzie używane** (ekran/druk/grawer/haft/animacja/urządzenie), ograniczenia prawne i techniczne, nazwa (długość, litery wysokie/niskie, inicjały).

## L1 Research konkurencji
3-8 logo z branży: symbole, metafory, kolory, fonty, układ. Wynik: tabelka TSV `marka / typ znaku / kolor / font / schemat` + **wolna przestrzeń wizualna** (czego nikt nie robi). Wyciągaj zasadę, nie kopiuj.

## L2 Kierunki i metafora
2-4 **mocno różne** kierunki odpowiadające na osie: techniczna-ludzka, premium-dostępna, minimalna-ekspresyjna, klasyczna-nowoczesna, poważna-lekka. Ujmuj wartość **metaforą**, nie ilustracją dosłowną (szybkość = ruch, nie strzałka; bezpieczeństwo = stabilność, nie kłódka; zaufanie = równowaga, nie uścisk dłoni).

## L3 Eksploracja (ilość przed dopracowaniem)
Typy: znak abstrakcyjny, monogram/inicjały, znak typograficzny (wordmark), znak łączony (sygnet + nazwa), negatywna przestrzeń, konstrukcja geometryczna, forma dynamiczna. Zrób **min. 8 szybkich szkiców SVG** (proste kształty, bez detali), potem selekcja do 2-4.

## L4 Ocena kierunków (1-5, wg strategii, nie gustu)
oryginalność · prostota (jeden dominujący pomysł) · czytelność w 16 px · dopasowanie do marki · skalowalność · trwałość (nie moda) · potencjał systemowy (monogram, ikona, animacja). Pokaż użytkownikowi w Figmie 2-4 warianty obok siebie z oceną; decyzja do `decisions.md` z powodem.

## L5 Konstrukcja wektorowa
Siatka konstrukcyjna, spójne grubości linii, promienie i kąty, **optyczne wyrównanie** (okręgi i „O” lekko większe/wystające, ukośne korekty), odstępy, krzywe z minimum punktów. **Monochrom najpierw**: forma musi działać czarno-biała, kolor dodajesz później. Zero gradientów, cieni, tekstur, efektów 3D, filtrów, przezroczystości jako nośnika znaczenia (nie przeżyją druku jednokolorowego, grawerunku, haftu).

## L6 Typografia logo
Font, grubość, odstępy (kerning ręcznie), proporcje, relacja sygnet-nazwa, wariant dla małych rozmiarów (większe odstępy, grubsze kreski). Nowoczesnie: prosta bezszeryfowa, 1-2 grubości. **Tekst w finalnym SVG zamień na krzywe** (obrys), ale zachowaj wersję edytowalną; sprawdź licencję fontu na logo/znak towarowy. Polskie znaki, jeśli nazwa je zawiera.

## L7 Kolor
1 kolor główny + 1 pomocniczy + neutralne, wysoki kontrast (`scripts/contrast.py`). Wersje: kolor, czarna, biała, jednokolorowa, na jasnym/ciemnym tle, na zdjęciu (z podkładem), CMYK/Pantone **DO WERYFIKACJI**. Dostępność: sprawdź czytelność przy zaburzeniach widzenia barw (znak nie może opierać się tylko na odcieniu).

## L8 System znaków (responsywne logo)
Nie jedno logo, tylko jeden system dopasowany do kontekstu: logo podstawowe · poziome · pionowe · skrócone · monogram · sygnet · ikona aplikacji (maska/zaokrąglenie, safe zone) · favicon (16/32) · wersje jasna/ciemna/mono. Digital-first (ekran, tryb ciemny), z jakością druku.

## L9 Ruch (kinetic logo, opcjonalnie)
Animuj **jeden element**, 0,5-1,5 s, proste kształty geometryczne, brak ciężkich tekstur, działa na mobile, zawsze wersja statyczna. Projektuj od początku z myślą o ruchu (Figma: motion). Wynik: krótki opis ruchu + klatki kluczowe.

## L10 Testy (bramka przed B3)
`python3 <katalog skilla>/scripts/logotest.py plik.svg [--sheet arkusz.html]` - lint (obraz rastrowy, gradient, filtr, nieobrysowany tekst, brak viewBox, liczba kolorów) + arkusz: 16/24/32/64/128 px, czarne/białe, jasne/ciemne tło. Dodatkowo ręcznie/we Figmie: wizytówka (10 mm), szyld, pojazd, billboard, opakowanie, merch, haft/grawer, profil social, e-mail, interfejs urządzenia. Logo nie działa w 16-24 px = niegotowe.

## L11 Prawo (DO WERYFIKACJI, nie udawaj prawnika)
Zaznacz do sprawdzenia: podobne znaki towarowe i nazwy (EUIPO/UPRP/WIPO, wyszukiwarka obrazu), znaczenia kulturowe/językowe symbolu, kolorów i liter w rynkach docelowych, licencje fontów i elementów, prawa autorskie (kto jest autorem, przeniesienie praw). Inicjuje użytkownik, plugin tylko przygotowuje listę.

## L12 Pakiet końcowy
SVG (źródło, krzywe), PDF/EPS, PNG przezroczysty + na jasnym + na ciemnym, czarna, biała, monogram, sygnet, favicon, ikona aplikacji, poziome, pionowe; paleta HEX/RGB/CMYK/Pantone (DO WERYFIKACJI); fonty z licencjami; pole ochronne, minimalny rozmiar; przykłady poprawne i **błędne**; dokumentacja praw. JPG/PNG nie jest plikiem źródłowym.

## AI w procesie
AI i generatory obrazów służą do **eksploracji** (kierunki, moodboardy, metafory), nie jako autor znaku: dają raster, uśrednione wzory, błędną typografię, brak systemu, brak gwarancji oryginalności i praw. Zawsze: odtworzenie ręczne jako czysty wektor, własna typografia, test, lista kontroli prawnej. Wynik generatora nigdy nie jest finalnym logo.
