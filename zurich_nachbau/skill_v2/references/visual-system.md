# Gestaltungssystem 2.0 (Zurich-Stil, kritisch überarbeitet)

Was bleibt (vom Nutzer bestätigt): weißer Grund, Titel links in Zurich Blue (Light), Kapitel-Pille, getönte Karten, dunkles Band,
Piktogramme in Scheiben, Ogg für große Zahlen, Kreisfotos, Quelle unten.
Was sich ändert (Befund aus Review der Decks v1 bis v2): **weniger Rahmen, mehr Beleg.**

## 1. Raster (16:9, Zoll)
Rand 0,4 · Inhaltsbreite 12,53 · Spaltenabstand 0,25 · Inhalt 1,5 bis 6,0 · Band 6,14 · Quelle 6,93.
Teilungen: voll · 2/3 + 1/3 (8,2 + 4,08) · 1/2 + 1/2 · 1/3 × 3. Funktionen `cols(n)`, `split(8.2)`.

## 2. Typo-Rollen
| Rolle | Größe | Schnitt | Farbe |
|---|---|---|---|
| Titel | 26 pt (Hero 40) | Light | Zurich Blue (dunkel: Weiß) |
| Teilaussage | 18 bis 19 pt | Medium | Dark Blue |
| Text | 14 pt | Light, Schlüsselzahlen Medium | Dark Blue |
| Diagramm-Kopf | 12 pt, Großbuchstaben, gesperrt | Medium | Zurich Blue, mit feiner Linie darunter |
| Beschriftung | 12 bis 13 pt | Light/Medium | Dark Blue |
| Quelle | 11 bis 12 pt | Light | Dark Blue |
| Große Zahl | 36 bis 46 pt | Ogg | Zurich Blue oder Weiß |
Maximal zwei Zeilen Titel. Bewusste Umbrüche, keine einzelnen Restwörter. Kein AutoFit.

## 3. Farbe nach Rolle
Hervorhebung = Zurich Blue · Kontext = Light Blue · Text = Dark Blue · eine dunkle Fläche je Folie (Band **oder** Kennzahlkarte).
Bedeutung nie nur über Farbe: Legende mit Text oder direkte Beschriftung. Mid Blue nur als Fläche/Linie ohne Text.

## 4. Rahmen-Regeln (die wichtigste Änderung)
- **Keine Karte um Diagramme.** Diagramme stehen auf Weiß unter einem Kopf mit feiner Linie (`header`).
- Getönte Karte nur für Kennzahl- oder Textgruppen; weiße Karte mit Linie nur für parallele Optionen; dunkle Karte nur für DIE Botschaft.
- **Höchstens ein dunkles Element** pro Folie. Hat die Folie eine dunkle Kennzahlkarte, wird der Schluss eine ruhige Zeile (`takeaway`).
- Das Band sagt etwas, das der Titel nicht sagt (Konsequenz, Bedingung, Bitte, Überleitung „ABER“).

## 5. Icons
Bedeutung tragen, eine Sprache: Piktogramm in heller Scheibe (`icon`), auf dunklem Grund in weißer Scheibe; in dunklen Köpfen weiß ohne Scheibe.
Gleicher Begriff = gleiches Icon im ganzen Deck:
| Begriff | Icon | Begriff | Icon |
|---|---|---|---|
| Markt, Wachstum | chart-line-up / trend-up | Ertrag, Geld | coins / hand-coins |
| Anteil | chart-pie-slice | Zeit, Amortisation | hourglass |
| Risiko, Absicherung | shield-check | Daten, Erhebung | database / magnifying-glass |
| Ziel, Fokus | target | Pilot, Test | flask |
| Kriterium, Schwelle | flag-banner / scales | Skalierung | steps |
| Entscheidung, Zusage | seal-check / gavel | Personen, Gremium | users-three |
Im Master-Modus durch Zurich-Piktogramme gleicher Bedeutung ersetzen.

## 6. Diagramm-Grammatik (Beratungsstandard)
- Native, editierbare Diagramme. Keine Gitterlinien, keine Achse, wenn direkte Beschriftung reicht; Nulllinie bei Bedarf gestrichelt.
- **Direkt beschriften** (Werte am Balkenende, Linienenden benannt), keine Legende, Dezimalkomma.
- Sortieren, wenn die Reihenfolge keine Bedeutung hat. Fokus hervorheben, Rest Kontextfarbe.
- **Die Aussage im Diagramm markieren:** Ereignis (Break-even), Lücke (Klammer „−30“), Schwelle (Linie), Spanne (Band).
- Kopf nennt Größe, Einheit, Zeitraum; Quelle/Rechenweg in der Fußzeile.
