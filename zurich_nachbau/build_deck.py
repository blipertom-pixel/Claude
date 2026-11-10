# -*- coding: utf-8 -*-
"""Vorstands-Deck (11 Folien) nach Skill-Regeln: Antwort zuerst, ein Argument je Folie, Entscheidung am Ende.
Alle Zahlen: fiktive Beispieldaten, aus einem Modell abgeleitet (siehe Anhang)."""
import sys
from zcharts import *

def tracker(n, label):
    shape(S.ROUNDED_RECTANGLE, 11.4, 0.93, 1.5, 0.3, fill="E9EBF0", rad=0.15)
    shape(S.OVAL, 11.45, 0.96, 0.24, 0.24, fill=DB); text(11.45, 0.96, 0.24, 0.24, str(n), 10, M, WHITE, "c", "m")
    text(11.78, 0.93, 1.1, 0.3, label, 11, L, DB, "l", "m")

def band(label, sentence, size=15, y=6.14):
    shape(S.ROUNDED_RECTANGLE, 0.4, y, 12.53, 0.66, fill=DB)
    text(0.65, y, 1.7, 0.66, label, 12, M, WHITE, "l", "m")
    text(2.45, y, 10.3, 0.66, sentence, size, L, WHITE, "l", "m")

def card(x, y, w, h, kind="white"):
    if kind == "dark": return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=DB)
    if kind == "tint": return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=LB, alpha=30)
    return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=WHITE, line=LB)

# ======================= 1  Titel (Dark Ground, These im Titel) =======================================
new_slide("Hero", "Situation: Der Markt wächst bis 2029 um 9,0 Mrd. €. Komplikation: 69 % davon entfallen auf drei Segmente, in denen wir nur "
          "2,1 % Anteil haben, und die Datenbasis ist noch zu glatt. Antwort: 80 Mio. € auf drei Segmente, mit Entscheidungspunkten. "
          "Alle Zahlen sind Beispieldaten, fiktiv.", dark=True)
for k, (d, a) in enumerate([(5.2, 12), (4.0, 16), (2.8, 22)]):
    shape(S.DONUT, 13.333 - d * 0.62, 7.5 - d * 0.62, d, d, fill=LB, alpha=a).adjustments[0] = 0.1
set_title("Wir setzen 80 Mio. € auf drei Segmente, in denen der Markt am stärksten wächst", 0.7, 2.2, 8.6, 2.4, 44, WHITE)
text(0.7, 5.0, 9.3, 0.4, "Vorlage für den Vorstand  ·  Marktfokus 2027 bis 2029  ·  10. November 2026", 17, L, WHITE)
text(0.4, 6.93, 9, 0.3, "Beispieldaten, fiktiv.", 12, L, WHITE)

# ======================= 2  Antwort zuerst ============================================================
new_slide("Wir setzen 80 Mio. € auf drei Segmente, in denen 69\u00a0% des Marktzuwachses liegen",
          "Antwort zuerst. Drei Argumente: (1) 69 % des Zuwachses von 9,0 Mrd. € liegen in Cyber, Gesundheit, Logistik, unser Anteil dort 2,1 %. "
          "(2) Option B bringt 1,16 € Mehr-Anteil je investiertem Euro, Option A 0,32 €. (3) Das Wachstum von 11,5 % pro Jahr ist klar, "
          "die Kurve ist aber 8-mal glatter als Zufall erlaubt. Beispieldaten, fiktiv.")
srows = [(g_gear1, "Der Markt wächst dort am stärksten", "Cyber, Gesundheit und Logistik liefern 6,2 von 9,0 Mrd. € Zuwachs bis 2029, unser Anteil liegt dort bei 2,1\u00a0%.", "69\u00a0%", "des Marktzuwachses"),
         (g_target, "Der Fokus rechnet sich besser als die Breite", "80 statt 140 Mio. € Investition bringen im Basisfall 93 statt 45 Mio. € Mehr-Anteil.", "1,16\u00a0€", "Beitrag je investiertem Euro"),
         (g_check, "Die Datenbasis ist vor dem Pilot zu prüfen", "Das Wachstum von 11,5\u00a0% pro Jahr ist klar, die Kurve ist aber 8-mal glatter, als Zufall erlaubt.", "×8", "zu glatt für echte Stichproben")]
for i, (g, ttl, desc, num, cap) in enumerate(srows):
    y = 1.62 + i * 1.47
    card(0.4, y, 12.53, 1.3)
    shape(S.OVAL, 0.6, y + 0.14, 0.32, 0.32, fill=DB); text(0.6, y + 0.14, 0.32, 0.32, str(i + 1), 12, M, WHITE, "c", "m")
    g(1.25, y + 0.68, 0.95)
    text(2.05, y + 0.2, 7.4, 0.36, ttl, 18, M, DB)
    text(2.05, y + 0.62, 7.3, 0.6, desc, 13, L, DB)
    shape(S.RECTANGLE, 9.65, y + 0.2, 0.02, 0.9, fill=DB)
    text(9.9, y + 0.15, 2.9, 0.6, num, 36, O, ZB, "l", "m"); text(9.9, y + 0.8, 2.9, 0.3, cap, 12, M, DB)
