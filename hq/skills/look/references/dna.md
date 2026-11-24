# DNA i idea (Y0-Y1) - dla `ui-designer`

Cel: zamienić markę i makietę w **zasady, które same podejmują decyzje**. Bez tego kierunki powstają z gustu modelu (poziom 1-2 z `ux-ui/references/direction-and-patterns.md`).

## Y0 `brief.md`
Produkt i odbiorca (1-2 zdania) · widoki krytyczne z `.hq/views/views.tsv` · realne teksty i dane (z makiet/briefu; lorem = błąd) · platformy i motywy (jasny/ciemny wymagany?) · marka efektywna: co dziedziczysz bez zmian (rdzeń org, kolory K, kroje T, logo), co wyprowadzasz (neutralne, stany, ruch, głębia), czego nie wolno ruszyć · tryb: nowy styl / rozwinięcie istniejącego systemu (wtedy kierunki dotyczą tylko różnic) · skala.
**Bez brandbooka:** ≤5 pytań (dla kogo, jakie wrażenie ma zostać po 10 s, czego się boisz, 1-3 marki/rzeczy spoza branży, które lubisz i dlaczego, ograniczenia), DNA z tagiem `[ZAŁOŻENIE]`, propozycja `hq:brand` Mini jako opcja.

## Y1 `dna.md` (szablon)
1. **Problem w 1 zdaniu**, bez słów: nowoczesny, minimalistyczny, premium, czysty, elegancki, intuicyjny. Test: zdanie nie pasuje do konkurenta.
2. **Mapa napięć:** obecny odbiór -> pożądany odbiór · konwencje kategorii (co robią wszyscy; `brand` K2) · co zachować (rozpoznawalne, działa) · co świadomie złamać i dlaczego.
3. **Idea w 1 zdaniu** = generator decyzji, nie hasło. Test: wypisz, jak wpływa na typografię, kompozycję, obraz, ruch, kolor; <4 konkretne konsekwencje = idea za słaba. Źródło: treść lub funkcja produktu, nie ozdoba.
4. **Macierz** (3-5 wierszy): `cecha marki | konsekwencja projektowa | gdzie widać | czego zakazuje`. Przykład: „rzetelny | liczby w kroju z cyframi tabelarycznymi, wyrównane do prawej | cennik, tabela, rezerwacja | zakaz gradientu i animowanych liczników”.
5. **Osobowość interakcji** (jedna): precyzyjna (krótko, bez overshoot, reakcja liniowa w przestrzeni) · elegancka (dłużej, miękkie wyhamowanie) · energiczna (szybko, dopuszczalny lekki overshoot) · techniczna (natychmiast, zmiana stanu zamiast ruchu) · organiczna (sprężyna, ruch z fizyką). Wartości: `motion.md`.
6. **DNA, sygnatura, momenty:** DNA (3-4 cechy widoczne na każdym widoku: krój i skala, rytm odstępów, proporcje koloru, sposób kadrowania obrazu) · 3-5 **kandydatów sygnatury** z uzasadnieniem z idei (jeden zostanie wybrany w Y3; musi pełnić funkcję w ≥3 kontekstach: np. znacznik stanu, kształt narożnika zdjęć, oś czasu, krój cyfr) · 1-3 **momenty ekspresji** (otwarcie, sukces, pusty stan, ładowanie). Sygnatura nie z gradientu ani glow.
7. **Anty-wzorce projektu:** 5-8 rzeczy, których nie robimy (z `slop.md` + ze złamanych konwencji).
8. **Budżet złożoności:** 1-3 autorskie animacje, jeden efekt specjalny (lub zero), biblioteki tylko gdy CSS nie wystarcza; każdy efekt: cel, koszt, prostsza alternatywa, mobile, reduced-motion.

## Soczewki (źródło różnorodności w Y2)
Zamiast katalogu trendów bierz **zasady** (nie wygląd przedmiotu) z innej dziedziny: typografia redakcyjna (gazeta, magazyn) · siatka szwajcarska i architektura · wnętrze auta i wzornictwo przemysłowe (pokrętła, skale) · materiał i rzemiosło (papier, tkanina, druk) · choreografia i montaż filmowy (rytm, cięcie) · level design gier (prowadzenie wzroku) · kartografia i infografika · oznakowanie (wayfinding). Każdy kierunek z innej soczewki; zapisz, jaką zasadę przeniosłeś.

## G1 (pytanie do użytkownika)
Pokaż: problem, ideę, macierz, osobowość interakcji, anty-wzorce. Pytanie: „Czy to jest interpretacja Twojej marki? Co skreślić?”. Bez obrazków na tym etapie (oceniamy myśl, nie fryzurę).
