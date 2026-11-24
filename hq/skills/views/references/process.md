# Widoki: etapy i szablony (dla `ux-designer`)

Katalog pracy: `.hq/views/`. Format: Markdown dla opisu, TSV dla list. ID: `VIEW-<NAZWA>`, `BLOCK-<NAZWA>`, `FLOW-<NAZWA>`, `TASK-<NAZWA>` (wielkie litery, myślniki); te same ID w specyfikacji, makiecie (`data-block`) i uwagach, żeby zmiana jednego miejsca pokazała, co jeszcze poprawić.

## V0 Wejście (`brief.md`, część 1)
Fundament z plików projektu (`.hq/product/`, `.hq/ux-ui/problem.md`, architektura), nie z pamięci: problem, odbiorcy i kontekst (urządzenie, pośpiech, stres), zakres funkcji, model biznesowy, dane, jakie system naprawdę ma (cena, dostępność, opinie, konto, płatność), ograniczenia techniczne i prawne, platformy, docelowy framework (jeśli znany - wpływa na wzorce nawigacji). Ruch mobile/desktop z analityki lub branży; brak = `[ZAŁOŻENIE]`. Typ i profil z `profiles.md`. Czegoś brakuje: status `blocked`, ≤4 pytania z rekomendacją.

## V1 Cele (`brief.md`, część 2)
- **Top tasks** (≤10): `TASK-ID | zadanie | kto | waga (częstość lub wartość) | miara sukcesu`.
- **Cel biznesowy** i jedna miara (np. odsetek rezerwacji bez telefonu).
- **Pytania i obawy w kolejności decyzji** (mapa pytań): etap -> pytanie użytkownika -> co musi zobaczyć, żeby iść dalej. Z tego wynika kolejność bloków.
- **Intencje wyszukiwania** (strony publiczne): grupy fraz, nie pojedyncze słowa; z danych lub `[ZAŁOŻENIE]`, do sprawdzenia w narzędziu SEO przed treścią.
- Priorytet grup użytkowników: kto dostaje najwięcej miejsca, kto obsługiwany pobocznie.
Zatwierdza użytkownik.

## V2 Ścieżki (`flows.md`)
Dla każdego top task: `FLOW-ID`: start (skąd wchodzi, także z wyszukiwarki na podstronę) -> kroki (widok, akcja, element) -> decyzje -> dane do wpisania -> **błędy i brak wyników** (brak terminu, zła data, płatność odrzucona) -> powrót/cofnięcie -> potwierdzenie i co dalej. Ścieżka alternatywna, gdy użytkownik zaczyna od innego pytania (np. najpierw cena, potem termin). Wireflow: tekstem albo SVG/Mermaid (ekrany, strzałki z warunkiem, element wywołujący akcję); przy fragmencie ekranu (modal, filtr) pokaż tylko ten fragment.

## V3 Architektura (`views.tsv`, `seo.md`)
`views.tsv` kolumny: `id	url	typ	cel	zadania	główna_akcja	rodzic	linki_do	nawigacja	krytyczny	status`.
- Typ = szablon (np. strona oferty, lista, formularz kroku, dashboard); wiele podstron może dzielić typ.
- Nawigacja globalna (≤7 pozycji, nazwy w języku użytkownika), lokalna, stopka, okruszki; aktualne miejsce zawsze widoczne.
- Ważne strony 1-2 kliknięcia od wejścia (heurystyka, nie dogmat; liczy się jasność każdego kroku).
- Rozbudowa: wzorce URL (`/oferta/<slug>`, `/blog/<slug>`, `/<język>/...`) i miejsce w nawigacji dla przyszłych sekcji, ale bez pustych stron „wkrótce”.
- **Model treści**: dla każdego typu obiektu (np. domek: zdjęcia, nazwa, liczba osób, łóżka, wyposażenie, odległości, cena od, dostępność, warunki) - jednostki informacji, nie tekst. Wyznacza zawartość kart i stron szczegółu.
- `seo.md` (strony publiczne) kolumny: `id	url	intencja (grupa fraz)	H1 (opis, nie copy)	H2 (sekcje)	linki wewnętrzne (do/od)	canonical/indeks	schema.org`. Zasady w `principles.md`.
Zatwierdza użytkownik (mapa widoków + `seo.md`) przed makietami.