shape(S.ROUNDED_RECTANGLE, 0.4, 6.14, 12.53, 0.66, fill=DB)
text(0.65, 6.14, 1.9, 0.66, "WIR EMPFEHLEN", 12, M, WHITE, "l", "m")
x = 2.55
for j, step in enumerate(["Fokus freigeben", "Erhebung prüfen", "Pilot starten"]):
    pill(x, 6.24, 2.5, step, WHITE, DB, h=0.46, size=14); x += 2.5
    if j < 2: shape(S.RIGHT_ARROW, x + 0.12, 6.3, 0.5, 0.34, fill=WHITE); x += 0.74
footer("Beispieldaten, fiktiv. Die Zahlen 1 bis 3 stehen im Anhang und auf den Folien 3 bis 6.")

# ======================= 1  Beleg: Wachstum vs. unser Anteil ============================================
new_slide("In den drei am stärksten wachsenden Segmenten ist unser Marktanteil am kleinsten",
          "Cyber, Gesundheit und Logistik liefern 6,2 von 9,0 Mrd. € Marktzuwachs (69 %). Unser Anteil liegt dort bei 2,1 %, in den "
          "übrigen fünf Segmenten bei 3,5 % (gewichtet nach Zuwachs). Beispieldaten, fiktiv.")
shape(S.ROUNDED_RECTANGLE, 11.4, 0.93, 1.5, 0.3, fill="E9EBF0", rad=0.15)
shape(S.OVAL, 11.45, 0.96, 0.24, 0.24, fill=DB); text(11.45, 0.96, 0.24, 0.24, "1", 10, M, WHITE, "c", "m")
text(11.78, 0.93, 1.1, 0.3, "Der Markt", 11, L, DB, "l", "m")
shape(S.ROUNDED_RECTANGLE, 0.4, 1.62, 8.5, 4.4, fill=WHITE, line=LB)
CH_Y, CH_H, PY, PH = 2.2, 3.7, 0.02, 0.96
rows_y0 = CH_Y + PY * CH_H; row_h = PH * CH_H / 8
shape(S.ROUNDED_RECTANGLE, 0.52, rows_y0 - 0.02, 8.26, 3 * row_h + 0.04, fill=LB, alpha=30, rad=0.08, name="Fokus-Zone")
pill(7.2, rows_y0 + 0.07, 1.5, "Fokus-Segmente", DB, WHITE, h=0.28, size=11)
text(0.65, 1.79, 4.4, 0.3, "MARKTZUWACHS 2026 BIS 2029, MRD. €", 12, M, ZB)
text(5.45, 1.79, 3.2, 0.3, "UNSER MARKTANTEIL, %", 12, M, ZB)
cats = ["Gesundheit", "Cyber", "Logistik", "Handwerk", "Handel", "Industrie", "Gastro", "Freie Berufe"]
grow = [2.4, 2.2, 1.6, 0.9, 0.9, 0.6, 0.2, 0.2]
share = [2.3, 2.0, 2.0, 3.6, 3.4, 3.8, 3.0, 3.5]
hbar(0.5, CH_Y, 4.7, CH_H, cats, grow, 3, 3.0, '0.0', True, (0.28, PY, 0.58, PH),
     "Balkendiagramm Marktzuwachs 2026 bis 2029 je Segment in Mrd. Euro, absteigend sortiert")
hbar(5.35, CH_Y, 3.4, CH_H, cats, share, 3, 5.0, '0.0', False, (0.02, PY, 0.82, PH),
     "Balkendiagramm Unser Marktanteil je Segment in Prozent, gleiche Reihenfolge wie links")
