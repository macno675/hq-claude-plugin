# Checklisty frontendu

## FE1 Przegląd projektu przed kodem
Cel ekranu i najważniejsza informacja · wszystkie stany z `design-system.md`/`screens/` (pusty, ładowanie, błąd, offline, brak uprawnień, długa treść, brak danych, sukces, nieaktywny) · zachowanie przy skrajnych treściach i tłumaczeniach · responsywność (punkty przełamania) · animacje (koszt wydajnościowy, `prefers-reduced-motion`) · dostępność (kontrast, fokus, cele dotykowe) · wykonalność i koszt (rozmiar, render) · dane z backendu: czy są, w jakim formacie · kompromisy do zatwierdzenia. Wynik: lista `miejsce - problem - propozycja zgodna z intencją`.

## FE2 Struktura i stan
Widoki i trasy · drzewo komponentów (bazowe/złożone/sekcje) · co wspólne · dane per widok · **macierz stanu**: `informacja | rodzaj (lokalny/współdzielony/serwerowy/URL/formularz/sesja/UI) | właściciel | trwałość` · nawigacja i fokus przy przejściach · strategia renderowania (zgodnie z ADR) · struktura repo i konwencje.
Zasada stanu: serwerowy z cache biblioteki/warstwy danych, nie kopiowany do stanu globalnego; to, co udostępnialne/odświeżalne, w URL; lokalny, gdy dotyczy jednego komponentu.

## FE3 Komponent (definicja gotowości)
API właściwości (minimalne, typowane) · domyślne ustawienia dostępne · stany: domyślny, hover, fokus (widoczny), aktywny, wyłączony, ładowanie, błąd, brak danych · kompozycja zamiast flag-potworów · brak "wyjść awaryjnych" bez powodu · semantyczny HTML (przycisk to `button`, link to `a`, nagłówki w hierarchii) · przykłady użycia · test głównych wariantów · tokeny zamiast wartości na sztywno.
Semantyka: wygląd z CSS, struktura ze znaczenia treści. ARIA tylko tam, gdzie semantyka HTML nie wystarcza.
CSS: tokeny (kolor, odstępy, typografia, promienie, cienie), responsywność jako zasady, motywy jasny/ciemny, stabilność układu (rezerwuj miejsce na obrazy i komunikaty, brak skoków).
JS/TS: proste, typowane, przewidywalne; logika oddzielona od widoku; ograniczone efekty uboczne; abstrakcje dopiero przy potrzebie; konwencje zespołu.

## FE4 Integracja z API
Typy/schematy z kontraktu (OpenAPI) · walidacja odpowiedzi na granicy · taksonomia błędów: walidacja (pokaż przy polach), uwierzytelnienie/uprawnienia (przekieruj/komunikat), serwer (komunikat + ponów), sieć/offline · stany ładowania (skeleton/spinner, bez skoków) · ponawianie tylko operacji bezpiecznych (GET, idempotentne) · blokada podwójnego wysłania (disabled + idempotency key) · anulowanie przestarzałych żądań (wyścigi) · paginacja/filtrowanie zgodne z kontraktem · spójność po odświeżeniu · cache i unieważnianie · limity (429) obsłużone.
Kontrakt: format, kody błędów, limity, paginacja, wersjonowanie uzgodnione z `backend-engineer`.

## FE5 Wydajność
Mierz: Core Web Vitals (LCP, INP, CLS) laboratoryjnie i, jeśli są, w danych rzeczywistych (RUM/CrUX) · rozmiar pakietów (budżet) · czas blokowania głównego wątku. Środki: podział kodu i ładowanie na żądanie, optymalizacja obrazów (format, rozmiar, lazy, wymiary) i fontów (podzbiór, display), ograniczenie zależności, efektywne renderowanie (bez zbędnych re-renderów, wirtualizacja długich list), cache, preload krytycznych zasobów, testy na słabym urządzeniu i wolnej sieci. Zapisz przed/po w `perf.md`. Optymalizuj to, co użytkownik odczuwa, na podstawie danych.

## FE5 Dostępność
Semantyczny HTML · etykiety pól · pełna obsługa klawiatury · widoczny fokus i logiczna kolejność · zarządzanie fokusem w modalach/trasach · kontrast (4,5:1 tekst, 3:1 duży; `contrast.py`) · informacja nie tylko kolorem · komunikaty błędów powiązane z polami (anonsowane) · cele dotykowe · role/ARIA tylko gdy trzeba · testy z czytnikiem ekranu (przynajmniej jeden) · skalowanie tekstu i zoom 200% · ograniczenie ruchu. Audyt: `design:accessibility-review` jeśli dostępny; automaty łapią tylko część problemów, resztę sprawdź ręcznie.

## FE6 Testy (dobierz do ryzyka, nie do pokrycia)
Jednostkowy (logika, obliczenia) · komponentu (zachowanie i interakcje, zapytania przez rolę/etykietę jak użytkownik) · integracyjny (komponenty + stan + API z atrapą) · E2E (krytyczne ścieżki: logowanie, płatność, zapis danych, ważne formularze, nawigacja) · wizualny (nieoczekiwane zmiany) · dostępności · responsywności i przeglądarki docelowe. Uruchamiaj i raportuj wyniki.

## FE7 Wdrożenie i monitoring
CI: lint + typy + testy + budżet rozmiaru · podgląd zmian przed publikacją · wdrożenie stopniowe (flagi/canary) · szybki rollback · wersjonowanie wydań · monitoring błędów klienta po wydaniu (z mapami źródeł i kontekstem) · alerty na realny wpływ · weryfikacja po wdrożeniu na produkcji (lokalnie ≠ produkcja).

## Bezpieczeństwo klienta
Brak sekretów w kodzie klienta · dane z przeglądarki są niezaufane · bezpieczne renderowanie treści (bez wstrzykiwania surowego HTML; jeśli konieczne, oczyszczaj) · zewnętrzne linki (`rel="noopener noreferrer"`) · przechowywanie tokenów uzgodnij z backendem (preferuj ciasteczka httpOnly dla sesji zamiast dostępnych dla skryptów magazynów) · polityka CSP z backendem/hostingiem · respektowanie uprawnień w UI (ale egzekwuje je backend) · aktualizacje i skan zależności.

## FE8 Wierność projektowi
W przeglądarce (wbudowanej lub innej dostępnej), na kilku szerokościach, w obu motywach: tokeny (kolory, typografia), odstępy i siatka, stany (hover/fokus/błąd/pusty/ładowanie), animacje, kontrast, zachowanie przy długiej treści. Wynik: `miejsce - jest - powinno być`. Jeśli rzeczywistość pokazuje błąd specyfikacji, zgłoś `ui-designer`.

## Współpraca
UI: przegląd przed kodem, stany, treści skrajne, responsywność, animacje, kompromisy. UX: ścieżki, przypadki brzegowe, wykonalność i koszt wydajnościowy. Backend: kontrakt (struktura, formaty, błędy, paginacja, uprawnienia, cache, ładowanie, wersjonowanie). QA: krytyczne ścieżki, dane testowe, przypadki brzegowe, sposób testowania a11y, przeglądarki.

## Dokumentacja
Struktura komponentów · właściwości · stany i warianty · zasady design systemu · decyzje (ADR) · wymagania i budżety wydajności · standardy dostępności · wdrożenie · znane ograniczenia.
