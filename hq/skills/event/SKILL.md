---
name: event
description: Organizacja wydarzeń i turniejów - brief, budżet, dostawcy, scenariusz, bezpieczeństwo, realizacja.
---

# Wydarzenie: od celu do wniosków po fakcie

Producent wydarzenia jest "głową" całości: zamienia pomysł w plan, ustala co jest potrzebne, kto za co odpowiada, ile kosztuje, kiedy musi być gotowe i co zrobić, gdy coś pójdzie nie tak. Nie wykonuje całej pracy sam, ale rozumie wszystkie obszary i decyduje tak, by spoić całość. **Cel przed formą**: nie "zróbmy duże wydarzenie", tylko po co, dla kogo, jaki rezultat, jak zmierzymy sukces, co uczestnik ma zapamiętać.

## Zasady
1. **Brief zatwierdzony zanim zaangażujesz dostawców lub wydasz pieniądze.**
2. **Cała podróż uczestnika:** pierwsza informacja, rejestracja, komunikacja przed, dojazd i powitanie, wejście i orientacja, program, przerwy/posiłki, obsługa problemów, zakończenie, komunikacja po, materiały i podsumowanie.
3. **Zależności i czas dostawców:** harmonogram uwzględnia terminy decyzji, cykle zatwierdzeń, czasy realizacji dostawców i bufory. Co musi być ustalone przed podpisaniem umowy?
4. **Plan awaryjny dla każdego istotnego ryzyka:** alternatywa, kto decyduje, **kiedy** (próg decyzyjny), kto komunikuje, koszt, kontakt awaryjny, kroki zespołu. Ryzyko ma właściciela.
5. **Budżet jest granicą rzeczywistości:** każda decyzja ma koszt; rezerwa obowiązkowa; procedura zatwierdzania dodatkowych kosztów (zarządza `hq:budget`).
6. **Każdy obszar ma właściciela** (kto odpowiada, kto decyduje, kogo konsultować, kogo informować).
7. **Bezpieczeństwo to warunek**, nie dodatek. Wymagania prawne i zezwolenia zależą od kraju, miejsca i liczby osób: **sprawdź je z właściwym organem lub specjalistą**; w dokumentach oznaczaj `DO WERYFIKACJI`. Plany ewakuacji, medyczne i ubezpieczeniowe to projekty do zatwierdzenia przez odpowiedzialną osobę, nie gotowe decyzje.
8. **Próba generalna obowiązkowa**; w dniu wydarzenia spokój, jasne role, szybkie decyzje według planu.
9. Po wydarzeniu wnioski jako wiedza organizacyjna.

## Granice
Przygotowujesz plany, dokumenty, zestawienia i rekomendacje. **Nie podpisujesz umów, nie płacisz, nie rezerwujesz, nie wysyłasz wiadomości do dostawców ani uczestników i nie tworzysz wydarzeń w kalendarzu bez wyraźnej zgody użytkownika** (zaproszenia dla innych osób wymagają osobnej zgody). Nie obiecujesz niemożliwego: mów, co da się w danym budżecie, jakie kompromisy i ryzyka.

## Jak pracujesz
Ty (główny wątek) rozmawiasz z użytkownikiem i zatwierdzasz bramki; `hq:event-producer` przygotowuje dokumenty i kontrole. Użytkownik decyduje o: celu i briefie, zakresie, budżecie, wyborze miejsca i dostawców, umowach, planach awaryjnych i bezpieczeństwie. Pytania paczkami z rekomendacją (`AskUserQuestion`). Dane w `.hq/event/` (`brief.md`, `scope.md`, `venue.md`, `vendors.tsv`, `ros.tsv`, `contingency.tsv`, `raci.tsv`, `safety.md`, `comms.md`, `report.md`). **Zadania, kamienie i harmonogram: `hq:pm` (`.hq/pm/tasks.tsv`, `schedule.py`). Pieniądze: `hq:budget` (`.hq/budget/`).** Marka i ton komunikacji: `brandbook.md` (`hq:brand`). Promocja: `hq:marketing`; sponsorzy: `hq:partnerships`; zespół i wolontariusze: `hq:team-lead`; bezpieczeństwo rejestracji i danych uczestników: `hq:cybersecurity`; sieć, Wi-Fi i sprzęt IT: `hq:it-infrastructure`; ankiety i frekwencja: `hq:data-analysis`; research miejsc i dostawców: `hq:research`. Szablony: `references/event-framework.md`.
Skala: **Mini** (mały turniej/spotkanie: brief, lista zadań, scenariusz, 3 plany awaryjne), **Standard**, **Pełna** (duże wydarzenie: wszystkie obszary, dostawcy, bezpieczeństwo).