shape(S.RECTANGLE, 5.28, CH_Y + 0.1, 0.01, CH_H - 0.2, fill=LB)
# rechte Spalte: eine Hauptaussage (dunkel) + Gegenwert (hell)
shape(S.ROUNDED_RECTANGLE, 9.15, 1.62, 3.78, 2.1, fill=DB)
g_gear1(9.62, 2.15, 0.6)
text(10.1, 1.82, 2.7, 0.75, "69 %", 46, O, WHITE, "l", "m")
text(9.4, 2.72, 3.3, 0.9, "des Zuwachses von 9,0 Mrd. € entfallen auf Cyber, Gesundheit und Logistik", 14, L, WHITE)
shape(S.ROUNDED_RECTANGLE, 9.15, 3.92, 3.78, 2.1, fill=LB, alpha=30)
g_c(9.62, 4.45, 0.6)
text(10.1, 4.12, 2.7, 0.75, "2,1 % statt 3,5 %", 24, O, ZB, "l", "m")
text(9.4, 5.02, 3.3, 0.9, "ist unser Anteil dort, verglichen mit den übrigen fünf Segmenten", 14, L, DB)
shape(S.ROUNDED_RECTANGLE, 0.4, 6.14, 12.53, 0.66, fill=DB)
text(0.65, 6.14, 1.7, 0.66, "EINORDNUNG", 12, M, WHITE, "l", "m")
text(2.45, 6.14, 10.3, 0.66, "Ein Prozentpunkt mehr Anteil am Zuwachs der Fokus-Segmente entspricht 62 Mio. €.", 16, L, WHITE, "l", "m")
footer("Beispieldaten, fiktiv. Marktanteil = Durchschnitt je Gruppe, gewichtet nach Marktzuwachs. 1 Pp × 6,2 Mrd. € = 62 Mio. €.")

# ======================= 2  Optionen bewerten ===========================================================
new_slide("Der Fokus auf drei Segmente bringt am meisten Beitrag je investiertem Euro",
          "Option B: +1,5 Pp auf 6,2 Mrd. € = 93 Mio. € bei 80 Mio. € Investition (1,16 € je Euro). Option A: +0,5 Pp auf 9,0 Mrd. € = 45 Mio. € "
          "bei 140 Mio. € (0,32 €). Option C: kein Beitrag, keine Investition. Beispieldaten, fiktiv.")
LX, LW, CWD, CG = 0.4, 3.0, 2.98, 0.165
cols = [LX + LW + CG + i * (CWD + CG) for i in range(3)]
heads = [("Option A", "Breit wachsen", "alle acht Segmente"), ("Option B", "Fokus auf drei Segmente", "Cyber, Gesundheit, Logistik"),
         ("Option C", "Bestand halten", "keine neue Investition")]
HY, HH, RY, RHH = 1.62, 1.0, 2.72, 0.8
for i, (x, (o, n, d)) in enumerate(zip(cols, heads)):
    rec = i == 1
    shape(S.ROUNDED_RECTANGLE, x, HY, CWD, HH, fill=DB if rec else "DDE4E3", rad=0.1)
    text(x + 0.2, HY + 0.12, CWD - 0.4, 0.25, o.upper(), 11, M, WHITE if rec else ZB, spacing=100)
    text(x + 0.2, HY + 0.37, CWD - 0.4, 0.3, n, 15, M, WHITE if rec else DB)
    text(x + 0.2, HY + 0.68, CWD - 0.4, 0.25, d, 12, L, WHITE if rec else DB)
pill(cols[1] + CWD - 1.25, HY + 0.1, 1.05, "Empfohlen", LB, DB, h=0.28, size=11)
labels = [("Mehr-Anteil bis 2029", "Pp-Gewinn × Marktzuwachs"), ("Investition 2027 bis 2029", None),
          ("Beitrag je investiertem Euro", None), ("Umsetzungsrisiko", None)]
cells = [[("45 Mio. €", "+0,5 Pp auf 9,0 Mrd. €"), ("93 Mio. €", "+1,5 Pp auf 6,2 Mrd. €"), ("0 Mio. €", "Anteil unverändert")],
         [("140 Mio. €", ""), ("80 Mio. €", ""), ("0 Mio. €", "")],
         [("0,32 €", "je investiertem Euro"), ("1,16 €", "je investiertem Euro"), ("kein Beitrag", "")],
         [("hoch", "acht Segmente parallel"), ("mittel", "drei Segmente, mit Pilot"), ("niedrig", "Anteil nicht gesichert")]]
risk_fill = {"hoch": 1.0, "mittel": 0.5, "niedrig": 0.0}
for r, ((lab, sub), crow) in enumerate(zip(labels, cells)):
    y = RY + r * RHH
    text(LX + 0.05, y + 0.14, LW - 0.2, 0.3, lab, 14, M, DB)
    if sub: text(LX + 0.05, y + 0.45, LW - 0.2, 0.25, sub, 12, L, DB)
    shape(S.RECTANGLE, LX, y + RHH - 0.01, LW + CG + 3 * CWD + 2 * CG, 0.012, fill="D5E3F2")
    for i, (x, (v, d)) in enumerate(zip(cols, crow)):
        if r < 3:
            text(x + 0.2, y + 0.07, CWD - 0.4, 0.5, v, 28 if i == 1 else 24, O, ZB if i == 1 else DB, "l", "m")
            if d: text(x + 0.2, y + 0.55, CWD - 0.4, 0.22, d, 12, L, DB)
        else:
            f = risk_fill[v]
            shape(S.OVAL, x + 0.2, y + 0.17, 0.26, 0.26, fill=DB if f == 1 else WHITE, line=DB, lw=1.5)
            if f == 0.5:
                ch_ = shape(S.CHORD, x + 0.2, y + 0.17, 0.26, 0.26, fill=DB); ch_.adjustments[0] = 54; ch_.adjustments[1] = 162
            text(x + 0.58, y + 0.12, CWD - 0.7, 0.3, v, 16, M, DB)
            text(x + 0.58, y + 0.43, CWD - 0.7, 0.3, d, 12, L, DB)
