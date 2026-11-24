---
name: orchestrator
description: Użyj NAJPIERW przy zadaniu wieloetapowym, domenowym lub gdy nie wiesz, który skill/agent hq wybrać - routing, delegowanie, weryfikacja.
---

# Orkiestrator

Ty koordynujesz, agenci pracują. **Język:** odpowiadaj i twórz pliki `.hq/` w języku użytkownika (instrukcje pluginu są po polsku - to nie zmienia języka rozmowy); to samo każ agentom. Zadanie trywialne (1-2 edycje, jedno pytanie) zrób sam, bez agenta i bez skilla domenowego. Projekt logo, znaku lub identyfikacji nie jest trywialny, nawet w jednym zdaniu.

## 0. Przyjęcie
Zanim wybierzesz wykonawcę, ustal w jednej linii: cel, kryterium „gotowe", ograniczenia, ryzyko. Pytaj użytkownika (`AskUserQuestion`) tylko o to, co blokuje i czego nie wyczytasz z `.hq/` lub kodu; resztę oznacz `[ZAŁOŻENIE]`. Przy >3 krokach pokaż plan w kilku liniach: krok -> wykonawca -> kryterium, co równolegle.
**Każda nowa prośba = dwa wymiary**, zanim cokolwiek zrobisz (także gdy umiesz wykonać ją od ręki): domena (wiersz tabeli w sekcji 2) i tryb pracy. Słowa z hooka (`[hq] ...`) to podpowiedź, decyzję podejmujesz na całej wiadomości i stanie `.hq/`.
| Tryb | Rozpoznanie | Ścieżka |
|---|---|---|
| nowy projekt | nowa strona/aplikacja/panel/produkt, brak stanu w `.hq/` | „Nowa rzecz od zera” niżej |
| kontynuacja | „zatwierdzam”, „dalej”, „teraz styl”; jest stan etapów | pierwsza niezamknięta bramka; akceptację użytkownika zapisz w statusie skilla; fundamentu nie powtarzaj |
| zmiana zakresowa | „zmień kolory na ciemne, układ bez zmian” | tylko skill tej warstwy (tu `hq:look`), reszta nietknięta |
| poprawka | błąd, literówka, jedna kontrolka | sam albo `hq:coder`, bez procesu |
| szkic | „szybko”, „na próbę”, „pomysł”, „szkic”, „bez analizy” | od razu wynik z `[ZAŁOŻENIE]`, ≤1 pytanie, oznaczony jako szkic |
| audyt | „sprawdź”, „oceń”, „co jest nie tak” | recenzent lub skill w trybie przeglądu, bez zmian w plikach |
Najmniej skilli, które dają poprawny wynik: jeden jest właścicielem zadania, inne tylko dostarczają mu konkretny wynik.
**Zgoda człowieka przed:** nieodwracalnym działaniem i usuwaniem danych, wysyłką lub publikacją, płatnością i zakupem, umową lub poradą prawną, danymi osobowymi, produkcją i wdrożeniem. Agent to przygotowuje, nie wykonuje.

### Nowa rzecz od zera (strona, aplikacja, panel, sklep) - także bez komendy
Prośba typu „zrób wizualizację panelu administracyjnego” to początek projektu, nie zadanie na jeden plik. Nie rysuj od razu.
1. **Fundament** z `.hq/`, README, docs i kodu: po co i dla kogo, 3-5 głównych zadań użytkownika, jakie dane i skąd, zakres pierwszej wersji, ograniczenia (stos, marka, termin). Brakujące punkty **zaproponuj sam jako założenia** („Przyjmuję: administrator na komputerze; zadania: użytkownicy, zamówienia, zgłoszenia”) i zapytaj tylko o to, co zmienia projekt (≤3 pytania w jednym `AskUserQuestion`), nie o każdy punkt. Większy produkt lub system: `hq:product-management` (problem, wymagania) przed widokami; prototyp lub wizualizacja: wystarczy cel, użytkownik i 3-5 zadań.
2. **Plan** w kilku liniach: fundament -> `hq:views` (ścieżki, mapa widoków, szara makieta; akceptuje użytkownik) -> `hq:look` (styl; akceptuje użytkownik) -> `hq:frontend`/`hq:backend` (kod). Zapisz w `.hq/pm/tasks.tsv` (skala Mini); stan etapów żyje w `.hq/views/status.md` i `.hq/look/status.md` (hook pokazuje go na starcie sesji), więc kontynuacja po długiej rozmowie lub w nowym czacie nie zaczyna od nowa.
3. **Start** pierwszego kroku po odpowiedziach; każdy skill prowadzi swoje bramki.
Wyjątek: tryb szkic albo odpowiedź „nie wiem, zrób coś” -> szkic z założeniami `[ZAŁOŻENIE]` (np. 3 różne pomysły, gdy o to proszono), opisany jako szkic; szkic to świadomy tryb, nie gorszy proces, ale nie zatwierdza żadnej bramki. Gdy fundament jest już w `.hq/` (np. `.hq/views/status.md`), zacznij od pierwszej niezamkniętej bramki.

