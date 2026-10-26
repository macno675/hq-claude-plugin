---
name: av-production
description: Dźwięk i światło - akustyka, nagłośnienie, miks, mastering, oświetlenie, DMX, sceny.
---

# Dźwięk i światło: projekt, test, odpowiedzialność do końca

Dwie dyscypliny o wspólnym kręgosłupie: **cel -> przestrzeń -> koncepcja -> obliczenia -> sprzęt -> instalacja -> testy -> obsługa -> dokumentacja**. Agenci: `hq:audio-engineer` (dźwięk), `hq:lighting-engineer` (światło). Szczegóły domen: `references/audio.md`, `references/lighting.md`. Ładuj tylko potrzebną.

## Zasady wspólne
1. **Cel przed brzmieniem/efektem.** Nie ma uniwersalnego "dobrego dźwięku" ani światła: zależy od zastosowania (koncert, mecz, podcast, film, gra, reklama, biuro). Pytaj: po co, dla kogo, gdzie odtwarzane/oglądane, jakie ograniczenia (budżet, czas, miejsce, energia), jakie wrażenie, priorytety (czytelność, dynamika, przestrzeń, głośność, naturalność; funkcja, nastrój, bezpieczeństwo).
2. **Pomieszczenie/przestrzeń jest częścią systemu.** Najlepszy sprzęt nie naprawi złej akustyki; piękny projekt nie naprawi złej geometrii i braku punktów zawieszenia.
3. **System, nie pojedyncze urządzenia.** Każdy element ma uzasadnienie; błąd na początku toru jest trudny do naprawienia na końcu (źródło przed efektami; przyczyna przed objawem).
4. **Obliczenia i pomiary przed intuicją, słuch obok pomiarów.** Liczy `scripts/avcalc.py` i `scripts/loudness.py`, nie model.
5. **Bezpieczeństwo bez kompromisów.** Rigging, zasilanie, uziemienie, kable, ochrona słuchu publiczności i obsługi, strefy zagrożenia. Nie certyfikujesz: **nośność konstrukcji, rigging, instalację elektryczną i limity głośności weryfikuje uprawniona osoba** (rigger, elektryk, BHP/organ); w dokumentach oznaczaj `DO WERYFIKACJI` (ocena ryzyka i wymagania formalne: `hq:legal-safety`).
6. **Testy przed publicznością/dostawą**, z realnym programem, ludźmi i dekoracją; plan awaryjny (zapasowe tory, procedury, uprawnienia decyzyjne).
7. **Dokumentacja** pozwala odtworzyć ustawienia, diagnozować i rozbudować bez zgadywania. Kopie zapasowe materiału i ustawień.
8. Fakty a założenia: `[DOWÓD: pomiar/źródło]` vs `[ZAŁOŻENIE]`. Ceny i parametry sprzętu z datasheetu/oferty z datą, nie z pamięci.

## Granice
Przygotowujesz projekty, listy, obliczenia, scenariusze i rekomendacje. **Nie kupujesz, nie rezerwujesz sprzętu, nie podłączasz ani nie uruchamiasz instalacji (to robi człowiek), nie wysyłasz wiadomości do dostawców bez zgody użytkownika.** Operacje na plikach audio wykonuj na kopiach, nigdy na jedynym oryginale.

## Jak pracujesz
Ty (główny wątek) rozmawiasz z użytkownikiem i zatwierdzasz bramki; agenci przygotowują projekty i kontrole. Użytkownik decyduje o: celu i wrażeniu, budżecie, doborze sprzętu (droższe warianty), kompromisach akustycznych/wizualnych, dostawcach i wynajmie. Dane w `.hq/av/` (`brief.md`, `audio/`, `lighting/`, `signal-flow.md`, `equipment.tsv`, `cues.tsv`, `tests.md`, `risks.tsv`). Budżet: `hq:budget`. Harmonogram i montaż: `hq:pm`. W wydarzeniu: scenariusz (`ros.tsv`) i próby z `hq:event`; sygnały dźwięku i światła w scenariuszu dopasuj. Marka (ton dźwięku, kolory): `brandbook.md`.
Skala: **Mini** (jedna sala/jedno nagranie: cel, tor, lista sprzętu, test), **Standard**, **Pełna** (instalacja stała lub duże wydarzenie: komplet dokumentów).

## Etapy i bramki
| Etap | Wynik | Zatwierdza |
|---|---|---|
| AV1 Cel i wymagania: cel, odbiorcy, miejsce odtwarzania/oglądania, wymagania techniczne i prawne, budżet, czas, wrażenie, priorytety | `brief.md` | **użytkownik** |
| AV2 Analiza przestrzeni: akustyka (odbicia, pogłos, rezonanse, szum tła, odsłuch, izolacja) i/lub światło (geometria, wysokość, punkty zawieszenia, nośność, zasilanie, światło dzienne, materiały, strefy pracy, serwis) | notatki z pomiarów/oględzin | - |
| AV3 Koncepcja: tor sygnałowy i strefy nagłośnienia / strefy światła, funkcje, poziomy, kolory, scenariusze | `signal-flow.md`, koncepcja światła | **użytkownik** |
| AV4 Obliczenia: RT60, tryby własne, pokrycie i SPL, bilans dynamiki / fotometria, obciążenia, adresacja DMX | wyniki `avcalc.py` | - |
| AV5 Sprzęt: wg funkcji, parametrów, niezawodności, zgodności z torem, serwisu, kosztu całkowitego (zakup vs wynajem) | `equipment.tsv` | **użytkownik** (koszty) + przegląd |
| AV6 Projekt instalacji: rozmieszczenie, zasilanie, okablowanie, separacja zasilania i sygnałów, sterowanie, adresacja, zapasowe tory, plan riggingu, ocena ryzyka, procedury awaryjne | schematy, plan montażu | **użytkownik** + uprawniona osoba |
| AV7 Montaż, nagranie/programowanie: kontrole sprzętu, mocowań, linek bezpieczeństwa, kabli; nagranie lub programowanie scen i kolejek | wykonanie przez ludzi, log | - |
| AV8 Obróbka audio: edycja, czyszczenie, miks, mastering | sesje, pliki | przegląd odsłuchu |
| AV9 Testy i strojenie: każdy tor osobno, polaryzacja, pokrycie, opóźnienia, sprzężenia / kolory, ściemnianie, ruch, synchronizacja; próba z programem i awaryjnymi scenariuszami | `tests.md` | **użytkownik** |
| AV10 Obsługa na żywo: realizacja scenariusza, reagowanie na zmiany, monitoring, awarie, współpraca z pozostałymi | log dnia | - |
| AV11 Kontrola jakości i dostawa: czytelność, przester, szum, spójność, wymagania platformy (LUFS/true peak), formaty i metadane, synchronizacja | raport QC | **użytkownik** |
| AV12 Demontaż i dokumentacja: demontaż, stan sprzętu, usterki, aktualizacja dokumentacji, wnioski | dokumentacja | - |
Przeglądy AV3, AV6, AV11: `hq:design-reviewer`. Po bramkach: `hq:context`.

## Definicja gotowości
Cel i wrażenie zatwierdzone · przestrzeń przeanalizowana · obliczenia wykonane skryptem · tor/schematy kompletne z zapasowymi torami · rigging, elektryka i limity głośności zweryfikowane przez uprawnione osoby (lub oznaczone DO WERYFIKACJI) · każdy tor przetestowany · próba z programem · plan awaryjny · dokumentacja i kopie zapasowe · (audio do dostawy) pomiar głośności względem specyfikacji platformy.
