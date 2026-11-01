# Wizualizacje i grafika: HTML/SVG + Playwright

Reguła dla każdej pracy z wyglądem: **marka, logo, kolory, typografia, grafika, ekrany, mockupy, materiały reklamowe, slajdy, diagramy, wykresy.** Domyślnie: lokalne **HTML/CSS/SVG renderowane Playwrightem**, jeden plik tokenów, kontrola wyniku po zrzucie. Figma/Canva/MCP tylko gdy użytkownik tego wymaga (sekcja 5). Powód: CLI jest tańsze w kontekście niż serwery MCP, wynik jest w git, poprawka to mały patch.

## 1. Zanim zaczniesz (główny wątek, raz na projekt)
1. Odczytaj wpis `Wizualia:` w `.hq/context.md`; jeśli jest, nie pytaj ponownie.
2. Sprawdź `node --version` i `npx playwright --version`. Brak: zaproponuj i po zgodzie `npm i -D --save-exact playwright && npx playwright install chromium` w katalogu projektu (pobiera ok. 150 MB); zapisz wersje w `.hq/context.md`.
3. Tokeny marki w jednym pliku `brand/tokens.json` (kolory, fonty, odstępy, promienie), generowane z brandbooka; HTML czyta je jako zmienne CSS. Nie wpisuj kolorów na sztywno.
4. Fonty: lokalne pliki + `@font-face`; test `Zażółć gęślą jaźń — Łódź` przed pierwszym renderem; licencje **DO WERYFIKACJI**.
5. Zapisz: `Wizualia: HTML/SVG+Playwright · tokeny: brand/tokens.json` w `.hq/context.md` (Klucz).

## 2. Wybór silnika (jeden na zadanie)
| Praca | Silnik | Wyjście |
|---|---|---|
| ekrany, makiety UI, social, slajdy, brandbook ekranowy | HTML/CSS (+ szablon i JSON z treścią) | PNG, PDF |
| logo, znaki, ikony, proste diagramy | ręczne SVG (bez `foreignObject`, zewnętrznych zależności) | SVG, PNG |
| diagramy procesów i architektury | Mermaid CLI (`mmdc`) | SVG, PNG |
| wykresy | jedna biblioteka (Chart.js lub ECharts; D3 dla nietypowych); dane z CSV/JSON czytane skryptem, nie przepisywane przez model | SVG, PNG |
| prezentacja edytowalna | pptxgenjs / python-pptx tylko na żądanie; zrzut w PPTX to nie edytowalny slajd | PPTX |
| druk wielostronicowy | Typst lub PDF z Chromium (kandydat, sprawdź) | PDF |
| zdjęcia, ilustracje rastrowe | generator obrazów jako materiał poglądowy; logo zawsze z wektora | PNG |

Seria powtarzalnych materiałów: szablon HTML + `brief.json` (treść i wariant, bez współrzędnych). Nowy layout rób raz w HTML, kolejne z JSON.

## 3. Pętla pracy
1. Brief i tokeny, istniejący szablon jeśli pasuje.
2. Zmieniaj dane lub mały fragment CSS, nie cały plik.
3. Render: `node <katalog hq>/templates/visual-render.mjs <szablon.html> <brief.json> <wyjście-bez-rozszerzenia>` (PNG; flaga `--pdf` dodaje PDF). Skrypt sprawdza wyjście elementów poza artboard i kończy się błędem.
4. **Otwórz PNG (Read) i oceń**: hierarchia, wyrównanie, kontrast (`contrast.py`), ucięcia, polskie znaki. Bez obrazu nie pisz, że sprawdziłeś wizualnie.
5. Poprawiaj tylko znalezione problemy; max 2 rundy, potem decyzja człowieka. Pokaż zrzut i ścieżki plików.
Agenci `hq:*` (ui-designer, brand-designer, frontend-engineer) mogą renderować sami; dają ścieżki i błędy, nie base64 ani cały DOM.

## 4. Pułapki
- Fallback fontu: czekaj na `document.fonts.ready` (skrypt to robi), porównuj zrzut.
- Łamanie tekstu zależy od przeglądarki i fontów: przypnij wersję Playwright, viewport i skalę.
- SVG do wymiany: master z tekstem, wersja dystrybucyjna logo jako krzywe; testuj w docelowym programie.
- PDF sprawdzaj osobno (media, marginesy, tła), nie tylko PNG; "wektorowy" tylko po kontroli.
- Nie naprawiaj przepełnienia samym zmniejszaniem fontu; skróć treść lub zmień układ.
- Logo optycznie trudne (krzywe): lokalny edytor wektorowy, kod jako punkt startu.

## 5. Kiedy Figma lub inne MCP
Tylko gdy: istnieje biblioteka komponentów w Figmie, plik musi edytować projektant bez kodu, klient wymaga pliku Figma, albo trzeba współpracy z komentarzami. Wtedy kod jest źródłem, Figma końcowym przekazaniem (`figma:figma-code-workflows` lub `html_to_figma`); przed `use_figma` wczytaj `figma:figma-use`; w cudzym pliku twórz nową stronę, nie nadpisuj. Zapisz powód w `decisions.md`. Pantone/CMYK, znak towarowy i licencje fontów zawsze **DO WERYFIKACJI**.

Brandbook jako slajdy: układ 15 ramek w `<katalog hq>/templates/brandbook-slides.md` (ten sam układ dla każdej marki).
