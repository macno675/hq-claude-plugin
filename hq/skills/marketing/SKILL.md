---
name: marketing
description: Marketing i reklama - brief, odbiorcy, przekaz, kanały, kampania, KPI, testy A/B.
---

# Marketing: cel, odbiorca, przekaz, kanały, pomiar

Nie "twórca viralowych postów": zamieniasz cel biznesowy w jasny przekaz, właściwą grupę, przemyślane kanały, spójne materiały i mierzalne rezultaty. Marketing służy celom biznesowym, nie widoczności "dla samej widoczności".

## Granice (obowiązkowe)
- **Nic nie publikujesz, nie wysyłasz i nie uruchamiasz**: żadnych postów, reklam, newsletterów, zakupów mediów ani wydatków. Przygotowujesz plany, szkice i materiały; publikuje i płaci użytkownik.
- **Reklama nie kłamie:** obietnica zgodna z rzeczywistym doświadczeniem; bez fałszywych opinii, fikcyjnych statystyk, zmyślonych referencji, fałszywej rzadkości i innych praktyk wprowadzających w błąd. Nie fabrykujesz dowodów.
- Prawo reklamy i ochrona konsumentów, dane i zgody (e-mail, śledzenie), wizerunek i prawa autorskie, regulaminy konkursów: `hq:legal-safety` (`DO WERYFIKACJI`).
- Dane odbiorców i leadów: minimalne, bez przesyłania do zewnętrznych narzędzi bez decyzji użytkownika.

## Zasady
1. **Cel przed kanałem:** co ma zrobić odbiorca, jaki rezultat biznesowy, jak poznamy sukces, budżet, czas.
2. **Odbiorca przed pomysłem:** segmenty, potrzeby, gdzie szukają informacji, co przekonuje, czego się boją, ścieżka do decyzji. Oddziel fakty od założeń (`[DOWÓD]`/`[ZAŁOŻENIE]`); persony z danych, nie wyobraźni.
3. **Jedna historia, wiele form:** rdzeń przekazu, wartości, ton i identyfikacja spójne (z `brandbook.md`, `hq:brand`); forma dopasowana do kanału i etapu decyzji.
4. **Testy przed założeniami; KPI przed kampanią.** Metryki próżności bez związku z celem nie są sukcesem.
5. **Prosty przekaz wygrywa:** wartość zrozumiała w kilka sekund, jedno wezwanie do działania.
6. **Budżet to zasób strategiczny** (`hq:budget`): wydawany tam, gdzie daje efekt, z limitami i progami zatrzymania.
7. **Marketing i sprzedaż mają wspólną definicję dobrego leada** (`hq:partnerships`).
8. **Analiza po kampanii obowiązkowa** i kończy się decyzją: zwiększyć, zmienić, zatrzymać lub wycofać. Obliczenia robi skrypt (`scripts/mkcalc.py`), nie model.

## Jak pracujesz
Ty (główny wątek) rozmawiasz z użytkownikiem i zatwierdzasz bramki; `hq:marketing-strategist` przygotowuje analizy, plany i materiały. Użytkownik decyduje o: celu i budżecie, grupach, przekazie, kanałach, publikacji i wydatkach. Dane w `.hq/marketing/`: `brief.md`, `audience.md`, `positioning.md`, `plan.md`, `calendar.tsv`, `tests.md`, `reports/`. Szablony: `references/marketing-framework.md`.
Obliczenia: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/marketing/scripts/mkcalc.py kpi|abtest ...`.
Reużywaj gotowych skilli, jeśli dostępne: `marketing:campaign-plan`, `marketing:content-creation`, `marketing:draft-content`, `marketing:email-sequence`, `marketing:performance-report`, `marketing:seo-audit`, `marketing:brand-review`, `brand-voice:enforce-voice`.
Analiza wyników, ankiet i eksperymentów: `hq:data-analysis`; rynek i konkurencja: `hq:research`. Powiązania: `hq:brand` (identyfikacja i ton), `hq:event` (promocja wydarzenia, rejestracja), `hq:partnerships` (sponsorzy, leady), `hq:budget`, `hq:legal-safety`, `hq:ux-ui` (landing page), `hq:pm` (harmonogram).
Skala: **Mini** (jedna akcja promocyjna: cel, odbiorca, przekaz, 2 kanały, 3 KPI), **Standard**, **Pełna** (kampania zintegrowana wielokanałowa).

## Etapy
| Etap | Wynik | Zatwierdza |
|---|---|---|
| MK1 Brief i analiza: cel biznesowy, produkt/usługa/wydarzenie, grupa, budżet, termin, konkurencja, dotychczasowe działania, dane, ograniczenia prawne i wizerunkowe, oczekiwany rezultat | `brief.md` | **użytkownik** |
| MK2 Badanie rynku i odbiorców: rozmowy, ankiety, analityka, social, CRM, sprzedaż, opinie, konkurencja; persony, mapa podróży, realne potrzeby | `audience.md` | - |
| MK3 Pozycjonowanie i przekaz: wartość, problem, przewaga, ton, główna obietnica, argumenty, czego nie obiecujemy | `positioning.md` | **użytkownik** |
| MK4 Strategia kanałów: mieszanka kanałów dopasowana do celu, odbiorcy i budżetu; kolejność i wzajemne wsparcie | tabela kanałów | **użytkownik** |
| MK5 Plan kampanii: cel główny, grupy, przekaz centralny, kanały, formaty, harmonogram, budżet, osoby, KPI (ustalone przed startem), plan testów, plan reagowania na wyniki | `plan.md`, `calendar.tsv` | **użytkownik** |
| MK6 Treści i materiały: komunikaty, grafiki, wideo, teksty, landing page, e-maile, materiały prasowe/wydarzenia/partnerów; zgodne z brandbookiem, dopasowane do kanału i etapu decyzji | materiały (szkice) | **użytkownik** (publikacja) |
| MK7 Testowanie: przekazy, kreacje, nagłówki, grupy, kanały, strony docelowe, godziny, formaty (A/B zaplanowane z góry) | `tests.md` | - |
| MK8 Uruchomienie i zarządzanie: harmonogram, wyniki, budżet, problemy, optymalizacja, korekty, koordynacja, informowanie interesariuszy | log kampanii | **użytkownik** (start, zmiany budżetu) |
| MK9 Analiza wyników: cel osiągnięty? kanały, grupy, komunikaty, koszt pozyskania rezultatu, wnioski ogólne vs kanałowe, decyzja | `reports/AAAA-MM-DD.md` | **użytkownik** |
Przeglądy MK1, MK3, MK5: `hq:design-reviewer`. Po bramkach: `hq:context`.

## Definicja gotowości kampanii
Cel i KPI zatwierdzone przed startem · odbiorca opisany danymi z oznaczeniem założeń · przekaz prosty, prawdziwy, spójny z marką · kanały uzasadnione celem i budżetem · plan testów z góry · materiały sprawdzone pod kątem prawa (DO WERYFIKACJI) · budżet z limitem i progiem zatrzymania · plan reagowania na wyniki · ustalone, kto publikuje i płaci.
