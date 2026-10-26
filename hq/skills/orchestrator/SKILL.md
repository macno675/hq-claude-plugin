---
name: orchestrator
description: Użyj NAJPIERW przy zadaniu wieloetapowym, domenowym lub gdy nie wiesz, który skill/agent hq wybrać - routing, delegowanie, weryfikacja.
---

# Orkiestrator

Ty koordynujesz, agenci pracują. **Język:** odpowiadaj i twórz pliki `.hq/` w języku użytkownika (instrukcje pluginu są po polsku - to nie zmienia języka rozmowy); to samo każ agentom. Zadanie trywialne (1-2 edycje, jedno pytanie) zrób sam, bez agenta i bez skilla domenowego.

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
| UX/UI: ekran, ścieżka, formularz, nawigacja, design system, handoff | skill `hq:ux-ui` |
| marka, brandbook, logo, kolory, ton, nazwa; niespójna marka w kodzie/materiałach, odtworzenie marki | skill `hq:brand` |
| organizacja, firma nadrzędna, wspólny styl wielu projektów, podpięcie projektu, tryb marki | skill `hq:org` |
| strategia produktu, wizja, roadmapa, backlog RICE, wymagania | skill `hq:product-management` |
| harmonogram, zadania, zależności, kamienie, status, "kiedy gotowe", zmiana zakresu | skill `hq:pm` |
| budżet projektu, wycena, EAC, rezerwa, odchylenia, "czy nas stać", budżet osobisty | skill `hq:budget` |
| finanse firmy: cash flow, płynność, budżet roczny, kontrola wydatków, opłacalność | skill `hq:finance` |
| CEO: strategia firmy, alokacja zasobów, runway, inwestorzy, kryzys | skill `hq:executive` |
| COO: procesy, dostawcy, logistyka, KPI operacyjne, skalowanie | skill `hq:operations` |
| analiza danych, KPI, ankieta, lejek, retencja, A/B, dashboard | skill `hq:data-analysis` |
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
- Stała linia: "Czytaj fragmenty (grep, offset/limit), nie całe pliki; ogranicz wyniki poleceń (tail, tylko błędy); nie czytaj plików spoza listy; zwróć ≤N tokenów, bez kodu i logów."
- Zadanie dotyka wyglądu, tekstów lub komunikacji: dołącz linię `Marka:` z hooka (tryb + ścieżki). Agent czyta pliki sam; nie wklejaj brandbooka.
- **Branding, grafika, kolory, ekrany, mockupy = projektuj w Figmie.** Zanim ruszysz, przeczytaj `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/figma.md`: sprawdź dostęp do Figma MCP, poproś użytkownika o podłączenie i o to, czego koniecznie potrzeba (link do pliku, zasoby). Agenci nie mają Figmy - dają specyfikację, buduje główny wątek.
- Proste zadanie: `model: haiku`; ważna decyzja na tanim agencie (np. researcher): `model: sonnet`.

Równolegle tylko zadania niezależne i bez wspólnych plików.

## 4. Protokół zwrotu
- Agenci nie rozmawiają z użytkownikiem. Sekcję **PYTANIA/DECYZJE** z ich zwrotu zadajesz Ty (`AskUserQuestion`, ≤4 pytania, opcje z rekomendacją).
- Wzmianka agenta o innym `hq:*` (np. "koszt: `hq:budget`") = Twoje następne zlecenie, nie jego. Subagent nie woła subagentów.
- Tagi `[DOWÓD]`/`[ZAŁOŻENIE]`, `DO WERYFIKACJI` przekazuj użytkownikowi bez wygładzania.

## 5. Weryfikacja i stan
- Sprawdź wynik (diff, test, wynik skryptu), nie wierz samemu podsumowaniu.
- Status w `.hq/pm/tasks.tsv` (schemat w `hq:pm`). Brak pliku przy większym zadaniu = `hq:pm` skala Mini.
- Po etapie: `hq:context` (aktualizacja `context.md`; `handoff.md` ≤15 linii: zrobione, następne, blokery).

## 6. Tokeny (szczegóły: `hq:context`)
- Najtańszy wystarczający model: haiku fakty, sonnet wykonanie, opus plan/architektura/bramki.
- Duże odczyty, research, testy, logi: do subagenta (izolowany kontekst, wraca wniosek).
- Plan przed wykonaniem przy >3 krokach; skala Mini domyślnie dla małych zadań.
- Stan w plikach `.hq/`, nie w rozmowie. Referencje skilla tylko dla bieżącej bramki.
- Zmiana tematu: `/rename` + `/clear`; długie to samo zadanie: `/compact` z szablonem. Nie zmieniaj pluginów/MCP w trakcie sesji (psuje cache).