shape(S.ROUNDED_RECTANGLE, cols[1] - 0.06, HY - 0.04, CWD + 0.12, RY + 4 * RHH - HY + 0.1, line=ZB, lw=2.5, rad=0.12, name="Empfehlungsrahmen")
shape(S.ROUNDED_RECTANGLE, 0.4, 6.14, 12.53, 0.66, fill=DB)
text(0.65, 6.14, 1.9, 0.66, "EMPFEHLUNG", 12, M, WHITE, "l", "m")
text(2.45, 6.14, 10.3, 0.66, "Option B: höchster Ertrag je Euro, mittleres Risiko und nur 80 statt 140 Mio. € Investition.", 15, L, WHITE, "l", "m")
footer("Beispieldaten, fiktiv. Mehr-Anteil = Pp-Gewinn × Marktzuwachs 2026 bis 2029 \n(A: 0,5 Pp × 9,0 Mrd. €; B: 1,5 Pp × 6,2 Mrd. €). Pp = Prozentpunkte.")

tracker(2, 'Die Rechnung')

# ======================= 5  Szenarien =================================================================
new_slide("Der Fokus rechnet sich ab 1,3 Prozentpunkten Mehr-Anteil, im Basisfall erreichen wir 1,5",
          "Szenarien sind Fortschreibungen des Anteilsgewinns, keine Prognosen. Break-even: 80 Mio. € geteilt durch 6,2 Mrd. € = 1,29 Pp. "
          "Vorsichtig +0,8 Pp = 50 Mio. €, Basis +1,5 Pp = 93 Mio. €, ambitioniert +2,2 Pp = 136 Mio. €. Beispieldaten, fiktiv.")
tracker(2, "Die Rechnung")
card(0.4, 1.62, 8.5, 4.4)
text(0.65, 1.79, 7.5, 0.3, "MEHR-ANTEIL BIS 2029 JE SZENARIO, MIO. € (OPTION B)", 12, M, ZB)
sc_cats = ["Vorsichtig  +0,8 Pp", "Basis  +1,5 Pp", "Ambitioniert  +2,2 Pp"]; sc_vals = [50, 93, 136]
cd = CategoryChartData(number_format='0'); cd.categories = sc_cats; cd.add_series("Mehr-Anteil, Mio. €", sc_vals)
FX, FY, FW, FH = 0.5, 2.15, 8.3, 3.75; IX, IY, IW, IH = 0.04, 0.1, 0.92, 0.72
gf = Z.s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(FX), Inches(FY), Inches(FW), Inches(FH), cd)
gf.name = "Säulendiagramm Szenarien"
gf._element.nvGraphicFramePr.cNvPr.set("descr", "Säulendiagramm: Mehr-Anteil bis 2029 in Mio. Euro. Vorsichtig 50, Basis 93, ambitioniert 136; Investition 80 als gestrichelte Linie.")
ch = gf.chart; ch.has_legend = False; ch.has_title = False
ch.font.size = Pt(13); ch.font.name = L; ch.font.color.rgb = rgb(DB)
pl = ch.plots[0]; pl.gap_width = 70; pl.vary_by_categories = False
for i, v in enumerate(sc_vals):
    pt = pl.series[0].points[i]; pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(ZB if v >= 80 else FOCUS_LIGHT)
