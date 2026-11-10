# -*- coding: utf-8 -*-
"""Deck "Was eine gute Folie ausmacht": sechs Folien, jede zeigt einen Mechanismus. Inhalt: Gestaltungsleitfaden v0.1."""
import sys
import zhelp as Z
from zhelp import *

def hair(x, y, w, color="D5E3F2"): shape(S.RECTANGLE, x, y, w, 0.012, fill=color)
def marker(cx, cy, n, d=0.36, fill=DB, tcol=WHITE):
    shape(S.OVAL, cx - d/2, cy - d/2, d, d, fill=fill); text(cx - d/2, cy - d/2, d, d, str(n), 13, M, tcol, "c", "m")

# ======================= 1  Hero ========================================================================
new_slide("Hero", "Die These: Eine Folie wird gut, wenn zuerst die Aussage und ihr Beleg stehen. Gestaltung macht beides sichtbar, sie ersetzt es nicht. "
          "Grundlage ist der Gestaltungsleitfaden v0.1 (10. November 2026).", dark=True)
set_title("Eine gute Folie beginnt mit einer Aussage, nicht mit einem Layout", 0.7, 2.3, 9.8, 2.6, 54, WHITE)
text(0.7, 5.3, 9, 0.4, "Wie der Präsentations-Skill Folien aufbaut  ·  Stand 10. November 2026", 18, L, WHITE)

# ======================= 2  Vorher / Nachher ============================================================
new_slide("Links steht ein Thema, rechts eine Aussage mit Beleg. Die Daten sind dieselben",
          "Beispiel aus dem Leitfaden: 'Kundenloyalität' ist ein Thema. 'Loyale Kunden bringen im Schnitt 42 % mehr Umsatz' ist eine Aussage, die der Chart belegt. "
          "Werte sind erfunden und nur zur Illustration.")
MW, MH, MY = 6.0, 3.38, 2.0
def mini_frame(x, hot):
    shape(S.ROUNDED_RECTANGLE, x, MY, MW, MH, fill=WHITE, line=ZB if hot else LB, lw=3 if hot else 1.25, rad=0.1)
    # Logo-Andeutung
    shape(S.OVAL, x + MW - 0.5, MY + 0.2, 0.24, 0.24, fill=ZB if hot else LB)
text(0.4, 1.55, 6, 0.3, "Thema und Stichpunkte", 15, M, DB)
text(6.93, 1.55, 6, 0.3, "Aussage und Beleg", 15, M, ZB)
# links
x = 0.4; mini_frame(x, False)
text(x + 0.3, MY + 0.25, 4.8, 0.4, "Kundenloyalität", 18, L, ZB)
for i, tx in enumerate(["Loyale Kunden: höherer Umsatz", "Gelegenheitskunden: niedrigerer Umsatz", "Details siehe Tabelle im Anhang"]):
    yy = MY + 1.1 + i * 0.55
    shape(S.RECTANGLE, x + 0.32, yy + 0.09, 0.09, 0.09, fill=DB)
    text(x + 0.55, yy, 5.2, 0.35, tx, 14, L, DB)
# rechts
x = 6.93; mini_frame(x, True)
text(x + 0.3, MY + 0.22, 4.9, 0.7, "Loyale Kunden bringen im Schnitt 42 % mehr Umsatz je Kunde", 16, L, ZB)
base = MY + 2.5
shape(S.RECTANGLE, x + 0.4, base, 3.5, 0.015, fill=DB)
for bx, v, col, lab, cat in [(x + 0.7, 740, ZB, "740 €", "Loyale Kunden"), (x + 2.3, 520, FOCUS_LIGHT, "520 €", "Übrige Kunden")]:
    h = v / 740 * 1.15
    shape(S.RECTANGLE, bx, base - h, 1.1, h, fill=col)
    text(bx, base - h - 0.3, 1.1, 0.25, lab, 13, M, DB, "c")
    text(bx - 0.2, base + 0.05, 1.5, 0.22, cat, 11, L, DB, "c")
