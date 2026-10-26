# hq: plugin do Claude Code

Uniwersalny plugin dla dowolnej organizacji, projektu i miniprojektu. Czatujesz z Claude jak zawsze, a plugin w tle:
- dobiera właściwego specjalistę (37 agentów, 29 skilli: kod, produkt, elektronika, marka, UX/UI, PM, budżet, marketing, prawo i inne);
- pamięta projekt i organizację;
- pilnuje spójnej marki;
- ładuje do kontekstu tylko to, co potrzebne.

> **English:** the plugin's instructions are written in Polish, but Claude answers and writes project files in **your** language. Install and just chat.

## Instalacja

Wymagania: Claude Code. Repozytorium: https://github.com/macno675/hq-claude-plugin

```bash
claude plugin marketplace add macno675/hq-claude-plugin
```

```bash
claude plugin install hq@hq-marketplace --scope user
```

`--scope user` włącza plugin we wszystkich Twoich projektach. Aktualizacja do nowej wersji:

```bash
claude plugin update hq@hq-marketplace
```

**Opcjonalne narzędzia** (plugin działa bez nich, tracisz tylko daną funkcję):

| Narzędzie | Do czego |
|---|---|
| `python3` | skrypty liczące (budżet, harmonogram, RICE, ryzyka, audyt marki itd.) |
| `jq` | ostrzeżenia o rozmiarze rozmowy |
| `ffmpeg` | pomiar głośności audio |
| MCP EasyEDA Pro | `hq:electronics`: schemat i PCB |
| klucze LCSC (`LCSC_APP_KEY`, `LCSC_SECRET`) | wyszukiwanie części przez API |

**Test (30 s):** w nowym czacie zapytaj „jakie linie [hq] dostałeś na starcie?”. Powinna pojawić się linia o `hq:orchestrator`.

## Trzy poziomy

| Poziom | Gdzie | Co trzyma |
|---|---|---|
| Organizacja | `~/.hq/orgs/<slug>/` | `org.md` (≤20 linii o firmie), `paths` (foldery projektów), `brand/` (marka z rdzeniem) |
| Projekt | `<projekt>/.hq/` | `context.md` (pamięć), `handoff.md`, `brand/brand.md` (tryb marki + różnice) |
| Miniprojekt | dowolny folder | nic, albo jeden `context.md`; marka organizacji działa z samej lokalizacji folderu |

Na starcie każdej sesji plugin sam rozpoznaje organizację po folderze i podaje Claude'owi tylko kilka linii plus ścieżki. Rejestr organizacji leży poza repozytoriami, w `~/.hq`; inną lokalizację ustawisz zmienną `HQ_HOME`. Możesz go trzymać w osobnym repo git i współdzielić z zespołem.

## Jak używać: po prostu pisz

Przykłady dla organizacji „Acme”:
- **„Załóż organizację Acme, projekty trzymam w ~/Projects/Acme”**: powstaje rejestr organizacji. Jeśli masz już logo, stronę albo kod, marka zostanie z nich **odtworzona**, a nie wymyślona od nowa.
- **„Zainicjuj ten projekt”** (w istniejącym repo): Claude mapuje kod, polecenia i stan oraz skanuje kolory i fonty. Potem zapisuje `.hq/` i pokazuje top problemy. Niczego nie naprawia bez Twojej zgody.
- **„Sprawdź, czy aplikacja trzyma się marki, i popraw błędy”**: `brandscan.py` wskazuje obce kolory i fonty z plikiem i linią. Poprawki idą przez tokeny, a ponowny skan jest dowodem.
- **„Nowy produkt dla dzieci, ma pasować do Acme, ale być weselszy”**: Claude zaproponuje tryb `rozszerza`. Rdzeń marki zostaje, zmieniają się akcent, ilustracje i ton w granicach skal.
- Każde inne zadanie (kod, elektronika, budżet, harmonogram, marketing, prawo…) idzie przez orkiestrator do właściwego specjalisty.

Bez organizacji też działa: plugin traktuje folder jako samodzielny projekt.

## Tryby marki projektu

| Tryb | Kiedy | Co wolno |
|---|---|---|
| `dziedziczy` (domyślny) | projekt wygląda jak organizacja | tylko elementy własne (nazwa produktu) |
| `rozszerza` | produkt/sub-marka z własnym charakterem | zmienić elementy **elastyczne**, rdzeń zostaje |
| `odrębna-zgodna` | projekt wymaga innego designu | własna identyfikacja + zasady zgodności (np. „by Acme”) |
| `niezależna` | projekt klienta, eksperyment | wszystko, bez związku z organizacją |

Rdzeń i elementy elastyczne opisuje sekcja 0 brandbooka organizacji. Rdzeń zmienia się tylko decyzją dla całej organizacji, nigdy „przy okazji” w projekcie.

## Oszczędzanie kontekstu (działa samo)

- Stale w kontekście są tylko opisy agentów i skilli (~1,4k tokenów) i kilka linii startowych.
- Skill ładuje się dopiero po wybraniu przez orkiestratora. Agent sam czyta swoją referencję i wraca z wnioskiem (≤300 tokenów).
- Przy dużej rozmowie plugin podpowie `/compact` albo nowy czat. Pamięć zostaje w `.hq/context.md`.

## Rozwój

- Lokalna praca nad pluginem: `claude plugin marketplace add /ścieżka/do/repo`. Plugin ładuje się wtedy z folderu, a zmiany działają od następnej sesji.
- `python3 tools/check.py`: spójność odwołań, selftesty skryptów, testy hooków i walidacja. Musi przejść przed każdym wydaniem.
- Wydanie: podnieś `version` w `hq/.claude-plugin/plugin.json` i dopisz `hq/CHANGELOG.md`. Bez podbicia wersji użytkownicy nie dostaną aktualizacji.
- Nowy agent: plik w `hq/agents/` z polem `tools:` plus wiersz w `hq/skills/orchestrator/SKILL.md`.

## Licencja

MIT © 2026 Maciej Bobrowski. Treść: [LICENSE](LICENSE).
