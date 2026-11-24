// Kontrola techniczna stylu hq:look na 360 i 1280 px + zrzuty (zwykły, skala szarości, bez [data-logo]).
// Sprawdza spójność i jakość techniczną, NIE estetykę. Tokeny = wszystkie --* z reguł :root/html.
// Użycie (z katalogu projektu z Playwright): node stylecheck.mjs <plik.html> [--dark] [--out <katalog>]   |   --test
// Wyjście: TSV "szerokość poziom reguła element"; kod 1 = jest FAIL, 3 = brak Playwright.
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath, pathToFileURL } from "node:url";

let chromium;
try { ({ chromium } = createRequire(path.join(process.cwd(), "x.js"))("playwright")); }
catch { try { ({ chromium } = await import("playwright")); } catch { console.log("brak Playwright w projekcie: npm i -D playwright && npx playwright install chromium"); process.exit(3); } }

const SIZES = [[360, 780], [1280, 800]];

function audit() { // działa w przeglądarce
  const out = [], seen = new Set();
  const add = (lvl, rule, el) => {
    const d = el ? `${el.tagName.toLowerCase()}${el.id ? "#" + el.id : ""}${el.classList?.length ? "." + [...el.classList].join(".") : ""} ${(el.textContent || "").trim().slice(0, 30)}` : "-";
    const k = lvl + rule + d; if (!seen.has(k)) { seen.add(k); out.push([lvl, rule, d]); }
  };
  const W = innerWidth, H = innerHeight, cs = el => getComputedStyle(el);
  const vis = el => { const r = el.getBoundingClientRect(), s = cs(el); return r.width > 0 && r.height > 0 && s.visibility !== "hidden"; };
  // kolor -> [r,g,b,a] przez canvas (działa dla rgb, oklch, hsl...)
  const ctx = Object.assign(document.createElement("canvas"), { width: 1, height: 1 }).getContext("2d", { willReadFrequently: true });
  const memo = new Map();
  const rgba = c => { if (!memo.has(c)) { ctx.clearRect(0, 0, 1, 1); ctx.fillStyle = "#000"; ctx.fillStyle = c; ctx.fillRect(0, 0, 1, 1); const d = ctx.getImageData(0, 0, 1, 1).data; memo.set(c, [d[0], d[1], d[2], d[3] / 255]); } return memo.get(c); };
  const key = c => rgba(c).slice(0, 3).join(","); // shortcut: porównanie bez kanału alfa; gdy wyjątki z alfą będą częste - dodać alfę
  const lum = ([r, g, b]) => { const f = v => (v /= 255) <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const blend = (top, bot) => [0, 1, 2].map(i => top[i] * top[3] + bot[i] * (1 - top[3])).concat(1);
  const hue = ([r, g, b]) => { const mx = Math.max(r, g, b), mn = Math.min(r, g, b), d = mx - mn; if (!d) return [-1, 0];
    let h = mx === r ? ((g - b) / d) % 6 : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; return [(h * 60 + 360) % 360, d / mx]; };

  // reguły CSS (płasko, z @media)
  const rules = [], walk = list => { for (const r of list) { rules.push(r); if (r.cssRules) walk(r.cssRules); } };
  for (const sh of document.styleSheets) { try { walk(sh.cssRules); } catch { } }
  const names = new Set();
  for (const r of rules) if (r.selectorText && /(^|,)\s*(:root|html)\b/.test(r.selectorText)) for (const p of r.style) if (p.startsWith("--")) names.add(p);
  if (!rules.length) add("WARN", "arkusze-CSS-nieczytelne (inne źródło): reguły @media i :hover niesprawdzone", null);
  const probe = document.body.appendChild(document.createElement("div")), root = cs(document.documentElement);
  const tok = { color: new Set(), radius: new Set(["0px"]), shadow: new Set(["none"]) }, tvals = [];
  for (const n of names) {
    const v = root.getPropertyValue(n).trim(); tvals.push(v);
    if (CSS.supports("color", v)) { tok.color.add(key(v)); continue; }
    if (/radi|corner|round/.test(n)) { probe.style.borderRadius = v; tok.radius.add(cs(probe).borderTopLeftRadius); }
    else if (/shadow|elev/.test(n)) { probe.style.boxShadow = v; tok.shadow.add(cs(probe).boxShadow); }
  }
  probe.remove();
  if (!tok.color.size) add("FAIL", "brak-tokenów-koloru-w-:root", null);

  if (document.documentElement.scrollWidth > W + 1) add("FAIL", "przewijanie-w-bok", null);
  const all = [...document.querySelectorAll("body *")].filter(vis);
  const hasText = el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
  const families = new Set();
  let motion = false, glass = 0;
  for (const el of all) {
    const s = cs(el), exc = el.closest("[data-style-exception]"), text = hasText(el);
    if (!exc && tok.color.size) {
      const used = [s.backgroundColor];
      if (text) used.push(s.color);
      for (const side of ["Top", "Right", "Bottom", "Left"]) if (parseFloat(s[`border${side}Width`]) > 0) used.push(s[`border${side}Color`]);
      for (const c of used) if (rgba(c)[3] > 0 && !tok.color.has(key(c))) { add("FAIL", `kolor-spoza-tokenów ${c}`, el); break; }
      if (!tok.radius.has(s.borderTopLeftRadius) && !/%$/.test(s.borderTopLeftRadius) && parseFloat(s.borderTopLeftRadius) < 999) add("FAIL", `promień-spoza-tokenów ${s.borderTopLeftRadius}`, el);
      if (!tok.shadow.has(s.boxShadow)) add("FAIL", "cień-spoza-tokenów", el);
    }
    if (text) {
      families.add(s.fontFamily.split(",")[0].replace(/["']/g, "").trim().toLowerCase());
      const fs = parseFloat(s.fontSize), em = (parseFloat(s.letterSpacing) || 0) / fs, upper = s.textTransform === "uppercase";
      if (!upper && fs < 20 && em > 0.021) add("FAIL", `tracking-${em.toFixed(3)}em-na-tekście`, el);
      if (fs < 16 && em < -0.001) add("FAIL", "ujemny-tracking-na-małym-tekście", el);
      if (upper && em > 0.12) add("WARN", "tracking-wersalików>0,12em", el);
      if (!el.closest(":disabled, [aria-disabled=true]")) {
        let layers = [], glassy = false;
        for (let e = el; e; e = e.parentElement) { const es = cs(e);
          if (es.backgroundImage !== "none" || es.backdropFilter !== "none") { glassy = true; break; }
          const b = rgba(es.backgroundColor); if (b[3] > 0) { layers.push(b); if (b[3] >= 1) break; } }
        if (glassy) add("WARN", "kontrast-na-obrazie/szkle-sprawdź-ręcznie", el);
        else {
          const bg = layers.reverse().reduce((acc, l) => blend(l, acc), [255, 255, 255, 1]), fg = blend(rgba(s.color), bg);
          const [a, b] = [lum(fg), lum(bg)], ratio = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
          const large = fs >= 24 || (fs >= 18.66 && +s.fontWeight >= 700);
          if (ratio < (large ? 3 : 4.5)) add("FAIL", `kontrast-${ratio.toFixed(2)}<${large ? 3 : 4.5}`, el);
        }
      }
    }
    if (el.matches("a, button, [role=button], [class*=icon]") && /\p{Extended_Pictographic}/u.test(el.textContent.replace(/[©®™]/g, ""))) add("FAIL", "emoji-jako-ikona", el);
    if (el.matches("a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button]") && s.display !== "inline") {
      const r = el.getBoundingClientRect(); if (Math.min(r.width, r.height) < 24) add("FAIL", "cel-dotykowy<24px", el);
    }
    const durs = (s.transitionDuration + "," + s.animationDuration).split(",").some(d => parseFloat(d) > 0);
    if (durs && (s.transitionProperty !== "none" || s.animationName !== "none")) {
      motion = true;
      if (/(^|,\s*)linear(,|$)/.test(s.transitionTimingFunction + "," + s.animationTimingFunction) && !el.matches("progress, [role=progressbar]")) add("WARN", "linear-poza-postępem", el);
      if (/filter/.test(s.transitionProperty)) add("WARN", "animowany-blur/filter", el);
    }
    if (s.backdropFilter !== "none") { const r = el.getBoundingClientRect(); if (r.width * r.height > 0.25 * W * H) glass++; }
    if (/text/.test(s.backgroundClip + s.webkitBackgroundClip)) add("WARN", "gradientowy-tekst", el);
    if (/gradient/.test(s.backgroundImage)) {
      const hs = (s.backgroundImage.match(/(rgba?|oklch|oklab|hsla?|lab|lch)\([^)]*\)/g) || []).map(c => hue(rgba(c))).filter(([, sat]) => sat > 0.3).map(([h]) => h);
      if (hs.some(h => h >= 260 && h <= 320) && hs.some(h => h >= 190 && h < 260)) add("WARN", "gradient-fioletowo-niebieski", el);
    }
    const card = e => { const t = cs(e), r = e.getBoundingClientRect(); return parseFloat(t.borderTopLeftRadius) > 0 && (t.boxShadow !== "none" || parseFloat(t.borderTopWidth) > 0) && r.width > 100 && r.height > 60; };
    if (card(el)) for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) if (card(p)) { add("WARN", "karta-w-karcie", el); break; }
    const kids = [...el.children].filter(vis), groups = {}, radii = new Set();
    for (const k of kids) { const t = cs(k), r = k.getBoundingClientRect();
      if (t.boxShadow !== "none" || rgba(t.backgroundColor)[3] > 0 || parseFloat(t.borderTopWidth) > 0) {
        const g = k.className + Math.round(r.width) + "x" + Math.round(r.height); groups[g] = (groups[g] || 0) + 1;
        const rad = parseFloat(t.borderTopLeftRadius); radii.add(rad === 0 ? "0" : rad <= 8 ? "s" : "m"); } }
    if (Object.values(groups).some(n => n >= 3)) add("WARN", "≥3-identyczne-karty", el);
    if (radii.has("0") && radii.has("s")) add("WARN", "promień-0-obok-małego", el);
  }
  if (glass > 2) add("WARN", `backdrop-filter-na-${glass}-dużych-obszarach`, null);
  const DEF = ["inter", "roboto", "arial", "helvetica", "helvetica neue", "system-ui", "-apple-system", "blinkmacsystemfont", "sans-serif", "segoe ui", "times new roman", "serif"];
  if (families.size && [...families].every(f => DEF.includes(f))) add("WARN", "tylko-domyślne-fonty", null);
  if (families.size > 2) add("WARN", `${families.size}-rodziny-pisma`, null);
  const rm = rules.some(r => r.conditionText?.includes("prefers-reduced-motion") || r.media?.mediaText?.includes("prefers-reduced-motion"));
  if (motion && !rm) add("FAIL", "ruch-bez-prefers-reduced-motion", null);
  const timing = rules.filter(r => r.style).map(r => r.style.cssText).join(" ") + " " + tvals.join(" ");
  if ((timing.match(/cubic-bezier\(([^)]*)\)/g) || []).some(c => { const n = c.match(/-?[\d.]+/g).map(Number); return n[1] > 1 || n[3] > 1 || n[1] < 0 || n[3] < 0; }))
    add("WARN", "overshoot (dopuszczalny tylko z zapisem w dna.md)", null);
  // liczone per selektor: ".a:hover, .b:hover" w jednej regule to ten sam efekt na dwóch elementach
  const hov = rules.flatMap(r => (r.selectorText || "").split(",").filter(x => x.includes(":hover")).map(() => r.style.cssText.replace(/\s+/g, " ").trim()));
  if (hov.length >= 3 && new Set(hov).size === 1) add("WARN", "jeden-efekt-hover-na-wszystkim", null);
  if (hov.length >= 2 && hov.every(b => b.split(";").filter(Boolean).every(d => /^\s*(transform|opacity|translate|scale)\s*:/.test(d)))) add("WARN", "hover-tylko-transform/opacity", null);
  return out;
}

async function check(file, { dark = false, outDir = null } = {}) {
  const browser = await chromium.launch({ args: ["--allow-file-access-from-files"] }), rows = []; // bez flagi arkusze z file:// są nieczytelne (cssRules)
  try {
    for (const [w, h] of SIZES) {
      const page = await browser.newPage({ viewport: { width: w, height: h }, colorScheme: dark ? "dark" : "light" });
      await page.goto(pathToFileURL(path.resolve(file)).href);
      for (const r of await page.evaluate(audit)) rows.push([w, ...r]);
      if (outDir) {
        fs.mkdirSync(outDir, { recursive: true });
        const base = path.join(outDir, `${path.basename(file, ".html")}${dark ? "-dark" : ""}-${w}`);
        await page.screenshot({ path: `${base}.png`, fullPage: true });
        const g = await page.addStyleTag({ content: "html{filter:grayscale(1)}" });
        await page.screenshot({ path: `${base}-gray.png`, fullPage: true });
        await g.evaluate(e => e.remove());
        await page.addStyleTag({ content: "[data-logo]{visibility:hidden!important}" });
        await page.screenshot({ path: `${base}-nologo.png`, fullPage: true });
      }
      await page.close();
    }
  } finally { await browser.close(); }
  return rows;
}

const args = process.argv.slice(2);
if (args.includes("--test")) {
  const here = path.dirname(fileURLToPath(import.meta.url));
  for (const dark of [false, true]) {
    const gf = (await check(path.join(here, "..", "assets", "example.html"), { dark })).filter(r => r[1] === "FAIL");
    if (gf.length) { console.log(`example.html${dark ? " (ciemny)" : ""} ma FAIL:\n` + gf.map(r => r.join("\t")).join("\n")); process.exit(1); }
  }
  const bad = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "style-")), "bad.html");
  fs.writeFileSync(bad, `<!doctype html><html><head><style>
    :root{--c-bg:#ffffff;--c-text:#111111;--radius:8px;--shadow:0 1px 2px #0002}
    body{margin:0;background:var(--c-bg);color:var(--c-text);font-family:Inter,sans-serif}
    .wide{width:900px}.pale{color:#bbbbbb}.off{color:#c00}.track{letter-spacing:.1em}.tiny{font-size:12px;letter-spacing:-.03em}
    .card{width:200px;height:100px;border-radius:13px;box-shadow:0 9px 30px #0004;background:var(--c-bg);transition:transform .2s}
    .card:hover,.b:hover,a:hover{transform:scale(1.05)}
    .grad{background:linear-gradient(90deg,#7c3aed,#2563eb);-webkit-background-clip:text;background-clip:text;color:transparent}
    button{width:16px;height:16px}</style></head><body>
    <div class="wide">x</div><p class="pale">blady</p><p class="off">czerwony</p><p class="track">rozstrzelony</p><p class="tiny">mały</p>
    <div><div class="card">a</div><div class="card">b</div><div class="card">c</div></div><h1 class="grad">Tytuł</h1>
    <a href="#">🚀 Start</a><button class="b"></button></body></html>`);
  const got = (await check(bad)).map(r => r[2]).join("\n");
  const need = ["przewijanie-w-bok", "kolor-spoza-tokenów", "kontrast-", "tracking-0.100em", "ujemny-tracking", "promień-spoza-tokenów", "cień-spoza-tokenów",
    "ruch-bez-prefers-reduced-motion", "emoji-jako-ikona", "cel-dotykowy<24px", "gradientowy-tekst", "gradient-fioletowo-niebieski", "≥3-identyczne-karty",
    "jeden-efekt-hover", "tylko-domyślne-fonty"];
  const miss = need.filter(n => !got.includes(n));
  if (miss.length) { console.log("nie wykryto: " + miss.join(", ") + "\n---\n" + got); process.exit(1); }
  console.log("OK"); process.exit(0);
}
const file = args.find(a => !a.startsWith("--") && args[args.indexOf(a) - 1] !== "--out");
if (!file) { console.log("Użycie: node stylecheck.mjs <plik.html> [--dark] [--out <katalog>] | --test"); process.exit(2); }
const oi = args.indexOf("--out");
const rows = await check(file, { dark: args.includes("--dark"), outDir: oi >= 0 ? args[oi + 1] : null });
console.log(["szerokość", "poziom", "reguła", "element"].join("\t"));
for (const r of rows.slice(0, 60)) console.log(r.join("\t"));
const fails = rows.filter(r => r[1] === "FAIL").length;
console.log(`FAIL ${fails} · WARN ${rows.length - fails}${rows.length > 60 ? " (pokazano 60)" : ""}`);
process.exit(fails ? 1 : 0);
