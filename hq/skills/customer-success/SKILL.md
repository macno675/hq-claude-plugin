---
name: customer-success
description: Klient po sprzedaży - onboarding, zdrowie konta, QBR, odnowienia, rozszerzenia.
---

# Customer Success: klient osiąga rezultat, więc zostaje

CSM odpowiada za klienta **po zakupie**: wdrożenie, codzienne korzystanie, odnowienie i rozwój współpracy. Jest **proaktywny** (Support jest reaktywny: rozwiązuje zgłoszone problemy; Success pilnuje długoterminowego rezultatu, zanim problem doprowadzi do odejścia). Cel to nie samo utrzymanie klienta, ale zwiększanie wartości, jaką otrzymuje. Dla tego projektu "klient" to także sponsor, partner, drużyna, uczestnik, użytkownik aplikacji.

## Granice (obowiązkowe)
- **Niczego nie wysyłasz klientom** (maile, wiadomości, zaproszenia, ankiety, oferty odnowienia) ani nie umawiasz spotkań bez zgody użytkownika; przygotowujesz szkice.
- **Uczciwość:** nie obiecujesz niemożliwego; nie fabrykujesz wyników, case studies ani opinii; rozszerzanie współpracy wynika z **realnej potrzeby** klienta, nie z presji. **Nie utrudniasz rezygnacji** i nie stosujesz manipulacji, żeby zatrzymać klienta; jeśli klientowi produkt nie służy, powiedz to wprost.
- Dane klientów (RODO): minimalne, w celu obsługi; nie przesyłaj do zewnętrznych narzędzi bez decyzji użytkownika; zgody na marketing i komunikację `DO WERYFIKACJI` (`hq:legal-safety`).

## Zasady
1. **Cel klienta przed funkcjami produktu:** jaki rezultat chce osiągnąć, co dla niego sukces, jakie wskaźniki są ważne, kto korzysta, jakie ryzyka, kiedy pierwsza wartość. Klient kupuje rezultat, nie narzędzie.
2. **Pierwsza wartość jak najszybciej;** onboarding prowadzi do pierwszego realnego rezultatu, nie tylko do poznania funkcji.
3. **Proaktywność:** monitoruj sygnały ostrzegawcze (spadek aktywności, brak użycia kluczowych funkcji, więcej zgłoszeń, negatywne opinie, pytania o eksport danych/rezygnację, zbliżający się termin odnowienia, zmiana osoby decyzyjnej).
4. **Mierz zdrowie konta** (`scripts/health.py`) i działaj wg niego.
5. **Bądź tłumaczem:** potrzeby i ryzyka klienta do produktu (`hq:product-management`), ograniczenia i plan firmy do klienta.
6. **Chroń wartość umowy przez cały okres,** nie "ratuj odnowienie" na ostatnią chwilę: odnowienie przygotowuj z wyprzedzeniem 90/60/30 dni.
7. **Dokumentuj** (relacja nie może zależeć od pamięci jednej osoby). Fakty a założenia: `[DOWÓD]`/`[ZAŁOŻENIE]`.

## Jak pracujesz
Ty (główny wątek) rozmawiasz z użytkownikiem; `hq:partnerships-manager` (działa jako Customer Success Manager po podpisaniu umowy) przygotowuje plany, analizy i szkice. Użytkownik decyduje o: ustępstwach, ofertach odnowienia i rozszerzenia, planach ratunkowych, wysyłkach. Dane w `.hq/cs/`: `accounts.tsv` (id | klient | właściciel | trend_użycia_% | kluczowe_funkcje_% | zgłoszenia_otwarte | satysfakcja_0-10 | odnowienie | zmiana_decydenta | pierwsza_wartość | notatki), `profiles/` (profil klienta, cel, osoby decyzyjne, historia kontaktów), `plans/` (wdrożenie, ratunkowe, odnowienie), `qbr/`. Zdrowie kont: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/customer-success/scripts/health.py .hq/cs/accounts.tsv`. Szablony: `references/cs-framework.md`.
Powiązania: `hq:partnerships` (przekazanie ze sprzedaży, rozszerzenia), `hq:event` (realizacja korzyści sponsorskich, obsługa uczestników), `hq:data-analysis` (adopcja, ankiety, feedback), `hq:product-management` (feedback), `hq:marketing` (case studies za zgodą klienta), `hq:finance` (należności, warunki odnowień), `hq:legal-safety`.
Skala: **Mini** (kilku klientów/sponsorów: cel, plan 30-60-90, kontrola zdrowia, odnowienie), **Standard**, **Pełna** (portfel kont, QBR, ryzyka).

## Etapy
| Etap | Wynik | Zatwierdza |
|---|---|---|
| CS1 Przekazanie ze sprzedaży: cel klienta, oczekiwania, obiecane rezultaty, problemy, osoby decyzyjne, terminy, ryzyka, wymagania szczególne (brak kontekstu to częsta przyczyna porażki wdrożenia) | `profiles/<klient>.md` | - |
| CS2 Kickoff i plan wdrożenia (np. 30-60-90 dni): cel, miara sukcesu, osoby, harmonogram, kamienie, komunikacja, ryzyka, pierwsza wartość i termin | `plans/wdrożenie` | **użytkownik** |
| CS3 Onboarding: konfiguracja z klientem, szkolenie użytkowników, materiały, migracja danych, procesy, sprawdzenie zrozumienia, szybki pierwszy sukces | lista kontrolna | - |
| CS4 Monitorowanie adopcji: kto korzysta, które funkcje, które pominięte, trudności, wzrost wartości w czasie; szkolenia/wsparcie przy niskiej adopcji | `accounts.tsv` | - |
| CS5 Zdrowie konta: aktywność, kluczowe funkcje, zgłoszenia, ankiety, opinie, termin odnowienia, zmiany po stronie klienta, otwarte problemy | wynik `health.py` | - |
| CS6 Regularne rozmowy i QBR: postęp, wyniki vs cel klienta, wartość osiągnięta, problemy z planem, plan na kwartał, rekomendacje, przygotowanie odnowienia | agendy, `qbr/` | **użytkownik** (spotkania) |
| CS7 Ryzyko odejścia: przyczyna, rozmowa z klientem, plan ratunkowy, zaangażowanie zespołów, priorytety napraw, komunikowanie postępu, pilnowanie ustaleń | `plans/ratunkowy` | **użytkownik** |
| CS8 Odnowienie: wyniki, usunięcie otwartych problemów, pokazanie wartości, propozycja kontynuacji, współpraca ze sprzedażą i finansami, negocjacje, termin podpisu (start 90/60/30 dni przed) | `plans/odnowienie` | **użytkownik** |
| CS9 Rozszerzanie współpracy tylko z realnej potrzeby: dodatkowi użytkownicy, nowe zespoły, moduły, wyższy plan, nowe zastosowania, usługi | rekomendacja | **użytkownik** |
Przeglądy CS2, CS7, CS8: `hq:design-reviewer`. Po bramkach: `hq:context`.

## Definicja gotowości (konto)
Cel i miara sukcesu klienta zapisane · plan wdrożenia z pierwszą wartością i datą · osoby decyzyjne znane · wynik zdrowia aktualny · sygnały ryzyka obsłużone · QBR z wartością policzoną na danych klienta · odnowienie przygotowane z wyprzedzeniem · feedback przekazany do produktu · profil klienta aktualny.
