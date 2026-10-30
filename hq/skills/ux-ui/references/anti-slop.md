# Zabezpieczenie przed "AI slop" (dla `ui-designer`, `frontend-engineer`, `hq:design-reviewer`)

Slop = poprawne, ale generyczne: szablonowy układ, ilustracje SVG z domyślnych kształtów, domyślne fonty i gradienty, brak decyzji autorskich. Przyczyna: model dostaje opis funkcji, nie język wizualny. **Jakość zależy od systemu designu i referencji, nie od długości promptu.**

## Przepływ (kolejność ma znaczenie)
1. **Specyfikacja przed generowaniem:** z krótkiego pomysłu zrób szczegółowy plik `.md` (cel, użytkownik, sekcje, treści, stany, ograniczenia) i dopiero z niego generuj; nie długi prompt "na żywca".
2. **Referencja estetyczna:** 1-3 realne wzorce (Pinterest, Mobbin, strona o charakterystycznej typografii) wskazane przez użytkownika lub wybrane z research (`direction-and-patterns.md`). Hierarchia: jedna główna, reszta tylko do wybranych cech (inaczej poziom 3 "Frankenstein").
3. **System designu z referencji, potem ekrany:** z referencji wyprowadź paletę, typografię, promienie, cienie, tła, mikrointerakcje, strukturę komponentów (`tokens.css`, `design-system.md`; w Figmie: zmienne i style). Gdy marka istnieje, system dziedziczy z niej i referencja dotyczy tylko różnic. Dopiero na systemie buduj układ.
4. **Przebuduj, nie dopieszczaj:** pierwszą generację traktuj jako szkic funkcji; zmień układ pod system (pełnoekranowe hero, ruch przy przewijaniu, kontrastowe sekcje, własny kursor tylko gdy pasuje do marki i dostępności).
5. **Prawdziwe obrazy zamiast generycznych ilustracji:** zdjęcia lub spójnie stylizowane materiały (własne, licencjonowane lub wygenerowane i zweryfikowane pod prawa); proste SVG z szablonu to znak slopu.
6. **Eksploracja drogo, wykończenie tanio:** szybkie kierunki wizualne w narzędziu graficznym (Figma, ew. Claude Design), gotowe układy do repo (`hq:frontend`) i szlifowanie lokalnie; nie pracuj długo w drogim narzędziu wizualnym.
7. **Ten sam system dla każdego materiału:** strona, menu/druk, posty social, prezentacje generuj z tych samych tokenów (spójność marki, `brandscan.py`).

## Lista wykrywania slopu (dla autoprzeglądu i recenzenta)
Domyślny font (Inter/Roboto/system) bez powodu · fioletowo-niebieski gradient · identyczne karty z cieniem i zaokrągleniem w siatce 3 kolumn · ikony z jednego pakietu w kółkach · hero "nagłówek + podtytuł + dwa przyciski + mockup" · stockowe SVG-bohaterowie · brak własnego motywu przewodniego (jedno zdanie wizji) · brak decyzji "czego nie robimy" · te same odstępy wszędzie, bez rytmu · brak stanów błędu/pustych (`premium-craft.md`) · tekst pisany "marketingowo" bez głosu marki. Dwa lub więcej trafień = wróć do kroku 2-3.

Pomocnicze: skill `frontend-design` (kierunek estetyczny, nieszablonowe wybory), `design:design-critique`, rubryka 15 pkt (`direction-and-patterns.md`).
