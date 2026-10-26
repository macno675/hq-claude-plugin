#!/usr/bin/env python3
"""Kontrola jakości pluginu hq przed wydaniem: spójność odwołań + wszystkie selftesty + walidacja.
Uruchom z katalogu repo: python3 tools/check.py   (kod wyjścia 0 = gotowe do wydania)"""
import glob, os, re, subprocess, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.chdir(os.path.join(ROOT, "hq"))
err = []
agents = {os.path.basename(f)[:-3] for f in glob.glob("agents/*.md")}
skills = {os.path.basename(os.path.dirname(f)) for f in glob.glob("skills/*/SKILL.md")}
docs = glob.glob("agents/*.md") + glob.glob("skills/**/*.md", recursive=True) + glob.glob("templates/*")
for f in docs:
    t = open(f, encoding="utf-8").read()
    for m in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([^`\s)]+)", t):
        if not os.path.exists(m.rstrip(".,;")):
            err.append(f"{f}: brak pliku {m}")
    if "/references/" in f and "${CLAUDE_PLUGIN_ROOT}" in t:
        err.append(f"{f}: ${{CLAUDE_PLUGIN_ROOT}} nie działa w referencjach (użyj <katalog skilla>)")
    if f.startswith("agents") and "`skills/" in t:
        err.append(f"{f}: ścieżka względna skills/ w agencie")
    for m in re.findall(r"hq:([a-z0-9-]+)", t):
        if m not in agents | skills:
            err.append(f"{f}: nieznane hq:{m}")
    if f.endswith("SKILL.md") or f.startswith("agents"):
        fm = t.split("\n---\n")[0]
        if not re.search(r"^description: .{10,}", fm, re.M):
            err.append(f"{f}: brak opisu we frontmatterze")
        if f.startswith("agents") and "\ntools:" not in fm:
            err.append(f"{f}: brak tools (agent dziedziczyłby wszystkie MCP)")
orch = open("skills/orchestrator/SKILL.md", encoding="utf-8").read()
for s in skills - {"orchestrator"}:
    if f"hq:{s}" not in orch:
        err.append(f"orchestrator: brak trasy do skill hq:{s}")
reach = orch + "".join(open(f, encoding="utf-8").read() for f in glob.glob("skills/*/SKILL.md"))
for a in agents:
    if a not in reach:
        err.append(f"agent {a} nieosiągalny z orkiestratora ani skilli")
desc = sum(len(re.search(r"^description: (.*)$", open(f, encoding="utf-8").read(), re.M).group(1))
           for f in glob.glob("agents/*.md") + glob.glob("skills/*/SKILL.md"))
for s in sorted(glob.glob("skills/*/scripts/*.py")):
    src = open(s, encoding="utf-8").read()
    if "--test" in src:
        r = subprocess.run([sys.executable, "-I", s, "--test"], capture_output=True, text=True)
        if r.returncode or "OK" not in r.stdout:
            err.append(f"{s}: selftest nie przeszedł: {(r.stdout + r.stderr)[-200:]}")
    else:
        r = subprocess.run([sys.executable, "-I", "-m", "py_compile", s], capture_output=True, text=True)
        if r.returncode:
            err.append(f"{s}: błąd składni")
r = subprocess.run(["bash", os.path.join(ROOT, "tools", "test_hooks.sh")], capture_output=True, text=True)
if r.returncode:
    err.append("hooki: " + r.stdout.strip())
for target in (".", ".."):
    try:
        r = subprocess.run(["claude", "plugin", "validate", target], capture_output=True, text=True)
        if r.returncode:
            err.append(f"claude plugin validate {target}: {r.stdout.strip()[-300:]}")
    except FileNotFoundError:
        print("uwaga: brak polecenia claude, pominięto walidację")
print(f"agenci {len(agents)} · skille {len(skills)} · opisy zawsze w kontekście ~{desc // 4} tokenów")
print("\n".join(err) if err else "WSZYSTKO OK - gotowe do wydania")
sys.exit(1 if err else 0)
