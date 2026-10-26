---
name: brand
description: Marka i brandbook - strategia, identyfikacja, logo, kolory, ton; dziedziczenie marki organizacji; audyt i naprawa niespójności w kodzie.
---

# Marka: od strategii do brandbooka

Marka to nie logo. To obietnica, skojarzenia, język, wygląd produktu i zachowanie w trudnych sytuacjach. **Strategia przed designem**: nie rysuj logo, zanim etap B1 nie jest zatwierdzony.

## Jak pracujesz
Ty (główny wątek) jesteś dyrektorem kreatywnym i **jedynym, kto rozmawia z użytkownikiem**. Agenci przygotowują propozycje i pisanie; nie pytają użytkownika. Każdy etap ma tę samą pętlę:
1. **Pytaj** paczkami (`AskUserQuestion`, max 4 pytania, opcje z rekomendacją i "Inne"). Banki pytań: `references/discovery-questions.md`. Zawsze dopytaj o **inspiracje**: 3-5 marek/produktów/stron, które lubi, i 1-2, których nie znosi, z powodem. Odpowiedzi zapisz skrótowo w `discovery.md`.
2. **Deleguj** do agenta z paczką: odpowiedzi + potrzebne sekcje brandbooka.
3. **Pokaż przykłady do wyboru**, nie opisy: 2-4 warianty obok siebie. **Najpierw w Figmie** (zasady, dostęp i mapowanie etapów: `${CLAUDE_PLUGIN_ROOT}/skills/orchestrator/references/figma.md`; poproś użytkownika o podłączenie Figma MCP i link do pliku, jeśli ich brak). Poza Figmą tylko za świadomą zgodą: wizualnie (widżet wizualny, jeśli dostępny, z SVG/HTML: moodboardy, palety z próbkami, specimeny fontów, szkice logo, mockupy zastosowań; w razie braku - plik HTML/Artifact), a gdy nie ma jak, opis + HEX + linki do realnych przykładów z sieci (marki-wzorce; wyciągaj zasadę, nie kopiuj).
4. **Użytkownik wybiera / łączy / odrzuca** - decyzję i powód zapisz w `decisions.md` marki.
5. **Agent wpisuje wynik** do swoich sekcji w `brandbook.md` (konkretne wartości, nie opisy ogólne).
Oceniaj kierunki wg strategii, nie gustu (kryteria w referencji). Odrzucone opcje z powodem wpisuj, bo chronią przed powrotem do tematu.

## Skala (zapytaj na początku, oszczędza tokeny)
- **Mini:** karta marki 1-2 strony (misja, osobowość, paleta, 2 fonty, ton, zasady logo). Dla małych projektów i wydarzeń.
- **Standard:** pełne etapy B1-B6, zastosowania wybrane.
- **Pełna:** + testy użytkowników, prawo/nazwa, wdrożenie i utrzymanie.
Wymagane też: **czyja to marka** - organizacji (`~/.hq/orgs/<slug>/brand/`, skill `hq:org`) czy projektu (`.hq/brand/`). Pliki: `brandbook.md`, `discovery.md`, `decisions.md`, `assets/`, opcjonalnie `tokens.css` (tokeny dla kodu).

## Dziedziczenie: marka efektywna
Hook na starcie sesji podaje linię `[hq] Marka: tryb=... rdzeń=... profil=...`. Marka efektywna projektu =
- `dziedziczy`: brandbook organizacji (profil projektu tylko z elementami własnymi, np. nazwa produktu);
- `rozszerza`: **rdzeń** org (sekcja 0) + elastyczne org nadpisane różnicami z `.hq/brand/brand.md`;
- `odrębna-zgodna`: brandbook projektu + **zasady zgodności** z sekcji 0 org (sprawdza `design-reviewer`);
- `niezależna` lub brak org: tylko marka projektu.
Rdzenia org nie zmieniasz w projekcie: gdy projekt naprawdę go potrzebuje - przedstaw użytkownikowi opcje (zostać przy rdzeniu / tryb `odrębna-zgodna` / zmiana rdzenia dla całej org) z konsekwencjami. Agentom przekazuj ścieżki, nie treść: linia `Marka:` w paczce.
Nowy projekt w org: zaproponuj tryb (domyślny z `org.md`) i utwórz profil z `${CLAUDE_PLUGIN_ROOT}/templates/brand-profile.md` - tylko różnice, bez kopiowania brandbooka.

## Istniejące materiały
**Odtworzenie** (marka jest w praktyce, brak brandbooka): zbierz źródła (logo, strona/kod, dokumenty, social) -> `scripts/brandscan.py KATALOG --brand <plik z listą HEX>` lub bez palety, żeby zobaczyć faktycznie używane kolory i fonty (najczęstsze = kandydaci na rdzeń) -> `brand-strategist` + `brand-designer` szkicują brandbook z sekcją 0 z **tego, co już działa** (nie wymyślaj nowej marki) -> użytkownik zatwierdza rdzeń -> wersja 1.0.
**Audyt i naprawa** (marka jest, kod/materiały się rozjechały): `python3 ${CLAUDE_PLUGIN_ROOT}/skills/brand/scripts/brandscan.py <katalog> --brand <brandbook rodzica> --brand .hq/brand/brand.md [--brand tokens.css]` -> raport TSV (OBCY, DRYF, FONT_OBCY z plik:linia) -> pokaż użytkownikowi top problemy i plan -> poprawki przez `hq:frontend`/`coder` (DRYF: zamiana na token/zmienną; OBCY: decyzja: błąd czy brakujący kolor marki) -> ponowny skan jako dowód. Teksty: zgodność z sekcją 8 (głos, słownictwo) sprawdza `brand-copywriter`. Nie przepisuj masowo bez zgody; najpierw tokeny w jednym miejscu, potem odwołania.