pl.has_data_labels = True
dl = pl.data_labels; dl.number_format = '0'; dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END; dl.font.size = Pt(14); dl.font.name = L; dl.font.color.rgb = rgb(DB)
va = ch.value_axis; va.minimum_scale, va.maximum_scale = 0, 160; va.has_major_gridlines = False; va.visible = False
ca = ch.category_axis; ca.major_tick_mark = XL_TICK_MARK.NONE; ca.format.line.color.rgb = rgb(LB); ca.tick_labels.font.size = Pt(13)
plot_layout(ch, IX, IY, IW, IH); transparent(ch)
ly = FY + FH * (IY + IH * (1 - 80 / 160))
ln = shape(S.RECTANGLE, FX + FW * IX, ly - 0.006, FW * IW, 0.012, fill=DB, name="Linie Investition 80 Mio. €")
text(FX + FW * IX + 0.05, ly - 0.36, 3.2, 0.3, "Investition 80 Mio. €", 13, M, DB)
shape(S.ROUNDED_RECTANGLE, 9.15, 1.62, 3.78, 2.1, fill=DB)
g_target(9.62, 2.15, 0.6)
text(10.1, 1.82, 2.7, 0.75, "1,3\u00a0Pp", 40, O, WHITE, "l", "m")
text(9.4, 2.72, 3.3, 0.9, "Break-even: 80 Mio. € geteilt durch 6,2 Mrd. € Marktzuwachs", 14, L, WHITE)
shape(S.ROUNDED_RECTANGLE, 9.15, 3.92, 3.78, 2.1, fill=LB, alpha=30)
g_hourglass(9.62, 4.45, 0.6)
text(10.1, 4.12, 2.7, 0.75, "−30 Mio. €", 30, O, ZB, "l", "m")
text(9.4, 5.02, 3.3, 0.9, "Lücke im vorsichtigen Fall: 50 statt 80 Mio. € Mehr-Anteil", 14, L, DB)
band("EINORDNUNG", "Das Risiko bleibt begrenzt, weil die großen Ausgaben erst nach dem Pilot-Entscheidungspunkt fließen.")
footer("Beispieldaten, fiktiv. Szenarien sind Fortschreibungen, keine Prognosen. Mehr-Anteil = Pp-Gewinn × 6,2 Mrd. € Marktzuwachs;\nkein Ergebnis.")

# ======================= 6  Datenbasis ================================================================
new_slide("Das Wachstum von 11,5\u00a0% pro Jahr ist klar, die Datenbasis dahinter ist noch zu glatt",
          "Situation: Der Anteil stieg von 28,0 % auf 34,5 %, alle 23 Monatsschritte zeigen nach oben. Komplikation: Das Tempo war zuletzt niedriger (0,17 statt 0,30 Pp), "
          "so niedrig war es schon im Aug 2025 (2 von 21 Fenstern), und die Kurve ist 8-mal glatter, als Zufall erlaubt. "
          "Schlussfolgerung: Nachlassen möglich, aber nicht belegt; erst die Erhebung prüfen. Fiktive Daten.")
tracker(3, "Die Daten")
card(0.4, 1.62, 6.1, 4.4); card(6.8, 1.62, 6.13, 4.4)
text(0.65, 1.79, 5.6, 0.3, "WACHSTUM DES ANTEILS PRO JAHR, %", 12, M, ZB)
AX0, AX1, AY = 0.9, 6.0, 4.3
def xv(v): return AX0 + (AX1 - AX0) * v / 20
shape(S.RECTANGLE, AX0, AY, AX1 - AX0, 0.02, fill=DB)
for v in (0, 5, 10, 15, 20):
    shape(S.RECTANGLE, xv(v) - 0.005, AY, 0.012, 0.1, fill=DB); text(xv(v) - 0.3, AY + 0.14, 0.6, 0.25, str(v), 12, L, DB, "c")
