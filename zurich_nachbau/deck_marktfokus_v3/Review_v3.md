# Partner-Review Marktfokus v3 (gegen skill_v2/references/partner-review.md)

## Inhaltliche Fehler aus v1/v2, in v3 behoben (rot)
| Fehler in v2 | Warum ein Vorstand ihn findet | v3 |
|---|---|---|
| „1,16 € je investiertem Euro“ | vergleicht Prämienvolumen mit Investition, sagt nichts über Rentabilität | Ergebnis = Prämie × Marge; kumulierte Kurve; Amortisation 2031 vs. 2040 (F5) |
| Folie 6 „Anteil am Markt 28 → 34,5 %“ vs. Folie 3 „Marktanteil 2,1 %“ | dieselbe Größe mit zwei Werten | Folie 4 zeigt die **Nachfrage in der Befragung**, eindeutig benannt |
| Anteilsgewinn auf den Zuwachs gerechnet | falsche Bezugsbasis | Anteilsgewinn auf das Marktvolumen (+0,9 Pp auf 20,2 Mrd. €) |
| Rahmen 2027–2029, alle Phasen 2027 | Zeitachse widerspricht sich | Tranchen 2027/2028/2029 wie im Business Case (F8) |
| Robustheit nur in drei Szenarien | Was, wenn Marge oder Anteil schlechter sind? | Sensitivitätsmatrix, daraus die Kriterien der Entscheidungspunkte (F6) |
| Datenrisiko nur behauptet („8-mal glatter“) | ohne Rechenweg nicht prüfbar | Stichprobenfehler bei 1.200 Befragten vs. tatsächliche Streuung, Band im Diagramm (F7) |
| Kosten des Nichtstuns fehlten | „Warum jetzt?“ bleibt offen | Band F3: Gesamtanteil sinkt von 3,1 auf 3,0 % |

## Storyline
SCQA in den Notizen; Antwort zuerst (F2); drei MECE-Argumente Chance/Ertrag/Risiko mit je zwei Belegfolien; Gegenargument (Daten) mit Daten
beantwortet und in ein Kriterium übersetzt; Ende = drei Beschlüsse, konsistent mit F2. Titel-Lesetest: bestanden.

## Visuell
Keine Karten um Diagramme; ein dunkles Element pro Folie; echte Icons mit fester Bedeutung; direkte Beschriftung mit Dezimalkomma;
Aussage im Diagramm markiert (Break-even, Tiefpunkt, Basisfall, Schwelle, Zufallsband).

## Prüfungen
`text_lint`: nur Platzhalter F9 (gewollt). `check_readability`: sauber. `geometry_audit`: nur gewollte Überlagerungen
(Motiv am Rand F1, Hervorhebungszone hinter Diagrammen F3). Nicht gelaufen: `fit_audit`, `brand_audit`, `verify`, `numtrace`
(brauchen die Zurich-Bibliothek). Kein PowerPoint-Render, nur LibreOffice mit Ersatzschriften.

## Offen
Alle Zahlen fiktiv; Marge, Hochlauf, Tranchen, Befragungsgröße sind Annahmen (F11). Entscheider/Termin `[DATA NEEDED]`.
