# Reguły systemu wizualnego i języka (dla agentów marki)

## Logo - proces i testy
Szkice (3-4 koncepcje) -> wybór 1-2 -> opracowanie wektorowe -> testy: bardzo małe (np. 16 px ikona, 10 mm druk) i duże · czarne, białe, kolorowe, mono · jasne i ciemne tło · poziom, pion, sygnet · czytelność i dostępność. Wynik w brandbooku: wersje, pole ochronne (np. wysokość litery), minimalny rozmiar, proporcje, wyrównanie, **błędne użycia** (rozciąganie, zmiana kolorów, cienie, zbyt małe, nieczytelne tło), formaty (SVG, PNG, PDF).
Szkice SVG tworzone tu są **koncepcjami**; finalny znak do produkcji wymaga dopracowania wektorowego (krzywe, optyka, kerning) i sprawdzenia prawnego - oznacz DO WERYFIKACJI.

## Kolor
Paleta wynika ze strategii, emocji, branży, czytelności i zastosowań, nie z gustu. Role: podstawowe (1-2) · pomocnicze · akcentowe (rzadko) · neutralne (skala szarości/odcienie) · stanów. Proporcje (np. 60/30/10). Zapis: HEX + RGB + CMYK + Pantone. CMYK i Pantone z konwersji są **przybliżone** (DO WERYFIKACJI na próbce wydruku). Kontrast: `python3 <katalog skilla>/scripts/contrast.py <HEX> <HEX> ...`; tekst zwykły co najmniej AA (4,5:1), duży tekst (3:1), cele: AAA tam, gdzie się da. Nie opieraj znaczenia wyłącznie na kolorze.

## Typografia
Max 2 rodziny (+ ewentualnie mono). Rola: nagłówki, tekst, interfejs. Wymagane: polskie znaki, grubości, hierarchia z wartościami (rozmiar/interlinia/odstępy), skala typograficzna, zasady ekran/druk, licencje (preferuj otwarte: Google Fonts/SIL OFL; płatne - opisz licencję), fonty zastępcze systemowe.

## Fotografia, ilustracja, ikony
Emocje, światło, kadry, kolorystyka, tematy; co wolno i czego nie (z przykładami błędnymi). Ikony: siatka, grubość linii, narożniki, wypełnienie - jeden styl.

## Elementy pomocnicze
Siatki, marginesy, odstępy (skala np. 4/8/16), wzory, linie, animacje (czas, easing, zasady), komponenty UI (przyciski, pola, stany), szablony dokumentów i prezentacji.

## Język
Głos = cechy osobowości przełożone na zdania. Zapis: nazwa marki (wielkość liter), skróty, forma zwracania się. Słownik: preferowane / zakazane. Komunikaty: każdy typ (powitanie, sukces, błąd, ostrzeżenie, pusty stan, reklamacja, status, aktualizacja) w 1-2 przykładach "tak" i "nie". Błędy: mówią co się stało i co zrobić, bez winienia użytkownika. Nazwa: łatwa do wymówienia i zapamiętania, możliwa do ochrony, dostępna domena, bez niechcianych znaczeń w innych językach; wstępne sprawdzenie w wyszukiwarce, rejestrach znaków (np. EUIPO, UPRP) i domenach - **to nie porada prawna**, ostateczną ocenę robi rzecznik patentowy (listy IP: `hq:legal-safety`).

## Zastosowania - zasada
Kierunek musi działać nie tylko na plakacie: mały ekran, opakowanie, dokumentacja, produkt. Pokaż mockup dla każdego realnego kanału i zapisz poprawki w brandbooku.

## Spójność i utrzymanie
Wersjonowanie (numer + data), jeden właściciel, proces wyjątków, przegląd okresowy. Odświeżenie (kolory, typografia, szablony) vs rebranding (zmiana strategii, oferty, grupy lub pozycji).
