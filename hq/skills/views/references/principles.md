# Zasady: psychologia, mobile-first, SEO, dostępność struktury

Zasada to narzędzie do uzasadnienia bloku, nie ozdoba. W specyfikacji podaj ją przy decyzji, którą wyjaśnia. Liczby od autorów filmów i blogów = `[ZAŁOŻENIE]`.

## Psychologia i prawa UX
| Zasada | Co znaczy w makiecie | Dowód | Nadużycie |
|---|---|---|---|
| Top tasks | najważniejsze zadanie ma najkrótszą ścieżkę i najbardziej widoczne miejsce | wysoki (NN/g) | „Rezerwuj” wszędzie, zanim użytkownik ma podstawy do decyzji |
| Obciążenie poznawcze | mniej równorzędnych decyzji, pól i elementów naraz; grupowanie | wysoki (NN/g) | chowanie kosztów i warunków „żeby było czysto” |
| Stopniowe ujawnianie | podstawy od razu, szczegóły pod „więcej”, akordeonem lub w kolejnym kroku | wysoki (NN/g) | krytyczna informacja (cena końcowa, anulowanie) jako „zaawansowane” |
| Fitts | główna akcja duża i blisko; na telefonie w zasięgu kciuka | wysoki | wszystko duże = nic nie jest główne |
| Hick | mniej równorzędnych opcji = szybsza decyzja; dziel długie procesy na kroki | średni | sztuczne limity („max 5 pozycji”) bez związku z zadaniem |
| Jakob | znane wzorce nawigacji, formularzy, kart, koszyka | wysoki jako zasada | kopiowanie wzorca, który nie pasuje do zadania |
| Bliskość i wspólny obszar | co razem działa, stoi razem lub we wspólnym tle | wysoki (Gestalt) | grupowanie wg działów firmy, nie zadań |
| Hierarchia | ≤3 poziomy wielkości; najwyższy kontrast = główna akcja (widoczne już w szarościach) | średni/wysoki (NN/g) | 5 rozmiarów nagłówków |
| Pozycja szeregowa | ważne na początku i końcu listy/menu | średni | CTA tylko na końcu długiej strony |
| Dowód społeczny, autorytet | opinie, certyfikaty, liczby obok decyzji, którą wspierają | średni, zależy od wiarygodności | fałszywe liczniki, wymyślone opinie |
| Szczyt i koniec | potwierdzenie i ostatni krok mają być jasne i spokojne | średni | — |
| Ślepota banerowa | nic kluczowego w prawej kolumnie bocznej ani w miejscach jak reklama | średni (NN/g, eyetracking) | — |
| Wzorzec F/Z | opis skanowania, nie reguła rozmieszczenia | niski jako reguła | stawianie CTA „bo F” |
| 7±2 (Miller) | dotyczy pamięci roboczej, nie liczby elementów na ekranie | — | limit elementów menu „bo Miller” |
**Zakazane (dark patterns):** fałszywa pilność i niedobór („ostatnie 2 pokoje” bez danych), ukryte opłaty dodane na końcu, trudne anulowanie, zaznaczone domyślnie zgody i dodatki, wabik cenowy w pakietach, zawstydzanie przy odmowie.

## Mobile-first
1. Projekt zaczyna się od 360-390 px: nad zgięciem kontekst (co to, gdzie), główna wartość i jedna akcja.
2. Jeden widok = jeden główny cel; akcje drugorzędne wyraźnie niżej w hierarchii.
3. Przyklejony pasek akcji (np. termin + cena od + „Sprawdź dostępność”) tylko gdy pomaga w zadaniu i nie zasłania pól ani treści; do sprawdzenia testem.
4. Cele dotykowe: projektowo ≥44×44 px (Apple) / 48 dp (Material); minimum WCAG 2.2 AA (2.5.8) to 24×24 px lub odstęp. Odstępy między celami.
5. Długie, wielowątkowe strony: sekcje w akordeonach rozwijanych w miejscu (opis, udogodnienia, zasady); spis zawartości widoczny wcześnie.
6. Formularze w krokach (np. termin i osoby -> wybór -> dane -> podsumowanie i płatność), właściwe typy klawiatury, autouzupełnianie.
7. Wyszukiwanie i filtry: jawne „Szukaj” i „Zastosuj”, wyjście z filtrów, liczba wyników.
8. Nic tylko na hover. Nawigacja pokazuje bieżące miejsce.
9. Desktop nie rozciąga mobile: kolumny dla porównań, więcej kontekstu, bez nowych zadań bez powodu.
10. Kolejność projektowania zależy od danych: przy decyzjach złożonych (B2B, porównania) desktop bywa ważniejszy - projektuj oba równolegle, priorytet treści nadal od mobile.

## SEO w architekturze (`seo.md`)
- Jedna strona = jeden temat i grupa bliskich intencji; synonimy na tej samej stronie, nie osobne podstrony (kanibalizacja).
- Strony pod miasta/atrakcje tylko z unikalną treścią lokalną; nie kopiuj stron ze zmienioną nazwą miasta.
- URL proste, stałe, małymi literami, z myślnikami; wzorce dla przyszłych sekcji i języków (`/en/...`) od początku.
- Każda ważna strona osiągalna linkiem `<a href>` z opisowym tekstem (Google nie podąża za przyciskami JS); linkuj do naturalnego następnego kroku, nie „wszystko ze wszystkim”; strony usług/ofert i lokalizacji linkują się wzajemnie.
- Nagłówki jako struktura treści: jeden `h1` na stronę, `h2` sekcji, `h3` podsekcji.
- FAQ przy stronie, której dotyczy (pytania o tę ofertę/usługę), zamiast jednej zbiorczej podstrony; FAQ ogólne (dojazd, zwierzęta) może zostać. Wyniki rozszerzone FAQ Google ogranicza od 2023 do stron rządowych i medycznych - FAQ dla ludzi, nie dla gwiazdek.
- schema.org per typ strony (JSON-LD, wdraża `hq:frontend`): `LocalBusiness`/`LodgingBusiness`/`Hotel`, `Product`+`Offer`, `BreadcrumbList`, `Organization`/`WebSite`; tylko dane widoczne na stronie.
- Lokalnie: kanoniczna strona kontaktu/dojazdu z adresem, mapą, godzinami, telefonem; spójne z wizytówką Google.
- Frazy i trudność sprawdza `hq:marketing` (`marketing:seo-audit`) przed treściami; w makiecie tylko intencje.
Źródła: developers.google.com/search/docs (url-structure, links-crawlable, structured-data/local-business), nngroup.com, baymard.com (stan 2024-2026, odczyt przez Perplexity; przy decyzji otwórz).

## Dostępność struktury (w makiecie, nie po fakcie)
Landmarki `header`/`nav`/`main`/`footer`; kolejność fokusu = kolejność czytania; każdy element interaktywny osiągalny klawiaturą; pola z `label`, nie tylko placeholder; ikony z nazwą; miejsce na komunikaty błędu i statusu przy polu i na górze formularza; „Przejdź do treści” na stronach z długą nawigacją.
