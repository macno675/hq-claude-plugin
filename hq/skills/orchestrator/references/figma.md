# Figma: miejsce projektowania

Reguła dla każdej pracy z wyglądem: **marka, logo, kolory, typografia, grafika, ekrany, mockupy, materiały reklamowe, slajdy, diagramy.** Figma jest domyślnym miejscem projektowania; HTML/SVG to zapas, nie pierwszy wybór.

## 1. Zanim zaczniesz projektować (główny wątek, raz na projekt)
1. **Sprawdź dostęp:** czy są narzędzia Figma MCP (`use_figma`, `get_design_context`, `get_screenshot`...) i skille `figma:*`. Odczytaj wpis `Figma:` w `.hq/context.md` - jeśli jest, nie pytaj ponownie.
2. **Brak narzędzi = poproś użytkownika o podłączenie** (nie możesz sam rozpocząć logowania): wtyczka Figma w Claude Code (`/plugin`) albo serwer MCP Figma, potem autoryzacja przez `/mcp`. Poczekaj na potwierdzenie.
3. **Poproś tylko o to, co niezbędne** (`AskUserQuestion`, jedna paczka): link do pliku/projektu Figma albo zgoda na nowy plik (w jakim zespole/planie); czy jest biblioteka lub istniejący plik marki; dostęp z prawem edycji; źródła, których nie wygenerujesz (oryginalne logo, licencjonowane fonty, zdjęcia produktu).
4. **Nigdy nie proś o tokeny, hasła ani klucze w rozmowie.** Jeśli użytkownik ma tylko token REST, niech wpisze go sam do zmiennej środowiskowej; do pracy wystarcza autoryzowany MCP.
5. Zapisz wynik: `Figma: <URL pliku> · biblioteka: <tak/nie>` w `.hq/context.md` (Klucz). Odmowa lub brak planu = świadoma decyzja w `decisions.md` ("projekt poza Figmą, bo ..."), dopiero wtedy HTML/SVG; w deliverable oznacz "poza Figmą, do przeniesienia".

## 2. Co robić w Figmie (robi to tylko główny wątek)
Przed każdym `use_figma` wczytaj skill `figma:figma-use`. Agenci `hq:*` nie mają narzędzi Figma i nie rozmawiają z użytkownikiem: dają specyfikację (tokeny, treści, struktury, wartości), a **główny wątek buduje ją w Figmie** i wraca z linkiem i zrzutem.

| Praca | Gdzie w Figmie | Skill |
|---|---|---|
| moodboardy, kierunki (B2 marki) | osobna strona na kierunek, ramki z paletą, typografią, odniesieniami | `figma:figma-use` |
| system wizualny (B3): logo, kolory, typografia | zmienne (tokeny), style, ramki logo z clearspace; biblioteka | `figma:figma-generate-library` |
| zastosowania (B5): social, banery, wizytówka, billboard, merch, stoisko | ramki w docelowych rozmiarach, mockupy | `figma:figma-generate-design` |
| wireframe'y i ekrany (U3, U4) | ekrany ze wszystkimi stanami, komponenty z wariantami | `figma:figma-generate-design` |
| diagramy, przepływy, ścieżki | FigJam | `figma:figma-generate-diagram`, `figma:figma-use-figjam` |
| prezentacje | Figma Slides | `figma:figma-use-slides` |
| handoff do kodu | Dev Mode, Code Connect, `get_design_context` | `figma:figma-design-to-code`, `figma:figma-code-connect` |
| istniejący projekt | najpierw czytaj: `get_design_context`, `get_variable_defs`, `get_screenshot`, `search_design_system`; używaj komponentów i zmiennych, które już są | - |

Figma jest źródłem prawdy dla wyglądu; `tokens.css` i `brandbook.md` zawierają link do pliku i są z niego generowane (nie odwrotnie).

## 3. Bezpieczeństwo pracy
- Przed pierwszym zapisem potwierdź docelowy plik; w cudzym lub istniejącym pliku twórz nową stronę, nie nadpisuj i nie usuwaj istniejącej pracy bez zgody.
- Po każdym etapie pokaż zrzut (`get_screenshot`) i link; użytkownik zatwierdza bramkę w Figmie lub w rozmowie.
- Czego Figma nie rozstrzyga: Pantone i CMYK do druku, znak towarowy, licencje fontów - oznacz **DO WERYFIKACJI**. Zdjęcia i ilustracje rastrowe: wstaw wygenerowane lub dostarczone (`generate_image`, `upload_assets`), nie udawaj ich wektorami.

Brandbook jako slajdy: układ i kolejność 15 ramek w `<katalog hq>/templates/brandbook-slides.md` (ten sam układ dla każdej marki).
