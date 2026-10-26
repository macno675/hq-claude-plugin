# Listy kontrolne przeglądu (dla `design-reviewer`)

Czytaj TYLKO sekcję domeny bieżącej bramki. Ścieżki `skills/...` są względem katalogu pluginu (trzy poziomy nad tym plikiem). Każda sekcja: co przeczytać -> co sprawdzić.

## Elektronika (G1-G4 skilla `hq:electronics`)
Czytaj: `.hq/product/` (jeśli jest: `requirements.md`, `architecture.md`, `interfaces.md`, `risks.md`, `changes.tsv`), `.hq/electronics/` (`plan.md`, `bom.tsv`, `decisions.md`, `risks.md`, `gates.md`), `skills/electronics/references/engineering-process.md` oraz dla schematu `schematic-checks.md`, dla PCB `pcb-rules.md`, dla części `component-selection.md`. Artefakty EDA tylko narzędziami odczytu.
Sprawdź: zgodność z wymaganiami i kryteriami gotowości, spójność architektury (interfejsy, napięcia, bilans mocy), ryzyka bez działania, decyzje bez uzasadnienia, części vs datasheet i budżet, testowalność, wykonalność produkcyjna (DFM/DFA), luki.

## Marka (B3/B6 `hq:brand`)
Czytaj: brandbook (i rodzica z sekcją 0, gdy projekt należy do organizacji), profil `.hq/brand/brand.md`, `skills/brand/references/visual-and-voice.md`. Uruchom `skills/brand/scripts/brandscan.py` na kodzie/zasobach, jeśli są. Sprawdź: zgodność z trybem (rdzeń nienaruszony; `odrębna-zgodna` spełnia zasady zgodności; profil zawiera tylko różnice), wynik skanu (OBCY/DRYF), kompletność względem szablonu (wartości zamiast opisów, przykłady poprawne i błędne), spójność ze strategią, kontrasty (`contrast.py`), przetestowanie logo, liczba fontów i licencje, zastosowania w realnych kanałach, DO WERYFIKACJI tam, gdzie brak danych (znak towarowy, Pantone/CMYK), wersja i właściciel.

## UX/UI (U3, U4, U7 `hq:ux-ui`)
Czytaj: `.hq/ux-ui/`, `skills/ux-ui/references/`. Sprawdź: wnioski z tagiem DOWÓD/ZAŁOŻENIE, problem z miarą sukcesu, ścieżki z błędami, komplet stanów komponentów i ekranów, tokeny zgodne z brandbookiem, kontrasty i cele dotykowe, czytelna hierarchia, handoff z intencjami i kryteriami akceptacji.

## ADR (`hq:tech-strategy`)
Czytaj: `.hq/tech/adr/`. Sprawdź: decyzja dla elementu, nie całości; rozważono kup/zbuduj/hybrydę/partnera; własne rozwiązanie z pomiarami przewagi; TCO z założeniami i horyzontem; ryzyka, plan wyjścia, uzależnienie od dostawcy; DOWÓD/ZAŁOŻENIE i aktualne źródła cen.

## Backend (BE2, BE4, BE6 `hq:backend`)
Czytaj: `.hq/backend/`, `skills/backend/references/backend-checklists.md`. Sprawdź: wymagania niefunkcjonalne z liczbami, obsługa awarii każdej zależności, granice warstw, model danych i odwracalność migracji, spójność API (błędy, wersjonowanie, zgodność wstecz, authz na zasobie), timeouty/idempotencja/limity, sekrety i logi, testy uruchomione, rollback, obserwowalność i runbook, uzasadnienie złożoności.

## Frontend (FE2, FE5, FE7 `hq:frontend`)
Czytaj: `.hq/frontend/`, `skills/frontend/references/frontend-checklists.md`. Sprawdź: handoff przejrzany przed kodem, komplet stanów, tokeny zamiast wartości na sztywno, właściciele stanu, zgodność z kontraktem API i obsługa błędów, dostępność (klawiatura, fokus, kontrast, etykiety), pomiary wydajności i budżet pakietów, testy krytycznych ścieżek uruchomione, odwracalność wdrożenia i monitoring, uzasadnienie zależności.

## Budżet (BM4 i duże zmiany `hq:budget`)
Czytaj: `.hq/budget/`, `skills/budget/references/budget-framework.md`. Sprawdź: powiązanie z zakresem i kamieniami, założenia i źródła z datą, scenariusze i wrażliwość, rezerwa z zasadami, brak podwójnego liczenia, arytmetyka z `budget.py`, przyczyny odchyleń, źródło środków dla zmian, jasne decyzje dla użytkownika.

## Plan projektu (PM1, PM2, PM4 `hq:pm`)
Czytaj: `.hq/pm/`, `skills/pm/references/pm-framework.md`; uruchom `schedule.py`. Sprawdź: brak błędów i cykli, zadania z właścicielem i DoD, mierzalne kamienie, zakres z wykluczeniami, szacunki ze źródłem i rezerwą, czas na decyzje użytkownika, ryzyka z właścicielami, zmiany z opcjami i wpływem.

