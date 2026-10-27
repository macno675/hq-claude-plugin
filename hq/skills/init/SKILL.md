---
name: init
description: Zakłada pamięć projektu .hq/ (nowy lub istniejący kod/marka, podpięcie do organizacji) - na prośbę lub po zgodzie użytkownika.
argument-hint: "[nazwa projektu]"
---

# Inicjalizacja projektu hq

Cel: każdy czat w projekcie startuje tanio z `.hq/context.md` i zna organizację oraz markę. Działa w nowym, istniejącym i mini projekcie.

0. **Już jest** `.hq/context.md`: nie nadpisuj. Pokaż 3 linie stanu, sprawdź tylko brakujące elementy (org, profil marki, blok hq w `CLAUDE.md`) i zakończ.
1. **Rozpoznaj** (bez pytania użytkownika): organizacja z linii hooka `[hq] Organizacja:` (lub brak), rodzaj folderu:
   - pusty/nowy · istniejący kod (`git log -1`, manifesty: `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`...) · materiały bez kodu (dokumenty, grafiki) · mini (1-3 pliki, krótkie zadanie).
2. **Mini:** tylko `.hq/context.md` w 10 liniach (cel, następny krok). Bez pytań, bez CLAUDE.md, bez profilu marki (marka org z hooka i tak obowiązuje). Koniec.
3. **Pytania** (`AskUserQuestion`, max 3, tylko czego nie da się wyczytać): cel projektu, przynależność do organizacji (gdy hook nie rozpoznał a istnieją org w `~/.hq/orgs/`), tryb marki (gdy jest org; rekomendacja: domyślny z `org.md`).
4. **Istniejący projekt = adopcja** (deleguj do subagenta `Explore`/`hq:researcher`, zwrot ≤300 tokenów): stos, struktura (5-10 kluczowych ścieżek), polecenia test/build/run, stan (co działa, ostatnie zmiany z `git log --oneline -15`), widoczne problemy (TODO/FIXME, padające testy, jeśli tanie do uruchomienia). Nie czytaj repo w głównym wątku.
   Jeśli są kolory/fonty w kodzie lub zasobach: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/brand/scripts/brandscan.py . --brand <brandbook org>` (bez marki: bez `--brand`, tylko inwentarz) - wynik zapisz jako `.hq/brand/scan.tsv`, w rozmowie tylko podsumowanie.
5. **Zapisz:**
   - `.hq/context.md` z `${CLAUDE_PLUGIN_ROOT}/templates/context.md` (Cel, Stan, Klucz; data dzisiejsza); wątki czatów w `.hq/threads/` powstają przy pierwszym handoffie;
   - `.hq/handoff.md`: `Zrobione: init` / `Następne: <krok>` / `Blokery: brak`;
   - `.hq/org` (slug), tylko gdy projekt nie leży w ścieżkach organizacji;
   - `.hq/brand/brand.md` z `${CLAUDE_PLUGIN_ROOT}/templates/brand-profile.md`, gdy jest org lub własna marka (tylko tryb, rodzic i różnice);
   - `CLAUDE.md` (obowiązkowo, bo ładuje się po każdym /compact i /clear, więc stale przypomina o hq):
     brak pliku: utwórz z `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE.md` (polecenia wyczytane z repo).
     plik istnieje: bez zmiany reszty dopisz na początku tylko blok `<!-- hq-begin -->...<!-- hq-end -->` z szablonu (gdy bloku brak; gdy jest, zaktualizuj tylko jego treść) i wspomnij o tym w raporcie.
     Nie dotykaj treści poza znacznikami.
   Katalogów domenowych (`.hq/pm/`, `.hq/product/`...) nie zakładaj na zapas - tworzą je skille.
6. **Raport** (max 6 linii): co powstało, organizacja i tryb marki, top 3 problemy z adopcji (kod, marka: liczba OBCY/DRYF), proponowany pierwszy krok. Naprawy tylko po zgodzie - prowadzi je `hq:orchestrator` (marka: `hq:brand` Audyt i naprawa).

Uwaga dla repo zespołowych: `.hq/` warto commitować (wspólna pamięć projektu); `.hq/brand/scan.tsv` można dodać do `.gitignore`.