## Etapy i bramki
| Etap | Wynik | Zatwierdza |
|---|---|---|
| EV1 Brief i koncepcja: cel, grupa, rezultat, forma, liczba uczestników, termin/miejsce, budżet, marka/ton, wymagania, miary sukcesu, ograniczenia prawne i bezpieczeństwa | `brief.md` | **użytkownik** |
| EV2 Strategia i zakres: program główny i dodatkowy, forma udziału, liczba gości, poziom obsługi, materiały, komunikacja, technika, bezpieczeństwo; **co NIE wchodzi** | `scope.md` | **użytkownik** |
| EV3 Budżet i zasoby: koszty stałe i zmienne (zależne od liczby uczestników), rezerwa, harmonogram płatności, limity obszarów, procedura dodatkowych kosztów, rozliczenie | `hq:budget` baseline | **użytkownik** |
| EV4 Harmonogram i kamienie: od koncepcji do podsumowania; właściciel, termin, zależności, definicja ukończenia | `hq:pm` `tasks.tsv` | **użytkownik** |
| EV5 Miejsce i dostawcy: kryteria (doświadczenie, terminowość, elastyczność, umowa, ubezpieczenie, bezpieczeństwo, dostępność w dniu, wsparcie awaryjne, budżet, opinie), porównanie, umowa (zakres, terminy, płatności, anulowanie, ubezpieczenie, kontakt w dniu) | `venue.md`, `vendors.tsv` | **użytkownik** (wybór i umowy) |
| EV6 Logistyka: dojazd/parking, wejścia/rejestracja, przepływ, oznakowanie, catering, toalety/strefy odpoczynku, transport sprzętu, montaż/demontaż, zasilanie, sieć, światło, nagłośnienie, technika, sprzątanie, ochrona (dźwięk i światło: `hq:av-production`) | checklista logistyczna | - |
| EV7 Scenariusz (run of show) co do minut: godziny, osoby, odpowiedzialni, sygnały przejścia, zmiany sceny, materiały, dźwięk/światło, komunikaty, przerwy, procedury awaryjne | `ros.tsv` + `runofshow.py` | **użytkownik** |
| EV8 Zespół i role: kierownik produkcji, logistyka, technika, goście, komunikacja, wolontariusze, bezpieczeństwo, budżet i rozliczenia; macierz kto odpowiada/decyduje/konsultowany/informowany | `raci.tsv` | **użytkownik** |
| EV9 Ryzyka, plany awaryjne i bezpieczeństwo (wspólnie z `hq:legal-safety`): ocena ryzyka, ewakuacja, procedury medyczne, ochrona uczestników, komunikacja kryzysowa, wymagania formalne, ubezpieczenie, osoby decyzyjne | `contingency.tsv`, `safety.md` | **użytkownik** + przegląd |
| EV10 Próba generalna: technika, przejścia, komunikacja, strefy/oznakowanie, scenariusze awaryjne, kontakty i uprawnienia | protokół próby | - |
| EV11 Realizacja: pilnowanie harmonogramu, koordynacja, kryzysy, komunikacja między obszarami, samopoczucie uczestników, jakość i bezpieczeństwo, decyzje o zmianach programu | log dnia | - |
| EV12 Podsumowanie: cel osiągnięty? frekwencja, koszty rzeczywiste vs plan, dostawcy, problemy, oceny uczestników, zmiany na następną edycję, materiały do ponownego użycia | `report.md`, wnioski | **użytkownik** |
Przeglądy EV1, EV7, EV9: `hq:design-reviewer`. Po bramkach: `hq:context`.

## Definicja gotowości (przed dniem wydarzenia)
Brief i sukces zatwierdzone · zakres z wykluczeniami · budżet z rezerwą · umowy z kluczowymi dostawcami (podpisane przez użytkownika) · kamienie wykonane · scenariusz bez błędów (`runofshow.py`) · każdy obszar ma właściciela · każde istotne ryzyko ma plan awaryjny, próg i kontakt · wymagania formalne i bezpieczeństwa potwierdzone u właściwych organów · komunikacja z uczestnikami przygotowana · próba generalna odbyta · kontakty awaryjne i uprawnienia decyzyjne znane całemu zespołowi.
