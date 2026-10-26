#!/bin/bash
# start: routing + organizacja (org.md) + linia Marka + .hq/context.md (+ handoff). check: dwustopniowe ostrzeżenie o rozmiarze rozmowy.
# shortcut: rozmiar transkryptu w bajtach ~ 4 B/token, niedokładne; kalibruj progi (dokładnie: /context).
COMPACT=${HQ_CTX_COMPACT:-300000}  # ~75k tokenów: podpowiedz /compact
LIMIT=${HQ_CTX_BYTES:-500000}      # ~125k tokenów: nowy czat
STEP=${HQ_CTX_STEP:-150000}        # kolejne ostrzeżenie dopiero po takim przyroście
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
    [ -f "$DIR/.hq/context.md" ] || { echo "[hq] Brak .hq/context.md - przy dłuższej pracy zaproponuj hq:init (adopcja istniejącego kodu i marki)."; exit 0; }
    cat "$DIR/.hq/context.md"
    [ -f "$DIR/.hq/handoff.md" ] && { echo; cat "$DIR/.hq/handoff.md"; }
    ;;
  check)
    command -v jq >/dev/null || exit 0
    f=$(jq -r '.transcript_path // empty' <<<"$in"); sid=$(jq -r '.session_id // "x"' <<<"$in")
    [ -f "$f" ] || exit 0
    size=$(wc -c <"$f"); mark="${TMPDIR:-/tmp}/hq-ctx-$sid"; last=$(cat "$mark" 2>/dev/null || echo 0)
    if [ "$size" -ge "$LIMIT" ] && [ "$size" -ge $((last + STEP)) ]; then
      echo "$size" >"$mark"
      echo "[hq] Rozmowa duża (~$((size / 4000))k tokenów). Po odpowiedzi na bieżącą prośbę zastosuj skill hq:context: zaktualizuj .hq/context.md i handoff.md, zaproponuj nowy czat (/rename, /clear) z linią startową."
    elif [ "$size" -ge "$COMPACT" ] && [ ! -f "$mark.compact" ]; then
      : >"$mark.compact"
      echo "[hq] Kontekst rośnie (~$((size / 4000))k tokenów). Jeśli to wciąż to samo zadanie, po odpowiedzi zaproponuj użytkownikowi /compact z szablonem ze skilla hq:context; przy zmianie zadania /rename i /clear."
    fi
    ;;
esac
exit 0
