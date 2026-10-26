# Typografia marki: proces (B3)

Font wyraża charakter marki i musi działać wszędzie, gdzie marka się pojawia. Wynik to **system typograficzny** (role, skala, zasady), nie jeden "ładny font".

## Proces T1-T10
1. **Wejście z B1:** osobowość, odbiorca, miejsca użycia (www, aplikacja, druk, opakowanie, ekran urządzenia, wideo), języki. Brak B1 = stop.
2. **Mapa kategorii:** fonty 5-8 konkurentów (agent `researcher`). Wynik: co zajęte, gdzie dopasować się, gdzie odróżnić. Nie kopiuj fontu konkurenta.
3. **Charakter:** serif wyrazisty (editorial, premium, kultura) · geometryczny sans (tech, produkt) · neutralny/szwajcarski sans (korporacja) · grotesk z charakterem (kreatywni) · miękki sans (lifestyle). Trend ≠ strategia.
4. **Role** (max 2 rodziny, czasem + mono):
   - **podstawowy** ("koń roboczy"): tekst, interfejs, dokumenty; czytelny w małych rozmiarach, wiele grubości, bogate znaki diakrytyczne, najlepiej zmienny;
   - **display**: nagłówki, hasła, kampanie; wyrazista sylwetka, tylko duży rozmiar, nigdy długi tekst;
   - **mono** (opcjonalnie): kod, dane, dokumentacja, ekrany urządzeń;
   - **liczby** (finanse, dashboardy): tabular figures, rozróżnialne 1/6/8/9, wyraźne zero.
5. **Parowanie:** kontrast, nie podobieństwo. Dobre: serif display + neutralny sans; geometryczny sans + humanistyczny serif; wyrazisty display + prosty sans; mono + serif. Złe: dwa podobne sansy, dwa mocne displaye. Jedna rodzina zmienna (osie: waga, szerokość) często wystarcza.
6. **Źródła z jasną licencją** (zacznij tu, nie tylko Google Fonts): Fontshare (nowoczesne, produktowe), Velvetyne i Collletttivo (odważne, kultura, editorial), Uncut.wtf (nieoczywiste), Open Foundry, The League of Moveable Type, Font Squirrel (kontrola licencji), IBM Plex (komplet sans/serif/mono dla tech), Public Sans (czytelność, dużo tekstu). Przykładowe pary (punkt startu, nie rozwiązanie): tech = Clash Display + Satoshi; SaaS = General Sans + IBM Plex Mono; premium = Boska + Switzer; editorial = Melodrama + Erode; korporacja = Switzer + IBM Plex Mono. Dostępność, wsparcie polskich znaków i licencje **sprawdź u źródła** (nie z pamięci): DO WERYFIKACJI.
7. **2-4 warianty do wyboru** (Figma, `figma.md`): ten sam nagłówek i akapit w każdym, z uzasadnieniem ze strategii. Wybór i powód w `decisions.md`.
8. **Skala i hierarchia:** H1-H6, tekst, podpis, przycisk, link, liczba, alert: rozmiar/interlinia/waga/odstęp (punkt startu: H1 48-72, H2 32-40, H3 24-28, tekst 16-18, small 14, caption 12 px). Wersja mobilna i ciemny tryb.
9. **Testy:** 12/14/16/18 px, długi akapit, przycisk, tabela, ciemny tryb · polskie znaki (ą ć ę ł ń ó ś ź ż, wielkie i małe), cudzysłowy, myślniki, cyfry · parowanie display + tekst w nagłówku, karcie, banerze, e-mailu, prezentacji, aplikacji · kontrast tekstu (`scripts/contrast.py`).
10. **Licencja** (zapis w brandbooku): komercyjne użycie, w logo, w aplikacji, osadzanie na www (webfont), druk, modyfikacje, wymóg podania autora, limity (odsłony, urządzenia). "Darmowy" ≠ "darmowy komercyjnie". Zapisz źródło, wersję i plik licencji. Zamiennik awaryjny (fallback) dla www.

## Zasady
- Charakter przed modą, czytelność przed efektem, system przed pojedynczym fontem.
- Display tylko w nagłówkach; długi tekst zawsze fontem podstawowym.
- Ruch (kinetic) krótko, bez długich tekstów, zawsze wersja statyczna.
- Fonty zmienne dla wydajności i spójności; ładuj tylko używane osie/wagi.
- Tokeny typografii (rodzina, rozmiar, interlinia, waga) w zmiennych Figmy i `tokens.css`.

## Błędy do wyłapania
Font z gustu · za dużo rodzin · dwa podobne sansy · display w długim tekście · brak polskich znaków · brak testu małych rozmiarów · brak licencji komercyjnej · font bez wersji webowej · zbyt luźny tracking lub ciasna interlinia · kopia konkurenta · wybór, bo popularny.
