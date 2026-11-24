---
name: look
description: Styl UI po zatwierdzonej makiecie - idea i DNA, trzy kierunki, widok referencyjny, tokeny z ruchem i interakcją, kontrola i ślepy krytyk, bramka akceptacji.
---

# Wygląd: idea, charakter i system stylu, zanim powstanie kod

Po zatwierdzonych makietach (`hq:views` = `approved`), a przed kodem (`hq:frontend`), ustalasz **jak produkt wygląda i się zachowuje**: kolory, typografię, odstępy, skalę, promienie, głębię, ruch i reakcje. Cel: jedna idea, rozpoznawalna na każdym widoku, bez AI slopu. Wykonuje agent `ui-designer`; krytykiem jest `hq:design-reviewer` na ślepo. Ty pytasz użytkownika i pokazujesz zrzuty. Artefakty w `.hq/look/`.

## Zasady
1. **Konflikt rozstrzyga kolejność: użyteczność i WCAG 2.2 AA > rozpoznawalność marki > efekt.** Rdzeń (nawigacja, formularze, wyszukiwanie, główne akcje) trzyma konwencję; eksperyment tylko w warstwie ekspresji.
2. **Idea przed formą.** Problem w jednym zdaniu bez słów-wytrychów (nowoczesny, minimalistyczny, premium, czysty, elegancki), mapa napięć, **idea w jednym zdaniu jako generator decyzji** (wpływa na ≥4 z: typografia, kompozycja, obraz, ruch, kolor). Szczegóły: `references/dna.md`.
3. **DNA wszędzie, sygnatura z funkcji, momenty rzadko.** DNA (typografia, rytm, proporcje koloru, kadrowanie) widać na każdym widoku; sygnatura to jeden element w ≥3 kontekstach, który coś robi; 1-3 momenty ekspresji. Większość interfejsu mówi cicho.
4. **Trzy kierunki to trzy idee, nie skala odwagi** (bez „bezpieczny/środkowy/odważny”). ≥4 różnice, po jednym odważnym ruchu, na prawdziwej treści, z trudnym fragmentem, nie tylko hero. Intensywność wybiera się dopiero wewnątrz kierunku (`references/directions.md`).
5. **Makieta jest kontraktem.** Kolejność i zawartość bloków z `hq:views` zablokowane; wolne: proporcje, wyrównanie, skala, kadrowanie, asymetria w bloku. Zmiana struktury = nowa wersja makiety. Skrócenie tekstu pod skalę = propozycja do akceptacji (`hq:brand` lub `design:ux-copy`).
6. **Tokeny wyprowadzasz z zatwierdzonego widoku referencyjnego**, nie odwrotnie; rozmiar systemu proporcjonalny do projektu (`references/craft.md`, `references/motion.md`).
7. **Trend tylko z warunkami** (`references/trends.md`): pasuje do DNA, kontrast liczony na najgorszym tle, wydajność, wersja awaryjna, a11y.
8. **Dwie kontrole, nigdy jedna.** `stylecheck` sprawdza technikę i spójność, nie estetykę; jego wynik nie jest dowodem „dobrego designu”. Estetykę ocenia ślepy krytyk i użytkownik (`references/critique.md`).
9. **AI nie zatwierdza sama.** Najwyżej `ready_for_review`; G1-G4 i `approved` nadaje tylko użytkownik. Każdy wyjątek od systemu i każda rezygnacja („nie użyłem X, bo…”) w `decisions.md`.

