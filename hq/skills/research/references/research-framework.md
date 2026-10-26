# Ramy researchu

## Brief (`brief.md`)
Cel · decyzja, którą wspiera · pytanie główne · pytania szczegółowe · odbiorca · zakres (co wchodzi, co nie) · okres analizy · wymagany poziom pewności · budżet i czas · format rezultatu · kryteria sukcesu · kryterium stopu. Dobry brief zapobiega zbieraniu materiałów "na zapas".

## Plan (`plan.md`)
Typy źródeł do przeszukania (oficjalne dokumenty i regulacje, raporty branżowe, publikacje naukowe, dokumentacja techniczna, bazy danych, archiwa, media branżowe, materiały firm, opinie użytkowników, fora i recenzje, eksperci, dane wewnętrzne) · słowa kluczowe i synonimy (także w innych językach) · kryteria włączenia/wykluczenia (okres, język, typ) · skala oceny jakości · sposób zapisu · przegląd postępu. Metody: research wtórny, wywiady, ankiety, analiza dokumentacji, testy produktów konkurencji, analiza danych.

## Ocena źródła (skala 1-5 per kryterium, zapis w `sources.tsv`)
Wiarygodność (znane, rzetelne?) · autorytet (wiedza i doświadczenie autora) · dokładność (poprawne, weryfikowalne dane) · aktualność · trafność (nasze pytanie i kontekst) · cel (nie ukryta reklama/propaganda) · stronniczość (interes w wniosku) · metodologia (jak powstały dane) · możliwość weryfikacji (źródła pierwotne dostępne).
Hierarchia (orientacyjnie): źródła pierwotne (akty prawne, dane urzędowe, dokumentacja producenta, publikacje recenzowane, dane własne) > opracowania wiarygodnych instytucji > media branżowe > materiały firm (interes!) > opinie/fora (sygnał, nie dowód).

## Rejestr źródeł (`sources.tsv`)
`id | tytuł | autor/instytucja | data publikacji | data dostępu | url | typ (pierwotne/wtórne) | wiarygodność 1-5 | stronniczość/interes | użyte w (finding id) | uwagi`

## Rejestr ustaleń (`findings.tsv`)
`id | twierdzenie | rodzaj (fakt/dane/opinia/hipoteza) | źródła (id) | pewność (wysoka/średnia/niska) | sprzeczności | wpływ na decyzję`

## Triangulacja (lista kontrolna)
Zgodność niezależnych źródeł · czy dane pochodzą z pierwotnego źródła (nie z cytatu cytatu) · czy liczby mają metodologię · czy cytat nie jest wyrwany z kontekstu · czy informacja nie jest nieaktualna · czy nie ma nowszego/lepszego źródła · czy "niezależne" źródła nie kopiują jednego raportu.

## Rodzaje researchu (co analizować)
- **Rynek:** wielkość, trendy, grupy odbiorców, potrzeby, ceny, kanały, bariery wejścia, zmiany regulacyjne.
- **Konkurencja:** bezpośredni i pośredni (rozwiązują ten sam problem inaczej); produkty, mocne/słabe strony, model biznesowy, cena, komunikacja, UX, opinie, pozycjonowanie. Produkty: macierz porównawcza (kryteria x konkurenci), SWOT.
- **Technologia:** dostępne rozwiązania, dojrzałość, koszty, ryzyka, dokumentacja, wsparcie, alternatywy, trendy, cykl życia (współpraca z `hq:tech-strategy`).
- **Użytkownicy:** potrzeby, problemy, zachowania, opinie, motywacje, bariery (współpraca z `hq:ux-ui`, `hq:data-analysis`).
- **Prawo i regulacje:** przepisy, normy, licencje, wymogi produktowe, obowiązki, interpretacje i wytyczne; źródła pierwotne; wynik jako informacja, wiążące ustalenia `DO WERYFIKACJI` (`hq:legal-safety`).
- **Przedwydarzeniowy:** grupa docelowa, oczekiwania uczestników, konkurencyjne wydarzenia, miejsca, dostawcy, ceny, trendy, ryzyka logistyczne (`hq:event`).

## Synteza
Co pewne (wysoka pewność) · co prawdopodobne · co niepewne · gdzie źródła się zgadzają / różnią (i dlaczego) · wzorce · wnioski wynikające z całości · luki w wiedzy i jak je zamknąć. Łącz dane ilościowe i jakościowe w jedną narrację.

## Raport (`report.md`)
Streszczenie decyzyjne (3-5 linii) · pytanie i zakres · metoda i źródła (skrót) · wnioski z poziomem pewności i dowodami · porównania (tabele) · sprzeczności i ograniczenia · ryzyka · opcje i rekomendowany kierunek · luki i kolejne pytania · aneks: `sources.tsv`. Wersje dla odbiorców: zarząd (krótko: co wiemy, co niepewne, opcje, rekomendacja), produkt (szczegóły i możliwości), inżynierowie (dane techniczne i porównania), marketing (trendy, odbiorcy, komunikacja), prawnik (akty i źródła pierwotne).

## Baza wiedzy
Brief, pytania, lista źródeł, notatki, ocena wiarygodności, cytaty i linki, daty dostępu, wersje, wnioski, rekomendacje, luki, historia decyzji. Cel: inna osoba odtworzy tok rozumowania i sprawdzi, skąd pochodzi każdy wniosek. Skrót ustaleń o trwałej wartości: `~/.hq/knowledge/`.