## Wydarzenie (EV1, EV7, EV9 `hq:event`)
Czytaj: `.hq/event/`, `skills/event/references/event-framework.md`; uruchom `runofshow.py`. Sprawdź: cel z miarami, zakres z wykluczeniami, budżet z rezerwą i procedurą dodatkowych kosztów, dostawcy wielokryterialnie z umowami, właściciel każdego obszaru, ryzyka z progami i planami awaryjnymi, bezpieczeństwo i wymagania formalne jako DO WERYFIKACJI z osobami, próba generalna.

## Dźwięk i światło (AV3, AV6, AV11 `hq:av-production`)
Czytaj: `.hq/av/`, `skills/av-production/references/`. Sprawdź: cel i wrażenie, analiza przestrzeni, obliczenia z `avcalc.py`, kompletność toru/schematów z zapasowymi torami, separacja zasilania i sygnałów, rigging/elektryka/głośność jako DO WERYFIKACJI z uprawnioną osobą, testy i próby, plan awaryjny, wymagania dostawy audio z aktualnego źródła i zmierzone `loudness.py`, dokumentacja i kopie zapasowe.

## Prawo i bezpieczeństwo (LS1, LS2, LS3 `hq:legal-safety`)
Czytaj: `.hq/legal/`; uruchom `riskscore.py`. Sprawdź: jurysdykcja ustalona, źródła z datą, każdy punkt wiążący jako DO WERYFIKACJI ze wskazanym specjalistą, brak sformułowań udających poradę prawną, ryzyka z właścicielem i środkiem (hierarchia środków), procedury krótkie i przypisane do ról, brak ujawnionych danych osobowych.

## AI (AI3, AI5, AI6 `hq:ai-strategy`)
Czytaj: `.hq/ai/`. Sprawdź: wykazana potrzeba AI i alternatywa bez AI, wybór kup/zbuduj/RAG z ADR i TCO, dane legalne i opisane, architektura z walidacją odpowiedzi, ograniczonymi uprawnieniami narzędzi, logami, limitem kosztów i ścieżką awaryjną, testy (skrajne i nadużycia) uruchomione z zapisanymi wynikami, nadzór człowieka, wyłącznik, wpis w rejestrze.

## Cyberbezpieczeństwo (CS3, CS4, CS7 `hq:cybersecurity`)
Czytaj: `.hq/security/`, `skills/cybersecurity/references/security-framework.md`. Sprawdź: zasoby i dane sklasyfikowane, model zagrożeń dla głównych przepływów, MFA i najmniejsze uprawnienia, brak sekretów w repo i dokumentach, szyfrowanie, proces aktualizacji i skanów, monitoring z właścicielem, kopie zapasowe testowane odtworzeniem, plan incydentu z rolami, testy tylko za zgodą i w zakresie, priorytety według ryzyka, brak działań zmieniających środowisko bez zatwierdzenia.

## Zespół (TL1, TL2, TL3, TL4 `hq:team-lead`)
Czytaj: `.hq/team/charter.md`, `roles.tsv` (bez notatek 1:1). Sprawdź: cel i kryteria sukcesu, role i zastępcy, ścieżka eskalacji, delegowanie z kontekstem i granicami, kryteria rekrutacji oparte na zachowaniach (bez cech chronionych), decyzje o ludziach zostawione człowiekowi, prywatność danych o ludziach.

## Partnerstwa (P4, P5, P7 `hq:partnerships`)
Czytaj: `.hq/partners/`; uruchom `pipeline.py`. Sprawdź: kwalifikacja (potrzeba, budżet, decydent, czas, dopasowanie), oferta indywidualna z mierzalnymi rezultatami i prawdziwymi dowodami (brak zmyślonych danych), uczciwe ryzyka i ograniczenia, realność względem możliwości realizacji, granice negocjacyjne zatwierdzone, zgodność kontaktu z przepisami (DO WERYFIKACJI), brak niewysłanych-bez-zgody komunikatów, następny krok w każdej otwartej szansie.

## Marketing (MK1, MK3, MK5 `hq:marketing`)
Czytaj: `.hq/marketing/`, `brandbook.md`. Sprawdź: cel i KPI przed startem, odbiorca z oznaczonymi założeniami, przekaz prosty, prawdziwy i spójny z marką, kanały uzasadnione, plan testów z góry, obliczenia z `mkcalc.py`, budżet z limitem i progiem zatrzymania, plan reagowania, zgodność z prawem (DO WERYFIKACJI), brak fałszywych dowodów, ustalone kto publikuje i płaci.

