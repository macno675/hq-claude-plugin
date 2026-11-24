#!/usr/bin/env python3
"""Wskazuje typowe zwroty tekstu pisanego przez AI (PL/EN). Użycie: textcheck.py <plik...> albo tekst na stdin.
Wyjście: plik:linia: zwrot -> podpowiedź; kod 1 przy trafieniach. Zasady: references/writing.md."""
import re, sys

# (wzorzec, podpowiedź); dopasowanie bez rozróżniania wielkości liter
RULES = [
    (r"świetne pytanie|great question", "usuń wstęp, zacznij od odpowiedzi"),
    (r"poniżej (przedstawiam|znajdziesz)|w tej sekcji (znajdziesz|omówi)|here'?s (a|an|the) (breakdown|overview)", "usuń zapowiedź"),
    (r"mam nadzieję, że (to )?pom|daj znać, jeśli|hope (this|that) helps|let me know if", "usuń zakończenie"),
    (r"warto (zauważyć|podkreślić|wspomnieć)|należy pamiętać|ważne jest, aby|it'?s worth noting|it is important to note", "usuń, podaj sam fakt"),
    (r"\bpodsumowując\b|\bin conclusion\b|\bto sum up\b", "podsumowanie tylko, gdy coś dodaje"),
    (r"kompleksow|innowacyjn|intuicyjn|bezproblemow|wyjątkow|niezwykle|na wyższy poziom|szyt\w* na miarę", "puste słowo: daj konkret"),
    (r"\bodkryj\b|zanurz się|w dzisiejszym (dynamicznym|szybko)", "slogan: napisz, co konkretnie"),
    (r"\b(seamless|robust|leverag\w*|delv\w*|elevat\w*|unlock\w*|streamlin\w*|cutting-edge|game.changer|tapestry)\b", "puste słowo (EN)"),
    (r"in today'?s (fast-paced|digital|ever)", "slogan (EN)"),
    (r"nie tylko\b.{1,60}\bale (też|również|także)|not only\b.{1,60}\bbut also", "konstrukcja z szablonu"),
    (r"\bdokonać\b|\bdokonuje\b|\bw oparciu o\b|\bdedykowan\w*|adresowa\w* (problem|potrzeb)|na koniec dnia|zrobić różnicę", "kalka/urzędowo: użyj czasownika"),
    (r"\bups\b|\boops\b|coś poszło nie tak|something went wrong", "błąd: co się stało i co zrobić"),
    (r"wygląda na to, że|it (looks|seems) like you", "wprost, bez asekuracji"),
    (r"(twój|twoja|twoje) .{0,40}(zobacz|widoczn)\w*", "oczywistość? usuń, jeśli czytelnik to wie"),
    (r"upewnij się, że|make sure (to|that)", "kalka: tryb rozkazujący (Sprawdź...)"),
    (r"\bw celu\b|\bcelem\b", "żeby / do"),
    (r"z przyjemnością (informujemy|przedstawiamy)|prosimy o uwzględnienie|we'?re (excited|thrilled) to", "usuń wstęp, podaj fakt"),
    (r"w (erze|dobie) (ai|sztucznej|cyfryzacji)|holistyczn|niezrównan|szerok\w* wachlarz|kluczow\w* (rol|znaczeni|aspekt)|istotn\w* aspekt|najlepsz\w* praktyk", "ogólnik: daj konkret"),
    (r"stworzon\w* z myślą o|ciesz się .{0,40}zajmiemy się", "slogan: dla kogo / co robi"),
    (r"zarówno .{1,40} jak i .{1,40}(zalet|wad|plus)", "fałszywa równowaga: kryterium i rekomendacja"),
    (r"uzupełnij wymagane pola|wystąpił błąd|dowiedz się więcej|\brozpocznij\b", "UI: powiedz, czego brakuje / co się stanie"),
    (r"\*\*ważne:?\*\*", "wyróżnienie bez powodu?"),
]
RX = [(re.compile(p, re.I), h) for p, h in RULES]
EMOJI = re.compile("[\U0001F300-\U0001FAFF✨✅❌⚡]")


def scan(text):
    """Zwraca listę (linia, zwrot, podpowiedź)."""
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        for rx, hint in RX:
            for m in rx.finditer(line):
                out.append((n, m.group(0), hint))
        if line.count("—") >= 2:
            out.append((n, "—", "myślniki jako pauzy: przecinek, kropka albo dwa zdania"))
        if EMOJI.search(line):
            out.append((n, EMOJI.search(line).group(0), "emoji jako ozdoba"))
    return out


def test():
    bad = "Świetne pytanie! Poniżej przedstawiam kompleksowe omówienie.\nTwój kod zobaczą gospodarze.\nUps! Coś poszło nie tak.\nMam nadzieję, że to pomoże — daj znać — pa.\nWe leverage a robust platform.\nUpewnij się, że kod jest poprawny.\nW celu dokonania zmian uzupełnij wymagane pola."
    hits = scan(bad)
    lines = {h[0] for h in hits}
    assert lines == {1, 2, 3, 4, 5, 6, 7}, hits
    good = "Brak rezerwacji. Dodaj pierwszą.\nNie zapisano. Brak połączenia - spróbuj za chwilę.\nZapisz zmiany\nPodaj nazwę firmy i NIP.\nRekomenduję B: 12 tys. zł, 2 tygodnie."
    assert scan(good) == [], scan(good)
    print("textcheck: OK")


if __name__ == "__main__":
    if "--test" in sys.argv:
        test(); sys.exit(0)
    files = [a for a in sys.argv[1:] if not a.startswith("-")]
    srcs = [(f, open(f, encoding="utf-8", errors="replace").read()) for f in files] or [("stdin", sys.stdin.read())]
    total = 0
    for name, text in srcs:
        for n, phrase, hint in scan(text):
            print(f"{name}:{n}: {phrase} -> {hint}"); total += 1
    print(f"trafień: {total}" if total else "textcheck: brak typowych zwrotów AI (przeczytaj jeszcze na głos)")
    sys.exit(1 if total else 0)
