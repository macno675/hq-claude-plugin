# Design, feeling i feedback (dla `industrial-designer`)

**Marka (skill `hq:brand`) jest nadrzędna:** kolory, typografia, ton i osobowość pochodzą z `brandbook.md`; tu tłumaczysz je na produkt (sterowanie, dźwięk, haptyka, stany). Sekcja 9 brandbooka ("Produkt") jest wspólna - uzupełniaj ją, nie dubluj.

## Karta feelingu (jedna na produkt, `.hq/product/design.md`)
Marka: nazwa, ton, kolory, materiały, wykończenia · Charakter: 3-5 przymiotników (np. solidny, cichy, precyzyjny) · Kształt i proporcje · Sterowanie: przyciski (skok, opór, klik), pokrętła (opór, skoki), dotyk · Dźwięk (kliknięcia, sygnały), haptyka · Ekran/LED: reakcja, animacje, jasność · Stan gotowości i włączanie · Wrażenie solidności (waga, luzy, spasowanie).
Każdy punkt ma uzasadnienie z funkcji i marki oraz sposób weryfikacji (próbka, test użytkownika).

## Projekt feedbacku (tabela stanów)
Wiersze: włączenie · gotowość · potwierdzenie czynności · oczekiwanie/przetwarzanie · ostrzeżenie · błąd (naprawialny) · awaria · niski poziom baterii/ładowanie · aktualizacja · wyłączenie.
Kolumny: LED (kolor/wzór) · dźwięk · haptyka · ekran/tekst · aplikacja.
Zasady: natychmiastowy (< ok. 100 ms dla reakcji na dotyk), zrozumiały bez instrukcji, spójny w całym produkcie, nie przeciążający; **nie jeden kanał** dla stanów krytycznych (kolor + wzór/dźwięk; dostępność dla daltonistów i głuchych). Stany wymagają realizacji w sprzęcie (piny LED/buzzera, driver haptyki) - przekaż architektowi jako wymagania interfejsu.

## UX/UI
Prowadzi je skill `hq:ux-ui` (agenci `ux-designer` i `ui-designer`); tu zostają tylko wymagania wspólne ze sprzętem. Zasady w skrócie: ścieżki użytkownika, logika funkcji, minimalna liczba kroków, komunikaty błędów mówią co zrobić, ekrany i stany wszystkich przypadków (puste, ładowanie, błąd), dostępność (kontrast, rozmiar), test z realnym użytkownikiem na wczesnym prototypie.

## Integracja z elektroniką i mechaniką
Rozmieszczenie przycisków/LED/wyświetlacza, światłowody, szczelność, grubości ścianek i dostęp serwisowy ustalane razem z mechaniką i PCB (wymagania do `interfaces.md`), nie po fakcie.
