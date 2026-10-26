# PCB: projekt, reguły, kontrola

Liczby produkcyjne (min. szerokość/odstęp, via, otwory, annular ring, miedź, stackup) **pobierz** z `easyeda_design_rules_lookup`, `easyeda_board_stackup` i strony możliwości JLCPCB dla wybranej usługi. Nie wpisuj ich z pamięci. Przed projektem zapisz je w `plan.md` jako "reguły produkcyjne".

## 1. Koncepcja (zanim cokolwiek położysz)
- **Rozmiar i kształt:** z gabarytów, złączy, otworów montażowych, obudowy; zostaw margines krawędziowy i miejsce na chłodzenie. Zaproponuj użytkownikowi 1-2 warianty.
- **Jedna płytka czy więcej:** dziel, gdy: strefy o różnych wymaganiach (analog/cyfra/moc/RF), element musi być w innym miejscu mechanicznie, wysokie napięcia, moduł wymienny, gabaryt przekracza sensowny koszt. Opisz wady (złącza, koszt).
- **Warstwy i stackup:** 2 vs 4 (z ciągłą masą) - uzasadnij EMC, gęstością, impedancją, ceną. Impedancje kontrolowane (USB, RF) -> stackup JLC z kalkulatorem.
- **Strefy i przepływ sygnału:** moc / analog / cyfra / RF / złącza; krytyczne sygnały najkrótsze. Plan zasilania i powrotów prądu (masa).
- Narysuj plan floorplan (`pcb_floorplan`) i pokaż użytkownikowi, zanim przejdziesz do układania.

## 2. Rozmieszczenie
- Najpierw elementy sztywne (złącza, otwory, przyciski, LED, wyświetlacz), potem układy kluczowe, potem pasywa.
- Kondensatory odsprzęgające **jak najbliżej pinów zasilania**, krótka pętla do masy; kwarc blisko MCU; regulatory i cewki zgodnie z notą aplikacyjną; elementy grzejące z dala od wrażliwych (termistory, kwarc, czujniki).
- Dostęp do punktów testowych, złącza programowania; spójna orientacja elementów (montaż).
- Odstępy: zgodnie z regułami JLC + zapas dla lutowania, kontroli, ręcznej przeróbki; wysokie elementy nie blokują innych. Strona montażu: jednostronny SMT jest tańszy; dwustronny tylko gdy konieczny.

## 3. Trasowanie
- Kolejność: zasilanie i masa -> sygnały krytyczne (zegary, szybkie, różnicowe, analogowe) -> reszta. `pcb_route_path_plan` przed `add_track`; `pcb_autoroute` tylko jako pomoc i zawsze do przeglądu.
- **Szerokość ścieżek z obliczeń** (IPC-2221, orientacyjnie): `I = k · ΔT^0,44 · A^0,725`, A w mil², k = 0,048 (warstwa zewnętrzna) / 0,024 (wewnętrzna). Dobierz ΔT (np. 10 °C) i miedź (oz). Przy dużych prądach, wysokich napięciach (odstępy/creepage) i krytycznych torach licz osobno, z zapasem. Prądy via - kilka via równolegle.
- Napięcia: odstępy skalowane napięciem (creepage/clearance wg normy dla zastosowania; dla sieci zewnętrzny specjalista).
- Pary różnicowe: stała szerokość/odstęp, równa długość, bez via jeśli się da. Szybkie sygnały: ciągła płaszczyzna odniesienia pod spodem, brak przecięć szczelin.
- Zakręty 45° lub łukowe, brak ostrych kątów, brak stubów, brak śladów w pobliżu krawędzi płytki ponad regułę.
- Masa: ciągła, jak najmniej przerw; analog/cyfra rozdzielone logicznie, łączone w jednym punkcie tam, gdzie potrzeba; stitching via; wylewki (`add_zone`, `zone_preflight`, `pcb_fills`) z termo-reliefami przy padach.
- Termika: miedź/via termiczne pod układami mocy, padom EP; sprawdź dopuszczalną temperaturę.

## 4. Przegląd krytyczny (każdy punkt: OK / problem + poprawka)
Zasilanie: spadki napięcia, pętle prądu, odsprzęganie · Sygnały: długości, odległości, crosstalk · Masa: ciągłość, powroty · Termika · Mechanika: otwory, złącza w osi z obudową, wysokości · Produkcja (DFM): minima JLC, annular ring, odstęp od krawędzi, maska/mostki, paste na padach · Montaż (DFA): orientacje, polaryzacja, fiducjały, odstępy dla pick&place, pady dla lutowania · Testowalność · Serwis · Bezpieczeństwo (odstępy wysokiego napięcia).

## 5. Kontrole narzędziowe (wszystkie czyste)
`easyeda_drc_run` · `pcb_constraint_check` + `pcb_constraint_report` · `pcb_production_review` · `easyeda_rule_check_summary` · `post_write_qa` · po zmianach schematu: `schematic_sync_to_pcb` i ponowny ERC. Netlista PCB = netlista schematu.

## 6. Wykończenie (G4)
- **Silkscreen:** referencje czytelne (nie pod elementami), polaryzacja/pin 1, opisy złącz, nazwa, wersja i data, logo/styl produktu; nic na padach.
- **Estetyka (styl z `brandbook.md`, jeśli istnieje - kolor maski, logo, krój i ton opisów na silkscreenie):** równe rzędy, spójne odstępy, wyrównanie, symetria tam gdzie pasuje, zaokrąglone rogi, kolor maski i opis zgodne ze stylem produktu - przedstaw użytkownikowi 1-2 propozycje.
- Otwory montażowe, fiducjały (dla SMT), znaczniki orientacji, punkty testowe opisane, panelizacja/V-cut jeśli potrzeba.
- Zrzuty widoku (`canvas_capture`, 3D jeśli dostępne) do akceptacji użytkownika.

## 7. Eksport i wycena
`export_gerbers`, `bom_export`, `export_pick_place`, `export_netlist`, `export_pdf`, `production_qa_artifacts`; `jlcpcb_quote_workflow` (porównaj z budżetem). Sprawdź pliki (liczba warstw, wymiary, wiercenia, orientacja pick&place względem rzeczywistych pozycji, polaryzacja w BOM/CPL - częsta wada JLC).
Plan uruchomienia (bring-up) dla użytkownika: kolejność włączania (bez układów, pomiary zasilania), pierwsze testy funkcji, kryteria zaliczenia, typowe awarie.
