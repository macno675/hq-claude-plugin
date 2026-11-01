// Użycie: node visual-render.mjs <szablon.html> <brief.json> <wyjście-bez-rozszerzenia> [--pdf]
// brief.json: {width, height, ...pola}; tokeny z brand/tokens.json (cwd) trafiają do zmiennych CSS --<grupa>-<nazwa>.
// Szablon: element #artboard, pola treści jako data-field="<klucz>".
import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { chromium } from "playwright";

const [tpl, briefPath, outBase] = process.argv.slice(2).filter(a => !a.startsWith("--"));
if (!tpl || !briefPath || !outBase) throw new Error("Użycie: visual-render.mjs <szablon.html> <brief.json> <wyjście> [--pdf]");
const brief = JSON.parse(await fs.readFile(briefPath, "utf8"));
const tokens = JSON.parse(await fs.readFile("brand/tokens.json", "utf8").catch(() => "{}"));
for (const k of ["width", "height"]) if (!Number.isInteger(brief[k]) || brief[k] <= 0) throw new Error(`brief.${k}`);

await fs.mkdir(path.dirname(path.resolve(outBase)), { recursive: true });
const browser = await chromium.launch();
try {
  const page = await browser.newPage({ viewport: { width: brief.width, height: brief.height } });
  await page.emulateMedia({ media: "screen", reducedMotion: "reduce" });
  await page.goto(pathToFileURL(path.resolve(tpl)).href);
  const issues = await page.evaluate(async ({ brief, tokens }) => {
    const root = document.documentElement.style;
    for (const [g, vals] of Object.entries(tokens))
      for (const [n, v] of Object.entries(vals)) root.setProperty(`--${g}-${n}`, typeof v === "number" ? `${v}px` : v);
    const art = document.querySelector("#artboard");
    art.style.width = `${brief.width}px`; art.style.height = `${brief.height}px`;
    for (const n of document.querySelectorAll("[data-field]")) n.textContent = brief[n.dataset.field] ?? "";
    await document.fonts.ready;
    await Promise.all([...document.images].map(i => i.decode()));
    const b = art.getBoundingClientRect();
    return [...art.querySelectorAll("[data-field]")].filter(n => {
      const r = n.getBoundingClientRect();
      return n.scrollWidth > n.clientWidth + 1 || n.scrollHeight > n.clientHeight + 1 ||
        r.left < b.left || r.top < b.top || r.right > b.right || r.bottom > b.bottom;
    }).map(n => `poza artboardem: ${n.dataset.field}`);
  }, { brief, tokens });
  if (issues.length) throw new Error(issues.join("\n"));
  await page.locator("#artboard").screenshot({ path: `${outBase}.png`, animations: "disabled" });
  if (process.argv.includes("--pdf"))
    await page.pdf({ path: `${outBase}.pdf`, width: `${brief.width}px`, height: `${brief.height}px`, printBackground: true });
} finally {
  await browser.close();
}