h1, h2 = 1.15, 520 / 740 * 1.15
shape(S.RECTANGLE, x + 3.9 + 0.0, base - h1, 0.02, h1 - h2, fill=DB)
pill(x + 4.1, base - h1 - 0.02, 0.95, "+42 %", ZB, WHITE, h=0.34, size=13)
text(x + 4.1, base - h1 + 0.4, 1.7, 0.7, "220 € mehr je Kunde und Jahr", 12, L, DB)
text(x + 0.3, MY + MH - 0.3, 5.3, 0.22, "Beispiel, fiktiv. Jahresumsatz je Kunde.", 10, L, DB)
hair(0.4, 5.75, 12.53)
text(0.4, 5.95, 12.5, 0.5, "Der Skill klärt zuerst die Aussage und ihren Beleg und wählt erst danach das Layout.", 20, M, DB)
footer("Beispiel aus dem Gestaltungsleitfaden v0.1, Werte fiktiv und nur zur Illustration.")

# ======================= 3  Reihenfolge =================================================================
new_slide("Sechs von acht Schritten laufen, bevor der Firmenstil angewendet wird",
          "Acht Arbeitsschritte je Folie (Leitfaden, Abschnitt 1). Die ersten sechs sind Denkarbeit: Auftrag, Aussage, Belege, Betrachteraufgabe, Darstellung, Hierarchie. "
          "Firmenstil (Master, Schriften, Farben, Icons) und Ausgabeprüfung sind die Schritte 7 und 8.")
groups = [("Inhalt klären", [("1", "Auftrag klären", "Wer sieht sie, was soll danach verstanden werden?"),
                              ("2", "Aussage formulieren", "Was lässt sich belegen, was ist noch Hypothese?"),
                              ("3", "Argumente prüfen", "Was stützt die Aussage, was spricht dagegen?")]),
          ("Darstellung festlegen", [("4", "Betrachteraufgabe bestimmen", "Vergleichen, ablesen, Entwicklung verfolgen oder Ablauf verstehen?"),
                                     ("5", "Darstellung wählen", "Chart, Tabelle, Prozess oder Textgruppen?"),
                                     ("6", "Hierarchie planen", "Was fällt zuerst auf, was kommt danach?")]),
          ("Stil und Prüfung", [("7", "Firmenstil anwenden", "Master, Schriften, Farben, Icons, soweit sie die Aufgabe stützen."),
                                ("8", "Ausgabe prüfen", "Rendern, Zielformat ansehen, Daten und Quelle prüfen.")])]
unit = None; gx = 0.4; GY = 2.25
GW = [4.15, 4.15, 3.83]
for gi, (gname, steps) in enumerate(groups):
    w = GW[gi]; last = gi == 2
    if last: shape(S.ROUNDED_RECTANGLE, gx, GY, w, 3.85, fill=WHITE, line=LB)
    else: shape(S.ROUNDED_RECTANGLE, gx, GY, w, 3.85, fill=LB, alpha=30)
    text(gx + 0.3, GY + 0.2, w - 0.6, 0.35, gname, 18, M, DB if last else ZB)
    for si, (n, nm, q) in enumerate(steps):
        yy = GY + 0.8 + si * 1.0
        marker(gx + 0.46, yy + 0.18, n, 0.34, fill=DB)
        text(gx + 0.8, yy, w - 1.0, 0.3, nm, 15, M, DB)
        text(gx + 0.8, yy + 0.3, w - 1.0, 0.6, q, 13, L, DB)
    gx += w + 0.2
# Klammer über Denkarbeit
bw = GW[0] + GW[1] + 0.2
shape(S.RECTANGLE, 0.4, 1.78, bw, 0.03, fill=ZB)
shape(S.RECTANGLE, 0.4, 1.78, 0.03, 0.2, fill=ZB); shape(S.RECTANGLE, 0.4 + bw - 0.03, 1.78, 0.03, 0.2, fill=ZB)
text(0.4, 1.4, bw, 0.3, "Denkarbeit: kein Layout, keine Firmenfarbe", 14, M, ZB)
footer("Quelle: Gestaltungsleitfaden v0.1, Abschnitt 1 „Arbeitsweise für jede Folie“.")

