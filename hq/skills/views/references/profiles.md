# Profile projektów: wspólny proces, inne akcenty

Proces V0-V8 jest wspólny. Profil zmienia: co jest głównym zadaniem, nawigację, zakres SEO i dodatkowe testy. Wzorce to punkt wyjścia do sprawdzenia z mapą pytań projektu, nie szablon do skopiowania.

| Profil | Główne zadanie | Nawigacja | SEO | Dodatkowe testy |
|---|---|---|---|---|
| Strona usługowa / nocleg / firma lokalna | znaleźć ofertę, zaufać, zarezerwować lub zapytać | IA treści | wysokie | widoczność oferty i ceny, kontakt, zaufanie |
| Sklep | znaleźć i kupić | kategorie, wyszukiwarka, filtry | wysokie | ścieżka zakupu, filtry, koszt dostawy przed checkoutem |
| SaaS / aplikacja webowa | wykonać pracę | funkcje, obiekty | strony publiczne | onboarding, stan pusty, uprawnienia, błędy |
| Aplikacja mobilna | szybkie zadanie w ruchu | dolna nawigacja (3-5) | tylko strony publiczne, deep linki | kciuk, offline, uprawnienia systemu, klawiatura |
| Desktop / narzędzie | wydajna praca | menu, panele, skróty | brak | klawiatura, gęstość, wiele okien |
| CLI / TUI | polecenie -> wynik | podpolecenia, `--help` | brak | błędy z naprawą, `--help`, wynik maszynowy (`--json`) |
| Ekran urządzenia / HMI | sterować bezpiecznie | stany urządzenia | brak | alarmy, pomyłki krytyczne, czytelność w warunkach, przyciski fizyczne |
Aplikacje (`--app` w `wirecheck`): `h1` nie jest wymagany, ale tytuł ekranu tak.

## Nocleg / agroturystyka (bezpośrednie rezerwacje)
Mapa pytań: co to i gdzie -> czy pasuje (dla kogo, otoczenie) -> jakie noclegi, dla ilu, ile kosztują -> czy wolne w moim terminie -> czy mogę zaufać -> jak dojadę i co robić w okolicy -> jak zarezerwować i co jeśli odwołam.
Mapa widoków (wzór): Start · Noclegi (lista) · Nocleg `[slug]` · Rezerwacja (termin i osoby -> wybór -> dane -> podsumowanie -> potwierdzenie) · O miejscu (gospodarstwo, udogodnienia, opinie) · Okolica (atrakcje, dojazd) · Kontakt i dojazd · Regulamin i prywatność · Blog (gdy będzie treść). FAQ przy noclegu i rezerwacji.
Start, mobile (wzór do sprawdzenia, nie dogmat): nagłówek (logo, menu, telefon) -> zdjęcie + nazwa + miejsce + wybór terminu i osób + „Sprawdź dostępność” -> 3-4 fakty kwalifikujące (typ, otoczenie, dla kogo) -> noclegi (karty: zdjęcie, nazwa, osoby, cena od, „Zobacz”) -> wyróżniki miejsca -> opinie -> lokalizacja i dojazd -> FAQ -> stopka; przyklejony „Sprawdź dostępność” po zjechaniu poniżej formularza.
Nocleg `[slug]`: galeria -> nazwa, osoby, cena od -> termin i dostępność + CTA -> najważniejsze udogodnienia -> opis (akordeon) -> zasady i anulowanie -> opinie o tym noclegu -> lokalizacja -> FAQ -> inne noclegi.
Stany: brak wolnego terminu (najbliższe wolne terminy, inny nocleg, kontakt), błąd płatności, rezerwacja wstępna vs potwierdzona.

## Strona usługi lokalnej
Usługa + obszar działania -> kontakt (telefon i krótki formularz wyceny, oba) -> zakres usług z linkami do stron usług -> jak to działa (kroki) + CTA -> cennik lub widełki -> realizacje i opinie z okolicy -> kto to robi -> FAQ tej usługi. Strony lokalizacji tylko z unikalną treścią.

## Sklep
Kategoria (filtry z „Zastosuj”, sortowanie, liczba wyników) -> lista -> produkt (zdjęcia, cena, wariant, dostępność, dostawa i zwroty przed koszykiem, CTA) -> koszyk (edycja, koszt całkowity) -> checkout (gość bez konta, kroki, błędy przy polu) -> potwierdzenie. Wyszukiwarka z przyciskiem „Szukaj” i podpowiedziami.

## SaaS / aplikacja webowa
Pierwsze uruchomienie (stan pusty, który uczy, jak zacząć) -> pulpit (status, co wymaga uwagi, główna operacja; nie marketingowy hero) -> lista obiektów -> szczegół -> edycja -> ustawienia i role. Tabela, gdy użytkownik porównuje; karty, gdy przegląda. Każda akcja nieodwracalna z potwierdzeniem lub cofnięciem.

## Aplikacja mobilna
Dolna nawigacja 3-5 sekcji z bieżącą zaznaczoną; główna akcja w dolnej części; uprawnienia systemu proszone w momencie potrzeby z wyjaśnieniem; offline i słabe łącze; klawiatura nie zasłania pola i przycisku.

## CLI / TUI
„Makieta” = zapis sesji: polecenie -> wynik -> błąd (co, dlaczego, jak naprawić) -> `--help`. Spójne nazwy podpoleceń i flag, wynik do czytania i `--json`, kody wyjścia.

## Ekran urządzenia / HMI
Rozdzielczość i proporcje z sprzętu, wejście (dotyk w rękawicach, enkoder, przyciski), odległość czytania; stan urządzenia zawsze widoczny; alarmy ponad wszystkim; akcje groźne z potwierdzeniem fizycznym. Ograniczenia pamięci i renderu z `hq:firmware-engineer`.