## V4 Spis bloków (`specs/<VIEW-ID>.md`)
Nagłówek: cel widoku, główny użytkownik i zadanie, główna akcja, następny krok, wejścia (skąd się tu trafia).
Blok po bloku w kolejności mobilnej:
```
BLOCK-REVIEWS · P2
po co: zmniejsza obawę „czy można ufać” przed CTA (TASK-BOOK)
dlaczego tu: po ofercie i cenie, przed końcowym CTA
treść: 3 opinie (ocena, 2-4 linie, data, źródło) + link do wszystkich
dane: system opinii X / brak -> pytanie
stany: brak opinii -> blok znika, nie pusty kontener
bez niego: użytkownik nie ma niezależnego potwierdzenia jakości
mobile/desktop: lista pionowa / 3 kolumny
```
Elementy interaktywne: typ (link `<a href>` dla nawigacji, przycisk dla akcji), stany: domyślny, fokus, nieaktywny, ładowanie, błąd, sukces (tylko te, które dotyczą). Widok: stany pusty, ładowanie, błąd, brak uprawnień, offline (aplikacje), długa treść.
**Test konieczności:** usuń blok w myślach - czy zadanie dalej da się wykonać i nic nie traci? Tak = usuń. **Wariant alternatywny:** dla każdego widoku krytycznego jeden inny układ (np. wyszukiwarka terminu na górze vs oferta na górze) i 2 zdania, czemu wybrany wygrywa.

## V5 Szare makiety (`wireframes/`)
- Plik na widok: `<VIEW-ID>.html`, prymitywy z `wire.css` (skopiuj z `<katalog skilla>/assets/`), wzór `example.html`. Bez własnych kolorów i fontów.
- Semantyka od razu: `header`, `nav`, `main`, `footer`, jeden `h1` (strony), `h2` sekcji, `label` przy polu, nawigacja jako `<a href>`.
- Blok: `<section data-block="BLOCK-ID" data-p="1" data-why="krótki powód">`; główne CTA `data-cta="primary" data-action="<akcja>"`.
- Etykiety placeholderów mówią typ i objętość, nie copy: `IMG 4:3 · domek z zewnątrz`, `H1 · nazwa + miejsce, 1-2 linie`, `TXT · 3 linie`. Etykiety przycisków i nawigacji = nazwa funkcji („Sprawdź dostępność”), bo to architektura, nie copywriting.
- Hierarchia w szarościach: ≤3 poziomy wielkości, najciemniejszy element = główna akcja, grupowanie odstępem i wspólnym tłem.
- Kolejność: 360 px -> 768 -> 1280. Desktop: kolumny dla rzeczy porównywanych, nic tylko na hover, nic kluczowego w prawej kolumnie bocznej.
- Najpierw widoki krytyczne; po ich akceptacji reszta na tym samym wzorcu.

## V6-V7 Kontrola i przegląd
Wg `quality.md`. Wynik w `qa.md`: TSV z `wirecheck`, wynik rubryki, uwagi testu świeżych oczu, przejścia ścieżek, pre-mortem, poprawki. Potem `hq:design-reviewer` (paczka: `brief.md`, `flows.md`, `views.tsv`, `specs/`, zrzuty, `quality.md`).

## V8 Akceptacja (`status.md`)
```
status: ready_for_review   # not_started | in_progress | blocked | ready_for_review | changes_requested | approved
wersja: 1
zatwierdził: -              # tylko użytkownik, imię lub „użytkownik”, data
zakres: VIEW-HOME, VIEW-OFFER, ...
uwagi: -
```
Pokaż użytkownikowi zrzuty mobile i desktop widoków krytycznych + mapę widoków + top 3 decyzje i ryzyka. Uwagi ogólne („bardziej przejrzyście”) tłumacz na konkretną zmianę bloku. Zmiana po `approved`: `wersja+1`, status `changes_requested` -> ponowna akceptacja zmienionych widoków. Decyzje i odrzucone warianty w `decisions.md`.
