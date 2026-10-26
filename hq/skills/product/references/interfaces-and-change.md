# Interfejsy i kontrola zmian

## Specyfikacja interfejsów (`interfaces.md`, właściciel: architekt)
Jeden wiersz = jedno połączenie między modułami/dyscyplinami. TSV:
`id | od -> do | co przekazuje | forma (sygnał/protokół/format) | parametry (napięcie, tempo, dokładność, opóźnienie) | ograniczenia czasowe | zachowanie awaryjne | właściciel | status | test`
Przykłady rodzajów: elektronika<->firmware (piny, magistrale, przerwania, adresy), elektronika<->mechanika (gabaryty, otwory, złącza, ciepło), firmware<->UI (zdarzenia, stany), urządzenie<->aplikacja/chmura (protokół, wersje, aktualizacje, bezpieczeństwo).
Zasada: zmiana interfejsu = kontrola zmian, nigdy po cichu u jednej strony.

## Kontrola zmian (`changes.tsv`)
`id | data | opis (problem/potrzeba) | wpływ: elektronika/fw/algorytmy/mechanika/design/testy/produkcja | koszt | ryzyko | czas | decyzja (kto) | dokumenty zaktualizowane | test potwierdzający`
Procedura: opis -> analiza wpływu na KAŻDĄ dyscyplinę (agent z danej dyscypliny odpowiada za swoją linię) -> koszt/ryzyko/czas -> decyzja (większe: użytkownik) -> aktualizacja dokumentów -> test skuteczności. Mała zmiana lokalna w jednej dyscyplinie bez wpływu na interfejsy: zapis w `decisions.md` wystarczy.

## Dokumentacja wspólna (stała lista)
Wymagania · architektura · interfejsy · BOM · wersje oprogramowania · wyniki testów · decyzje · znane problemy · instrukcje produkcyjne. Zmiana w jednym miejscu = natychmiastowa aktualizacja pozostałych, które jej dotyczą.
