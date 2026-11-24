// Kontrola szarej makiety hq:views na 360/768/1280 px + zrzuty.
// Użycie (z katalogu projektu z Playwright): node wirecheck.mjs <makieta.html> [--app] [--out <katalog>]   |   --test
// Wyjście: TSV "szerokość poziom reguła element"; kod 1 = jest FAIL, 3 = brak Playwright.
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath, pathToFileURL } from "node:url";

let chromium;
try { ({ chromium } = createRequire(path.join(process.cwd(), "x.js"))("playwright")); }
catch { try { ({ chromium } = await import("playwright")); } catch { console.log("brak Playwright w projekcie: npm i -D playwright && npx playwright install chromium"); process.exit(3); } }

const SIZES = [[360, 780], [768, 1024], [1280, 800]];

function audit(app) { // działa w przeglądarce
  const out = [], seen = new Set();
  const add = (lvl, rule, el) => {
    const d = el ? `${el.tagName.toLowerCase()}${el.id ? "#" + el.id : ""}${el.dataset?.block ? "[" + el.dataset.block + "]" : ""} ${(el.textContent || "").trim().slice(0, 30)}` : "-";
    const k = lvl + rule + d; if (!seen.has(k)) { seen.add(k); out.push([lvl, rule, d]); }
  };
  const vis = el => { const r = el.getBoundingClientRect(), s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== "hidden"; };
  const W = innerWidth, H = innerHeight, mobile = W < 768;
  if (document.documentElement.scrollWidth > W + 1) add("FAIL", "przewijanie-w-bok", null);
  for (const el of document.querySelectorAll("body *")) {
    const s = getComputedStyle(el);
    for (const c of [s.color, s.backgroundColor, s.borderTopColor]) {
      const m = c.match(/[\d.]+/g); if (!m) continue;
      const [r, g, b, a = 1] = m.map(Number);
      if (+a > 0 && Math.max(r, g, b) - Math.min(r, g, b) > 8) { add("FAIL", "kolor-poza-szarością", el); break; }
    }
  }
  for (const el of document.querySelectorAll("a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button]")) {
    if (!vis(el) || getComputedStyle(el).display === "inline") continue; // linki w tekście: wyjątek WCAG 2.5.8
    const r = el.getBoundingClientRect(), m = Math.min(r.width, r.height);
    if (m < 24) add("FAIL", "cel-dotykowy<24px", el); else if (mobile && m < 44) add("WARN", "cel-dotykowy<44px", el);
  }
  for (const el of document.querySelectorAll("input:not([type=hidden]):not([type=submit]):not([type=button]), select, textarea"))
    if (!(el.labels?.length || el.getAttribute("aria-label") || el.getAttribute("aria-labelledby"))) add("FAIL", "pole-bez-etykiety", el);
  const hs = [...document.querySelectorAll("h1,h2,h3,h4,h5,h6")].filter(vis);
  const h1 = hs.filter(h => h.tagName === "H1").length;
  if (!app && h1 !== 1) add("FAIL", `h1=${h1} (strona: dokładnie 1)`, null);
  hs.forEach((h, i) => { if (i && +h.tagName[1] > +hs[i - 1].tagName[1] + 1) add("WARN", "przeskok-nagłówka", h); });
  if (!document.querySelector("main")) add("FAIL", "brak-main", null);
  if (!document.querySelector("nav")) add("WARN", "brak-nav", null);
  for (const el of document.querySelectorAll("[data-nav]")) if (!el.matches("a[href]")) add("FAIL", "nawigacja-nie-jako-a-href", el);
  const blocks = [...document.querySelectorAll("[data-block]")];
  if (!blocks.length) add("WARN", "brak-data-block", null);
  for (const b of blocks) if (!b.dataset.p || !b.dataset.why) add("FAIL", "blok-bez-data-p/why", b);
  const area = b => { const r = b.getBoundingClientRect(); return r.width * r.height; };
  const p1 = Math.max(0, ...blocks.filter(b => b.dataset.p === "1" && vis(b)).map(area));
  for (const b of blocks) if (b.dataset.p === "3" && vis(b) && p1 && area(b) > p1) add("WARN", "P3-większy-niż-P1", b);
  for (const el of document.querySelectorAll(".w-img")) if (!el.dataset.l) add("WARN", "obraz-bez-etykiety", el);
  const cta = [...document.querySelectorAll("[data-cta=primary]")].filter(vis);
  if (!cta.length) add("WARN", "brak-głównego-CTA (podaj powód w qa.md)", null);
  if (new Set(cta.map(c => c.dataset.action || c.textContent.trim())).size > 1) add("WARN", "kilka-różnych-głównych-akcji", null);
  if (mobile && cta.length) {
    const pinned = c => { for (let e = c; e; e = e.parentElement) if (/fixed|sticky/.test(getComputedStyle(e).position)) return true; return false; };
    const first = cta.some(c => pinned(c) || c.getBoundingClientRect().top + scrollY < H);
    if (!first) add("WARN", "główne-CTA-poza-1.-ekranem-bez-paska", cta[0]);
  }
  return out;
}

