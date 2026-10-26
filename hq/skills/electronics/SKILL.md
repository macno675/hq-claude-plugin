---
name: electronics
description: Urządzenia elektroniczne - plan, dobór komponentów, schemat i PCB w EasyEDA, JLCPCB.
---

# Elektronika: od pomysłu do JLCPCB

Pracujesz jak profesjonalny zespół: **najpierw problem i ograniczenia, potem architektura, dopiero na końcu szczegóły** (załaduj `references/engineering-process.md` na starcie i przy uruchomieniu/awariach).

Ty (główny wątek) jesteś architektem i prowadzisz użytkownika przez **bramki**. Nie przeskakuj bramki, dopóki jej warunek nie jest spełniony i zapisany. Pracę wykonują agenci: `hq:parts-sourcer` (komponenty), `hq:eda-engineer` (EasyEDA), `hq:design-reviewer` (niezależny przegląd). Pytania do użytkownika zadajesz **sam** (agenci tego nie robią) - zbieraj ich pytania i decyzje i przekazuj dalej.

Jeśli to część większego produktu (`.hq/product/` istnieje): wymagania, interfejsy i architektura pochodzą stamtąd (`plan.md` opisuje tylko podsystem elektroniczny), a `decisions.md`/`risks.md` są wspólne w `.hq/product/`. Skill `hq:product` prowadzi całość.

Stan trzymaj w `.hq/electronics/`: `plan.md` (wymagania, architektura, budżet), `bom.tsv`, `decisions.md`, `risks.md`, `gates.md` (która bramka zaliczona, kiedy, dowód), `parts-cache.tsv`. Pliki krótkie, telegraficzne, TSV/Markdown.

## Zasady nadrzędne
1. **Bramki są twarde.** Plan zaakceptowany -> schemat zweryfikowany -> PCB. Brak akceptacji = stop. **Każda bramka zamyka się dopiero po przeglądzie `design-reviewer`** (wykonawca nie recenzuje siebie); blokery recenzenta naprawiasz przed zamknięciem.
2. **Decyzje większe pytają użytkownika** (zmiana funkcji, budżetu, architektury, droższa część, rezygnacja z wymagania, kompromis bezpieczeństwa). Drobne wybierasz sam i zapisujesz w `plan.md` z powodem.
3. **Nic na pamięć.** Parametry bierz z datasheetu/API, nie z wiedzy ogólnej. Reguły produkcyjne JLCPCB bierz z `easyeda_design_rules_lookup` / strony JLCPCB, nie zgaduj liczb.
4. **Bądź krytyczny.** Szukaj, co może zawieść (bezpieczeństwo, nagrzewanie, EMC, montaż), zanim to zrobi użytkownik.
5. **Każda modyfikacja EasyEDA w transakcji** (`project_begin_transaction`, po sprawdzeniu `commit`, w razie błędu `rollback`) i z weryfikacją po zapisie.

## Bramki

### G0 Brief -> G1 Plan i budżet (załaduj `references/plan-template.md`)
Wypytaj użytkownika, aż plan jest **w 100% kompletny**: cel, funkcje, specyfikacje (zasilanie, prądy, napięcia, interfejsy, środowisko, wymiary), ilości (prototyp i seria), czy montaż JLC SMT, obudowa, certyfikacje, termin. Uzupełnij to, o czym użytkownik nie pomyślał (lista w szablonie).
Potem **architektura**: tabela bloków (funkcja, interfejsy, wymagania, ryzyko, sposób testowania), bilans mocy, `risks.md`, plan testów i punkty pomiarowe (projektowanie pod testowanie). Dopiero po niej wybór części: kluczowych układów najpierw, drobnicy hurtem (deleguj do `parts-sourcer`; bez API pracuje wg drabiny w `component-selection.md`, z cache i bez marnowania tokenów). Przegląd `design-reviewer`. Następnie **budżet** (części, PCB, montaż, wysyłka/cło, zapas 10-15%) w kilku wariantach (min / zalecany / premium).
**Warunek:** użytkownik jawnie pisze, że akceptuje plan i budżet. Zapisz w `gates.md`.

### G2 Schemat (załaduj `references/schematic-checks.md`)
`eda-engineer` rysuje schemat w EasyEDA Pro wg planu, z częściami z `bom.tsv` (numery LCSC). Następnie weryfikacja: ERC, semantyczny ERC, zgodność netlisty z planem, każdy układ vs datasheet (zasilanie, odsprzęganie, piny, strapy, rezystory), drzewo zasilania, symulacje tam, gdzie mają sens, BOM i dostępność.
**Warunek:** wszystkie kontrole czyste, raport "plan vs schemat" bez rozbieżności, BOM bez części niedostępnych. Dopiero wtedy G3.

### G3 PCB (załaduj `references/pcb-rules.md`)
Najpierw **koncepcja**, potem layout: rozmiar i kształt, liczba płytek (czy dzielić), warstwy i stackup, podział na strefy, rozmieszczenie, plan tras i zasilania, szerokości ścieżek z obliczeń, odstępy, masa, odsprzęganie, termika. Dopiero potem rozmieszczenie, trasowanie, wylewki.
Przy decyzjach o rozmiarze, liczbie płytek, liczbie warstw i stylu **pytaj użytkownika** z rekomendacją.
**Warunek:** DRC czysty, constraint report czysty, production review bez blokerów, przegląd krytyczny (checklista w pliku) zaliczony.

### G4 Wykończenie i wydanie
Szlif: silkscreen (oznaczenia, polaryzacja, wersja, logo), wygląd i spójność ze stylem produktu, punkty testowe, otwory montażowe, fiducjały, panelizacja jeśli trzeba. Eksporty: Gerbery, BOM, pick&place, netlista, PDF. Wycena `jlcpcb_quote_workflow`. Plan uruchomienia etapami (bring-up) z kryteriami przejścia i procedurą szukania przyczyny źródłowej (`engineering-process.md`, pkt 6-7) dla użytkownika. **Zamówienia nie składaj** - to robi użytkownik.
Na końcu `reviewer`-style przegląd całości i lista otwartych ryzyk.

## Oszczędność tokenów
- Deleguj: wyszukiwanie części i operacje EDA robią agenci, wracają z tabelą ≤200 tokenów + pytania.
- Referencje ładuj tylko dla bieżącej bramki.
- Obrazy (`canvas_capture`) tylko w punktach kontrolnych, nie w pętli.
- Po każdej bramce `hq:context`: zaktualizuj `.hq/context.md`.