# ======================= 4  Anatomie ====================================================================
new_slide("Jede Folie hat fünf Rollen, und jede Rolle sieht anders aus",
          "Rollen nach Leitfaden Abschnitt 3: Titel, Hauptinhalt, Unteraussage, Detail, Einordnung. Der Titel muss nicht das größte Objekt sein; "
          "eine große Zahl oder ein Diagramm kann die zentrale Evidenz sein.")
FX, FY, FW_, FH_ = 0.4, 1.62, 8.1, 4.55
shape(S.ROUNDED_RECTANGLE, FX, FY, FW_, FH_, fill=WHITE, line=LB, lw=1.25, rad=0.1)
text(FX + 0.5, FY + 0.3, 7.0, 0.8, "Loyale Kunden bringen im Schnitt 42 % mehr Umsatz je Kunde", 22, L, ZB)
base = FY + 3.85
shape(S.RECTANGLE, FX + 0.5, base, 4.6, 0.015, fill=DB)
for bx, v, col, lab, cat in [(FX + 0.9, 740, ZB, "740 €", "Loyale Kunden"), (FX + 3.0, 520, FOCUS_LIGHT, "520 €", "Übrige Kunden")]:
    h = v / 740 * 1.9
    shape(S.RECTANGLE, bx, base - h, 1.4, h, fill=col)
    text(bx, base - h - 0.34, 1.4, 0.28, lab, 14, M, DB, "c")
    text(bx - 0.2, base + 0.06, 1.8, 0.25, cat, 13, L, DB, "c")
shape(S.ROUNDED_RECTANGLE, FX + 5.55, FY + 1.7, 2.2, 1.55, fill=LB, alpha=30)
text(FX + 5.75, FY + 1.8, 1.9, 0.6, "+42 %", 34, O, ZB, "l", "m")
text(FX + 5.75, FY + 2.45, 1.9, 0.7, "220 € mehr je Kunde und Jahr", 14, L, DB)
text(FX + 0.5, FY + FH_ - 0.35, 7.0, 0.25, "Beispiel, fiktiv. Jahresumsatz je Kunde, Stichprobe.", 11, L, DB)
roles = [("Titel", "Die Aussage, nicht das Thema.", (FX + 0.2, FY + 0.45)),
         ("Hauptinhalt", "Der Beleg bekommt die meiste Fläche.", (FX + 1.6, FY + 2.9)),
         ("Unteraussage", "Wirkt über Gewicht und Abstand.", (FX + 5.4, FY + 1.7)),
         ("Detail", "Steht nah am Objekt, bleibt ruhig.", (FX + 2.45, FY + 1.75)),
         ("Einordnung", "Quelle, Basis und Zeitraum, lesbar.", (FX + 0.2, FY + FH_ - 0.22))]
# Reihenfolge der Marker im Bild: Detail liegt über dem ersten Balken
for i, (rn, rule, (mx_, my_)) in enumerate(roles, start=1):
    marker(mx_, my_, i, 0.34, fill=ZB if i != 2 else WHITE, tcol=WHITE if i != 2 else DB)
    yy = 1.62 + (i - 1) * 0.93
    marker(9.2, yy + 0.2, i, 0.34, fill=ZB)
    text(9.55, yy, 3.4, 0.3, rn, 16, M, DB)
    text(9.55, yy + 0.32, 3.38, 0.5, rule, 14, L, DB)
footer("Quelle: Gestaltungsleitfaden v0.1, Abschnitt 3 „Visuelle Hierarchie“.")

# ======================= 5  Nähe =======================================================================
new_slide("Was zusammengehört, steht näher beieinander als der Rest",
          "Gruppierung (Leitfaden Abschnitt 5): Zusammengehörige Elemente stehen näher beieinander als Elemente verschiedener Gruppen. "
          "Die Zentimeterwerte sind Testwerte für 16:9, nicht am Zurich-Master geprüft. Die Zeichnung ist 2-fach vergrößert.")