shape(S.ROUNDED_RECTANGLE, xv(5.5), AY - 0.55, xv(17.8) - xv(5.5), 0.34, fill=FOCUS_LIGHT, rad=0.08)
text(xv(5.5), AY - 0.95, 4.0, 0.3, "Spanne 5,5 bis 17,8\u00a0%", 13, L, DB)
shape(S.ROUNDED_RECTANGLE, xv(11.5), AY - 0.55, xv(12.3) - xv(11.5), 0.34, fill=ZB, rad=0.04)
shape(S.ISOSCELES_TRIANGLE, xv(11.9) - 0.12, AY - 0.18, 0.24, 0.18, fill=DB)
text(xv(11.9) - 1.3, AY + 0.5, 2.6, 0.62, "11,5 bis 12,3\u00a0%\ndrei Rechenwege", 13, M, DB, "c")
text(0.65, 5.35, 5.6, 0.55, "Drei Rechenwege kommen zum selben Ergebnis. Das Wachstum ist klar.", 14, L, DB)
text(7.05, 1.79, 5.7, 0.3, "DREIMONATSFENSTER MIT SO LANGSAMEM TEMPO", 12, M, ZB)
for k in range(21):
    cx = 7.35 + (k % 7) * 0.78; cy = 2.65 + (k // 7) * 0.78
    hot = k in (13, 20)
    shape(S.OVAL, cx, cy, 0.5, 0.5, fill=DB if hot else LB, alpha=None if hot else 55,
          name=("Fenster so langsam" if hot else "Fenster"), alt=("Fenster mit Tempo bis 0,17 Pp" if hot else None))
text(7.05, 5.1, 5.7, 0.3, "2 von 21", 24, O, ZB)
text(7.05, 5.5, 5.7, 0.5, "Fenster so langsam wie zuletzt (0,17 Pp pro Monat); schon im Aug 2025 war es so. Nachlassen: möglich, nicht belegt.", 12, L, DB)
band("BEZUG", "Darum steht die Prüfung der Erhebung als Entscheidungspunkt vor dem Pilot, nicht danach.")
footer("Fiktive Daten. Spanne = 95-Prozent-Bereich (Normalnäherung); 23 Monate = 1,92 Jahre; Wachstum des Anteils,\nnicht der Prozentpunkte. Pp = Prozentpunkte.")

# ======================= 7  Risiken mit Gegenmaßnahme ==================================================
new_slide("Drei Risiken sind benannt, jedes hat eine Gegenmaßnahme und einen festen Zeitpunkt",
          "Risiken stehen neben der Entscheidung, die sie betreffen. Beispiel, fiktiv.")
heads7 = [("Risiko", 0.65), ("Was dann passiert", 4.1), ("Gegenmaßnahme", 7.2), ("Wann", 11.45)]
for t_, x_ in heads7: text(x_, 1.65, min(3.0, 13.0 - x_), 0.28, t_.upper(), 11, M, ZB, spacing=100)
risks = [(g_info, "Die Datenbasis trägt nicht", "Steuerung auf Monatswerten mit ±3,2 Pp Streuung", "Erhebung prüfen, Budget an Jahreswerten (±0,9 Pp) ausrichten", "vor Phase 1"),
         (g_scales, "Der Anteilsgewinn bleibt unter 1,3 Pp", "Der Beitrag deckt die 80 Mio. € nicht", "Pilot in einem Segment, Ausbau nur bei Gewinn über Zufall", "vor Phase 3"),
         (g_hourglass, "Das Wachstum lässt nach", "Tempo 0,17 statt 0,30 Pp pro Monat, nicht belegt", "Dreimonatsfenster monatlich beobachten, bei Bestätigung neu bewerten", "laufend")]
for i, (g, r_, w_, m_, t_) in enumerate(risks):
    y = 2.0 + i * 1.38
    card(0.4, y, 12.53, 1.22)
    g(0.95, y + 0.61, 0.62)
    text(1.4, y + 0.2, 2.4, 0.85, r_, 16, M, DB, "l", "m")
    text(4.1, y + 0.2, 2.8, 0.85, w_, 13, L, DB, "l", "m")
    shape(S.ROUNDED_RECTANGLE, 6.95, y + 0.14, 4.3, 0.94, fill=LB, alpha=30, rad=0.08)
    text(7.2, y + 0.14, 3.9, 0.94, m_, 13, L, DB, "l", "m")
    pill(11.45, y + 0.45, 1.3, t_, DB, WHITE, h=0.32, size=11)
band("EINORDNUNG", "Kein Risiko bleibt offen: Das größte, die Datenbasis, wird zuerst und vor jeder Ausgabe geprüft.")
footer("Beispiel, fiktiv. Pp = Prozentpunkte. Phasen und Entscheidungspunkte: Folie 8.")

# ======================= 3  Fahrplan mit Entscheidungspunkten ============================================
new_slide("In vier Schritten vom Piloten zur Skalierung, mit einer Entscheidung vor jedem Ausbau",
          "Phase 1 klärt die Datenbasis, Phase 2 pilotiert ein Segment, Phase 3 weitet auf drei Segmente aus, Phase 4 steuert auf Jahreswerte. "
          "Vor jeder Phase steht ein Entscheidungspunkt. Beispiel, fiktiv.")
phases = [("1", "Datenbasis klären", "Q1 2027", g_check, "Erhebung und Monatswerte prüfen", "Belastbare Datenbasis", "Erhebung belastbar?"),
          ("2", "Pilot in einem Segment", "Q2 2027", g_flask, "Fabric- und Databricks-Dataset testen", "Messbarer Anteilsgewinn", "Gewinn über Zufall?"),
          ("3", "Auf drei Segmente ausweiten", "Q3 2027", g_gear1, "Cyber, Gesundheit, Logistik anbinden", "Drei Segmente live", "Ertrag je Euro hält?"),
          ("4", "Auf Jahreswerte steuern", "Q4 2027", g_trend, "Budget an Jahreswerten ausrichten", "Steuerung im Regelbetrieb", "Dauerbetrieb freigeben?")]
LBLW = 1.55
colw = (12.53 - LBLW - 3 * 0.1) / 4
xs = [0.4 + LBLW + i * (colw + 0.1) for i in range(4)]
shades = [LB, MB, ZB, DB]
for i, (x, (n, t, q, g, what, res, gate)) in enumerate(zip(xs, phases)):
    shp = shape(S.PENTAGON, x, 1.62, colw + (0.1 if i < 3 else 0), 1.0, fill=shades[i] if i != 1 else ZB)
    dark_txt = i == 0
    text(x + 0.22, 1.7, colw - 0.9, 0.25, q.upper(), 11, M, DB if dark_txt else WHITE, spacing=100)
    text(x + 0.22, 1.95, colw - 0.6, 0.6, t, 15, M, DB if dark_txt else WHITE)
LANES = [("Was passiert", 2.85, 1.0), ("Ergebnis", 3.95, 0.85), ("Entscheidung", 4.92, 1.0)]
for lab, y, h in LANES:
    shape(S.RECTANGLE, 0.4, y - 0.04, 12.53, 0.01, fill="D5E3F2")
    text(0.4, y + 0.1, LBLW - 0.15, 0.3, lab, 13, M, ZB)
for i, (x, (n, t, q, g, what, res, gate)) in enumerate(zip(xs, phases)):
    g(x + 0.38, 3.33, 0.5)
    text(x + 0.75, 3.05, colw - 0.8, 0.8, what, 13, L, DB)
    text(x + 0.2, 4.07, colw - 0.3, 0.6, res, 14, M, DB)
    shape(S.DIAMOND, x + 0.2, 5.12, 0.34, 0.34, fill=DB, name="Entscheidungspunkt %s" % n,
          alt="Entscheidungspunkt vor Phase " + n)
    text(x + 0.65, 5.1, colw - 0.75, 0.55, gate, 14, M, DB, "l", "m")
shape(S.ROUNDED_RECTANGLE, 0.4, 6.14, 12.53, 0.66, fill=DB)
text(0.65, 6.14, 1.9, 0.66, "LOGIK", 12, M, WHITE, "l", "m")
text(2.45, 6.14, 10.3, 0.66, "Jede Phase kostet erst Geld, wenn der Entscheidungspunkt davor bestanden ist.", 16, L, WHITE, "l", "m")
shape(S.DIAMOND, 0.4, 6.98, 0.2, 0.2, fill=DB)
footer("       = Entscheidungspunkt. Zeitplan und Inhalte sind ein Beispiel (fiktiv).")

# ======================= 4  Entscheidung (Dark Ground) ===================================================
new_slide("Wir bitten um drei Entscheidungen, damit der Pilot im ersten Quartal startet",
          "1 Fokus freigeben (Option B, 80 Mio. €), 2 Datenerhebung prüfen, 3 Steuerung auf Jahreswerte. Beispiel, fiktiv.", dark=True)
asks = [("1", g_gear1, "Fokus freigeben", "Option B für Cyber, Gesundheit und Logistik", "80 Mio. €", "Investition 2027 bis 2029"),
        ("2", g_check, "Datenerhebung prüfen", "Gate 1 vor dem Pilot: Ist die Erhebung belastbar?", "Q1 2027", "Entscheidung im ersten Quartal"),
        ("3", g_scales, "Auf Jahreswerte steuern", "Monatswerte sind zu ungenau, um daran Budget zu binden", "±0,9 Pp", "Genauigkeit der Jahreswerte")]
cw3 = (12.53 - 2 * 0.25) / 3
for i, (n, g, t, d, big, cap) in enumerate(asks):
    x = 0.4 + i * (cw3 + 0.25)
    shape(S.ROUNDED_RECTANGLE, x, 1.7, cw3, 4.75, fill=ZB, rad=0.14)
    shape(S.OVAL, x + 0.3, 2.0, 0.5, 0.5, fill=WHITE)
    text(x + 0.3, 2.0, 0.5, 0.5, n, 18, M, ZB, "c", "m")
    g(x + cw3 - 0.75, 2.25, 0.8)
    text(x + 0.3, 2.85, cw3 - 0.6, 0.45, t, 20, M, WHITE)
    text(x + 0.3, 3.35, cw3 - 0.6, 0.8, d, 14, L, WHITE)
    shape(S.RECTANGLE, x + 0.3, 4.6, cw3 - 0.6, 0.015, fill=WHITE)
    text(x + 0.3, 4.75, cw3 - 0.6, 0.85, big, 44, O, WHITE, "l", "m")
    text(x + 0.3, 5.7, cw3 - 0.6, 0.3, cap, 12, M, WHITE)
text(0.4, 6.62, 12.0, 0.3, "Entscheider und Termin: [DATA NEEDED: Gremium und Termin der Entscheidung]", 14, M, WHITE)
footer("Beispieldaten, fiktiv. Pp = Prozentpunkte; Investition aus Option B, Folie 4.")


# ======================= 10  Anhang: Segmentdaten ======================================================
new_slide("Ein Prozentpunkt Anteil ist in Gesundheit 24 Mio. € wert, in Gastro nur 2 Mio. €",
          "Anhang. Wert von 1 Pp = Marktzuwachs 2026 bis 2029 × 1 %. Beispieldaten, fiktiv.")
tracker("A", "Anhang")
segs = [("Gesundheit", 2.4, 2.3), ("Cyber", 2.2, 2.0), ("Logistik", 1.6, 2.0), ("Handwerk", 0.9, 3.6), ("Handel", 0.9, 3.4),
        ("Industrie", 0.6, 3.8), ("Gastro", 0.2, 3.0), ("Freie Berufe", 0.2, 3.5)]
fmt = lambda v: f"{v:.1f}".replace(".", ",")
gt = Z.s.shapes.add_table(9, 4, Inches(0.4), Inches(1.62), Inches(12.53), Inches(4.4))
gt.name = "Tabelle Segmentdaten"; tbl = gt.table
tbl.first_row = True
for j, w in enumerate((3.4, 3.1, 3.0, 3.03)): tbl.columns[j].width = Inches(w)
tbl.rows[0].height = Inches(0.5)
for i in range(1, 9): tbl.rows[i].height = Inches(0.484)
hdr = ["Segment", "Marktzuwachs 2026 bis 2029, Mrd. €", "Unser Marktanteil, %", "Wert von 1 Pp, Mio. €"]
def setc(c, t, size, font, color, fill, align):
    c.fill.solid(); c.fill.fore_color.rgb = rgb(fill)
    c.margin_left = c.margin_right = Inches(0.15); c.margin_top = c.margin_bottom = Inches(0.03)
    c.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = c.text_frame.paragraphs[0]; p.alignment = {"l": PP_ALIGN.LEFT, "r": PP_ALIGN.RIGHT}[align]
    r = p.add_run(); r.text = t; r.font.size = Pt(size); r.font.name = font; r.font.color.rgb = rgb(color)
for j, h in enumerate(hdr): setc(tbl.cell(0, j), h, 13, M, WHITE, DB, "l" if j == 0 else "r")
for i, (n_, z_, a_) in enumerate(segs, start=1):
    fill = "DCEAF6" if i <= 3 else WHITE
    for j, v in enumerate((n_, fmt(z_), fmt(a_), str(round(z_ * 10)))):
        setc(tbl.cell(i, j), v, 14, M if (j == 0 and i <= 3) else L, DB, fill, "l" if j == 0 else "r")
tcPr = None
band("EINORDNUNG", "Die drei hell hinterlegten Fokus-Segmente sind je Prozentpunkt 62 Mio. € wert, die übrigen fünf 28 Mio. €.")
footer("Beispieldaten, fiktiv. Wert von 1 Pp = Marktzuwachs × 1 %. Pp = Prozentpunkte.")

# ======================= 11  Anhang: Annahmen ==========================================================
new_slide("Alle Werte folgen aus fünf Annahmen, die wir offenlegen",
          "Anhang: Methodik. Beispieldaten, fiktiv.")
tracker("A", "Anhang")
ass = [("Marktzuwachs", "Zuwachs je Segment 2026 bis 2029, Summe 9,0 Mrd. €, davon 6,2 Mrd. € in den drei Fokus-Segmenten."),
       ("Marktanteil", "Durchschnitt je Gruppe, gewichtet nach Marktzuwachs: Fokus 2,1\u00a0%, übrige fünf 3,5\u00a0%."),
       ("Mehr-Anteil", "Pp-Gewinn × Marktzuwachs. Option A: +0,5 Pp auf 9,0 Mrd. €; Option B: +1,5 Pp auf 6,2 Mrd. €. Kein Ergebnis."),
       ("Szenarien", "Fortschreibung des Pp-Gewinns (+0,8, +1,5, +2,2 Pp), keine Prognose. Break-even bei 80 Mio. € Investition: 1,3 Pp."),
       ("Wachstumsrate", "Relatives Wachstum des Anteils (28,0 auf 34,5\u00a0% in 23 Monaten = 1,92 Jahre); Spanne = 95-Prozent-Bereich.")]
for i, (k, v) in enumerate(ass):
    y = 1.62 + i * 0.88
    card(0.4, y, 12.53, 0.76, "tint")
    shape(S.OVAL, 0.6, y + 0.2, 0.36, 0.36, fill=DB); text(0.6, y + 0.2, 0.36, 0.36, str(i + 1), 13, M, WHITE, "c", "m")
    text(1.2, y, 2.4, 0.76, k, 16, M, DB, "l", "m")
    text(3.7, y, 9.1, 0.76, v, 13, L, DB, "l", "m")
footer("Beispieldaten, fiktiv. Pp = Prozentpunkte.")
prs.save(sys.argv[1])
