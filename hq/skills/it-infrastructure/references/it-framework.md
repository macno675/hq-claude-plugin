# Ramy infrastruktury IT

## Analiza potrzeb (`needs.md`)
Rola/użytkownik | zadania | oprogramowanie | dane (wolumen, wrażliwość) | miejsce pracy i mobilność | wymagania wydajnościowe | bezpieczeństwo | budżet | plan rozwoju. Pytaj użytkowników o realne obciążenie i sposób pracy, ale nie kupuj według osobistych preferencji.

## Standardy (`standards.md`)
Per rola: konfiguracja bazowa (CPU/RAM/dysk/ekran, system, gwarancja), akcesoria, oprogramowanie, okres użytkowania i wymiany, uzasadnienie. Role: biuro, grafik/inżynier/stacja robocza, laptop mobilny, serwer/NAS, urządzenia sieciowe, sprzęt konferencyjny/AV. Mało modeli = łatwiejszy serwis, bezpieczeństwo, licencje i prognoza.

## Dobór (kryteria)
Wydajność względem obciążenia · pamięć · dyski (typ, pojemność, szyfrowanie) · grafika · zasilacz · głośność i ciepło · mobilność/waga/bateria · trwałość · kompatybilność · rozbudowa · dostępność części i serwis · gwarancja i wsparcie producenta (jak długo aktualizacje) · pobór energii · wbudowane bezpieczeństwo (TPM, szyfrowanie, aktualizacje firmware) · cena całkowita. Wynik: tabela opcji 2-4 z TCO (`itcalc.py tco nazwa:zakup:koszt_roczny:lata[:odsprzedaż[:waty:godz_dzień]] --kwh CENA`).

## Dostawcy (`vendors.tsv`)
`dostawca | autoryzacja | cena (data) | termin | gwarancja | serwis | części | zwroty | wsparcie | stabilność | ocena | uwagi`. Kryteria obiektywne: specyfikacja, bezpieczeństwo, jakość, wsparcie, koszt całkowity.

## Przygotowanie po zakupie (lista kontrolna)
Wpis do inwentarza (numer seryjny, daty gwarancji i wsparcia) · instalacja systemu · konfiguracja bezpieczeństwa (szyfrowanie dysku, aktualizacje, MFA, najmniejsze uprawnienia, zapora, ochrona końcówki) · oprogramowanie i licencje · dołączenie do zarządzania · kopia zapasowa · konto użytkownika · test działania · przypisanie · dokumentacja. Wykonuje człowiek lub po zatwierdzeniu.

## Ewidencja i cykl życia
Cykl: analiza -> specyfikacja -> dostawca -> zakup -> konfiguracja -> wdrożenie -> monitoring -> konserwacja i aktualizacje -> naprawy/gwarancja -> przeniesienie/ponowne użycie -> bezpieczne wycofanie -> recykling. `inventory.tsv` (kolumny w nagłówku `itcalc.py`); kontrola: `itcalc.py inventory plik [--warn 90] [--eos 180]` flaguje wygasającą gwarancję i koniec wsparcia producenta. Harmonogram wymian w budżecie (`hq:budget`).

## Niezawodność
Zapasowe urządzenia · kopie zapasowe (kilka kopii, w tym poza miejscem, **test odtworzenia**) · procedura szybkiej wymiany · umowy serwisowe · zapas części · monitoring stanu · plan wymiany przed końcem wsparcia · procedury po awarii · udokumentowana kolejność odbudowy.

## Sieć (`network.md`)
Sieć przewodowa i Wi-Fi (pokrycie, pojemność, kanały) · routery i przełączniki · zapora · VPN · segmentacja (np. goście/biuro/urządzenia) · adresacja IP · kontrola dostępu · monitoring · kopie konfiguracji · aktualizacje firmware · diagramy. Dobra sieć: szybka, stabilna, bezpieczna, łatwa do diagnozy.
**Sieć na wydarzeniu:** liczba urządzeń i typ ruchu (rejestracja, płatności, streaming, wyniki na żywo), łącze główne i zapasowe, pokrycie hali, odseparowana sieć dla obsługi i dla gości, zasilanie awaryjne, punkt kontaktowy w dniu, próba przed wydarzeniem (`hq:event`).

## Serwery i dane
Serwery fizyczne i wirtualne, systemy, aktualizacje, kopie zapasowe, odtwarzanie po awarii, pojemność dysków, wydajność, bezpieczeństwo, dostęp do danych. Chmura vs lokalnie: decyzja przez `hq:tech-strategy`.

## Serwis
Diagnoza przyczyny -> opłacalność naprawy (porównaj z wymianą: koszt naprawy, wiek, gwarancja, ryzyko) -> gwarancja -> urządzenie zastępcze -> zabezpieczenie danych -> serwis -> dokumentacja -> aktualizacja inwentarza.

## Wycofanie (protokół)
Kopia lub migracja danych (potwierdzona) -> bezpieczne usunięcie danych odpowiednią metodą dla nośnika (szyfrowanie + kasowanie kryptograficzne, wielokrotne nadpisanie lub fizyczne zniszczenie, zgodnie z wymaganiami) -> cofnięcie uprawnień i licencji -> usunięcie z systemów zarządzania i monitoringu -> wpis w ewidencji -> recykling/sprzedaż/utylizacja zgodnie z przepisami (DO WERYFIKACJI) -> potwierdzenie zniszczenia danych od wykonawcy. Zwykłe "usunięcie plików" nie wystarcza. Wykonuje człowiek po potwierdzeniu.

## Dokumentacja
Inwentarz · przypisania · specyfikacje · umowy gwarancyjne i serwisowe · harmonogram wymian · licencje · konfiguracje sieci · diagramy · procedury awaryjne · historia napraw · plan budżetu sprzętowego.

## Współpraca
Zarząd: plan zakupów, koszty, ryzyka. Pracownicy: potrzeby, nie preferencje. Cyberbezpieczeństwo: konfiguracja, aktualizacje, dostęp, ochrona danych. Zakupy: dostawcy, negocjacje, umowy serwisowe. Finanse: budżet, amortyzacja, wymiany. Projekty i wydarzenia: sprzęt i infrastruktura na czas.
