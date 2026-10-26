# Kolor marki: proces (B3)

Kolor wynika ze strategii (B1), nie z gustu. Wynik to **system ról**, nie lista ładnych barw.

## Proces K1-K8
1. **Wejście z B1:** osobowość, emocja docelowa, odbiorca, miejsca użycia (ekran, druk, produkt, wideo). Brak B1 = stop.
2. **Mapa kategorii:** kolory 5-8 konkurentów i konwencje branży (agent `researcher`, źródła). Wynik: co zajęte, gdzie dopasować się (zaufanie), gdzie odróżnić (pamięć). Zwykle: znajoma baza + jeden nieoczekiwany akcent.
3. **Skojarzenia** (kulturowe, nie prawa): niebieski zaufanie/spokój · czerń prestiż · zieleń zdrowie/wzrost · czerwień energia/pilność · pomarańcz energia/kreatywność · żółty optymizm (słaby kontrast na bieli) · fiolet luksus/kreatywność · brąz rzemiosło/ciepło · szarość technologia · biel przestrzeń. Ryzyka: generyczność (niebieski), "eko" (zieleń), tanio (pomarańcz).
4. **Harmonia:** monochromat (premium, minimalizm) · analogiczna (spokój) · komplementarna (jeden dominuje, drugi akcent) · split-complementary (wyraziście, nie agresywnie) · triada tylko z dyscypliną.
5. **Trzy pokrętła:** barwa, nasycenie (wysokie = energia, średnie = profesjonalizm, niskie = elegancja/premium), jasność. Dwa odcienie tej samej barwy działają różnie po zmianie jasności.
6. **2-4 warianty do wyboru** (Figma, `figma.md`), każdy z uzasadnieniem ze strategii i ryzykiem. Wybór wg kryteriów, zapis w `decisions.md`.
7. **Rozbudowa do systemu:** kolor główny (jeden, rozpoznawalny, działa w mono) · pomocniczy (wspiera, nie konkuruje: ciemniejszy/jaśniejszy odcień, sąsiad na kole) · akcent (rzadki, tylko CTA/link/alert/focus; jeden na widok) · neutralne (biel, złamana biel, szarości, grafit) · stany (sukces, ostrzeżenie, błąd, info, nieaktywny, focus, hover) w barwach **innych niż marka**. Dla każdego koloru wersja na jasne i ciemne tło, obraz, mono, tryb ciemny.
8. **Testy i zapis:** `scripts/contrast.py` dla każdej pary tekst/tło, przycisku, ikony, linku, focusu (tekst 4,5:1, duży 3:1, elementy UI 3:1); symulacja zaburzeń widzenia barw; wersja mono; test w realnych punktach styku (logo 16 px, favicon, www, e-mail, social, slajdy, druk, produkt). Zapis: HEX/RGB/CMYK/Pantone (CMYK i Pantone **DO WERYFIKACJI** na próbce wydruku), proporcje, dozwolone i zakazane kombinacje, przykłady poprawne i błędne.

## Zasady
- Proporcje 60/30/10 (dominujący/pomocniczy/akcent) jako punkt wyjścia; akcent działa tylko, gdy rzadki.
- Przyciąga kontrast, nie jaskrawość: jasne na ciemnym, jeden nasycony wśród neutralnych, zmiana temperatury.
- Informacji nie niesie sam kolor: dodaj ikonę, tekst lub kształt.
- Kolor marki nie służy komunikatom błędu/sukcesu.
- Jeden odcień na wszystkich materiałach: wartości tylko z tokenów (zmienne Figmy, `tokens.css`); `brandscan.py` łapie dryf.

## Błędy do wyłapania
Kolor z gustu założyciela · za dużo kolorów · brak neutralnych · akcent wszędzie · brak wersji mono/ciemnej · brak testu kontrastu · kopia konkurenta bez strategii · odcienie zmieniane per materiał · kolor jako jedyny nośnik informacji · trend zamiast strategii · brak dokumentacji wartości.