## Research (R1, R7 `hq:research`)
Czytaj: `.hq/research/`. Sprawdź: pytanie i decyzja jasne, każde twierdzenie z id źródła, które faktycznie otwarto (brak zmyślonych źródeł, cytatów, adresów), oceny źródeł i daty, triangulacja ważnych faktów (niezależność źródeł), rozdzielenie fakt/opinia/hipoteza, sprzeczności i luki jawne, poziom pewności przy wnioskach, rekomendacja dla odbiorcy, kryterium stopu użyte, odtwarzalność rozumowania.

## Analityka (DA1, DA6, DA8 `hq:data-analysis`)
Czytaj: `.hq/analytics/`. Sprawdź: pytanie powiązane z decyzją, definicje metryk zapisane, jakość danych opisana, kod i wyniki zapisane (powtarzalne), segmenty i hipotezy przeciwne rozważone, brak wybiórczego raportowania, A/B zaplanowany z góry (próba z `samplesize`, kryteria zakończenia), poziom pewności i ograniczenia, rekomendacja z kosztem, ryzykiem, pomiarem i terminem, prywatność danych.

## Infrastruktura IT (IT2, IT3, IT9 `hq:it-infrastructure`)
Czytaj: `.hq/it/`; uruchom `itcalc.py inventory`. Sprawdź: potrzeby przed doborem, standardy per rola, TCO z założeniami i źródłami cen z datą, dostawca oceniony wielokryterialnie, ewidencja kompletna z datami, plan wymian przed końcem wsparcia, backup z testem odtworzenia, konfiguracja bezpieczeństwa przed użyciem, procedura wycofania z bezpiecznym usunięciem danych, segmentacja i dokumentacja sieci, brak zakupów i działań destrukcyjnych bez zatwierdzenia.

## Zarządzanie produktem (PD3, PD4, PD6 `hq:product-management`)
Czytaj: `.hq/product/` (`vision.md`, `strategy.md`, `roadmap.md`, `backlog.tsv`, `requirements.md`); uruchom `prioritize.py`. Sprawdź: problem z dowodami i miarą sukcesu, wizja prosta i spójna z firmą, strategia z "czego nie robimy", roadmapa jako kierunek z poziomem pewności (nie obietnice), RICE policzone skryptem i flagi niskiej pewności obsłużone, wymagania z zakresem w/poza i przypadkami brzegowymi, hipotezy z progami, plan pomiaru po wdrożeniu.

## Zarząd (CE2, CE3, CE6 `hq:executive`)
Czytaj: `.hq/exec/`; uruchom `runway.py` na danych użytkownika. Sprawdź: decyzja ma min. 3 opcje (w tym "nie rób"), fakty z źródłami i założenia oznaczone, wpływ na gotówkę/runway policzony skryptem, odwracalność i ryzyka, rekomendacja z właścicielem decyzji i terminem, wpis w rejestrze z przeglądem, materiały dla inwestorów tylko z prawdziwych danych (brak zawyżeń), brak porad inwestycyjnych/prawnych/podatkowych (DO WERYFIKACJI), brak niewysłanych-bez-zgody komunikatów.

## Operacje (OP2, OP3, OP8 `hq:operations`)
Czytaj: `.hq/ops/`. Sprawdź: diagnoza oparta na rzeczywistym przepływie i danych, procesy z właścicielem, kryteriami ukończenia i jakości, eskalacją i miernikiem, usunięte zbędne kroki, test skalowalności, narzędzia uzasadnione procesem, dostawcy oceniani wielokryterialnie z planem B dla krytycznych, KPI z definicjami, brak zmian systemów/zamówień bez zatwierdzenia.

## Finanse firmy (FN2, FN4, FN6 `hq:finance`)
Czytaj: `.hq/finance/`; uruchom `cashflow.py`. Sprawdź: dane źródłowe od użytkownika opisane, prognoza w 3 scenariuszach liczona skryptem z jawnymi założeniami o pewności wpływów, próg gotówki i działania po jego przekroczeniu, budżet z rezerwą, kontrole wewnętrzne (rozdzielenie obowiązków, limity, podwójne zatwierdzanie dużych płatności), ryzyka z właścicielami, punkty księgowe/podatkowe/prawne jako DO WERYFIKACJI, brak dostępu do kont i płatności, brak zmyślonych lub "poprawionych" liczb.

## Customer Success (CS2, CS7, CS8 `hq:customer-success`)
Czytaj: `.hq/cs/`; uruchom `health.py`. Sprawdź: cel i miara sukcesu klienta zapisane, plan wdrożenia z pierwszą wartością i datą, przekazanie ze sprzedaży kompletne, sygnały ryzyka obsłużone, wagi health score potraktowane jako heurystyka, odnowienie przygotowane z wyprzedzeniem 90/60/30, brak presji i utrudniania rezygnacji, brak fabrykowanych wyników, brak wysłanych-bez-zgody komunikatów, dane klientów minimalne.
