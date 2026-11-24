# AI slop: lista, FAIL i flagi (Y7) - dla `ui-designer`, `hq:design-reviewer`, `frontend-engineer`

Slop = poprawne, ale generyczne: decyzje domyślne zamiast autorskich. Przyczyna: model dostaje funkcję, nie ideę i system. Leczenie: `dna.md` przed formą, nie dłuższy prompt.

## FAIL (`stylecheck`, blokuje)
Kontrast tekstu <4,5:1 (duży <3:1) · kolor, promień lub cień spoza tokenów `:root` bez `data-style-exception` · brak tokenów · `transition`/`animation` bez reguły `prefers-reduced-motion` · emoji jako ikona w przycisku/linku · tracking >0,02em na tekście ciągłym lub <0 na tekście <16 px · przewijanie w bok · cel dotykowy <24 px.

## Flagi (`stylecheck` WARN, do oceny człowieka, nie blokują)
Domyślny font jako jedyny (Inter, Roboto, Arial, Helvetica, system-ui) · >2 rodziny pisma · gradient fioletowo-niebieski · gradientowy tekst · `backdrop-filter` na >2 dużych obszarach lub animowany · ≥3 identyczne karty obok siebie · karta w karcie · 0 i mały promień w sąsiednich elementach · jeden efekt hover na wszystkim lub hover tylko transform/opacity · overshoot bez zapisu w DNA · `linear` poza postępem · tracking wersalików >0,12em.

## Do oka (autoprzegląd i krytyk)
Hero „nagłówek + podtytuł + dwa przyciski + mockup” bez powodu z idei · ikony z jednego pakietu w kółkach · stockowe SVG-bohaterowie · glow i miękkie gradienty jako „AI-owość” · te same odstępy wszędzie, bez rytmu · >50% sekcji tej samej konstrukcji · ramki wokół wszystkiego · nasycony akcent na kilku akcjach naraz · tekst marketingowy bez głosu marki · charakter tylko w hero (formularz i pusty stan generyczne) · „czy to pasuje do dowolnej marki z branży?” = tak.
Dwa lub więcej trafień z tej sekcji = ćwiczenie presji (`critique.md`) i powrót do Y5/Y6; brak idei = powrót do Y1.

Logo i znaki: osobna lista w `brand/references/logo.md` L4a.
