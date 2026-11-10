# Partner-Review: kritisch prüfen, bevor der Vorstand es tut (Phase 3 und 5)

Jede Frage stammt aus einem echten Fehler in den Vorversionen dieses Skills. Rot = muss vor Abgabe behoben sein.

## A. Zahlen und Logik (rot)
1. **Misst die Kennzahl, was der Titel behauptet?** v1: „rechnet sich“ mit Prämienvolumen je Euro belegt. Richtig: Ergebnis (Prämie × Marge),
   kumuliert nach Investition, Amortisationsjahr.
2. **Gleiche Größe, gleiche Definition auf allen Folien?** v1: „Anteil am Markt 28 → 34,5 %“ auf Folie 6, „Marktanteil 2,1 %“ auf Folie 3.
   Richtig: verschiedene Dinge verschieden benennen (Nachfrage in der Befragung ≠ Marktanteil).
3. **Bezugsbasis korrekt?** v1: Anteilsgewinn nur auf den Zuwachs gerechnet. Richtig: auf das Marktvolumen.
4. **Zeitachse konsistent?** v1: Rahmen „2027 bis 2029“, alle Phasen in 2027. Richtig: Tranchen über die Jahre wie im Business Case.
5. **Logik der Entscheidungspunkte:** Entscheidung am Ende einer Phase, Kriterium messbar, Geld erst danach.
6. **Ein Modell:** Jede Zahl aus `modell.py`, Aussagen als `assert` (z. B. 69 %, Amortisation 2031, Stopp nach 2/10/50).

## B. Storyline (rot)
1. Argumente MECE? (v1 vermischte Daten und Umsetzung.) Titel-Lesetest bestanden?
2. Antwort-Folie und Entscheidungsfolie verlangen dasselbe? (v1: 80 Mio. € vs. „beobachten“.)
3. Das stärkste Gegenargument wird mit Daten beantwortet (hier: Daten zu glatt → Prüfung vor dem Pilot).
4. Kosten des Nichtstuns gezeigt? (hier: Gesamtanteil sinkt von 3,1 auf 3,0 %).

## C. Message (rot/gelb)
1. Jede Behauptung hat einen sichtbaren Beleg auf der Folie (v1 Folie 2: Zahlen ohne Vergleich).
2. Schlechte Fälle stehen im Titel oder Diagramm (v1 verschwieg die Lücke im vorsichtigen Fall).
3. Band wiederholt den Titel nicht; höchstens ein dunkles Element.
4. Titel ≤ 2 Zeilen, keine Restwörter, keine Fachkürzel ohne Erklärung in der Fußzeile.

## D. Visuell (gelb)
1. Squint-Test: Was fällt zuerst auf? Ist es der Beleg?
2. Keine Rahmen um Diagramme, keine verschachtelten Kästen.
3. Gleiche Abstände für gleiche Rollen; Text näher am eigenen Icon als am Nachbarn.
4. Icons tragen Bedeutung und sind deckweit gleich verwendet.
5. Keine Platzhalter-Beschriftungen (z. B. „m0“), kein Überlauf, kein Text über Kanten.

## E. Ablauf der Schleife
Render jeder Folie ansehen → Befunde A bis D notieren (Review-Notiz) → beheben → neu rendern → bis keine roten Befunde.
Die Review-Notiz bleibt beim Deck (z. B. `Review_SchleifeN.md`) und ist Teil der Übergabe.
