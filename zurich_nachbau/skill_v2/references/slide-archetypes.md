# Archetypen: welcher Folientyp für welche Aufgabe (Phase 4)

Die Frage ist nie „Was sieht gut aus?“, sondern **„Was soll der Betrachter tun?“**. Jeder Archetyp hat eine feste Anatomie im
Zurich-Stil. Funktionen aus `scripts/deck_lite.py` in Klammern; Beispiel = Folie in `examples/marktfokus_v3`.

| Aufgabe des Betrachters | Archetyp | Anatomie | Beispiel |
|---|---|---|---|
| Antwort und Gründe in einer Minute | **Antwort zuerst** | 3 Zeilen: Icon, Behauptung (18 pt), Satz mit fetten Zahlen, rechts je ein **Vergleichspaar** (`compare_bars`); dunkles Band mit Bitte | F2 |
| Mehrere Objekte über drei Sichten vergleichen | **Dreispalter** | 3 Spalten mit dunklem Kopf (Icon weiß), gleiche Zeilen, Hervorhebungszone quer, Takeaway mit fetten Zahlen je Spalte (`bars_h`) | F3 |
| Zwei Teilaussagen belegen („A, aber B“) | **Zwei Belege** | 2 Hälften ohne Karten, getrennt durch feine Linie: Teilaussage mit Icon (`claim`), Kopf (`header`), Diagramm, Erklärung | F4 |
| Entwicklung, Break-even, Vergleich über Zeit | **Kurve + Kennzahl** | links 2/3 Liniendiagramm mit direkter Beschriftung und markiertem Ereignis, rechts 1 dunkle + 1 helle Kennzahlkarte | F5 |
| Robustheit, „hält das bei schlechteren Annahmen?“ | **Sensitivitätsmatrix** | Raster zwei Annahmen × Ergebniswert, 3 Farbstufen + Text-Legende, Basisfall gerahmt, tragfähiger Bereich gestrichelt | F6 |
| Datenqualität, Abweichung vom Erwarteten | **Abweichung gegen Band** | Säulen/Werte gegen Referenzband (z. B. Zufallsband), Band beschriftet, rechts Ist- und Soll-Kennzahl | F7 |
| Ablauf mit Geld und Entscheidungen | **Roadmap mit Gates** | Pfeile = Phasen, Zeilen: Was / Ergebnis / Entscheidungspunkt (Raute + Kriterium) / Tranche (Balken), Klammer für gebundenes Geld | F8 |
| Entscheiden | **Entscheidungsfolie** (dunkel) | 3 Karten = 3 Beschlüsse mit Zahl, Platzhalter für Entscheider/Termin | F9 |
| Aufbau verstehen | **Pyramide** | Frage → Antwort → Argumente → Belegfolien | F10 |
| Exakte Werte nachschlagen | **Tabelle** | Kopf dunkel, Zahlen rechtsbündig, Fokuszeilen hell, Summenzeilen | F12 |
| Herleitung prüfen | **Annahmenliste** | nummerierte Zeilen: Begriff, Definition/Wert | F11 |
| Optionen über Kriterien bewerten | **Optionen-Matrix** | Kriterien als Zeilen, Optionen als Spalten, Empfehlung gerahmt, Kennzahl je Zelle, Risiko als Symbol + Wort | v2 F4 |
| Eine Zahl/These trägt alles | **Hero** | ein Satz oder eine Zahl, dunkel, Motiv | F1 |

## Diagrammwahl innerhalb eines Archetyps
Vergleich/Rangfolge → Balken (sortiert). Zeit → Linie. Anteil am Ganzen → gestapelter 100-%-Balken. Abweichung → Abweichungsbalken
oder Punkt mit Referenzlinie. Beiträge → Waterfall. Zusammenhang → Streudiagramm. Spanne → Intervall. Schwelle → Säule mit Linie.
Mischen ist erwünscht, wenn jedes Diagramm eine eigene Frage beantwortet und alle dieselben Zeilen/Zeitachse teilen.

## Folgen im Deck
- Nie zwei gleiche Archetypen direkt hintereinander (Ausnahme: bewusst parallele Belegfolien).
- Nach einer dichten Folie eine ruhigere.
- Jede Belegfolie trägt die Kapitel-Pille mit Argumentnummer (`tracker`).
