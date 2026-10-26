# Changelog hq

## 1.1.0 · 2026-10-26
- Orkiestrator nie ginie w długiej rozmowie: `hq:init` wpisuje do `CLAUDE.md` blok `hq-begin/end` (ładowany po /compact i /clear; w istniejącym pliku dopisuje tylko blok), hook co 6. wiadomość (`HQ_REMIND_EVERY`) przypomina o `hq:orchestrator` i agentach `hq:*`, a start sesji zgłasza brak bloku.

## 1.0.1 · 2026-10-26
- `hq:brand`: obowiązkowy zestaw 15 elementów nowej marki (logo, logomark, clearspace, typografia, paleta, imagery, patterny, social, bannery, mockupy, wizytówka, billboard, merch, stoisko konferencyjne); warunek gotowości brandbooka.

## 1.0.0 · 2026-10-26
- Uniwersalny: brak założeń o konkretnej organizacji; przykłady neutralne (Acme); odpowiedzi i pliki `.hq/` w języku użytkownika; przeglądarka i widżety opcjonalne (działa w CLI i aplikacji).
- Organizacje (`hq:org`): rejestr `~/.hq/orgs/<slug>/`, automatyczne rozpoznanie projektu po folderze (`paths`) lub `.hq/org`.
- Dziedziczenie marki: rdzeń/elastyczne/zgodność (sekcja 0 brandbooka), tryby projektu `dziedziczy | rozszerza | odrębna-zgodna | niezależna`, profil projektu zawiera tylko różnice.
- `brandscan.py`: audyt kolorów i fontów w kodzie względem marki (MARKA/DRYF/OBCY z plik:linia); tryby Odtworzenie oraz Audyt i naprawa w `hq:brand`.
- `hq:init`: nowy, istniejący (adopcja kodu, danych, marki) i mini projekt.
- Hook startowy: routing + org.md + linia `Marka:` + kontekst projektu; obsługa dowiązań macOS i polskich znaków.
- Marketplace (`hq@hq-marketplace`), `tools/check.py` i `tools/test_hooks.sh` jako bramka wydania.

## 0.2.0 · 2026-10-26
- Ścieżki agentów przez `${CLAUDE_PLUGIN_ROOT}`, jawne `tools` u wszystkich agentów, orkiestrator pokrywa wszystkich agentów, skill `init`.
