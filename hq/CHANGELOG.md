# Changelog hq

## 1.14.0 · 2026-11-20
- Logo z prośby bez briefu dawało zestaw ikon UI (niedomknięte koło, strzałka, łuki, siatka kropek). `brand/references/logo.md`: **L00** szybka prośba (≤5 pytań o brief albo brief `[ZAŁOŻENIE]`, 6 koncepcji z ideą/zasadą konstrukcji/wyróżnikiem/ryzykiem przed rysowaniem, 4 o różnej idei), **L4a** obowiązkowa autokrytyka (wygląda jak ikona funkcji, same prymitywy, wszędzie okrągłe końcówki, przypadkowe zgrubienia, różnica tylko figurą), **L4b** prezentacja (równa wielkość optyczna, bez kafelków ikony aplikacji, ≤3 zdania: związek z marką, decyzja formalna, słabość), **L5a** rzemiosło (kształty wypełnione zamiast obrysów, figura i tło, jedna świadoma decyzja, reguła konstrukcji, optyka, redukcja idei).
- Druga runda (odpowiedzi autora + Perplexity): **postój po kierunkach** zawsze (brief -> kierunki tekstem -> wybór użytkownika -> projekty -> dopracowanie), główne napięcie briefu, zakaz ogólników w uzasadnieniu i wymuszonych ukrytych znaczeń; **L1a** analiza referencji Behance/Dribbble bez kopiowania; **L4c** karta oceny 8 pól; **L4d** dopracowanie (A widoczne / B do testu / C gust, ≤3 problemy, warianty zmieniające jeden parametr) i tłumacz ogólnych uwag („bardziej premium” -> konkretna zmiana). Kształty wypełnione to domyślna zasada, nie zakaz linii.
- Identyfikacja jako system (`brand/references/system.md`, S1-S9): typ zadania, zakres fundament + moduły wg briefu (identyfikacja ≠ design system produktu), mechanizm systemu (stałe/zmienne, rozpoznawalność nie musi wynikać z logo), kompozycja (materiał wizerunkowy/informacyjny/gęsty), testy obciążeniowe, reguła = zasada/powód/przykład/wyjątek/plik, test przekazania (nowy materiał tylko z brandbooka), struktura plików 01-09 + `manifest.tsv`, kontrola jakości 8 obszarów z dowodem (A/B/C/D), status propozycja/zatwierdzone/sprawdzone. Podpięte w etapach B0-B7 `hq:brand`, szablonie brandbooka (2a Zasada systemu, 6a Kompozycja, testy w 9, manifest w 10), `pattern.md`, slajdach i `brand-designer`. Zestaw 15 pozycji: pozycje niepasujące do briefu proponowane do wykreślenia/zamiany. Definicja gotowości: slajdy HTML/PDF + `tokens.json` zamiast pliku Figma.
- `logotest.py`: nowe uwagi `styl-ikony` (okrągłe końce linii) i `obrys` (znak z obrysów), selftest rozszerzony.
- Orkiestrator: projekt logo nigdy nie jest „trywialny”. Podpięte w `hq:brand`, `brand-designer`, `anti-slop.md`. Eval `logo-no-brief`.

## 1.13.0 · 2026-11-12
- Nowy skill `hq:external-ai`: Claude sam decyduje, kiedy warto sięgnąć po inne AI, i daje gotowy prompt do wklejenia (bez API, zgodnie z regulaminami): **Perplexity** do wiedzy z zewnątrz (reguła: zwykłe wyszukiwanie vs Deep Research wg skutków decyzji, liczby podpytań i podmiotów), **ChatGPT** do pomysłów, nowych funkcji i drugiej opinii (krytyka planu), **Gemini** do obrazów, konceptów wizualnych i streszczeń YouTube. Szablony w `external-ai/references/prompts.md`; zasady prywatności promptu i weryfikacji odpowiedzi (Perplexity = trop, cytujemy otwarty URL; obraz AI = materiał roboczy, nie logo; YouTube = źródło wtórne).
- Podpięte: trasa w orkiestratorze, sekcja **PROMPT ZEWNĘTRZNY** w protokole zwrotu agentów, `hq:research` (Perplexity zamiast długiego szukania w skali Standard/Pełna), `researcher`, `brand`, `ux-ui`, `marketing`, `product-management`.
- Evals: `external-ai-research` (Deep Research + ChatGPT), `external-ai-trivial` (bez zewnętrznego AI przy prostym fakcie). README: liczby skilli, limity zwrotu agentów.

