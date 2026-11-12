# Szablony promptów do zewnętrznych AI

Wypełnij nawiasy, usuń zbędne linie. Krótko i konkretnie: kontekst w 2-4 zdaniach, nie cała historia projektu. Nazwy trybów w aplikacjach się zmieniają - podaj najbliższy odpowiednik (np. "Deep Research" bywa nazwany "Research").

## Perplexity: zwykłe wyszukiwanie
```
Context: [2-3 zdania: czego dotyczy projekt i jaka decyzja od tego zależy].
Question: [jedno pytanie główne].
Also answer: [1-3 podpytania].
Scope: [kraj/rynek], [okres, np. 2025-2026], [typ źródeł: dokumentacja producenta, normy, badania, recenzje].
Output: short answer first, then a table [kolumny]. Cite a source URL and publication date for every claim. Prefer primary sources. If sources disagree or data is missing, say so explicitly. Answer in Polish.
```

## Perplexity: Deep Research
```
Goal: I need to decide [decyzja] for [krótki opis projektu, bez nazw własnych].
Main question: [pytanie główne].
Sub-questions:
1. [...]
2. [...]
3. [...]
Constraints: [budżet, region, technologia, termin].
Scope: [okres], [rynek], include [typy źródeł], exclude [marketing bez danych, źródła bez daty].
Method: compare at least [N] options/competitors; triangulate key numbers across independent sources; list contradictions and gaps.
Output (in Polish):
1. Executive summary (5 bullets) with confidence level (high/medium/low) per bullet.
2. Comparison table: [kolumny, np. option | price | key features | pros | cons | source].
3. What is certain / probable / uncertain.
4. Recommendation for my situation and open questions.
Every claim needs a URL and date. Do not invent numbers; write "no data" instead.
```

**Wzorce:** konkurencja (`kolumny: firma | oferta | cena | segment | przewaga | słabość | źródło`), "jak to powinno wyglądać/działać" (`najlepsze przykłady z linkami + wspólne zasady + błędy, których unikać`), technologia (`dojrzałość, licencja, koszty, społeczność, ryzyka, alternatywy`).

## ChatGPT: pomysły i funkcje
```
Kontekst: [czym jest projekt, dla kogo, co już ma - 3-4 zdania].
Ograniczenia: [budżet, czas, technologia, marka/ton, czego nie chcemy].
Zadanie: wymyśl [N=15-20] pomysłów na [funkcje / nazwy / dodatki / kampanię].
- Zróżnicuj je: ~1/3 oczywiste i tanie, ~1/3 ambitne, ~1/3 nieoczywiste lub z innych branż.
- Przy każdym: 1 zdanie opisu, dla kogo, dlaczego zadziała, największe ryzyko, nakład (S/M/L).
- Potem sam skrytykuj listę i wybierz top 5 z uzasadnieniem.
- Na końcu: 3 pytania, które powinienem sobie zadać, zanim wybiorę.
Nie powtarzaj tego, co projekt już ma: [lista].
```

## ChatGPT: druga opinia (krytyka planu)
```
Oto plan/rozwiązanie przygotowane przez innego asystenta AI: [plan w punktach, bez sekretów i kodu].
Cel: [cel]. Ograniczenia: [...].
Zagraj rolę sceptycznego eksperta [dziedzina]. Wskaż: 1) błędy i luki, 2) ryzyka, które pominięto, 3) prostsze lub lepsze alternatywy, 4) co zrobiłbyś inaczej i dlaczego. Bądź konkretny, bez ogólników; oceń pewność każdej uwagi.
```

## Gemini: obraz
```
Create an image: [obiekt/scena w 1 zdaniu].
Purpose: [moodboard / hero na stronę / post / mockup produktu / ilustracja].
Style: [fotografia, ilustracja płaska, 3D, szkic]; mood: [3 przymiotniki z marki].
Composition: [kadr, punkt widzenia, położenie obiektu, miejsce na tekst].
Lighting and color: [światło]; palette: [HEX z tokenów marki z rolami, np. primary #..., background #...].
Format: [proporcje, np. 16:9 / 1:1 / 4:5].
Text in image: [none / dokładny tekst w cudzysłowie].
Avoid: [zakazy marki, logo innych firm, rozpoznawalne osoby, przesadne efekty].
Generate [2-4] variants that differ in [kompozycja / światło / styl].
```

## Gemini: wizualizacja koncepcji
```
Visualize [koncepcja/proces/układ] as [diagram / infografika / szkic ekranu / scena].
Key elements: [lista]. Relationships: [co z czym]. Audience: [kto ogląda].
Style: clean, minimal, palette [HEX]. Labels in Polish, short.
```
Wizualizacja do wdrożenia (ekran, wykres, slajd) powstaje w HTML/SVG; obraz z Gemini to tylko koncept.

## Gemini: streszczenie YouTube
```
Summarize this video: [URL]
I need it for: [cel, np. zasady projektowania logo do mojego procesu].
Output in Polish:
1. Main thesis (2 sentences).
2. Key points with timestamps [mm:ss].
3. Concrete steps, rules, numbers and tools mentioned (exact values).
4. Which claims are the author's opinion vs. backed by data or sources.
5. What is missing or questionable.
Do not add information that is not in the video.
```
