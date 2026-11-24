# Trendy z warunkami - dla `ui-designer`

Trend wchodzi tylko, gdy: (1) wynika z idei lub osobowości w `dna.md`, nie z mody; (2) kontrast policzony na najgorszym tle; (3) koszt wydajności znany na słabym telefonie; (4) jest wersja awaryjna; (5) szanuje preferencje systemu. Inaczej zapisz rezygnację w `decisions.md`. Źródłem różnorodności są soczewki (`dna.md`), nie ta lista.

## Szkło i translucencja („liquid glass”)
Kiedy: warstwa sterująca nad przewijaną treścią (pasek, toolbar, arkusz), gdy idea dotyczy warstw, światła lub kontekstu pod spodem. Nie: tło kart, treść, tekst ciągły, formularze.
Reguły: nigdy szkło na szkle · bez barwienia elementów na szkle poza główną akcją · ≤2 duże obszary blur na widok · nie animuj `blur` · kontrast liczony na najjaśniejszym i najciemniejszym fragmencie treści pod spodem (dodaj warstwę przyciemnienia/rozjaśnienia, jeśli trzeba).
Fallback (web): `@supports not (backdrop-filter: blur(1px))` -> półprzezroczyste jednolite tło; `@media (prefers-reduced-transparency: reduce)` i `(prefers-contrast: more)` -> tło nieprzezroczyste. Platformy Apple: szanuj Reduce Transparency i Increase Contrast.

## Ciemny motyw
Kiedy: wymaga go platforma lub kontekst (wieczór, media, narzędzia długiej pracy). Wyprowadzony, nie odwrócony (`craft.md`); osobny przegląd kontrastu i zrzutów (`stylecheck --dark`).

## Typografia zmienna i duża skala
Kiedy: idea redakcyjna lub typograficzna. Oś `wght`/`opsz` zamiast kilku plików; reakcje typograficzne (`motion.md`). Koszt: rozmiar fontu (subset, `font-display: swap`), polskie znaki.

## Siatka bento
Kiedy: treść naprawdę ma różne wagi (różne rozmiary pól wynikają z priorytetów P1-P3 z `hq:views`). Nie: jako domyślny układ kart funkcji (≥3 identyczne pola = flaga).

## Ruch przy przewijaniu (scroll-driven)
Kiedy: opowieść krok po kroku, wynikająca z kolejności decyzji z makiety. CSS `animation-timeline` z `@supports` i wersją statyczną; reduced-motion = brak. Nie: na każdej sekcji, na tekście do czytania.

## Elementy odręczne, ziarno, tekstura
Kiedy: soczewka materiału lub rzemiosła w DNA. Tekstura w tle o niskim kontraście, nie pod tekstem; obraz jako plik lub CSS, nie ciężki filtr SVG na całej stronie.

## Odrzucone jako domyślne
Neumorfizm (kontrast elementów UI <3:1) · glassmorfizm na kartach · gradientowe „aurory” i glow jako znak „AI” · kursory niestandardowe (tylko z idei i bez utraty dostępności) · 3D/WebGL bez budżetu złożoności.
