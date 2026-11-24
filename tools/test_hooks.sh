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
# slug z .hq/org nie może wychodzić z orgs/ (../, ścieżka absolutna)
mkdir -p "$T/evil" "$T/klient2/.hq"; echo "# EVIL" >"$T/evil/org.md"
for bad in "../../evil" "/etc" ".ukryta"; do echo "$bad" >"$T/klient2/.hq/org"; o=$(run "$T/klient2"); ok "$o" "Nieprawidłowy slug" "slug $bad"; no "$o" "# EVIL" "traversal $bad"; done
# po /compact (spadek usage) ostrzeżenia startują od nowa; JSON z odstępami też jest mierzony
tr2="$T/tr2.jsonl"; chk2() { echo "{\"transcript_path\":\"$tr2\",\"session_id\":\"c$1\"}" | TMPDIR="$T" HQ_REMIND_EVERY=999 bash "$H" check; }
msg2() { printf '{ "type": "assistant", "message": { "usage": { "input_tokens": 1, "cache_creation_input_tokens": 0, "cache_read_input_tokens": %s } } }\n' "$1"; }
msg2 90000 >"$tr2"; msg2 160000 >>"$tr2"; o=$(chk2 1); ok "$o" "/compact" "JSON z odstępami"
msg2 40000 >>"$tr2"; o=$(chk2 1); [ -z "$o" ] || { echo "FAIL: po compact bez alarmu"; fail=1; }
msg2 160000 >>"$tr2"; o=$(chk2 1); ok "$o" "/compact" "ostrzeżenie po kompakcji wraca"
# filtr testów zachowuje kod wyjścia i pełny log
F="$(cd "$(dirname "$0")/.." && pwd)/hq/hooks/filter-bash.sh"; mkdir -p "$T/bin"
printf '#!/bin/bash\necho "FAIL: x"; echo "1 failed"; exit 3\n' >"$T/bin/pytest"; chmod +x "$T/bin/pytest"
c=$(jq -nr --arg c "pytest" '{tool_input:{command:$c}}' | HQ_FILTER_OUTPUT=1 bash "$F" | jq -r '.hookSpecificOutput.updatedInput.command')
o=$(PATH="$T/bin:$PATH" bash -c "$c"); rc=$?; [ $rc = 3 ] || { echo "FAIL: filtr zgubił kod wyjścia ($rc)"; fail=1; }; ok "$o" "FAIL: x" "filtr pokazuje błąd"; ok "$o" "exit=3" "filtr podaje kod"
# prośba o logo (także kontynuacja rozmowy) = przypomnienie o warunku startu; inna prośba = cisza
lg() { jq -nc --arg p "$1" '{prompt:$p,transcript_path:"/brak",session_id:"lg"}' | TMPDIR="$T" HQ_REMIND_EVERY=999 bash "$H" check; }
o=$(lg "Stwórz teraz 4 propozycje logo"); ok "$o" "Warunek startu" "logo: przypomnienie"
o=$(lg "Napraw test w kalendarzu"); [ -z "$o" ] || { echo "FAIL: przypomnienie logo bez logo"; fail=1; }
# słowo-klucz głęboko we wklejonym tekście = cisza; prośba o makietę = przypomnienie hq:views
o=$(lg "Przeanalizuj odpowiedzi i wdróż zmiany. $(printf 'x%.0s' {1..500}) logotypy partnerów"); [ -z "$o" ] || { echo "FAIL: przypomnienie z głębi wklejonego tekstu"; fail=1; }
o=$(lg "Zaprojektuj stronę agroturystyki, najpierw makieta"); ok "$o" "hq:views" "widoki: przypomnienie"
o=$(lg "Makiety zatwierdzone, ustal styl strony z liquid glass"); ok "$o" "hq:look" "wygląd: przypomnienie"
o=$(lg "Popraw literówkę w stopce"); no "$o" "hq:look" "wygląd: cisza bez prośby o styl"
# intencje bez komendy: nowa rzecz -> fundament, teksty -> zasady pisania; "logowanie" to nie logo
o=$(lg "zrób proszę wizualizację panelu administracyjnego"); ok "$o" "od fundamentu" "nowa rzecz: fundament"; no "$o" "Logo:" "panel bez logo"
o=$(lg "chcę mieć stronę dla agroturystyki"); ok "$o" "od fundamentu" "nowa strona: fundament"
o=$(lg "dodaj ekran logowania do aplikacji"); no "$o" "Logo:" "logowanie to nie logo"
o=$(lg "napisz teksty na stronę główną"); ok "$o" "writing.md" "teksty: zasady pisania"; no "$o" '${CLAUDE_PLUGIN_ROOT}' "ścieżka rozwinięta"
o=$(run "$T/solo"); ok "$o" "Pisanie (czat" "zasada pisania na starcie"
# blok hq w CLAUDE.md starszy niż szablon = podpowiedź odświeżenia; aktualny = cisza
printf '<!-- hq-begin -->\nstary\n<!-- hq-end -->\n' >"$T/solo/CLAUDE.md"; o=$(run "$T/solo"); ok "$o" "różni się od wersji" "stary blok"
cp "$(dirname "$H")/../templates/CLAUDE.md" "$T/solo/CLAUDE.md"; o=$(run "$T/solo"); no "$o" "różni się" "aktualny blok"; no "$o" "Brak bloku hq" "blok jest"
# etapy z plików statusu; doctor: konflikt znaczników = BŁĄD, aktualny projekt bez BŁĄD
mkdir -p "$T/solo/.hq/views"; echo "# CTX solo" >"$T/solo/.hq/context.md"; printf 'status: approved\n' >"$T/solo/.hq/views/status.md"
o=$(run "$T/solo"); ok "$o" "Etapy: views=approved" "etapy"
DR="$(dirname "$H")/../skills/init/scripts/doctor.sh"; o=$(bash "$DR" "$T/solo"); rc=$?; [ $rc = 0 ] || { echo "FAIL: doctor zgłasza błąd w poprawnym projekcie: $o"; fail=1; }
printf '<!-- hq-begin -->\n<!-- hq-begin -->\n<!-- hq-end -->\n' >"$T/solo/CLAUDE.md"; o=$(bash "$DR" "$T/solo"); ok "$o" "konflikt znaczników" "doctor: konflikt"
[ $fail = 0 ] && echo "hooki: OK" || exit 1
