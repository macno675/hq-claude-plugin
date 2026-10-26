# Ramy cyberbezpieczeństwa

## Model zagrożeń (`threat-model.md`)
Dla przepływu/komponentu: zasoby -> granice zaufania -> aktorzy (zewnętrzny atakujący, użytkownik z uprawnieniami, wtajemniczony, dostawca) -> zagrożenia (STRIDE: podszycie, manipulacja danymi, wyparcie się, ujawnienie informacji, odmowa usługi, podniesienie uprawnień) -> skutek -> istniejące środki -> brakujące -> priorytet (`riskscore.py`). Pytania: kto atakuje i po co? co chce przejąć? gdzie system jest najsłabszy? co się stanie po udanym ataku? jak ograniczyć skutek? Aktualizuj przy zmianie architektury.

## Lista środków ochronnych (Protect)
Tożsamość: MFA, brak współdzielonych kont, przegląd uprawnień, natychmiastowe odebranie dostępu przy odejściu · Dostęp: najmniejsze uprawnienia, RBAC, rozdzielenie środowisk (dev/test/prod) · Dane: klasyfikacja, szyfrowanie w tranzycie i spoczynku, minimalizacja, retencja, usuwanie · Sekrety: menedżer sekretów/zmienne środowiskowe, rotacja, brak w repo i logach, osobne klucze per środowisko · Konfiguracja: bezpieczne domyślne, utwardzanie, brak domyślnych haseł, minimalna powierzchnia ataku (wyłącz nieużywane usługi i porty) · Aktualizacje: regularne łatanie, skan zależności i obrazów, przypinanie wersji · Sieć: segmentacja, zapora, brak publicznej ekspozycji paneli administracyjnych · Końcówki: szyfrowanie dysku, blokada ekranu, ochrona przed złośliwym oprogramowaniem · Backup: reguła kilku kopii, w tym odłączona/niezmienialna, **test odtworzenia** · Ludzie: szkolenie z phishingu, procedura zgłaszania, kultura bez karania za zgłoszenie · Wdrożenia: CI/CD z testami i skanami, podpisywanie artefaktów, kontrola zmian.

## Secure SDLC
Wymagania bezpieczeństwa -> przegląd architektury i threat modeling -> bezpieczne wzorce (walidacja wejścia, parametryzowane zapytania, kodowanie wyjścia, authz na zasobie) -> przegląd kodu (`security-review`) -> skan zależności, sekretów i kodu (SAST) w CI -> testy bezpieczeństwa (w tym negatywne) -> priorytetyzacja podatności wg ryzyka -> naprawa z terminem -> weryfikacja poprawki -> szkolenie. Bezpieczeństwo uczestniczy od wymagań do wdrożenia.

## Bezpieczeństwo produktu i urządzeń połączonych
Unikalne poświadczenia urządzenia (brak haseł domyślnych) · bezpieczny rozruch i aktualizacje (podpis, weryfikacja, wycofanie, ochrona kluczy podpisu) · szyfrowana komunikacja i uwierzytelnianie urządzenie-chmura · ograniczenie interfejsów debugowania w produkcji · przechowywanie sekretów w sprzęcie jeśli możliwe · SBOM/lista komponentów i śledzenie podatności zależności · proces przyjmowania zgłoszeń podatności i okres wsparcia aktualizacjami · prywatność użytkownika (minimalizacja, retencja) · zgodność prawna (`hq:legal-safety`).

## Detect
Centralne zbieranie logów (z zachowaniem prywatności) · monitoring sieci i końcówek · alerty o znaczeniu operacyjnym (nie szum) z właścicielem i runbookiem · analiza anomalii i korelacja zdarzeń · wskaźniki kompromitacji · monitorowanie uprawnień i nietypowych logowań · alerty o wygaśnięciu certyfikatów.

## Respond (plan incydentu `ir-plan.md`)
Role (dowodzący, techniczny, komunikacja, kontakt prawny) i zastępcy · kanały komunikacji awaryjnej poza systemem, który może być skompromitowany · klasyfikacja ważności · kroki: potwierdź -> oceń skalę i wpływ -> izoluj -> powstrzymaj rozprzestrzenianie -> zabezpiecz dowody (logi, obrazy; nie nadpisuj) -> usuń przyczynę -> komunikuj interesariuszom -> powiadom organy/osoby jeśli wymagane (`hq:legal-safety`, zegar zaczyna biec od stwierdzenia) -> analiza przyczyny źródłowej -> poprawki. Każdy krok zmieniający środowisko zatwierdza człowiek. Przećwicz scenariusz (np. wyciek klucza, ransomware, przejęcie konta) w ćwiczeniu na sucho.

## Recover (`backup-plan.md`)
Co jest krytyczne, RPO/RTO, lokalizacje kopii, kto i jak odtwarza, kolejność odbudowy, zmiana wszystkich poświadczeń i kluczy, weryfikacja czystości środowiska (brak powrotu tej samej podatności), testy usług przed uruchomieniem dla użytkowników, komunikacja, analiza po incydencie, aktualizacja planu i rejestru ryzyk.

## Podatności (`vulns.tsv`)
Źródła: skany, pentesty, zgłoszenia, alerty zależności. Priorytet = ryzyko (prawdopodobieństwo wykorzystania x wpływ x ekspozycja zasobu), nie sama ocena techniczna ani liczba znalezisk. Termin naprawy zależny od ważności; wyjątki z uzasadnieniem i środkiem zastępczym; weryfikacja poprawki.

## Testy
Skan: systemy, aplikacje, zależności, kontenery, chmura, konfiguracje, certyfikaty, uprawnienia (narzędzia zainstalowane lub zalecone). Testy penetracyjne: **tylko za pisemną zgodą**, z zakresem, oknem czasowym, kontaktami i zasadami (bez destrukcji, bez danych produkcyjnych jeśli możliwe); wynik z priorytetyzacją ryzyka. Testy ludzi: symulacje phishingu za wiedzą zarządu, instrukcja zgłaszania, brak karania.

## Współpraca
Zarząd/użytkownik: ryzyka w języku biznesu (co zagrożone, koszt incydentu, priorytety, decyzje). Produkt: bezpieczeństwo funkcji, dane, kompromisy wygoda-ochrona. Backend/frontend: bezpieczne API, authn/authz, ochrona danych, błędy, aktualizacje. DevOps: infrastruktura, CI/CD, sekrety, konfiguracja, monitoring. Prawo/compliance: wymagania, ochrona danych, obowiązki po naruszeniu. PM: bezpieczeństwo w harmonogramie, budżecie, ryzykach, kryteriach akceptacji. AI: `hq:ai-strategy` (prompt injection, uprawnienia agentów).

## Dokumentacja
Inwentaryzacja zasobów · rejestr ryzyk · polityki · standardy konfiguracji · procedury dostępu · plan reagowania i runbooki · plan backupu i odtwarzania · wyniki testów · rejestr podatności · dokumentacja incydentów · raporty. Aktualna, dostępna offline dla kluczowych osób (w kryzysie nie ma czasu na zgadywanie).
