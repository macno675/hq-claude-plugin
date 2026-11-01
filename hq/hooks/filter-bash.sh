#!/bin/bash
# PreToolUse (Bash), OPT-IN: HQ_FILTER_OUTPUT=1 skraca wyniki znanych poleceń testowych do błędów (mniej tokenów).
# Zachowuje kod wyjścia polecenia i pełny log w pliku tymczasowym; pokazuje błędy i 3 ostatnie linie (podsumowanie). Domyślnie wyłączony.
input=$(cat)
[ "$HQ_FILTER_OUTPUT" = "1" ] || { echo "{}"; exit 0; }
cmd=$(jq -r '.tool_input.command // empty' <<<"$input")
pattern='^(npm test|pytest|go test)( [^;&|<>`$#\\[:cntrl:]]*)?$'
if [[ "$cmd" =~ $pattern ]]; then
  filtered="log=\$(mktemp); $cmd >\"\$log\" 2>&1; rc=\$?; grep -A 5 -E '(FAIL|ERROR|error:)' \"\$log\" | head -100; tail -3 \"\$log\"; echo \"[hq] exit=\$rc, pełny log: \$log\"; exit \$rc"
  jq -n --arg c "$filtered" --argjson i "$input" '{hookSpecificOutput:{hookEventName:"PreToolUse",updatedInput:($i.tool_input + {command:$c})}}'
else
  echo "{}"
fi
