# Gestaltungssystem 2.1 „Editorial“ (Zurich-Stil, nach Nutzer-Feedback vom 10.11.2026)

## 0. Verbindliche Vorgaben des Nutzers
- **Keine dunklen Folien** (kein Dark-Blue-Grund, auch nicht für Titel oder Entscheidung).
- **Kein Balken unten auf jeder Folie.** Das dunkle Konsequenz-Band ist abgeschafft.
- **Keine Kennzahl-Blöcke rechts** neben dem Diagramm.
- **Keine getönten oder „billigen“ Kästen** (hellblaue Rundrechtecke, Rahmen um Inhalte).
- **Nicht ständig das gleiche Layout:** jede Folie bekommt die Form, die ihre Aussage zeigt.
- Erlaubt und erwünscht: **ein Zurich-Blue-Band quer durch die Mitte mit weißen, leicht schwebenden Karten** (Titel, Antwort zuerst, Entscheidung).
- Icons sind erwünscht (lockern auf), mit fester Bedeutung.

## 1. Haltung
Ein Bild je Folie, groß. Weißraum statt Rahmen. Typografie trägt die Hierarchie. Anmerkungen stehen im Bild, nicht daneben.
Zahlen, die die Aussage tragen, werden zum Gestaltungselement (Ogg, 44 bis 66 pt), direkt am Ereignis (z. B. „2031“ über dem Break-even).

## 2. Raster (16:9, Zoll), `scripts/editorial.py`
Rand 0,6 · Inhaltsbreite 12,13 · Titel bei 0,48 · Inhalt 1,6 bis 6,0 · Schlusssatz 6,2 bis 6,5 · Quelle 6,98.

## 3. Typo-Rollen
| Rolle | Größe | Schnitt | Farbe |
|---|---|---|---|
| Titel | 26 pt (Titelfolie 40 pt weiß auf Band) | Light | Zurich Blue |
| Kicker (Großbuchstaben, gesperrt) | 10 pt | Medium | Zurich Blue oder Dark Blue |
| Teilaussage | 15 bis 17 pt | Medium | Dark Blue |
| Text | 13 bis 14 pt | Light, Zahlen Medium | Dark Blue |
| Große Zahl | 44 bis 66 pt | Ogg | Zurich Blue (Kontext: Dark Blue) |
| Schlusssatz | 15 bis 17 pt | Medium, mit kurzem Akzentstrich darüber | Dark Blue |
| Quelle | 10 pt | Light | Dark Blue |

## 4. Elemente
| Element | Funktion | Statt |
|---|---|---|
| `statement()` Akzentstrich + Satz | Konsequenz/Bitte, die der Titel nicht sagt | dunkles Band |
| `kicker()` | Kopf eines Diagramms, Kapitelmarke oben rechts | Pille, Kopfbalken |
| `big()` | tragende Zahl am Ereignis oder im Kartenkopf | Kennzahl-Box rechts |
| `blue_band()` + `white_card()` | Antwort zuerst, Entscheidung, Titel | dunkle Folie, getönte Kacheln |
| `leader()` | Anmerkung mit Linie zum Datenpunkt | Legende, Erklärbox |
| feine Linien (`D.rule`) | Gliederung von Listen, Tabellen, Anhang | Kästen |
| getönte Fläche im Diagramm | Zone mit Bedeutung (Zielzone, Zufallsband, Investitionsphase) | Rahmen |

## 5. Farbe
Weißer Grund. Zurich Blue = Hervorhebung und Band. Light Blue = Kontext, Flächen im Diagramm (nie Textfarbe). Dark Blue = Text.
Mid Blue nur für Linien. Bedeutung nie nur über Farbe: direkt beschriften.

## 6. Diagramm-Grammatik
Native Diagramme oder präzise gezeichnete Formen aus dem Modell. Keine Gitter, keine Achse, wo direkte Beschriftung reicht.
Die Aussage wird **im Diagramm** markiert: Ereignis, Lücke, Schwelle, Zone, Band. Kopf (Kicker) nennt Größe, Einheit, Zeitraum.

## 7. Icons
Phosphor (MIT), Zurich Blue; Zuordnung Begriff → Icon wie bisher (chart-line-up = Markt, coins = Ertrag, shield-check = Risiko,
target = Fokus/Basisfall, flag-banner = Schwelle, warning = Grenze, hand-coins = Freigabe, seal-check = Zusage, users-three = Gremium).
In weißen Karten mit heller Scheibe, im Text ohne Scheibe. Im Master-Modus durch Zurich-Piktogramme ersetzen.

## 8. Bekannte Fehlalarme der Audits
`geometry_audit` meldet Karten auf dem Band und Zonen im Diagramm als „Überlagerung“. Das ist gewollt; im Render prüfen.