async function check(file, { app = false, outDir = null } = {}) {
  const browser = await chromium.launch(), rows = [];
  try {
    for (const [w, h] of SIZES) {
      const page = await browser.newPage({ viewport: { width: w, height: h } });
      await page.goto(pathToFileURL(path.resolve(file)).href);
      for (const r of await page.evaluate(audit, app)) rows.push([w, ...r]);
      if (outDir) { fs.mkdirSync(outDir, { recursive: true }); await page.screenshot({ path: path.join(outDir, `${path.basename(file, ".html")}-${w}.png`), fullPage: true }); }
      await page.close();
    }
  } finally { await browser.close(); }
  return rows;
}

const args = process.argv.slice(2);
if (args.includes("--test")) {
  const here = path.dirname(fileURLToPath(import.meta.url));
  const good = await check(path.join(here, "..", "assets", "example.html"));
  const gf = good.filter(r => r[1] === "FAIL");
  if (gf.length) { console.log("example.html ma FAIL:\n" + gf.map(r => r.join("\t")).join("\n")); process.exit(1); }
  const bad = path.join(fs.mkdtempSync(path.join(os.tmpdir(), "wire-")), "bad.html");
  fs.writeFileSync(bad, `<!doctype html><html><body><div style="width:900px;color:#c00">x</div><div data-nav onclick="">Menu</div>
    <input id="q"><button style="width:16px;height:16px"></button><section data-block="BLOCK-X">x</section><h2>a</h2><h4>b</h4></body></html>`);
  const got = new Set((await check(bad)).map(r => r[2]));
  const need = ["przewijanie-w-bok", "kolor-poza-szarością", "nawigacja-nie-jako-a-href", "pole-bez-etykiety", "cel-dotykowy<24px", "blok-bez-data-p/why", "h1=0 (strona: dokładnie 1)", "brak-main", "przeskok-nagłówka"];
  const miss = need.filter(n => !got.has(n));
  if (miss.length) { console.log("nie wykryto: " + miss.join(", ")); process.exit(1); }
  console.log("OK"); process.exit(0);
}
const file = args.find(a => !a.startsWith("--") && args[args.indexOf(a) - 1] !== "--out");
if (!file) { console.log("Użycie: node wirecheck.mjs <makieta.html> [--app] [--out <katalog>] | --test"); process.exit(2); }
const oi = args.indexOf("--out");
const rows = await check(file, { app: args.includes("--app"), outDir: oi >= 0 ? args[oi + 1] : null });
console.log(["szerokość", "poziom", "reguła", "element"].join("\t"));
for (const r of rows.slice(0, 60)) console.log(r.join("\t"));
const fails = rows.filter(r => r[1] === "FAIL").length;
console.log(`FAIL ${fails} · WARN ${rows.length - fails}${rows.length > 60 ? " (pokazano 60)" : ""}`);
process.exit(fails ? 1 : 0);
