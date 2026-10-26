# Proces zespołu profesjonalnego (jak pracujemy)

Zasada stała: **problem i ograniczenia -> architektura -> szczegóły.** Każda decyzja ma właściciela, recenzenta, uzasadnienie i sposób sprawdzenia. Nie zaczynaj od schematu ani doboru części.

## Role = kto to robi u nas
| Rola | Wykonawca | Odpowiada za |
|---|---|---|
| Architekt, inżynier systemowy, właściciel wymagań | główny wątek (skill) + użytkownik | wymagania, bloki, kompromisy, akceptacje |
| Dobór technologii i komponentów, koszt | `hq:parts-sourcer` | BOM, ryzyka dostaw, alternatywy |
| Schemat, zasilanie, PCB, DFM | `hq:eda-engineer` | wykonanie i kontrole narzędziowe |
| Recenzent (SI/PI/EMC, DFM, walidacja) | `hq:design-reviewer` (osobny kontekst, tylko odczyt) | niezależna ocena każdej bramki |
Wykonawca nie recenzuje własnej pracy. Recenzję robi inny agent, zawsze przed zamknięciem bramki.

## 1. Wymagania (jeden dokument: `plan.md`)
Funkcje (MUST/SHOULD/NICE), parametry do spełnienia, warunki pracy, koszt/wymiary/pobór/temperatura, niezawodność, **kryteria gotowości** ("projekt skończony gdy…"). Jedno źródło prawdy. Sprzeczności zgłoś użytkownikowi.

## 2. Architektura przed szczegółami (część G1)
Tabela bloków: `blok | funkcja | wejścia/wyjścia (sygnał, napięcie, interfejs) | wymagania | ryzyko | jak testujemy`. Do tego bilans mocy i lista pytań. Dopiero po przeglądzie i akceptacji: wybór technologii i części.

## 3. Rejestry (krótkie, TSV/Markdown w `.hq/electronics/`)
- `decisions.md`: `data | decyzja | dlaczego | odrzucone alternatywy | kto | jak sprawdzone`
- `risks.md`: `ryzyko | skutek | prawdopodobieństwo | działanie | status`
Wpis po każdej większej decyzji. Cel: nie wracać do rozstrzygniętych tematów i nie tracić wiedzy.

## 4. Przeglądy (każdy przez `hq:design-reviewer`)
Wymagania i architektura (G1) · dobór komponentów (przed G2) · schemat (G2) · PCB (G3) · gotowość do produkcji (G4) · wyniki testów (po uruchomieniu).
Recenzent dostaje: artefakty bramki, `plan.md`, rejestry. Zwraca: werdykt, problemy od najpoważniejszego (`miejsce - problem - ryzyko - poprawka`), czego nie sprawdził. Bramka zamyka się dopiero przy braku blokerów.

## 5. Projektowanie pod testowanie (od G1)
Plan testów powstaje razem z architekturą: dla każdego bloku pomiar i kryterium. W projekcie: punkty pomiarowe na szynach i kluczowych sygnałach, możliwość odłączenia sekcji zasilania (zworki, 0 Ω, rezystory pomiarowe), uruchamianie etapami, złącze programowania/aktualizacji, dostęp do pomiarów bez demontażu.

## 6. Uruchomienie etapami (plan dla użytkownika w G4)
1. Oględziny, mostki lutownicze, kontrola mechaniki. 2. Pomiar rezystancji szyn zasilania względem masy (zwarcia). 3. Zasilanie kontrolowane (zasilacz laboratoryjny, limit prądu), pomiar napięć i prądu spoczynkowego. 4. Zegary, reset, komunikacja, programowanie. 5. Pojedyncze bloki. 6. Współpraca bloków. 7. Pełny test w warunkach rzeczywistych.
Każdy etap: kryterium przejścia (wartość +/- tolerancja) zapisane przed testem.

## 7. Analiza przyczyny źródłowej (gdy coś nie działa)
Co dokładnie nie działa -> kiedy -> w jakich warunkach -> hipotezy -> pomiar, który każdą potwierdzi lub odrzuci -> zmiana w projekcie/dokumentacji/procesie. Poprawka zamknięta dopiero po potwierdzeniu, że usunęła przyczynę, nie objaw. Wpis do `risks.md`/`decisions.md`.

## 8. Dokumentacja jako produkt
Na końcu każdej bramki aktualne: wymagania, architektura, schemat, BOM, decyzje, wyniki testów, znane problemy i ograniczenia, instrukcja montażu/produkcji. Aktualizuj `.hq/context.md` (skill `hq:context`).