items = [("Datenkatalog", "findbar"), ("Metadaten", "verständlich"), ("Datenqualität", "vertrauenswürdig")]
def row(x0, y0, gap_in, gap_out):
    x = x0
    for nm, sub in items:
        shape(S.OVAL, x, y0, 0.6, 0.6, fill=BG)
        shape(S.OVAL, x + 0.19, y0 + 0.19, 0.22, 0.22, fill=ZB)
        text(x + 0.6 + gap_in, y0 + 0.0, 1.5, 0.3, nm, 15, M, DB)
        text(x + 0.6 + gap_in, y0 + 0.32, 1.5, 0.3, sub, 13, L, DB)
        x += 0.6 + gap_in + 1.5 + gap_out
for k, (y, ttl, verdict, gi, go, ok) in enumerate([
        (1.62, "Gleiche Abstände überall", "Unklar: Gehört ein Text zum Icon links oder rechts?", 0.35, 0.35, False),
        (3.82, "Abstand nach Zugehörigkeit", "Klar: Jeder Text steht an seinem eigenen Icon.", 0.12, 0.75, True)]):
    shape(S.ROUNDED_RECTANGLE, 0.4, y, 12.53, 1.95, fill=WHITE, line=ZB if ok else LB, lw=3 if ok else 1.25)
    text(0.75, y + 0.4, 3.45, 0.4, ttl, 17, M, ZB if ok else DB)
    text(0.75, y + 0.95, 3.1, 0.7, verdict, 14, L, DB)
    row(4.3, y + 0.67, gi, go)
text(0.4, 5.95, 12.5, 0.5, "Als Startwert: Icon zu Text etwa 0,2 bis 0,3 cm, zwischen Gruppen etwa 0,6 bis 0,8 cm.", 20, M, DB)
footer("Quelle: Gestaltungsleitfaden v0.1, Abschnitt 5. Testwerte für 16:9, noch nicht am Zurich-Master geprüft. Zeichnung 2-fach vergrößert.")

# ======================= 6  Was fehlt (Dark) ============================================================
new_slide("Für den ersten Einsatz fehlen Master, Schriften und Icons",
          "Aus dem Backup fehlen: Master-PowerPoint, Zurich-Schriften, Icon- und Bildbibliothek, Logos, config.json, layouts.json. "
          "Die Beispielfolien wurden deshalb ohne Master mit Ersatzschriften und nachgebauten Formen erstellt. "
          "Danach sollen drei Kalibrierfolien am Zielgerät geprüft werden (Leitfaden Abschnitt 5).", dark=True)
miss = [("Master-PowerPoint", "Ohne Master gibt es keine echten Titelplatzhalter, Logos und Seitenzahlen aus dem Layout.", "Jetzt: leere Folie, Rahmen nachgebaut"),
        ("Zurich-Schriften", "Zeilenumbrüche und Größen stimmen erst mit Zurich Sans und Ogg.", "Jetzt: Inter und Source Serif 4"),
        ("Icon-Bibliothek", "Die Piktogramme tragen den Firmenstil, selbst gezeichnete Formen tun das nicht.", "Jetzt: einfache Formen")]
cw3 = (12.53 - 2 * 0.3) / 3
for i, (nm, why, now) in enumerate(miss):
    x = 0.4 + i * (cw3 + 0.3)
    shape(S.ROUNDED_RECTANGLE, x, 1.75, cw3, 3.5, fill=ZB, rad=0.14)
    text(x + 0.35, 2.05, cw3 - 0.7, 0.45, nm, 22, M, WHITE)
    text(x + 0.35, 2.7, cw3 - 0.7, 1.3, why, 16, L, WHITE)
    shape(S.RECTANGLE, x + 0.35, 4.2, cw3 - 0.7, 0.015, fill=WHITE)
    text(x + 0.35, 4.4, cw3 - 0.7, 0.6, now, 15, M, WHITE)
text(0.4, 5.65, 12.5, 0.5, "Wir brauchen die Dateien. Danach prüfen wir drei Kalibrierfolien am Zielgerät.", 22, M, WHITE)
text(0.4, 6.2, 12.0, 0.35, "Von: [DATA NEEDED: wer liefert Master, Schriften und Icons]", 15, L, WHITE)
footer("Quelle: Backup „Zurich_Praesentationsskill“, README, Abschnitt „Was fehlt“.")
prs.save(sys.argv[1])
