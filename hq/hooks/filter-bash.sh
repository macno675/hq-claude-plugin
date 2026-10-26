#!/bin/bash
# PreToolUse (Bash), OPT-IN: HQ_FILTER_OUTPUT=1 skraca wyniki znanych poleceń testowych do błędów (mniej tokenów).
# Ukrywa liczbę przechodzących testów, dlatego jest wyłączony domyślnie. Wzorzec z dokumentacji Claude Code.
input=$(cat)
[ "$HQ_FILTER_OUTPUT" = "1" ] || { echo "{}"; exit 0; }
cmd=$(jq -r '.tool_input.command // empty' <<<"$input")
pattern='^(npm test|pytest|go test)( [^;&|<>`$#\\[:cntrl:]]*)?$'
if [[ "$cmd" =~ $pattern ]]; then
  filtered="$cmd 2>&1 | grep -A 5 -E '(FAIL|ERROR|error:)' | head -100"
  jq -n --arg c "$filtered" --argjson i "$input" '{hookSpecificOutput:{hookEventName:"PreToolUse",updatedInput:($i.tool_input + {command:$c})}}'
else
  echo "{}"
fi