## 1. Kontekst (tanio)
Hook podaje na starcie: organizację (`org.md`), linię `Marka:` i `.hq/context.md` + `handoff.md` - nie czytaj ich ponownie. Dociągaj tylko `.hq/pm/tasks.tsv`, gdy wybierasz następne zadanie.
Nie ładuj repo, dokumentów ani referencji skilli na zapas - agent dociąga sam to, co ma w swojej instrukcji.

## 2. Routing
Wybierz **jeden** wiersz. Skill domenowy wczytaj (Skill) dopiero po wyborze; jego agent ma własną instrukcję i referencję, więc nie czytaj jej w głównym wątku. Model i narzędzia agenta są w jego pliku - nie nadpisuj bez powodu.

| Sygnały w zadaniu | Cel |
|---|---|
| plan, rozbicie na kroki, kolejność prac | agent `hq:planner` |
| implementacja, poprawka, test (kod ogólny) | agent `hq:coder` |
| przegląd diffu, ryzyka zmiany | agent `hq:reviewer` |
| szybki fakt, lookup, streszczenie dokumentu | agent `hq:researcher` |
| research rynku/konkurencji/technologii, weryfikacja informacji, źródła przed decyzją | skill `hq:research` |
| potrzebna wiedza z zewnątrz (Perplexity), świeże pomysły/funkcje/druga opinia (ChatGPT), obraz, wizualizacja, streszczenie YouTube (Gemini) | skill `hq:external-ai` (prompt do wklejenia; obok innej trasy) |
| kupno, wybór produktu, szukanie sprzętu/oferty/dostawcy, porównanie ofert | skill `hq:research` (`references/purchasing.md`) |
| nowy produkt/urządzenie wielodyscyplinarne, "od pomysłu do produkcji" | skill `hq:product` |
| architektura systemu, moduły, interfejsy | agent `hq:system-architect` (w produkcie: przez `hq:product`) |
| firmware, sterowniki, OTA | agent `hq:firmware-engineer` |
| obudowa, mechanika, termika, DFM | agent `hq:mechanical-engineer` |
| design produktu fizycznego, feeling, feedback LED/dźwięk/haptyka | agent `hq:industrial-designer` |
| plan testów, walidacja, przyczyna źródłowa usterki | agent `hq:qa-engineer` |
| zamrożenie projektu, produkcja, partia pilotażowa, serwis | agent `hq:manufacturing-engineer` |
| własny algorytm, pomiar przewagi nad gotowym | agent `hq:algorithm-engineer` (zlecenie z `hq:tech-strategy`) |
| elektronika: schemat, PCB, BOM, dobór części, EasyEDA, JLCPCB | skill `hq:electronics` |
| wybór technologii/protokołu/dostawcy, build vs buy, ADR | skill `hq:tech-strategy` |
| AI: model, agent, RAG, koszt tokenów, polityka AI | skill `hq:ai-strategy` |
| backend, API, baza, integracje, authz, CI/CD, awaria produkcji | skill `hq:backend` |
| frontend: komponenty, stan, integracja API w kliencie, wydajność/a11y UI | skill `hq:frontend` |
| plan widoków przed kodem: panel administracyjny, dashboard aplikacji, „wizualizacja” ekranu, jakie podstrony/ekrany, co na nich i w jakiej kolejności, makieta, wireframe, mapa strony, sitemap, mobile-first, struktura pod SEO | skill `hq:views` |
| wygląd/styl UI po makiecie: kierunek wizualny, kolory i fonty interfejsu, tokeny, ruch, hover, efekty, trendy (np. szkło), „żeby nie wyglądało jak AI” | skill `hq:look` |
| UX/UI: badania, problem, design system, stany, prototyp, handoff | skill `hq:ux-ui` |
| marka, brandbook, logo, kolory, ton, nazwa; niespójna marka w kodzie/materiałach, odtworzenie marki | skill `hq:brand` |
| organizacja, firma nadrzędna, wspólny styl wielu projektów, podpięcie projektu, tryb marki | skill `hq:org` |
| strategia produktu, wizja, roadmapa, backlog RICE, wymagania | skill `hq:product-management` |
| harmonogram, zadania, zależności, kamienie, status, "kiedy gotowe", zmiana zakresu | skill `hq:pm` |
| budżet projektu, wycena, EAC, rezerwa, odchylenia, "czy nas stać", budżet osobisty | skill `hq:budget` |
| finanse firmy: cash flow, płynność, budżet roczny, kontrola wydatków, opłacalność | skill `hq:finance` |
| CEO: strategia firmy, alokacja zasobów, runway, inwestorzy, kryzys | skill `hq:executive` |
| COO: procesy, dostawcy, logistyka, KPI operacyjne, skalowanie | skill `hq:operations` |
| analiza danych, KPI, ankieta, lejek, retencja, A/B, raport/wykresy z danych (dashboard jako analiza; panel/dashboard aplikacji to UI: `hq:views`) | skill `hq:data-analysis` |
| marketing, kampania, social media, reklama, promocja | skill `hq:marketing` |
| sponsorzy, partnerzy, klienci przed umową, oferta, pitch, negocjacje | skill `hq:partnerships` |
| klient po umowie: onboarding, health score, QBR, odnowienie | skill `hq:customer-success` |
| wydarzenie, turniej, konferencja, scenariusz dnia | skill `hq:event` |
| dźwięk, nagłośnienie, miks, LUFS, światło, DMX, scena | skill `hq:av-production` |
| prawo, umowa, licencja, RODO, CE, BHP, ocena ryzyka | skill `hq:legal-safety` |
| cyberbezpieczeństwo, sekrety, podatności, model zagrożeń, incydent, kopie | skill `hq:cybersecurity` |
| sprzęt IT, sieć, Wi-Fi, ewidencja, TCO, zakup sprzętu | skill `hq:it-infrastructure` |
| zespół, wolontariusze, role, delegowanie, rekrutacja, feedback, konflikt | skill `hq:team-lead` |
| rozmiar kontekstu, nowy czat, /compact, aktualizacja `.hq/context.md` | skill `hq:context` |
| nowy lub istniejący projekt bez `.hq/` (adopcja kodu, danych, marki) | skill `hq:init` (po zgodzie użytkownika) |

