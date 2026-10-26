# claude-ag (plugin hq)

<!-- hq-begin (blok zarządzany przez hq:init; edytuj poza znacznikami) -->
## hq (obowiązuje w całej rozmowie, także po /compact i /clear)
- Zadanie wieloetapowe lub domenowe (kod, marka, elektronika, PM, produkt, finanse, marketing, bezpieczeństwo, research...): najpierw skill `hq:orchestrator`, potem tylko wybrany skill/agent `hq:*`. Nie rób sam tego, co ma agent hq.
- Marka i organizacja: linie `[hq] Marka/Organizacja` ze startu sesji; nowe materiały wizualne i teksty zgodne z brandbookiem (`hq:brand`).
- Stan: czytaj `.hq/context.md` i `.hq/handoff.md`; po ważnej zmianie aktualizuj (`hq:context`). Zadania: `.hq/pm/tasks.tsv`.
- Długa rozmowa lub zmiana zadania: `hq:context` (handoff, nowy czat), nie ciągnij historii.
<!-- hq-end -->

## Cel
Plugin `hq` do Claude Code: orkiestrator, agenci i skille domenowe z oszczędnym kontekstem. Tylko Claude Code, bez API.

## Struktura
- hq/ - plugin (agents, skills, hooks, templates, CHANGELOG)
- .claude-plugin/marketplace.json - lokalny marketplace
- tools/ - check.py (bramka wydania), test_hooks.sh
- .hq/, .hq-backups/ - prywatna pamięć autora (w .gitignore)

## Zasady
- Plugin uniwersalny: zero nazw konkretnych organizacji w hq/ (przykład: Acme).
- Opisy skilli i agentów jednozdaniowe; szczegóły w references/ ładowanych na żądanie.
- Agent bez `tools:` dziedziczy wszystkie MCP; zawsze podawaj listę.
- Przed wydaniem: `python3 tools/check.py`, podbij wersję w plugin.json i CHANGELOG.

## Polecenia
- Bramka: `python3 tools/check.py` · Hooki: `bash tools/test_hooks.sh`

# Compact instructions
Przy kompaktowaniu zachowaj: cel zadania, zmienione pliki, decyzje z powodem, nieudane testy, otwarte problemy, ograniczenia, następny krok. Usuń: logi i pełne wyniki poleceń, nieaktualne plany, martwe ścieżki, powtórzone treści plików.