## Etapy
| Etap | Wynik w `.hq/look/` | Warunek przejścia |
|---|---|---|
| Y0 Wejście: `.hq/views/status.md` = `approved`, marka efektywna (linia `Marka:`), realna treść z makiet, platformy, tryb (nowy styl / rozwinięcie istniejącego systemu), skala | `brief.md` | brak makiety = `blocked` i propozycja `hq:views`. Brak brandbooka: wywiad ≤5 pytań i DNA z `[ZAŁOŻENIE]` (`hq:brand` Mini jako opcja, nie blokada) |
| Y1 DNA i idea: problem, mapa napięć, idea, macierz cecha -> konsekwencja -> gdzie -> zakaz, osobowość interakcji, sygnatura (kandydaci), anty-wzorce, budżet złożoności | `dna.md` | **G1 użytkownik** |
| Y2 Dywergencja: 8-12 idei w zdaniu -> 3 kierunki jako stylescape (otwarcie, trudny fragment, typografia, interakcja) + lista odrzuconych | `directions/*.html` + zrzuty | `stylecheck` bez FAIL kontrastu |
| Y3 Wybór kierunku, potem intensywności (spokojna/ekspresyjna); responsywnie 2 finaliści tylko przy wątpliwości | `decisions.md` | **G2 użytkownik** |
| Y4 Widok referencyjny: krytyczny widok w pełnym stylu, wszystkie stany, mobile i desktop (ciemny, jeśli wymagany) | `reference/` | **G3 użytkownik** |
| Y5 Fundament: tokeny z widoku (DTCG -> `tokens.css`), ruch, przepisy interakcji, mało wariantów komponentów, reguły z przykładem dobrym i złym | `tokens.css`, `design-system.md`, `motion.md` | wszystko z tokenów |
| Y6 Rozszerzenie na pozostałe widoki | `screens/` | - |
| Y7 Kontrola: odejmowanie (5 elementów) -> `stylecheck` + skala szarości + bez logo -> ślepy krytyk (12 pytań z dowodem, 3 najbardziej generyczne elementy, rubryka 15) -> przy problemie ćwiczenie presji i powrót do Y5/Y6 | `qa.md` | zero FAIL, rubryka ≥12, werdykt F -> `ready_for_review` |
| Y8 Akceptacja: zrzuty mobile i desktop, uwagi (max 2 rundy na uwagę) | `status.md` | **G4 użytkownik**: `approved` + wersja |

Skala: **Mini** (landing, 1-3 widoki: G1+G2 razem, Y2 = 3 kierunki bez rozszerzonej dywergencji, Y4 = Y6, krytyk opcjonalny, tokeny w skali Mini), **Standard** (wszystko), **Pełna** (+ test z ludźmi na widoku referencyjnym; ludzi daje użytkownik). Zapytaj o skalę na początku.

## Ślepy krytyk (Y7)
Paczka dla `hq:design-reviewer` (domena „Wygląd”): `brief.md`, `dna.md`, zrzuty (normalne, w skali szarości, bez logo), `tokens.css`, `references/critique.md`. **Bez** uzasadnień autora, rekomendacji wariantu i wyniku `stylecheck` jako argumentu. Krytyk musi wskazać 3 najbardziej generyczne elementy i odpowiedzieć na 12 pytań dowodem ze zrzutu lub CSS.

## Narzędzia
- Kierunki i widoki jako HTML/SVG + Playwright (`${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/visual.md`); szablon tokenów: `${CLAUDE_PLUGIN_ROOT}/skills/look/assets/tokens.css`. Zrzut otwórz (Read), zanim napiszesz, że wygląda dobrze.
- Kontrola: `node ${CLAUDE_PLUGIN_ROOT}/skills/look/scripts/stylecheck.mjs <plik.html> [--dark] [--out <katalog>]` z katalogu projektu. Sprawdza na 360 i 1280 px: kontrast, kolory/promienie/cienie spoza tokenów (`:root`), `prefers-reduced-motion`, emoji jako ikony, tracking, przewijanie w bok, cele dotykowe (FAIL) oraz flagi slopu (`references/slop.md`); zapisuje zrzuty zwykłe, w skali szarości i bez elementów `[data-logo]`. Świadomy wyjątek: atrybut `data-style-exception` + wpis w `decisions.md`.
- Kontrast pojedynczych par: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/brand/scripts/contrast.py`.

## Gdzie w procesie
Wejście: `hq:views` (makiety, `approved`), `hq:brand` (kolor K, typografia T, logo, system S). Wyjście: `hq:ux-ui` U5-U7 (prototyp, testy, handoff), `hq:frontend` (nie stylizuje nowego widoku bez `.hq/look/status.md` = `approved`). Wiedza z zewnątrz (wzorce kategorii, filmy o rzemiośle): `hq:external-ai`.

## Definicja gotowości
`status.md` = `approved` z wersją i datą · `dna.md` z ideą, macierzą i zakazami (G1) · wybrany kierunek i intensywność z listą odrzuconych (G2) · widok referencyjny ze stanami (G3) · `tokens.css` i `design-system.md`, każda wartość z tokenów albo wyjątek w `decisions.md` · `stylecheck` bez FAIL na wszystkich widokach · `qa.md` z odpowiedziami krytyka i rubryką. Potem `hq:context`.
