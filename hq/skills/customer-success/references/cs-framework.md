# Ramy Customer Success

## Profil klienta (`profiles/<klient>.md`)
Kim jest · cel współpracy (jego słowami) i miara sukcesu · obiecane rezultaty (co zadeklarowała sprzedaż) · osoby (decydent, użytkownicy, wpływowi, blokerzy) · terminy · ryzyka · historia kontaktów (data, temat, ustalenia) · preferencje komunikacji · plan wdrożenia/odnowienia · linki do umowy. Aktualizowany po każdym kontakcie.

## Przekazanie ze sprzedaży (lista)
Cel i oczekiwania klienta · obiecane rezultaty i ograniczenia (czego NIE obiecano) · problemy do rozwiązania · osoby decyzyjne · terminy i cykl budżetowy · ryzyka · szczególne wymagania · konkurencja rozważana · warunki umowy i odnowienia. Spotkanie przekazania: sprzedaż i CS razem.

## Plan wdrożenia 30-60-90
Dni 0-30: kickoff, konfiguracja, szkolenie, migracja danych, **pierwsza wartość** (konkretny rezultat i data). Dni 31-60: pełna adopcja przez kluczowych użytkowników, procesy ustawione, pierwszy przegląd wyników. Dni 61-90: wartość mierzalna względem celu klienta, plan rozwoju, pierwszy QBR. Każdy etap: cel, miara, właściciel po obu stronach, ryzyka, kryteria "zrobione". Dla wydarzeń: plan korzyści sponsorskich z terminami aktywacji (`hq:event`).

## Onboarding (lista kontrolna)
Konfiguracja z klientem · szkolenie użytkowników (krótkie, praktyczne, nagrane lub materiał) · materiały i szybki start · migracja/import danych · ustawione procesy · sprawdzenie zrozumienia (zadanie praktyczne) · osoba kontaktowa i kanał pomocy · zaplanowane kolejne spotkanie. Cel: pierwsza znacząca wartość, nie tylko znajomość funkcji.

## Sygnały ostrzegawcze
Spadek aktywności · brak użycia kluczowych funkcji · wzrost zgłoszeń · negatywne opinie/ankiety · pytania o eksport danych lub warunki rezygnacji · niezadowolenie po wdrożeniu · zbliżające się odnowienie bez rozmowy · zmiana osoby decyzyjnej lub sponsora po stronie klienta · opóźnione płatności (z `hq:finance`). Rejestruj w `accounts.tsv` i w profilu.

## Zdrowie konta (`health.py`)
Heurystyka: adopcja kluczowych funkcji (30%), trend użycia (25%), satysfakcja (20%), otwarte zgłoszenia (15%), pierwsza wartość (10%), kara za zmianę decydenta. Poziomy: zdrowe >= 75, uwaga 50-74, zagrożone < 50. **Wagi i progi to punkt wyjścia:** sprawdzaj je na historii odejść i dostosuj; wynik jest sygnałem do rozmowy, nie wyrokiem o kliencie. Braki danych (np. brak ankiety) są flagowane, nie ukrywane.

## Spotkania i QBR
Cykliczne rozmowy (np. co 2-4 tygodnie na początku, potem miesięcznie): postęp, problemy, edukacja, nowe możliwości, feedback. **QBR (kwartalny):** wyniki vs cel klienta (liczby klienta), wartość osiągnięta dzięki produktowi/współpracy, problemy i plan, plan na kolejny kwartał, rekomendacje rozwojowe, przygotowanie odnowienia. Agenda wysłana wcześniej (przez użytkownika), po spotkaniu podsumowanie z ustaleniami, właścicielami i terminami.

## Plan ratunkowy (`plans/ratunkowy`)
Konto: wynik, sygnały · przyczyna (rozmowa z klientem: co się zmieniło, co nie działa) · cel naprawy (miara) · działania z właścicielami i terminami (produkt, wsparcie, sprzedaż) · komunikacja z klientem (częstotliwość, kto) · kryteria sukcesu i data przeglądu · decyzja, czy kontynuować walkę o konto (czasem uczciwie lepiej zakończyć współpracę). Bez obietnic bez pokrycia.

## Odnowienie (90 / 60 / 30 dni)
90 dni: przegląd wyników i zdrowia, lista otwartych problemów, plan ich zamknięcia, ustalenie osoby decyzyjnej i procesu zakupowego klienta. 60 dni: podsumowanie wartości (liczby klienta), propozycja kontynuacji (zakres, cena, warunki), ustalenie ze sprzedażą i finansami. 30 dni: negocjacje, dokumenty (`hq:legal-safety`), termin podpisu, plan B. Po terminie bez podpisu: eskalacja do użytkownika.

## Rozszerzanie
Sygnały realnej potrzeby: klient prosi o więcej użytkowników/funkcji, osiąga limity, nowe zespoły chcą skorzystać, cel klienta wymaga dodatkowego modułu. Oferta oparta na jego celu i dowodzie wartości; bez presji. Przekazanie sygnału do `hq:partnerships`.

## Feedback do produktu
Powtarzające się problemy · niezrozumiałe funkcje · brakujące możliwości · oczekiwania rynku · ryzyka odejścia · pomysły. Format: `temat | liczba klientów | przykłady (anonimowe) | wpływ na retencję/wartość | proponowane rozwiązanie`. Priorytety rozwoju decyduje `hq:product-management`. Do klienta: plan działania, status, wyjaśnienie ograniczeń, harmonogram poprawek, wartość wdrożonych zmian.

## Współpraca
Sprzedaż: kontekst i sygnały rozszerzeń. Support: rozwiązuje bieżące problemy; CS pilnuje, czy powtarzalne nie zagrażają relacji. Produkt: potrzeby klientów. Marketing: case studies i opinie **tylko za zgodą klienta**. Finanse: odnowienia, rozliczenia, ryzyko utraty przychodu.

## Dokumentacja
Profil klienta · cel współpracy · plan wdrożenia · kamienie · osoby decyzyjne · historia kontaktów · wyniki adopcji · health score · ryzyka · plany ratunkowe · QBR · plan odnowienia · wnioski.
