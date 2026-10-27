# Changelog hq

## 1.10.0 · 2026-10-27
- Równoległe czaty w jednym projekcie: `context.md` wspólny, fokus/następne/blokery/handoff każdego czatu w własnym `.hq/threads/<slug>.md` (szablon `templates/thread.md`), bo jeden nadpisywany plik gubił wątki drugiego czatu. Skill `hq:context`: zasady (zapis tylko do swojego wątku, ponowny odczyt i punktowa edycja wspólnego pliku); hook SessionStart wczytuje wszystkie wątki; `handoff.md` nadal wczytywany. Testy hooka rozszerzone.

## 1.9.0 · 2026-10-26
- Zakupy i wybór produktu: `research/references/purchasing.md` (proces Z1-Z11: potrzeba, wymagania twarde/miękkie, TCO, lista kandydatów, opinie, dokumentacja, sprzedawca, dostępność i dostawa, gwarancja i serwis, macierz z wagami, zapis decyzji, checklist); podpięte w `hq:research` i routingu orkiestratora; zakup/płatność tylko po zgodzie człowieka.

## 1.8.0 · 2026-10-26
- Orkiestrator wzmocniony wg analizy wzorców orkiestracji: krok 0 (cel, kryterium, ryzyko, plan >3 kroków), zgoda człowieka przed działaniami nieodwracalnymi/zewnętrznymi, najmniejsze uprawnienia w paczce, limity (≤3 równolegle, 1 ponowienie), recenzent niezależny dla wyników krytycznych, rozstrzyganie sprzecznych zwrotów, struktura odpowiedzi końcowej. Pominięte jako nieprzydatne w Claude Code: rejestry, circuit breakery, logi kosztów, warstwy pamięci (są w `.hq/`).

## 1.7.0 · 2026-10-26
- Wywiad o marce przepisany (`brand/references/discovery-questions.md`): ~200 pytań z ankiety sprowadzone do 4 rund rdzenia (16 pytań) + rundy dodatkowe D1-D5 na żądanie; zasady: najpierw skan org/projektu i potwierdzanie zamiast pytania od zera, opcje z rekomendacją, "nie wiem" = propozycja, wizualne rundy pokazem; tryby Szybki/Standard/Pełny.

## 1.6.0 · 2026-10-26
- Dobór motywu i wzorów marki: `brand/references/pattern.md` (proces W1-W8: wejście ze strategii, metafora, motyw z logo/produktu/wartości, typ wzoru, moduł i rytm, system 5 warstw w skalach mikro/średnia/makro, kolor wzoru, testy skali, powtarzalności, czytelności i mono; szablon zapisu).
- Podpięte w `hq:brand` (B3), `brand-designer`, referencji `visual-and-voice.md` i sekcji 6 szablonu brandbooka.
- Styl graficzny, zdjęcia, grafiki i mockupy: `brand/references/imagery.md` (proces G1-G9: emocje, słownik wizualny, moodboard, zasady fotografii, styl ilustracji/ikon/3D, mockupy jako test, shot list, stock, szablon zapisu); podpięte w B3, B5, `brand-designer`, `visual-and-voice.md`, sekcji 7 brandbooka i opisach slajdów 7-8.

## 1.5.0 · 2026-10-26
- Profesjonalny dobór kolorów: `brand/references/color.md` (proces K1-K8: strategia, mapa kategorii, harmonie, role, stany, wersje jasna/ciemna/mono, testy kontrastu i punktów styku, zapis).
- Profesjonalny dobór fontów: `brand/references/typography.md` (proces T1-T10: role, parowanie, źródła z jasną licencją, polskie znaki, skala, licencja).
- Podpięte w `hq:brand` (B3), `brand-designer` i szablonie brandbooka (sekcje 4-5).

## 1.4.0 · 2026-10-26
- Szablon slajdów brandbooka `templates/brandbook-slides.md`: 15 ramek o stałym układzie (tytuł 2-liniowy, opis, zaokrąglony panel treści) w kolejności obowiązkowego zestawu; podpięty w `hq:brand`, `brand-designer`, referencji Figmy.

## 1.3.0 · 2026-10-26
- Bez osobnego taga i commita: zmiany weszły do wydania 1.4.0 (tag v1.4.0).
- Lepsze tworzenie logo: `brand/references/logo.md` (proces L0-L12: brief, research konkurencji, kierunki i metafora, eksploracja 8+ szkiców, ocena, wektor mono-first, typografia, kolor, system znaków, kinetic, testy, prawo, pakiet końcowy, rola AI) i `scripts/logotest.py` (lint SVG + arkusz 16-128 px); podpięte w `hq:brand` i `brand-designer`.

## 1.2.0 · 2026-10-26
- Branding, grafika, kolory i ekrany zawsze w Figmie: wspólna referencja `orchestrator/references/figma.md` (sprawdzenie Figma MCP, prośba o podłączenie i o niezbędne dane, mapowanie etapów marki i UX na Figmę, bezpieczeństwo zapisu, odmowa tylko jako zapisana decyzja); odwołania w orkiestratorze, `hq:brand`, `hq:ux-ui`, wpis `Figma:` w szablonie `context.md`.

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
