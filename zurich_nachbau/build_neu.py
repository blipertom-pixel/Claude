# -*- coding: utf-8 -*-
"""Vier neue Zurich-Folien (ohne Master), nach Gestaltungsleitfaden: Beleg, Optionen, Fahrplan, Entscheidung.
Alle Zahlen sind fiktive Beispieldaten und aus einem Modell abgeleitet (siehe Fußnoten)."""
import sys
import zhelp as Z
from zhelp import *
from pptx.oxml import parse_xml

C_NS = "http://schemas.openxmlformats.org/drawingml/2006/chart"


def plot_layout(chart, x, y, w, h):
    pa = chart._chartSpace.chart.plotArea
    for old in pa.findall(qn("c:layout")): pa.remove(old)
    lay = parse_xml(f'<c:layout xmlns:c="{C_NS}"><c:manualLayout><c:layoutTarget val="inner"/><c:xMode val="edge"/>'
                    f'<c:yMode val="edge"/><c:x val="{x}"/><c:y val="{y}"/><c:w val="{w}"/><c:h val="{h}"/></c:manualLayout></c:layout>')
    pa.insert(0, lay)


def transparent(chart):
    cs = chart._chartSpace
    sp = parse_xml('<c:spPr xmlns:c="%s" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr>' % C_NS)
    for old in cs.findall(qn("c:spPr")): cs.remove(old)
    cs.insert(list(cs).index(cs.find(qn("c:chart"))) + 1, sp)


def hbar(x, y, w, h, cats, vals, nfocus, vmax, fmt, show_cats, inner, alt):
    cd = CategoryChartData(number_format=fmt); cd.categories = cats; cd.add_series("Wert", vals)
    gf = Z.s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    gf._element.nvGraphicFramePr.cNvPr.set("descr", alt); gf.name = alt[:40]
    ch = gf.chart; ch.has_legend = False; ch.has_title = False
    ch.font.size = Pt(13); ch.font.name = L; ch.font.color.rgb = rgb(DB)
    pl = ch.plots[0]; pl.gap_width = 38; pl.vary_by_categories = False
    for i in range(len(vals)):
        pt = pl.series[0].points[i]; pt.format.fill.solid()
        pt.format.fill.fore_color.rgb = rgb(ZB if i < nfocus else FOCUS_LIGHT)
    pl.has_data_labels = True
    dl = pl.data_labels; dl.number_format = fmt; dl.number_format_is_linked = False
    dl.position = XL_LABEL_POSITION.OUTSIDE_END; dl.font.size = Pt(13); dl.font.name = L; dl.font.color.rgb = rgb(DB)
    va = ch.value_axis; va.minimum_scale, va.maximum_scale = 0, vmax
    va.has_major_gridlines = False; va.visible = False
    ca = ch.category_axis; ca.reverse_order = True; ca.major_tick_mark = XL_TICK_MARK.NONE
    ca.format.line.color.rgb = rgb(LB)
    if show_cats:
        ca.tick_labels.font.size = Pt(13)
    else:
        from pptx.enum.chart import XL_TICK_LABEL_POSITION
        ca.tick_label_position = XL_TICK_LABEL_POSITION.NONE
    plot_layout(ch, *inner); transparent(ch)
    return gf


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
    shape(S.ROUNDED_RECTANGLE, x, 1.75, cw3, 4.75, fill=ZB, rad=0.14)
    shape(S.OVAL, x + 0.3, 2.0, 0.5, 0.5, fill=WHITE)
    text(x + 0.3, 2.0, 0.5, 0.5, n, 18, M, ZB, "c", "m")
    g(x + cw3 - 0.75, 2.25, 0.8)
    text(x + 0.3, 2.85, cw3 - 0.6, 0.45, t, 20, M, WHITE)
    text(x + 0.3, 3.35, cw3 - 0.6, 0.8, d, 14, L, WHITE)
    shape(S.RECTANGLE, x + 0.3, 4.6, cw3 - 0.6, 0.015, fill=WHITE)
    text(x + 0.3, 4.75, cw3 - 0.6, 0.85, big, 44, O, WHITE, "l", "m")
    text(x + 0.3, 5.7, cw3 - 0.6, 0.3, cap, 12, M, WHITE)
footer("Beispieldaten, fiktiv. Pp = Prozentpunkte; Investition aus Option B, Folie 2.")
prs.save(sys.argv[1])