## 1.12.0 · 2026-11-01
- Wizualizacje i grafika: domyślnie lokalne HTML/SVG + Playwright zamiast Figmy (`orchestrator/references/visual.md` zastępuje `figma.md`): wybór silnika wg zadania, tokeny w `brand/tokens.json`, pętla render - zrzut - ocena (max 2 rundy), pułapki (fonty, PDF, SVG). Figma/MCP tylko na żądanie lub przy istniejącej bibliotece; kod jest wtedy źródłem. Powód: CLI tańsze w kontekście niż MCP, wynik w git, poprawka = mały patch.
- `templates/visual-render.mjs`: szablon HTML + brief JSON + tokeny -> PNG/PDF, wykrywa przepełnienie i wyjście poza artboard (przetestowane: polskie znaki, PDF, błąd przy przepełnieniu). Przepięte: orkiestrator, `hq:ux-ui`, brand (referencje i brandbook slajdy), szablony context/org.
- Audyt (Perplexity + weryfikacja w kodzie), P0 naprawione i przetestowane (testy padają na starym kodzie): slug z `.hq/org` walidowany (koniec `../` i ścieżek absolutnych); hook rozmiaru czyta transkrypt przez `jq` (odporny na odstępy w JSON) i po spadku usage (`/compact`, `/clear`) zaczyna nowy cykl ostrzeżeń; komunikat nie nazywa już pierwszej odpowiedzi "stałym narzutem"; filtr testów (opt-in) zachowuje kod wyjścia, pełny log w pliku i 3 ostatnie linie.
- `hq/evals/`: 6 przypadków dla `claude plugin eval` (trywialne bez orkiestratora, routing wielodomenowy, bramka zgody, injection w danych, elektronika bez API, render polskich znaków). Nie uruchomione: zużywa limit; najpierw `--no-publish`.
- Liczby i rankingi z Perplexity (koszt tokenów, kategorie ocen) to `[ZAŁOŻENIE]`; do własnego pomiaru na 4 zadaniach (slajd, social, wykres, ekran).

## 1.11.0 · 2026-10-30
- Ochrona przed AI slop: `ux-ui/references/anti-slop.md` (przepływ: specyfikacja .md -> referencja estetyczna -> system designu z referencji -> układ -> prawdziwe obrazy -> wykończenie w kodzie; ten sam system dla www/druku/social; lista wykrywania generyczności). Podpięte w `hq:ux-ui`, `ui-designer` i liście kontrolnej recenzenta.
- Logo (`brand/references/logo.md`): głos marki przed rysowaniem (5+5 słów, zdanie-tweet), luka unikalności (20 logo na planszy), start od kontekstu zamiast pustej planszy, forma ostra/organiczna i asymetria, prostota z duszą, test 1 sekundy, wariant eksperymentalny w prezentacji, font zmienny, powtarzalny test skalowania, README w pakiecie, AI jako szkicownik. Pominięte: triki Illustratora (projektujemy w Figmie).
- Kolor i typografia: `brand/references/color.md` (5 warstw koloru funkcjonalna/emocjonalna/kulturalna/konkurencyjna/strategiczna, brak stałych znaczeń, role palety, neutralne jako skala) i `typography.md` (rodziny jako ton głosu, waga, interlinia, tracking/kerning, linie odniesienia, rem/em, siatka 12 kol., kontrast AA 4,5:1 vs AAA 7:1 - skorygowane z filmu).
- Projektowanie i grafika, wiedza z materiałów wideo: `ux-ui/references/premium-craft.md` (teatr designu, status/cofnięcie/wyjście z błędu, spójność w skali, testy długiej sesji i celowego psucia, paradoks naprawy usługi, projektowanie emocjonalne), `direction-and-patterns.md` (4 poziomy pracy z AI, rubryka 15 pkt Wizja/Spójność/Wykonanie, wzorce list i filtrów wg dojrzałości, research wzorców/Mobbin), `onboarding-paywall.md` (onboarding domyślnie najkrótszy i kiedy wydłużać, 6 wzorców paywalla). Liczby z filmów oznaczone jako wtórne `[ZAŁOŻENIE]`. Podpięte w `hq:ux-ui` (zasada 8, definicja gotowości), `ui-designer`, `ux-designer` i liście kontrolnej `design-reviewer` (UX/UI).

## 1.10.1 · 2026-10-27
- Hook rozmiaru mierzy rzeczywiste tokeny z `usage` ostatniej odpowiedzi (jak `/context`), nie bajty transkryptu (te zawyżały wynik ~2x i rosły mimo `/compact`). Progi liczone od przyrostu względem pierwszej odpowiedzi, bo stały narzut narzędzi/MCP (~90k) nie jest winą rozmowy: compact od +60k, nowy czat od +110k, kolejne ostrzeżenie co +50k. Brak odpowiedzi = brak ostrzeżenia. Zmienne: `HQ_CTX_COMPACT`, `HQ_CTX_TOKENS`, `HQ_CTX_STEP` (teraz w tokenach; `HQ_CTX_BYTES` usunięta). Komunikat podaje stały narzut i przyrost.

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