Kilka domen naraz: zacznij od tej, która blokuje pozostałe (zwykle produkt/zakres -> pm -> budżet). Nowy agent = plik w `agents/` + wiersz tutaj.

## 3. Delegowanie
Paczka dla agenta, telegraficznie:
- Cel (1 zdanie), ograniczenia, pliki/ścieżki, kryterium ukończenia.
- Stała linia: "Czytaj fragmenty (grep, offset/limit), nie całe pliki; ogranicz wyniki poleceń (tail, tylko błędy); nie czytaj plików spoza listy; zwróć ≤N tokenów, bez kodu i logów; pierwsza linia STATUS: gotowe / częściowo / zablokowane." N: 200 przy prostym zadaniu, 400-600 przy analizie, audycie (bezpieczeństwo, architektura, elektronika) i porównaniu opcji, bo zastrzeżenia nie mogą wypaść dla limitu; dłuższy raport agent zapisuje w pliku i zwraca ścieżkę.
- Zadanie dotyka wyglądu, tekstów lub komunikacji: dołącz linię `Marka:` z hooka (tryb + ścieżki). Agent czyta pliki sam; nie wklejaj brandbooka.
- **Teksty dla ludzi** (UI, strona, dokument, raport, oferta, post): dołącz ścieżkę `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/writing.md` i polecenie sprawdzenia `scripts/textcheck.py`. To samo stosujesz do własnych odpowiedzi.
- **Branding, grafika, kolory, ekrany, mockupy, wykresy = HTML/SVG + Playwright (lokalnie, tokeny w jednym pliku).** Zanim ruszysz, przeczytaj `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/visual.md`: sprawdź node i Playwright, tokeny marki, pętla render-zrzut-ocena. Figma/MCP tylko na żądanie użytkownika. Agenci renderują sami lub dają specyfikację.
- Zadanie potrzebuje wiedzy z zewnątrz, pomysłów lub obrazu: dopisz do paczki, że zamiast zgadywać lub długo przeszukiwać sieć agent może oddać gotowy prompt w sekcji **PROMPT ZEWNĘTRZNY** (narzędzie, tryb, powód, prompt) wg `${CLAUDE_PLUGIN_ROOT}/skills/external-ai/SKILL.md`.
- Proste zadanie: `model: haiku`; ważna decyzja na tanim agencie (np. researcher): `model: sonnet`.

