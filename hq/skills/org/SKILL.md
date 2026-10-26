---
name: org
description: Organizacje (firma/marka nadrzędna) - załóż, podepnij projekt, ustaw tryb dziedziczenia marki, pokaż listę.
argument-hint: "[nowa <nazwa> | podepnij <slug> | lista]"
---

# Organizacje

Organizacja = wspólny kontekst i marka dla wielu projektów. Rejestr: `$HQ_HOME/orgs/<slug>/` (domyślnie `~/.hq/orgs/`), poza repozytoriami, więc działa w każdym projekcie i miniprojekcie.

```
~/.hq/orgs/<slug>/
  org.md          # ≤20 linii, wstrzykiwane do każdej sesji projektu tej org (szablon ${CLAUDE_PLUGIN_ROOT}/templates/org.md)
  paths           # prefiksy folderów projektów, po 1 w linii (np. ~/Projects/Acme) - automatyczne rozpoznanie
  brand/          # brandbook.md (z sekcją 0 Dziedziczenie), tokens.css, assets/, decisions.md  -> skill hq:brand
  decisions.md    # decyzje obowiązujące całą organizację
```
Projekt należy do organizacji, gdy: plik `.hq/org` (1 linia: slug lub `brak`) albo folder projektu leży pod ścieżką z `paths` (najdłuższe dopasowanie wygrywa). Plik `.hq/org` ma pierwszeństwo.

## Nowa organizacja
1. Zapytaj (`AskUserQuestion`, ≤4): nazwa, czym się zajmuje (1 zdanie), folder(y), w których trzyma projekty tej org, czy ma już markę (pliki, strona www, repozytorium z kodem).
2. Slug: małe litery, cyfry, `-` (np. `acme`). Utwórz `org.md` z szablonu (krótko, bez lania wody) i `paths`.
3. Marka:
   - istniejące materiały -> `hq:brand` w trybie **Odtworzenie** (wyciąga markę z plików/kodu, użytkownik zatwierdza rdzeń);
   - brak -> `hq:brand` (skala wg potrzeb) z właścicielem = organizacja.
   W brandbooku org **zawsze** wypełnij sekcję 0 (rdzeń / elastyczne / zasady zgodności) - bez niej projekty nie wiedzą, co wolno zmienić.
4. Zaproponuj `git init` w katalogu org (historia zmian marki, synchronizacja między komputerami/zespołem). Nie wykonuj bez zgody.

## Podepnij projekt
1. Jeśli folder pasuje do `paths` - nic nie trzeba. Inaczej zapisz slug w `.hq/org`.
2. Ustal **tryb marki** projektu (`AskUserQuestion`, rekomendacja z uzasadnieniem):
   - `dziedziczy` - projekt wygląda i brzmi jak organizacja (domyślne);
   - `rozszerza` - rdzeń org + własne elementy elastyczne (np. akcent, ilustracje) - sub-marka/produkt;
   - `odrębna-zgodna` - własna identyfikacja, ale spełnia zasady zgodności org (np. "by Acme");
   - `niezależna` - bez związku (projekt klienta, eksperyment).
3. Utwórz `.hq/brand/brand.md` z `${CLAUDE_PLUGIN_ROOT}/templates/brand-profile.md`: tryb, rodzic i **tylko różnice**. Nie kopiuj brandbooka organizacji do projektu (rozjedzie się).
4. `odrębna-zgodna` -> własny brandbook projektu przez `hq:brand`, przegląd zgodności z rodzicem przez `hq:design-reviewer`.

## Lista
`ls $HQ_HOME/orgs` + pierwsza linia każdego `org.md` + liczba ścieżek w `paths`.

## Zasady
- Rdzeń marki org zmienia tylko decyzja na poziomie org (wpis w `orgs/<slug>/decisions.md` + podbicie wersji brandbooka); projekt nie nadpisuje rdzenia "przy okazji".
- `org.md` krótki: to koszt w każdej sesji. Szczegóły w plikach obok, czytane na żądanie.
- Zmiana `org.md`/marki org dotyczy wszystkich projektów: przed zmianą powiedz użytkownikowi, co się zmieni.
