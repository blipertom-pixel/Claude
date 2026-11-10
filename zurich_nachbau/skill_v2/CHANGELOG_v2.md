# Was sich in Version 2 geändert hat, und warum

Grundlage: Arbeit an echten Folien mit dem Nutzer (10. November 2026), Gestaltungsleitfaden v0.1, Beratungspraxis
(Pyramidenprinzip, SCQA, MECE, Ghost Deck, Action Titles), kritisches Review der eigenen Zwischenstände.

## Was der Nutzer will (bestätigt)
- Klarheit und Argumentationslogik wie Analyst Academy: aussagekräftiger Titel, nachvollziehbare Argumente, passende Belege.
- Zurich-Stil: Karten, dunkles Band, Kapitel-Pille, **Icons** (lockern auf), Ogg-Zahlen.
- Komplexere Folien: zwei bis drei Belege mit Erklärung darunter; gemischte Diagrammtypen.
- Ein Deck mit rotem Faden, das eine Entscheidung treibt und aus dem man lernen kann.
- Behauptungen müssen **gezeigt** werden („Nur weil du schreibst, dass die Rechnung aufgeht, beweist du es nicht“).

## Was nicht funktioniert hat (und jetzt Regel ist)
| Befund | Neue Regel | Wo |
|---|---|---|
| Folien gebaut, bevor die Aussage stand | Fünf Phasen mit Prüfsteinen; Bauen erst in Phase 4 | SKILL.md |
| Zahlen ohne Vergleich, Behauptung statt Beleg | Jede Behauptung mit sichtbarem Beleg; Vergleichspaare auf der Antwort-Folie | partner-review C1, archetypes |
| Methodisch falsche Kennzahl („1,16 € je Euro“) | Kennzahl = Behauptung; Business Case mit Marge und Amortisation | partner-review A1 |
| Widersprüchliche Größen und Zeitachsen | Ein Modell, Definitionen gleich, asserts | partner-review A2 bis A6 |
| Zu viele Rahmen, Karten um Diagramme, Band überall | Diagramme ohne Karte, ein dunkles Element pro Folie | visual-system 4 |
| Selbst gezeichnete Icons ohne Bedeutung | Icon-Bibliothek mit Begriffszuordnung | visual-system 5, assets/icons |
| Alles auf einmal ändern | Schleife mit Review-Notiz; kleine Schritte, wenn der Nutzer es verlangt | partner-review E |

## Neu
- `scripts/deck_lite.py`: Bau ohne Master (Raster, Typo, Farben, Icons, Diagramme mit Dezimalkomma, Tabellen, Warnungen für Titel/Notizen).
- `assets/icons/`: 31 Phosphor-Icons (MIT) in Zurich Blue und Weiß.
- `references/storyline.md`, `slide-archetypes.md`, `visual-system.md`, `partner-review.md`.
- `examples/marktfokus_v3/`: komplettes Lern-Deck (12 Folien) mit Modell, Build-Skript und Erklärungen in den Notizen.

## Offen
- Master Playbook, Zurich-Schriften und Zurich-Piktogramme fehlen; im Lite-Modus sind Logo und Icons Ersatz.
- Die Zentimeterwerte des Leitfadens sind noch nicht am Master kalibriert.
- `fit_audit.py`, `brand_audit.py`, `verify.py`, `numtrace.py` brauchen die Bibliothek und liefen deshalb nicht.