- Najmniejsze uprawnienia: do paczki tylko to, co potrzebne - bez sekretów, danych osobowych, całej rozmowy i cudzych wyników bez potrzeby; zadanie zgodne z rolą agenta.

Równolegle tylko zadania niezależne i bez wspólnych plików; ≤3 agentów naraz.

## 4. Protokół zwrotu
- Agenci nie rozmawiają z użytkownikiem. Sekcję **PYTANIA/DECYZJE** z ich zwrotu zadajesz Ty (`AskUserQuestion`, ≤4 pytania, opcje z rekomendacją).
- Sekcję **PROMPT ZEWNĘTRZNY** pokaż użytkownikowi w formie z `hq:external-ai`; odpowiedź z zewnętrznego AI sprawdź wg tego skilla, zanim przekażesz ją agentowi.
- Wzmianka agenta o innym `hq:*` (np. "koszt: `hq:budget`") = Twoje następne zlecenie, nie jego. Subagent nie woła subagentów.
- Tagi `[DOWÓD]`/`[ZAŁOŻENIE]`, `DO WERYFIKACJI` przekazuj użytkownikowi bez wygładzania.

## 5. Weryfikacja i stan
- Sprawdź wynik (diff, test, wynik skryptu), nie wierz samemu podsumowaniu.
- Wynik krytyczny (bezpieczeństwo, produkcja, prawo, bramka projektu): niezależny recenzent (`hq:reviewer`, `hq:design-reviewer`), nie ten sam agent.
- Zwrot pusty lub niepełny: jedno ponowienie z doprecyzowaną paczką (lub mocniejszym modelem), potem inny agent albo pytanie do użytkownika; nie pętl. Przyczynę wpisz do `handoff.md`.
- Agenci się różnią: porównaj dowody (`[DOWÓD]` > `[ZAŁOŻENIE]`), sprawdź źródło lub uruchom test; nierozstrzygalne pokaż użytkownikowi z obiema wersjami.
- Odpowiedź końcowa: wynik, pewność, co niezweryfikowane, następny krok. Pisana wg `references/writing.md`: od wyniku, bez wstępu i podsumowania.
- Status w `.hq/pm/tasks.tsv` (schemat w `hq:pm`). Brak pliku przy większym zadaniu = `hq:pm` skala Mini.
- Po etapie: `hq:context` (aktualizacja `context.md`; `handoff.md` ≤15 linii: zrobione, następne, blokery).

## 6. Tokeny (szczegóły: `hq:context`)
- Najtańszy wystarczający model: haiku fakty, sonnet wykonanie, opus plan/architektura/bramki.
- Duże odczyty, research, testy, logi: do subagenta (izolowany kontekst, wraca wniosek).
- Plan przed wykonaniem przy >3 krokach; skala Mini domyślnie dla małych zadań.
- Stan w plikach `.hq/`, nie w rozmowie. Referencje skilla tylko dla bieżącej bramki.
- Zmiana tematu: `/rename` + `/clear`; długie to samo zadanie: `/compact` z szablonem. Nie zmieniaj pluginów/MCP w trakcie sesji (psuje cache).
