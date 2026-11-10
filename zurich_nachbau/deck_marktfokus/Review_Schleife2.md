# Review, Schleife 2: Frameworks gegen das Deck (Marktfokus, fiktiv)

Geprüft wurde `Marktfokus_Deck_v1` gegen Pyramidenprinzip, MECE, SCQA, Horizontal-/Vertikal-Logik, Action-Titel, Chart-Wahl und den Gestaltungsleitfaden.
Ergebnis: `Marktfokus_Deck_v2`. Die alte Fassung liegt als `build_deck_v1_backup.py` vor.

## A. Storytelling und Logik

| # | Befund | Framework | Korrektur in v2 |
|---|---|---|---|
| A1 | Argument 3 vermischte „Daten“ und „Umsetzung“; Folie 2 und Folie 9 nannten es verschieden | MECE | Drei Argumente: **Chance, Ertrag, Risiko**. Argument 3 heißt überall „Das Risiko bleibt begrenzt“ |
| A2 | Entscheidungspunkte auf Folie 7 standen am Phasenanfang, ihre Frage bezog sich aber auf das Phasenergebnis | Vertikale Logik | Rauten am **Phasenende**; Tranche i wird erst nach Entscheidungspunkt i−1 frei |
| A3 | Entscheidungsfolie widersprach Folie 2 (80 Mio. € gegen „Beobachten“) | Ende = Auftrag (was, wer, bis wann) | Drei echte Beschlüsse: 10 Mio. € sofort, 80 Mio. € Rahmen, Entscheider benennen |
| A4 | Titelfolie und Folie 2 hatten fast denselben Titel | Horizontale Logik (Titel-Lesetest) | Titelfolie: „Wo der Markt am stärksten wächst, setzen wir 80 Mio. € ein“; Folie 2 liefert das „weil“ |

## B. Message

| # | Befund | Framework | Korrektur in v2 |
|---|---|---|---|
| B1 | Folie 5 behauptete „rechnet sich“, verschwieg aber die Lücke (Basisfall nur knapp über der Schwelle, vorsichtiger Fall −30 Mio. €) | Unsicherheit nicht verstecken (Leitfaden §2/§9) | Titel nennt die Lücke; im Diagramm ist sie eingezeichnet |
| B2 | Folie 3: Titel mit drei Aussagen, sehr lang | Action-Titel, höchstens 2 Zeilen | Kürzer, ohne Inhalt zu verlieren |
| B3 | Dunkles Band auf fast jeder Folie | Band muss Neues sagen, sonst ruhige Zeile | Folie 7 und 10 haben jetzt eine ruhige Schlusszeile; Folie 7 sagt etwas Neues: „Stopp nach höchstens 2, 10 oder 50 Mio. € statt 80“ |
| B4 | Folie 2, Zeile 3 belegte „wir prüfen vor jeder Ausgabe“ nicht | Behauptung braucht Beleg | Mini-Beleg: Wachstumslinie und Tranchenbalken (10 von 80 = 12,5 %) |

## C. Visuell

| # | Befund | Korrektur in v2 |
|---|---|---|
| C1 | Lücke von 30 Mio. € auf Folie 5 nicht sichtbar | Klammer „−30“ zwischen Balken und Linie |
| C2 | Folie 7 hatte keine Antwort auf „wie viel Geld wann“ | Tranchen-Zeile mit Balken, Freigabe-Hinweis und Klammer 10 = 12,5 % |
| C3 | Zeilenumbrüche mit Einzelwörtern, Titel mit drei Zeilen | Texte und Titel angepasst |

## D. Was gut war und blieb
Dreispalter (Folie 3), Zwei Belege (Folie 6), Optionen-Matrix mit Balken (Folie 4), Pyramiden-Lernfolie (Folie 9), alle Zahlen aus einem Modell mit `assert`-Prüfung.

## E. Noch offen
- Alle Zahlen sind fiktiv; Tranchen sind Annahmen. Entscheider und Termin: `[DATA NEEDED]`.
- Argument 3 enthält zwei Belege (Daten und Fahrplan). Wenn das Deck länger werden soll, könnten die Daten eine eigene Folie bekommen.
- Logo, Schriften und Icons sind Ersatz.
