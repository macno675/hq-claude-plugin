# Ramy marketingowe

## Brief (`brief.md`)
Cel biznesowy · produkt/usługa/marka/wydarzenie · grupa docelowa · budżet · termin · konkurencja · dotychczasowe działania · dostępne dane · ograniczenia prawne i wizerunkowe · oczekiwany rezultat (liczbowo). Bez briefu kampania to zbiór przypadkowych działań.

## Odbiorcy (`audience.md`)
Źródła: rozmowy z klientami, ankiety, analityka strony, media społecznościowe, CRM, dane sprzedaży, opinie i recenzje, konkurencja. Segmenty/persony: kto, cele i problemy, jak decyduje, gdzie szuka informacji, co przekonuje, czego się obawia, ograniczenia, ścieżka od pierwszego kontaktu do decyzji (mapa podróży). Każdy wniosek z tagiem `[DOWÓD: źródło]` lub `[ZAŁOŻENIE]`; luki zamień w hipotezy do sprawdzenia testem.

## Pozycjonowanie i przekaz (`positioning.md`)
Dlaczego klient ma wybrać nas, a nie inną opcję? Wartość · problem, który rozwiązujemy · przewaga nad konkurencją · ton · główna obietnica · argumenty wspierające (dowody prawdziwe) · czego nie obiecujemy. Przekaz zrozumiały dla odbiorcy, nie dla twórcy; jedno główne wezwanie do działania.

## Kanały (dobór według celu, odbiorcy i budżetu)
Media społecznościowe · reklama płatna · wyszukiwarki (SEO/SEM) · e-mail · content marketing · PR · współprace z twórcami · wydarzenia · partnerstwa · outdoor · radio/TV/prasa · programy poleceń · marketing bezpośredni. Tabela: `kanał | rola w ścieżce | odbiorca | format | koszt | KPI | ryzyko`. Wybierz mieszankę i kolejność, nie wszystkie kanały.

## Plan kampanii (`plan.md`)
Cel główny · grupy docelowe · przekaz centralny · kanały i formaty · harmonogram i kalendarz (`calendar.tsv`: data | kanał | treść | odbiorca | właściciel | status) · budżet (podział, limity, próg zatrzymania) · osoby odpowiedzialne · **KPI ustalone przed startem** · plan testów · plan reagowania na wyniki (jeśli X to Y) · zależności (np. landing page gotowy przed reklamą, rejestracja działa).

## KPI (wybierz związane z celem)
Zasięg i świadomość · zaangażowanie · ruch · rejestracje · zapytania · leady (i ich jakość) · sprzedaż · koszt pozyskania (CPA/CAC) · zwrot z reklamy (ROAS/ROI) · retencja i lojalność. Obliczenia: `mkcalc.py kpi KOSZT WYŚWIETLENIA KLIKNIĘCIA KONWERSJE [PRZYCHÓD]`.

## Testy (`tests.md`)
Z góry: hipoteza, jedna zmienna, metryka decyzyjna, wielkość próby i czas, kryterium decyzji. Testuj: przekazy, kreacje, nagłówki, grupy, kanały, strony docelowe, godziny, formaty. Ocena: `mkcalc.py abtest N_A KONW_A N_B KONW_B`; nie zatrzymuj testu "gdy wygląda dobrze", nie testuj wielu rzeczy naraz bez korekty. Wynik p < 0,05 to wskazówka, nie dowód.

## Promocja wydarzenia (etapy)
1) Świadomość (wiedzą, że wydarzenie istnieje) · 2) zainteresowanie (dlaczego warto) · 3) decyzja (program, prelegenci/drużyny, korzyści, warunki) · 4) rejestracja (prosta, jasna, szybka; `hq:ux-ui`) · 5) przypomnienia · 6) zaangażowanie przed (oczekiwanie, społeczność) · 7) realizacja (doświadczenie potwierdza obietnice) · 8) po wydarzeniu (materiały, podziękowania, relacje, kolejna edycja). Kanały łączone, każdy wspiera kolejny etap decyzji. Współpraca z `hq:event` (EV: komunikacja, rejestracja) i `hq:partnerships` (sponsorzy w komunikacji).

## Idealna reklama (lista kontrolna)
Mówi do właściwej osoby · we właściwym miejscu i momencie · prostym językiem · pokazuje realną korzyść · wyróżnia się · spójna z marką · prowadzi do jednego jasnego działania · mierzalna · nie obiecuje więcej, niż produkt daje · zgodna z prawem (DO WERYFIKACJI). Trafna, nie najgłośniejsza.

## Treści i materiały
Komunikaty reklamowe, grafiki, wideo, teksty, landing page, e-maile, materiały prasowe, materiały wydarzenia i dla partnerów, prezentacje, treści do social media. Zgodne z brandbookiem; dostosowane do kanału i etapu decyzji; wersjonowane. Prawa do zdjęć/muzyki/fontów i zgody wizerunkowe sprawdzone.

## Analiza po kampanii (`reports/`)
Czy cel osiągnięty (KPI vs plan) · najlepsze kanały i grupy · skuteczne komunikaty · koszt pozyskania rezultatu · co zmienić · wnioski uniwersalne vs kanałowe · **decyzja** dla każdego działania: zwiększyć / zmienić / zatrzymać / wycofać · wiedza do `~/.hq/marketing-lessons.md`.

## Prawo i etyka (DO WERYFIKACJI, `hq:legal-safety`)
Reklama nie wprowadza w błąd · oznaczanie treści sponsorowanych i współprac · zgody na marketing elektroniczny i śledzenie · prawa autorskie i wizerunkowe · regulaminy konkursów i promocji · porównania z konkurencją · dane małoletnich. Brak fałszywych opinii, fałszywej rzadkości i innych manipulacji.

## Współpraca
Zarząd: rezultat, koszt, ryzyka, miary. Produkt: co gotowe do promocji, mocne strony i ograniczenia. Marka: brandbook. Sprzedaż/partnerstwa: wspólna definicja leada. Wydarzenie: harmonogram, komunikacja, rejestracja, obsługa, raport. Prawnik: zgodność reklam.

## Dokumentacja
Brief · persony i segmenty · pozycjonowanie · plan kanałów · kalendarz · budżet · KPI · briefy kreatywne · wersje materiałów · wyniki testów · raporty · wnioski.
