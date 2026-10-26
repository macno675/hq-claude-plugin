# Ramy decyzji technologicznych

## Opcje (decyzja osobno dla każdego elementu)
| Opcja | Kiedy ma sens | Główne ryzyko |
|---|---|---|
| Kup gotowe | funkcja standardowa, czas krytyczny, rozwiązanie dojrzałe i bezpieczne | uzależnienie od dostawcy, mała kontrola |
| Zbuduj własne | technologia daje przewagę, wymagania nietypowe, są kompetencje do utrzymania latami | koszt, czas, utrzymanie |
| Hybryda | standard kupiony, przewaga we własnej warstwie | złożoność integracji |
| Partner | potrzebna modyfikacja bez budowy wszystkiego | mała kontrola nad roadmapą |

## 12 kryteriów oceny (skala 1-5, waga zależna od projektu; zapisz wagi i powody)
Dopasowanie do wymagań · Wydajność (teraz i później) · Niezawodność w trudnych warunkach · Bezpieczeństwo · Skalowalność · Koszt całkowity (cykl życia) · Czas wdrożenia · Utrzymanie (kto rozwija i naprawia) · Zależność od dostawcy · Elastyczność przyszłej zmiany · Kompetencje zespołu · Przewaga rynkowa.
Tabela: `opcja | kryterium -> ocena | uzasadnienie [DOWÓD/ZAŁOŻENIE]`. Suma ważona jest pomocą, nie wyrokiem - sprawdź, czy wynik zgadza się z intuicją, a jeśli nie, dlaczego.

## TCO (koszt całkowity, horyzont min. 3-5 lat)
Rozwój/zakup · integracja · licencje i opłaty cykliczne · infrastruktura · szkolenia · utrzymanie i aktualizacje · wsparcie · bezpieczeństwo/audyty · koszt ryzyka (przestój, incydent) · koszt migracji lub wyjścia. Podaj założenia i wrażliwość (co jeśli koszt x2 lub czas x2).

## Własny protokół/technologia - test (uzasadniona przy spełnieniu większości, w tym punktów 1 i 3)
1. Istniejące rozwiązania nie spełniają wydajności, bezpieczeństwa lub kontroli (udowodnione, z liczbami).
2. Potrzebny specjalny sposób wymiany danych.
3. Będzie częścią przewagi produktu.
4. Firma może go utrzymywać, dokumentować, rozwijać (osoby, czas).
5. Da się zapewnić zgodność wsteczną i wersjonowanie.
6. Bezpieczeństwo zaplanowane od początku (nie własna kryptografia - użyj sprawdzonych bibliotek i standardów).
7. Da się testować w warunkach rzeczywistych.
8. Koszt utrzymania akceptowalny w horyzoncie lat.
Brak spełnienia = rekomenduj standard lub rozszerzenie standardu. Pytanie kontrolne: "czy to przewaga, czy kosztowne ego projektu?"

## Projekt własnej technologii (gdy decyzja o budowie zapadła)
Problem i cele -> analiza istniejących -> wymagania i ograniczenia -> koncepcja -> model bezpieczeństwa -> interfejsy i formaty danych -> prototyp -> testy (wydajność, niezawodność, bezpieczeństwo) -> dokumentacja -> wersjonowanie i plan rozwoju -> wdrożenie -> monitoring i poprawki. Projektuj do utrzymania latami, nie do demo.

## Walidacja przed wdrożeniem
Wydajność normalna i maksymalna · błędy transmisji · opóźnienia · bezpieczeństwo danych · wymagania prawne · zachowanie po awarii · aktualizacje · zgodność ze starszymi wersjami · łatwość integracji · koszt operacyjny. Dowód = pomiar własnego vs alternatywa, nie teoria.

## Ryzyka (wybierz świadomie, zaplanuj ograniczenie)
Własne: za długi rozwój · brak specjalistów · koszt utrzymania · błędy bezpieczeństwa · rekrutacja · zależność od jednej osoby · brak dokumentacji · zgodność wsteczna.
Zewnętrzne: wzrost cen i zmiana warunków · koniec wsparcia · ograniczona modyfikacja · uzależnienie od ekosystemu · prywatność danych · niezgodność z wymaganiami · przejęcie dostawcy.
`vendors.tsv`: `dostawca | za co odpowiada | licencja/koszt (data) | ryzyko uzależnienia | alternatywy | plan zamiany | data przeglądu`.

## ADR (`.hq/tech/adr/NNN-tytuł.md`)
Status (proponowany/zatwierdzony/zastąpiony) · Data · Właściciel · Problem · Wymagania i ograniczenia · Opcje (zalety/wady) · Wyniki testów i analiz [DOWÓD/ZAŁOŻENIE] · Decyzja · Uzasadnienie · TCO i założenia · Akceptowane ryzyka · Plan wdrożenia · Plan wycofania lub zmiany (kryteria porzucenia) · Odpowiedzialni · Powiązane ADR.
Język biznesowy w podsumowaniu (3 linie): ile kosztuje, ile czasu, jakie ryzyko, co jeśli błąd.

## Przegląd okresowy
Raz na 6-12 miesięcy lub przy zmianie dostawcy/ceny/wymagań: czy decyzja nadal najlepsza? czy dostawca stabilny? czy powstał lepszy standard? Zmiana decyzji = nowy ADR zastępujący stary.