## Etapy i bramki
| Etap | Agent | Wynik | Zatwierdza |
|---|---|---|---|
| B0 Wywiad i badania: historia, cele, produkt, klient, konkurencja, rynek, ograniczenia, obecne materiały | `brand-strategist` | `discovery.md` | - |
| B1 **Strategia**: misja, wizja, wartości, pozycjonowanie, przewaga, grupa docelowa, osobowość (skale: formalna-swobodna, ekspercka-przystępna, emocjonalna-rzeczowa), obietnica, historia | `brand-strategist` | sekcje 1-2 brandbooka | **użytkownik** |
| B2 **Kierunek kreatywny**: 2-4 moodboardy, ocena wg kryteriów, wybór lub połączenie | `brand-designer` | kierunek + moodboard | **użytkownik** |
| B3 **System wizualny**: logo (proces L0-L12 w `references/logo.md`: research, 8+ szkiców, ocena, wektor mono-first, system znaków, `scripts/logotest.py`), kolory (proces K1-K8 w `references/color.md`: strategia, mapa kategorii, role, kontrast, testy), typografia (proces T1-T10 w `references/typography.md`: role, parowanie, źródła, polskie znaki, licencja), wzory i motyw (proces W1-W8 w `references/pattern.md`: metafora, motyw z logo, system 5 warstw, skale, testy), fotografia/ilustracje/ikony/3D (proces G1-G9 w `references/imagery.md`: emocje, słownik wizualny, światło, kompozycja, retusz, stock, shot list), elementy pomocnicze | `brand-designer` | sekcje 3-7 | **użytkownik** + przegląd |
| B4 **Język**: nazwa (jeśli trzeba), hasło, narracja, głos, zasady pisania, słownictwo, przykłady komunikatów | `brand-copywriter` | sekcja 8 | **użytkownik** |
| B5 **Zastosowania**: test w realnych kanałach (pokaż mockupy wg `references/imagery.md`: realistyczne, bez ozdobników): www/aplikacja, social, e-mail, prezentacje, druk, opakowanie, **produkt i interfejs urządzenia**, obsługa klienta | `brand-designer` + `brand-copywriter` | sekcja 9, poprawki | **użytkownik** |
| B6 **Brandbook**: kompilacja, szybki start, zasady techniczne, przegląd kompletności | wszyscy + `hq:design-reviewer` | `brandbook.md` v1.0 | **użytkownik** |
| B7 Wdrożenie (Pełna/Standard): biblioteka zasobów, szablony, instrukcje, właściciel marki | `brand-designer` | `assets/`, szablony | - |
| B8 Utrzymanie: przegląd co ~6-12 mies., kryteria odświeżenia vs rebrandingu | `brand-strategist` | wpis w historii zmian | - |
Nie przechodź do kolejnego etapu bez zatwierdzenia bramki (zapis w `decisions.md`). Zmiana strategii po B3 = powrót do B1 i ocena wpływu na sekcje 3-9.

## Obowiązkowy zestaw przy tworzeniu nowej marki
Nowy branding (Standard/Pełna; w Mini: pozycje 1-7) **musi** dostarczyć wszystkie pozycje; brak którejś = brandbook niegotowy, chyba że użytkownik świadomie ją wykreślił (zapis w `decisions.md`).
B3 (system wizualny): 1. primary logo, 2. logomark (sygnet), 3. logo clearspace (pole ochronne + minimalny rozmiar), 4. primary typeface, 5. typeface hierarchy (H1-H6, body, caption: rozmiar/interlinia/waga), 6. color palette (role, HEX/RGB/CMYK), 7. brand imagery (kierunek zdjęć/ilustracji wg `references/imagery.md`), 8. graphic patterns (system wzorów wg `references/pattern.md`).
B5 (zastosowania, jako mockupy): 9. social media creatives, 10. social media page banners, 11. brand mockups (ogólne: www/app/druk/opakowanie), 12. business card, 13. brand billboard, 14. brand merch, 15. conference display (roll-up/ścianka/stoisko).

## Definicja gotowości brandbooka
Treść: `templates/brandbook.md`. **Forma (slajdy w Figmie, 15 ramek o jednym układzie: tytuł 2-liniowy, opis, zaokrąglony panel):** `${CLAUDE_PLUGIN_ROOT}/templates/brandbook-slides.md`. Gotowy, gdy: dostarczony cały zestaw obowiązkowy (15 pozycji wyżej) w pliku Figma z linkiem w brandbooku (tokeny jako zmienne Figmy), każda sekcja ma **konkretne wartości** (HEX/RGB/CMYK, rozmiary, pola ochronne, wielkości fontów, przykłady zdań), przykłady **poprawne i błędne**, kontrasty sprawdzone (`scripts/contrast.py`), dla marki organizacji wypełniona sekcja 0 (rdzeń / elastyczne / zgodność), logo przetestowane (`references/logo.md` L10, `scripts/logotest.py` bez BLAD), lista kontroli prawnej logo jako DO WERYFIKACJI, licencje fontów opisane, wersja i data, właściciel marki, sekcja "Szybki start" (logo, kolory, fonty na jednej stronie). Czego nie da się ustalić bez specjalisty (znak towarowy, Pantone, druk CMYK), oznacz jako **DO WERYFIKACJI**, nie zgaduj.

## Powiązania
Kampanie i promocja z użyciem marki: `hq:marketing`; sponsorzy i partnerzy: `hq:partnerships`.
Marka zasila `industrial-designer` (feeling i feedback produktu, `hq:product`), estetykę PCB/obudowy i komunikaty urządzenia. Po zatwierdzeniu dopisz ścieżkę brandbooka do `.hq/context.md`.
