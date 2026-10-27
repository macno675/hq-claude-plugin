#!/bin/bash
# start: routing + organizacja (org.md) + linia Marka + .hq/context.md (+ handoff, wątki). check: dwustopniowe ostrzeżenie o rozmiarze rozmowy.
# Rozmiar = rzeczywiste tokeny z usage ostatniej odpowiedzi (jak /context), liczone jako przyrost od pierwszej odpowiedzi,
# bo stały narzut (narzędzia, skille, MCP) bywa ~90k i nie jest winą rozmowy. Po /compact usage spada samo.
COMPACT=${HQ_CTX_COMPACT:-60000}   # przyrost tokenów: podpowiedz /compact
LIMIT=${HQ_CTX_TOKENS:-110000}     # przyrost tokenów: nowy czat
STEP=${HQ_CTX_STEP:-50000}         # kolejne ostrzeżenie dopiero po takim przyroście
DIR=${CLAUDE_PROJECT_DIR:-.}

in=$(cat)
case "$1" in
  start)
    echo "[hq] Zadanie wieloetapowe lub domenowe: najpierw skill hq:orchestrator (routing), potem tylko wybrany skill/agent; skilli i referencji hq nie ładuj na zapas. Odpowiadaj w języku użytkownika."
    # Organizacja: .hq/org (slug lub "brak") ma pierwszeństwo, inaczej najdłuższy prefiks z $HQ_HOME/orgs/*/paths.
    HQ=${HQ_HOME:-$HOME/.hq}; real=$(cd "$DIR" 2>/dev/null && pwd -P); org=""; best=0
    if [ -f "$DIR/.hq/org" ]; then
      org=$(head -1 "$DIR/.hq/org" | tr -d '[:space:]'); [ "$org" = "brak" ] && org=""
    else
      for pf in "$HQ"/orgs/*/paths; do
        [ -f "$pf" ] || continue
        while IFS= read -r p || [ -n "$p" ]; do
          p=${p%%#*}; p=$(printf '%s' "$p" | sed 's/[[:space:]]*$//'); [ -z "$p" ] && continue
          p=${p/#\~/$HOME}; p=${p%/}; pr=$(cd "$p" 2>/dev/null && pwd -P || echo "$p")  # dowiązania (np. /var, iCloud)
          case "$real/" in "$pr"/*) [ ${#pr} -gt $best ] && { best=${#pr}; org=$(basename "$(dirname "$pf")"); } ;; esac
        done <"$pf"
      done
    fi
    od="$HQ/orgs/$org"
    if [ -n "$org" ]; then
      if [ -d "$od" ]; then
        echo "[hq] Organizacja: $org ($od)"; [ -f "$od/org.md" ] && head -25 "$od/org.md"
      else
        echo "[hq] .hq/org wskazuje '$org', ale brak $od - zaproponuj hq:org (załóż lub popraw)."; org=""
      fi
    fi
    # Marka efektywna: tryb z .hq/brand/brand.md (linia "tryb:"), domyślnie "dziedziczy" w organizacji.
    prof="$DIR/.hq/brand/brand.md"; mode=""
    [ -f "$prof" ] && mode=$(sed -n 's/^tryb:[[:space:]]*\([^[:space:]<|]*\).*/\1/p' "$prof" | head -1)
    [ -z "$mode" ] && [ -n "$org" ] && mode="dziedziczy"
    case "$mode" in dziedziczy|rozszerza|odrębna-zgodna|niezależna|"") ;; *) echo "[hq] Nieznany tryb marki '$mode' w .hq/brand/brand.md (dozwolone: dziedziczy, rozszerza, odrębna-zgodna, niezależna)." ;; esac
    line=""
    if [ -n "$org" ] && [ "$mode" != "niezależna" ]; then
      core="$od/brand/brandbook.md"; [ -f "$core" ] || core="brak - zaproponuj hq:brand dla organizacji"
      line="tryb=$mode · rdzeń=$core"
    elif [ -n "$mode" ]; then line="tryb=$mode"; fi
    [ -f "$prof" ] && line="${line:+$line · }profil=.hq/brand/brand.md"
    [ -f "$DIR/.hq/brand/brandbook.md" ] && line="${line:+$line · }własny=.hq/brand/brandbook.md"
    [ -n "$line" ] && echo "[hq] Marka: $line"
    grep -qs 'hq-begin' "$DIR/CLAUDE.md" || echo "[hq] Brak bloku hq w CLAUDE.md - uruchom hq:init (dopisze przypomnienie o orkiestratorze, trwa po /compact i /clear)."
    [ -f "$DIR/.hq/context.md" ] || { echo "[hq] Brak .hq/context.md - przy dłuższej pracy zaproponuj hq:init (adopcja istniejącego kodu i marki)."; exit 0; }
    cat "$DIR/.hq/context.md"
    [ -f "$DIR/.hq/handoff.md" ] && { echo; cat "$DIR/.hq/handoff.md"; }
    # Wątki równoległych czatów: każdy czat edytuje tylko swój plik (skill hq:context).
    th=("$DIR"/.hq/threads/*.md)
    if [ -f "${th[0]}" ]; then
      echo; echo "[hq] Wątki ($(for f in "${th[@]}"; do basename "$f" .md; done | paste -sd, -)): ten czat pracuje w jednym; jeśli użytkownik go nie wskazał, zapytaj. Zapisuj tylko własny .hq/threads/<slug>.md."
      for f in "${th[@]}"; do echo; cat "$f"; done
    fi
    ;;
  check)
    command -v jq >/dev/null || exit 0
    f=$(jq -r '.transcript_path // empty' <<<"$in"); sid=$(jq -r '.session_id // "x"' <<<"$in")
    [ -f "$f" ] || exit 0
    mark="${TMPDIR:-/tmp}/hq-ctx-$sid"
    # Przypominajka co N-tą wiadomość: instrukcja ze startu ginie w długiej rozmowie.
    n=$(( $(cat "$mark.n" 2>/dev/null || echo 0) + 1 )); echo "$n" >"$mark.n"
    [ $((n % ${HQ_REMIND_EVERY:-6})) -eq 0 ] && echo "[hq] Przypomnienie: zadanie wieloetapowe lub domenowe (kod, marka, elektronika, PM, finanse, marketing...) zaczynaj od skilla hq:orchestrator i deleguj do agentów hq:*. Stan pracy: .hq/context.md."
    tok() { jq -r 'select(.message.usage) | .message.usage | .input_tokens + .cache_creation_input_tokens + .cache_read_input_tokens' 2>/dev/null; }
    lines=$(grep '"type":"assistant"' "$f" | grep -v '"isSidechain":true' | grep '"input_tokens"')
    cur=$(tail -1 <<<"$lines" | tok); [ -n "$cur" ] || exit 0   # jeszcze brak odpowiedzi: nic nie mierzymy
    [ -f "$mark.base" ] || head -1 <<<"$lines" | tok >"$mark.base"
    base=$(cat "$mark.base"); size=$((cur - base)); last=$(cat "$mark" 2>/dev/null || echo 0)
    info="~$((cur / 1000))k tokenów, w tym ~$((base / 1000))k stałego narzutu; rozmowa ~$((size / 1000))k. Dokładnie: /context"
    if [ "$size" -ge "$LIMIT" ] && [ "$size" -ge $((last + STEP)) ]; then
      echo "$size" >"$mark"
      echo "[hq] Rozmowa duża ($info). Po odpowiedzi na bieżącą prośbę zastosuj skill hq:context: zaktualizuj .hq/context.md i swój wątek, zaproponuj nowy czat (/rename, /clear) z linią startową."
    elif [ "$size" -ge "$COMPACT" ] && [ ! -f "$mark.compact" ]; then
      : >"$mark.compact"
      echo "[hq] Kontekst rośnie ($info). Jeśli to wciąż to samo zadanie, po odpowiedzi zaproponuj /compact z szablonem ze skilla hq:context; przy zmianie zadania /rename i /clear."
    fi
    ;;
esac
exit 0
