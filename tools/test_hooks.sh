#!/bin/bash
# Testy hooka startowego hq: organizacja, tryby marki, kontekst. Uruchom: bash tools/test_hooks.sh
H="$(cd "$(dirname "$0")/.." && pwd)/hq/hooks/context-guard.sh"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
export HQ_HOME="$T/home"; fail=0
run() { echo '{}' | CLAUDE_PROJECT_DIR="$1" bash "$H" start; }
ok() { if grep -qF -- "$2" <<<"$1"; then :; else echo "FAIL: $3 (brak: $2)"; fail=1; fi; }
no() { if grep -qF -- "$2" <<<"$1"; then echo "FAIL: $3 (jest: $2)"; fail=1; fi; }
mkdir -p "$HQ_HOME/orgs/acme/brand" "$HQ_HOME/orgs/acme-labs" "$T/Projects/ACME/app/.hq/brand" "$T/Projects/ACME/Labs/x" "$T/solo" "$T/klient/.hq"
printf '# ORG ACME\nMarka: brand/brandbook.md\n' >"$HQ_HOME/orgs/acme/org.md"; echo "# BB" >"$HQ_HOME/orgs/acme/brand/brandbook.md"
printf '%s/Projects/ACME  # komentarz\n' "$T" >"$HQ_HOME/orgs/acme/paths"
printf '# ORG LABS\n' >"$HQ_HOME/orgs/acme-labs/org.md"; printf '%s/Projects/ACME/Labs/\n' "$T" >"$HQ_HOME/orgs/acme-labs/paths"
o=$(run "$T/solo"); ok "$o" "hq:orchestrator" "routing zawsze"; ok "$o" "Brak .hq/context.md" "brak kontekstu"; no "$o" "Organizacja" "solo bez org"; no "$o" "Marka:" "solo bez marki"
printf 'tryb: odrębna-zgodna\n' >"$T/Projects/ACME/app/.hq/brand/brand.md"; echo "# CTX app" >"$T/Projects/ACME/app/.hq/context.md"
o=$(run "$T/Projects/ACME/app"); ok "$o" "Organizacja: acme" "org po ścieżce"; ok "$o" "# ORG ACME" "org.md"; ok "$o" "tryb=odrębna-zgodna" "polski znak w trybie"; ok "$o" "rdzeń=$HQ_HOME/orgs/acme/brand/brandbook.md" "rdzeń"; ok "$o" "# CTX app" "context"
o=$(run "$T/Projects/ACME/Labs/x"); ok "$o" "Organizacja: acme-labs" "najdłuższy prefiks"; ok "$o" "tryb=dziedziczy" "tryb domyślny"; ok "$o" "rdzeń=brak" "brak brandbooka org"
o=$(run "$T/Projects/ACME"); ok "$o" "Organizacja: acme" "sam katalog org"
echo acme >"$T/klient/.hq/org"; o=$(run "$T/klient"); ok "$o" "Organizacja: acme" "jawne .hq/org"
echo brak >"$T/Projects/ACME/app/.hq/org"; o=$(run "$T/Projects/ACME/app"); no "$o" "Organizacja" ".hq/org=brak"; ok "$o" "tryb=odrębna-zgodna · profil" "tryb bez org"
echo nieznana >"$T/klient/.hq/org"; o=$(run "$T/klient"); ok "$o" "zaproponuj hq:org" "zła org"
mkdir -p "$T/klient/.hq/brand"; printf 'tryb: zly\n' >"$T/klient/.hq/brand/brand.md"; o=$(run "$T/klient"); ok "$o" "Nieznany tryb marki" "zły tryb"
echo acme >"$T/klient/.hq/org"; printf 'tryb: niezależna\n' >"$T/klient/.hq/brand/brand.md"; o=$(run "$T/klient"); no "$o" "rdzeń=" "niezależna bez rdzenia"; ok "$o" "tryb=niezależna" "niezależna"
mkdir -p "$T/Projects/ACME/app/.hq/threads"; printf '# WATEK a\nFokus: AAA\n' >"$T/Projects/ACME/app/.hq/threads/a.md"; printf '# WATEK b\nFokus: BBB\n' >"$T/Projects/ACME/app/.hq/threads/b.md"
o=$(run "$T/Projects/ACME/app"); ok "$o" "Wątki (a,b)" "lista wątków"; ok "$o" "Fokus: AAA" "wątek a"; ok "$o" "Fokus: BBB" "wątek b"; ok "$o" "# CTX app" "context obok wątków"
o=$(run "$T/solo"); no "$o" "Wątki" "brak wątków bez plików"
# check: pomiar z usage (przyrost od pierwszej odpowiedzi), bez odpowiedzi = cisza
tr="$T/tr.jsonl"; chk() { echo "{\"transcript_path\":\"$tr\",\"session_id\":\"s$1\"}" | TMPDIR="$T" HQ_REMIND_EVERY=999 bash "$H" check; }
msg() { printf '{"type":"assistant","message":{"usage":{"input_tokens":1,"cache_creation_input_tokens":0,"cache_read_input_tokens":%s}}}\n' "$1"; }
echo '{"type":"user"}' >"$tr"; o=$(chk 1); [ -z "$o" ] || { echo "FAIL: ostrzeżenie bez odpowiedzi"; fail=1; }
msg 90000 >"$tr"; msg 100000 >>"$tr"; o=$(chk 2); [ -z "$o" ] || { echo "FAIL: narzut stały nie powinien alarmować"; fail=1; }
msg 160000 >>"$tr"; o=$(chk 3); ok "$o" "/compact" "próg compact po przyroście 70k"
msg 210000 >>"$tr"; o=$(chk 3); ok "$o" "nowy czat" "próg nowego czatu po przyroście 120k"
[ $fail = 0 ] && echo "hooki: OK" || exit 1
