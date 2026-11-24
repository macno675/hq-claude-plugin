# Zabezpieczenie przed "AI slop" (dla `ui-designer`, `frontend-engineer`, `hq:design-reviewer`)

Slop = poprawne, ale generyczne: decyzje domyślne zamiast autorskich. Przyczyna: model dostaje opis funkcji, nie ideę i system. **Jakość zależy od idei, systemu i referencji, nie od długości promptu.**

Proces wyglądu (idea i DNA -> 3 kierunki -> widok referencyjny -> tokeny -> kontrola i ślepy krytyk) i pełna lista slopu z podziałem na FAIL i flagi: skill `hq:look`, `look/references/slop.md`; kontrola techniczna: `look/scripts/stylecheck.mjs`.

Zostaje tutaj (dotyczy każdego materiału, nie tylko UI):
1. **Specyfikacja przed generowaniem:** z krótkiego pomysłu zrób szczegółowy plik `.md` (cel, użytkownik, sekcje, treści, stany, ograniczenia) i dopiero z niego generuj.
2. **Referencje z hierarchią:** jedna główna, reszta tylko do wybranych cech (inaczej poziom 3 "Frankenstein", `direction-and-patterns.md`).
3. **Prawdziwe obrazy zamiast generycznych ilustracji:** zdjęcia lub spójnie stylizowane materiały (własne, licencjonowane lub wygenerowane i zweryfikowane pod prawa); proste SVG z szablonu to znak slopu.
4. **Eksploracja drogo, wykończenie tanio:** kierunki w HTML/SVG, gotowe układy do repo (`hq:frontend`), szlif lokalnie.
5. **Ten sam system dla każdego materiału:** strona, druk, social, prezentacje z tych samych tokenów (spójność marki, `brandscan.py`).
Logo i znaki: osobna lista w `brand/references/logo.md` L4a.
