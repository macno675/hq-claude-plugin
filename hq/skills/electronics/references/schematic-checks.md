# Schemat: projekt i weryfikacja (EasyEDA Pro przez MCP)

## Przed rysowaniem
- `easyeda_bridge_status` / `easyeda_health_check`: czy most działa i jaki projekt jest otwarty.
- Plan sekcji arkusza: zasilanie, MCU, interfejsy, czujniki, UI. Sygnały między sekcjami przez net labels/porty.
- Części wyłącznie z `bom.tsv` (wyszukaj `easyeda_schematic_search_device` po numerze LCSC; zweryfikuj `easyeda_catalog_verify_device`). Footprint zgodny z pakietem w BOM.

## Rysowanie
- Transakcja (`project_begin_transaction`), zapis partiami (`schematic_batch_write` / workflowy `workflow_*`), po każdej partii `schematic_verify_write`.
- Konwencje: zasilanie w górę, masa w dół, sygnały lewo -> prawo; sygnały i szyny nazwane czytelnie; wartości i referencje widoczne; niewykorzystane piny jawnie (no-connect lub podciągnięte zgodnie z datasheetem).
- Odsprzęganie 100 nF przy każdym pinie zasilania układu, zbiorczy kondensator na szynę, zgodnie z noty aplikacyjnej.
- Ochrona: ESD/TVS na złączach zewnętrznych, odwrotna polaryzacja, bezpiecznik/PTC, filtry; rezystory podciągające I2C, terminacje, strapy MCU, reset, boot.
- Piny programowania/debug i punkty testowe w schemacie.

## Weryfikacja (wszystko musi przejść)
1. `easyeda_erc_run` + `easyeda_semantic_erc_auto` / `_validate`: zero błędów; ostrzeżenia uzasadnione na piśmie.
2. `schematic_validate_netlist` + `schematic_nets`: brak pływających wejść, zwarć, nets jednopinowych, pominiętych zasilań.
3. **Układ po układzie vs datasheet** (tabela): pin, funkcja, podłączenie, zgodność z noty aplikacyjnej, wartości elementów zewnętrznych, limity napięć i prądów. Każdą rozbieżność popraw lub uzasadnij.
4. `power_tree_analyze`: bilans mocy, spadki, prądy szczytowe, sprawność, rezerwa regulatorów, start/kolejność zasilania.
5. Symulacja (`simulate_operating_point` / `_transient`) tam, gdzie są dzielniki, filtry, RC, ograniczanie prądu, soft-start; wynik porównaj z obliczeniami.
6. `bom_generate` + `bom_validate` + `bom_sourcing`: wszystkie części dostępne, ceny w budżecie, brak duplikatów/niezgodności.
7. **Plan vs schemat:** każda funkcja MUST z `plan.md` ma konkretną realizację w schemacie (tabela funkcja -> blok/ układ/ piny). Brak = bramka niezaliczona.
8. `easyeda_schematic_layout_qa` (czytelność). Zrzut `canvas_capture` do przeglądu.

## Raport do bramki G2
Tabela: kontrola -> wynik -> dowód. Plus: otwarte ryzyka, rzeczy do decyzji użytkownika. Dopiero przy czystym raporcie `schematic_sync_to_pcb` i G3.
