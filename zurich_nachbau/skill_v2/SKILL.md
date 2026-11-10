---
name: pptx-zurich
description: "Create Zurich-branded PowerPoint decks that argue one message: storyline first (SCQA, pyramid, MECE, ghost deck), one number model, slide archetypes chosen by the viewer's task, Zurich visual system, partner review loop. Use for Zurich presentations, board decks, slide design, charts, tables and deck reviews."
allowed-tools: "Bash(python3:*) Read Write Edit Grep Glob"
metadata:
  author: "siehe Original-Skill (nicht im Repo)"
  updated: "2026-11-10"
  version: "2.0 (siehe CHANGELOG_v2.md)"
---

# Zurich PowerPoint, Version 2

Ziel: Ein Deck, das **eine Botschaft treibt** und jede Behauptung **sichtbar belegt**, im Zurich-Stil.
Grundsatz: **Erst denken, dann rechnen, dann zeichnen, dann kritisch prüfen.** Wer bei den Folien anfängt, baut schöne Behauptungen.

## Ablauf (fünf Phasen, jede mit Prüfstein)

| Phase | Was | Ergebnis | Prüfstein (bevor es weitergeht) |
|---|---|---|---|
| 1 Auftrag | Zuhörer, Entscheidung, Nutzung (präsentiert/gelesen) | 1 Satz | Wer entscheidet was bis wann? |
| 2 Storyline | SCQA → Kernaussage → 2 bis 4 MECE-Argumente → Ghost Deck | Titelliste, 1 Zeile je Folie | **Titel-Lesetest**: Titel nacheinander gelesen = ein begründender Absatz |
| 3 Modell | Alle Zahlen in EINER Datei (`modell.py`), jede Aussage als `assert` | geprüfte Zahlen | **Kennzahl = Behauptung** (siehe `references/partner-review.md`, A) |
| 4 Bauen | Archetyp je Folie nach Aufgabe des Betrachters, Gestaltungssystem | Deck | Audits sauber, jede Folie im Render angesehen |
| 5 Partner-Review | Kritische Fragen Logik, Message, Visuell; Schleife bis keine roten Befunde | Deck vN+1 + Review-Notiz | Keine Behauptung ohne Beleg, keine Widersprüche zwischen Folien |

Details: `references/storyline.md` (Phase 1 bis 2), `references/slide-archetypes.md` (Phase 4),
`references/visual-system.md` (Stil), `references/partner-review.md` (Phase 3 und 5).
Zeige dem Nutzer das Ghost Deck nur, wenn eine wesentliche Unklarheit besteht oder er es verlangt; sonst baue das ganze Deck.

## Zwei Bau-Modi

- **Master-Modus** (Standard, wenn `config.json` auf die Zurich-Bibliothek zeigt): `scripts/zurich_kit.py` + `zurich_frame.py`
  mit echten Layouts, Schriften, Piktogrammen. Erst `python3 scripts/setup_check.py`.
- **Lite-Modus** (ohne Master, Schriften, Piktogramme): `scripts/deck_lite.py`. Gleiches Gestaltungssystem, Ersatz-Logo,
  Icons aus `assets/icons` (Phosphor, MIT). Schriftnamen bleiben Zurich Sans/Ogg, damit Originalschriften greifen, sobald installiert.
  Beim Übergang in den Master-Modus: Logo/Seitenzahl kommen aus dem Layout, Icons durch Zurich-Piktogramme gleicher Bedeutung ersetzen.

Beispiel für ein vollständiges Deck in beiden Denk- und Bauschritten: `examples/marktfokus_v3/` (Modell, Build, Notizen je Folie).

## Nicht verhandelbar

- **Jede Behauptung hat einen Beleg auf derselben Folie** (Diagramm, Tabelle, Vergleichszahl). Ein Satz, der etwas behauptet, ist kein Beleg.
- **Ein Modell, eine Wahrheit:** Jede Zahl kommt aus `modell.py`; dieselbe Größe heißt überall gleich und ist überall gleich definiert.
- **Kennzahl passt zur Behauptung:** „rechnet sich“ braucht Ergebnis/Marge/Amortisation, nicht Volumen. „wächst“ braucht Zeitreihe oder Rate.
- **Unsicherheit sichtbar:** Lücken, Spannen, schlechte Szenarien stehen im Titel oder im Diagramm, nicht versteckt in Fußnoten.
- **Frameworks strukturieren, sie stehen nie auf der Folie** (keine Labels „Situation/Komplikation“).
- Echte Daten nur aus Quellen des Nutzers. Ohne Daten: fiktive Beispieldaten **kennzeichnen** oder `[DATA NEEDED: …]`.
- Zurich-Textfarben laut `references/brand-colors.md`; Fotos nur als Kreis; kein AutoFit; Quelle auf jeder Folie mit Zahlen.
- Vor Abgabe: `text_lint.py`, `check_readability.py`, `geometry_audit.py` (Master-Modus zusätzlich `verify.py`, `fit_audit.py`,
  `brand_audit.py`, `numtrace.py`) und **jede Folie im Render ansehen**. Grüne Audits beweisen keine gute Folie.

## Übergabe an den Nutzer
Pfad, Titel-Liste, was fiktiv ist, welche Platzhalter offen sind, welche Prüfungen liefen und welche nicht, was nicht gesehen wurde
(z. B. kein PowerPoint-Render). Keine Erfolgsbehauptung ohne Prüfung.

## Ältere Referenzen (weiter gültig, wo nicht ersetzt)
`zurich-house-style.md`, `writing-rules.md`, `keynote-playbook.md`, `brand-colors.md`, `cards.md`, `dataviz.md`, `workflow-details.md`.
Bei Widerspruch gelten die neuen Referenzen (Stand 2.0).
