#!/bin/bash
# Diagnostyka projektu hq: wersja pluginu, narzędzia, blok w CLAUDE.md, pliki .hq/, hook startowy.
# Użycie: bash doctor.sh [katalog projektu]. Wyjście: OK/UWAGA/BŁĄD <tab> opis; kod 1 przy BŁĄD.
R=$(cd "$(dirname "$0")/../../.." && pwd); D=${1:-.}; bad=0
say() { printf '%s\t%s\n' "$1" "$2"; [ "$1" = BŁĄD ] && bad=1; return 0; }
v=$(sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' "$R/.claude-plugin/plugin.json"); say OK "plugin hq $v ($R)"
command -v jq >/dev/null && say OK "jq" || say BŁĄD "brak jq: hook nie mierzy rozmowy i nie daje podpowiedzi (brew install jq)"
command -v python3 >/dev/null && say OK "python3" || say UWAGA "brak python3: skrypty skilli nie zadziałają"
command -v node >/dev/null && say OK "node $(node -v)" || say UWAGA "brak node: wizualia HTML/SVG i makiety bez zrzutów"
c="$D/CLAUDE.md"; b=$(grep -c 'hq-begin' "$c" 2>/dev/null); e=$(grep -c 'hq-end' "$c" 2>/dev/null)
blk() { sed -n '/hq-begin/,/hq-end/p' "$1"; }
if [ ! -f "$c" ] || [ "${b:-0}" = 0 ]; then say BŁĄD "brak bloku hq w CLAUDE.md: /hq:init"
elif [ "$b" != 1 ] || [ "$e" != 1 ]; then say BŁĄD "konflikt znaczników hq w CLAUDE.md (begin=$b, end=$e): popraw ręcznie, init go nie ruszy"
elif [ "$(blk "$c")" != "$(blk "$R/templates/CLAUDE.md")" ]; then say UWAGA "blok hq w CLAUDE.md starszy niż plugin: /hq:init odświeży tylko blok"
else say OK "blok hq w CLAUDE.md aktualny"; fi
if [ -f "$D/.hq/context.md" ]; then
  n=$(( $(wc -l <"$D/.hq/context.md") )); [ "$n" -gt 60 ] && say UWAGA ".hq/context.md ma $n linii (cel ~40): hq:context" || say OK ".hq/context.md ($n linii)"
else say BŁĄD "brak .hq/context.md: /hq:init"; fi
[ -f "$D/.hq/handoff.md" ] || ls "$D"/.hq/threads/*.md >/dev/null 2>&1 && say OK "handoff/wątki" || say UWAGA "brak .hq/handoff.md i wątków"
o=$(echo '{}' | CLAUDE_PROJECT_DIR="$D" CLAUDE_PLUGIN_ROOT="$R" bash "$R/hooks/context-guard.sh" start 2>&1)
grep -q 'Nieprawidłowy slug\|Nieznany tryb\|wskazuje' <<<"$o" && say BŁĄD "hook: $(grep -m1 'Nieprawidłowy\|Nieznany\|wskazuje' <<<"$o")" || say OK "hook startowy"
grep -q '^\[hq\] Organizacja' <<<"$o" && say OK "$(grep -m1 '^\[hq\] Organizacja' <<<"$o" | cut -c6-)"
grep -q '^\[hq\] Marka' <<<"$o" && say OK "$(grep -m1 '^\[hq\] Marka' <<<"$o" | cut -c6-)"
exit $bad
