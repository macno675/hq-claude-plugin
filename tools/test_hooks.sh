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
[ $fail = 0 ] && echo "hooki: OK" || exit 1
