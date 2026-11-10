# -*- coding: utf-8 -*-
"""Vier Zurich-Folien (ohne Master) nach Beispielfotos, verbessert nach Gestaltungsleitfaden v0.1.
Schriftnamen: Zurich Sans Light/Medium + Ogg (Ersatz beim Rendern: Inter / Source Serif 4)."""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE as S
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_TICK_MARK
from pptx.oxml.ns import qn
from lxml import etree

DB, ZB, MB, LB, WHITE = "23366F", "2167AE", "5495CF", "91BFE3", "FFFFFF"
L, M, O = "Zurich Sans Light", "Zurich Sans Medium", "Ogg"
BG, FOCUS_LIGHT = "BFD6EE", "7FB0E0"
rgb = RGBColor.from_string
prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
s = None
PAGE = 0


def new_slide(title, notes, title_w=10.3):
    """Titel zuerst (Lesereihenfolge), dann Logo; feste Ränder 0,4 in (~1 cm)."""
    global s, PAGE
    PAGE += 1
    s = prs.slides.add_slide(prs.slide_layouts[6])
    text(0.44, 0.34, title_w, 0.9, title, 26, L, ZB).name = "Titel"
    shape(S.OVAL, 11.45, 0.42, 0.4, 0.4, fill=ZB, name="Logo (Nachbildung)", alt="Zurich Logo")
    text(11.45, 0.42, 0.4, 0.4, "Z", 16, M, WHITE, "c", "m")
    text(11.95, 0.42, 1.1, 0.4, "ZURICH", 15, M, ZB, "l", "m", spacing=100)
    s.notes_slide.notes_text_frame.text = notes


def footer(src=None):
    if src: text(0.4, 6.93, 11.0, 0.45, src, 12, L, DB).name = "Quelle"
    text(11.9, 6.95, 0.3, 0.25, str(PAGE), 10, L, DB, "r")
    text(12.3, 6.95, 0.65, 0.25, "© Zurich", 10, L, DB)


def shape(kind, x, y, w, h, fill=None, line=None, lw=1.0, rad=None, alpha=None, name=None, alt=None):
    sp = s.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    st = sp._element.find(qn("p:style"))
    if st is not None: sp._element.remove(st)            # kein Theme-Schatten
    if kind == S.ROUNDED_RECTANGLE:
        sp.adjustments[0] = min(0.5, (rad or 0.12) / min(w, h))
    if fill:
        sp.fill.solid(); sp.fill.fore_color.rgb = rgb(fill)
        if alpha:
            etree.SubElement(sp._element.spPr.find(qn("a:solidFill"))[0], qn("a:alpha")).set("val", str(alpha * 1000))
    else:
        sp.fill.background()
    if line:
        sp.line.color.rgb = rgb(line); sp.line.width = Pt(lw)
    else:
        sp.line.fill.background()
    if name: sp.name = name
    if alt: sp._element.nvSpPr.cNvPr.set("descr", alt)
    return sp


def text(x, y, w, h, t, size=14, font=L, color=DB, align="l", anchor="t", spacing=None):
    """Kein AutoFit; mit \\n werden bewusst Zeilen umbrochen (keine einzelnen Restwörter)."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE}[anchor]
    for i, line in enumerate(t.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[align]
        r = p.add_run(); r.text = line
        r.font.size = Pt(size); r.font.name = font; r.font.color.rgb = rgb(color)
        if spacing: r._r.get_or_add_rPr().set("spc", str(spacing))
    return tb


def pill(x, y, w, t, fill, color, h=0.32, size=12):
    shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=fill, rad=h / 2)
    text(x, y, w, h, t, size, M, color, "c", "m")


def poly(pts, cx, cy, d, fg, w=2.2):
    fb = s.shapes.build_freeform(Inches(cx + pts[0][0] * d), Inches(cy + pts[0][1] * d))
    fb.add_line_segments([(Inches(cx + a * d), Inches(cy + b * d)) for a, b in pts[1:]], close=False)
    f = fb.convert_to_shape(); f.fill.background()
    st = f._element.find(qn("p:style"))
    if st is not None: f._element.remove(st)
    f.line.color.rgb = rgb(fg); f.line.width = Pt(w); return f


# ---------- Piktogramme: einheitliche Sprache = helle Scheibe + Glyphe in Zurich/Dark Blue ----------
def disc(cx, cy, d, bg, alt):
    return shape(S.OVAL, cx - d / 2, cy - d / 2, d, d, fill=bg, name="Icon: " + alt, alt=alt)

def g_flask(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Reagenzglas für Prototypen")
    shape(S.ISOSCELES_TRIANGLE, cx - d*.2, cy - d*.05, d*.4, d*.38, fill=ZB)
    shape(S.RECTANGLE, cx - d*.07, cy - d*.3, d*.14, d*.28, fill=ZB)
    shape(S.RECTANGLE, cx - d*.12, cy - d*.32, d*.24, d*.04, fill=DB)

def g_search(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Lupe für Datenkataloge")
    shape(S.DONUT, cx - d*.28, cy - d*.3, d*.46, d*.46, fill=ZB).adjustments[0] = 0.18
    poly([(.15, .13), (.3, .3)], cx, cy, d, ZB, 3.5)

def g_network(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Netzwerk für APIs und MCP-Tools")
    P = [(-.18, .12), (.2, .16), (0, -.2)]
    for a, b in P: poly([(0, 0), (a, b)], cx, cy, d, DB, 1.2)
    shape(S.OVAL, cx - d*.07, cy - d*.07, d*.14, d*.14, fill=DB)
    for a, b in P: shape(S.OVAL, cx + a*d - d*.07, cy + b*d - d*.07, d*.14, d*.14, fill=ZB)

def g_info(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Info-Symbol für Metadaten")
    shape(S.OVAL, cx - d*.06, cy - d*.3, d*.12, d*.12, fill=ZB)
    shape(S.RECTANGLE, cx - d*.05, cy - d*.13, d*.10, d*.40, fill=ZB)

def g_check(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Haken für Datenqualität")
    poly([(-.22, .02), (-.06, .18), (.24, -.16)], cx, cy, d, ZB, 3.5)

def g_people(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Personengruppe für Zuständigkeiten")
    for dx, r, c in [(-.2, .11, ZB), (.2, .11, ZB), (0, .14, DB)]:
        shape(S.ROUNDED_RECTANGLE, cx + dx*d - r*1.5*d, cy + .1*d, r*3*d, r*1.7*d, fill=c, rad=0.05)
        shape(S.OVAL, cx + dx*d - r*d, cy - .02*d - r*2*d, 2*r*d, 2*r*d, fill=c)

def g_code(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Code-Symbol für Programmierung")
    shape(S.ROUNDED_RECTANGLE, cx - d*.3, cy - d*.25, d*.6, d*.5, fill=WHITE, rad=0.05)
    text(cx - d*.3, cy - d*.25, d*.6, d*.5, "</>", 12, M, ZB, "c", "m")

def g_lowcode(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Bausteine für Low Code")
    for i, w in enumerate((.5, .36, .44)):
        shape(S.ROUNDED_RECTANGLE, cx - d*.25, cy - d*.24 + i*d*.17, d*w, d*.11, fill=ZB, rad=0.03)
    shape(S.OVAL, cx + d*.1, cy + d*.02, d*.2, d*.24, fill=DB)

def g_gears(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Zahnräder für Automatisierung")
    shape(S.GEAR_6, cx - d*.3, cy - d*.3, d*.38, d*.38, fill=ZB)
    shape(S.GEAR_6, cx - d*.02, cy - d*.02, d*.32, d*.32, fill=DB)

def g_head(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Person für KI")
    shape(S.OVAL, cx - d*.2, cy - d*.3, d*.4, d*.44, fill=ZB)
    shape(S.ROUNDED_RECTANGLE, cx - d*.3, cy + d*.12, d*.6, d*.22, fill=DB, rad=0.08)

def g_target(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Zielscheibe für Problemverständnis")
    shape(S.DONUT, cx - d*.3, cy - d*.3, d*.6, d*.6, fill=ZB).adjustments[0] = 0.12
    shape(S.OVAL, cx - d*.1, cy - d*.1, d*.2, d*.2, fill=DB)

def g_star(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Person mit Sternen für Fachwissen")
    shape(S.OVAL, cx - d*.15, cy - d*.1, d*.3, d*.3, fill=DB)
    shape(S.ROUNDED_RECTANGLE, cx - d*.25, cy + d*.22, d*.5, d*.14, fill=DB, rad=0.07)
    for dx, dy in ((-.2, -.2), (0, -.3), (.2, -.2)):
        shape(S.STAR_5_POINT, cx + dx*d - d*.07, cy + dy*d - d*.07, d*.14, d*.14, fill=ZB)

def g_bulb(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Glühbirne für Kreativität")
    shape(S.OVAL, cx - d*.2, cy - d*.3, d*.4, d*.42, fill=ZB)
    shape(S.RECTANGLE, cx - d*.09, cy + d*.1, d*.18, d*.14, fill=DB)

def g_scales(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Waage für Urteilskraft")
    shape(S.RECTANGLE, cx - d*.015, cy - d*.3, d*.03, d*.55, fill=DB)
    shape(S.RECTANGLE, cx - d*.3, cy - d*.2, d*.6, d*.03, fill=DB)
    shape(S.RECTANGLE, cx - d*.12, cy + d*.25, d*.24, d*.04, fill=DB)
    for dx in (-.22, .22):
        shape(S.FLOWCHART_DELAY, cx + dx*d - d*.09, cy - d*.04, d*.18, d*.22, fill=ZB).rotation = 90

def g_trend(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Trendlinie für Wachstum")
    poly([(-.30, .16), (-.14, -.04), (0, .08), (.14, -.12), (.30, .06)], cx, cy, d, DB, 2.5)

def g_hourglass(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Sanduhr für Tempo")
    shape(S.FLOWCHART_COLLATE, cx - d*.2, cy - d*.3, d*.4, d*.6, fill=ZB)
    shape(S.RECTANGLE, cx - d*.26, cy - d*.33, d*.52, d*.05, fill=DB)
    shape(S.RECTANGLE, cx - d*.26, cy + d*.28, d*.52, d*.05, fill=DB)

def g_gear1(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Zahnrad für Fokus-Segmente")
    shape(S.GEAR_6, cx - d*.3, cy - d*.3, d*.6, d*.6, fill=ZB)
    shape(S.OVAL, cx - d*.09, cy - d*.09, d*.18, d*.18, fill=bg)

def g_c(cx, cy, d, bg=BG):
    disc(cx, cy, d, bg, "Ring-Symbol für Marktanteil")
    shape(S.DONUT, cx - d*.3, cy - d*.3, d*.6, d*.6, fill=ZB).adjustments[0] = 0.25
    shape(S.RECTANGLE, cx + d*.05, cy - d*.1, d*.3, d*.2, fill=bg)
    shape(S.RECTANGLE, cx - d*.02, cy - d*.06, d*.34, d*.12, fill=ZB)


# ======================= Folie 1: Marktzuwachs (Chart + Kennzahlen) =====================================
new_slide("69 % des Marktzuwachses liegen in drei Segmenten, dort haben wir nur 2,1 % Anteil",
          "Der Markt wächst dort am stärksten, wo wir mit 2,1 % Anteil klein sind (Beispieldaten, fiktiv). Das ist der Hebel.")
shape(S.ROUNDED_RECTANGLE, 11.4, 0.93, 1.5, 0.3, fill="E9EBF0", rad=0.15)
shape(S.OVAL, 11.45, 0.96, 0.24, 0.24, fill=DB)
text(11.45, 0.96, 0.24, 0.24, "1", 10, M, WHITE, "c", "m")
text(11.78, 0.93, 1.1, 0.3, "Der Markt", 11, L, DB, "l", "m")
shape(S.ROUNDED_RECTANGLE, 0.4, 1.62, 8.0, 4.4, fill=WHITE, line=LB)
text(0.65, 1.79, 4.6, 0.3, "MARKTZUWACHS 2026 BIS 2029 JE SEGMENT, MRD. €", 12, M, ZB)
# Legende: Bedeutung der Farbe steht auch als Text da (nicht nur Farbe)
shape(S.RECTANGLE, 5.3, 1.85, 0.14, 0.14, fill=ZB); text(5.51, 1.79, 1.4, 0.26, "Fokus-Segmente", 11, L, DB, "l", "m")
shape(S.RECTANGLE, 7.2, 1.85, 0.14, 0.14, fill=FOCUS_LIGHT); text(7.41, 1.79, 0.85, 0.26, "übrige", 11, L, DB, "l", "m")
cats = ["Cyber", "Gesundheit", "Logistik", "Handwerk", "Handel", "Industrie", "Gastro", "Freie Berufe"]
vals = [2.2, 2.4, 1.6, 0.9, 0.9, 0.6, 0.2, 0.2]
cd = CategoryChartData(number_format="0.0"); cd.categories = cats; cd.add_series("Marktzuwachs 2026 bis 2029, Mrd. €", vals)
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.5), Inches(2.15), Inches(7.8), Inches(3.75), cd)
gf.name = "Säulendiagramm Marktzuwachs"
gf._element.nvGraphicFramePr.cNvPr.set("descr", "Säulendiagramm: Marktzuwachs 2026 bis 2029 je Segment in Mrd. Euro. Cyber 2,2; Gesundheit 2,4; Logistik 1,6 (Fokus-Segmente); Handwerk 0,9; Handel 0,9; Industrie 0,6; Gastro 0,2; Freie Berufe 0,2.")
ch = gf.chart; ch.has_legend = False; ch.has_title = False
ch.font.size = Pt(12); ch.font.name = L; ch.font.color.rgb = rgb(DB)
pl = ch.plots[0]; pl.gap_width = 45; pl.vary_by_categories = False
for i in range(len(vals)):
    pt = pl.series[0].points[i]; pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(ZB if i < 3 else FOCUS_LIGHT)
pl.has_data_labels = True
dl = pl.data_labels; dl.number_format = '0.0'; dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END; dl.font.size = Pt(12); dl.font.name = L; dl.font.color.rgb = rgb(DB)
va = ch.value_axis; va.minimum_scale, va.maximum_scale, va.major_unit = 0, 3, 1   # Nullbasis
va.tick_labels.number_format = '0'; va.tick_labels.number_format_is_linked = False
va.has_major_gridlines = True
va.major_gridlines.format.line.color.rgb = rgb("E3EAF2"); va.major_gridlines.format.line.width = Pt(0.75)
va.format.line.fill.background(); va.tick_labels.font.size = Pt(12)
ca = ch.category_axis; ca.format.line.color.rgb = rgb(LB); ca.tick_labels.font.size = Pt(12)
ca.major_tick_mark = va.major_tick_mark = XL_TICK_MARK.NONE
# Kennzahl-Karten: Dunkle Karte = die eine Hauptaussage
shape(S.ROUNDED_RECTANGLE, 8.65, 1.62, 4.28, 2.07, fill=DB)
g_gear1(9.17, 2.15, 0.62)
text(9.55, 1.82, 3.2, 0.75, "69 %", 46, O, WHITE, "l", "m")
text(8.95, 2.72, 3.75, 0.8, "des Marktzuwachses von 9,0 Mrd. € liegen in Cyber, Gesundheit und Logistik", 14, L, WHITE)
shape(S.ROUNDED_RECTANGLE, 8.65, 3.93, 4.28, 2.07, fill=LB, alpha=30)
g_c(9.17, 4.46, 0.62)
text(9.55, 4.13, 3.2, 0.75, "2,1 %", 46, O, ZB, "l", "m")
text(8.95, 5.06, 3.75, 0.8, "ist unser Marktanteil dort. In den übrigen fünf Segmenten liegt er bei 3,5 %.", 14, L, DB)
shape(S.ROUNDED_RECTANGLE, 0.4, 6.14, 12.53, 0.66, fill=DB)
text(0.65, 6.14, 1.7, 0.66, "EINORDNUNG", 12, M, WHITE, "l", "m")
text(2.45, 6.14, 10.2, 0.66, "Wir sind dort klein, wo der Markt am stärksten wächst. Das ist der Hebel.", 16, L, WHITE, "l", "m")
footer("Beispieldaten, fiktiv. Marktzuwachs je Segment 2026 bis 2029; blau = Fokus-Segmente.")

# ======================= Folie 2: drei Argumente mit Piktogrammen =======================================
new_slide("Das Interesse wächst klar um 11,5 % pro Jahr; vor einer Skalierung prüfen wir die Datenbasis.",
          "Befund: Wachstum klar belegt. Vorbehalte: Nachlassen möglich, aber nicht belegt; Datenbasis vor Steuerung klären (fiktive Daten).")
rows = [
    (g_trend, "BEFUND", "Das Wachstum ist klar",
     "Der Anteil stieg von 28,0 % auf 34,5 %; alle 23 Monatsschritte zeigen nach oben,\ndrei Rechenwege liefern 11,5 bis 12,3 %.",
     "+11,5 %", "pro Jahr, Spanne 5,5 bis 17,8 %"),
    (g_hourglass, "VORBEHALT", "Ein Nachlassen ist möglich, aber nicht belegt",
     "Zuletzt 0,17 statt 0,30 Pp pro Monat; so niedrig war das Tempo\nschon im Aug 2025, danach stieg es auf 0,41.",
     "2 von 21", "Dreimonatsfenster so langsam"),
    (g_scales, "VORBEHALT", "Erst die Datenbasis, dann die Steuerung",
     "Die Kurve ist 8-mal glatter, als Zufall erlaubt; Jahreswerte sind\nauf ±0,9 Pp genau, Monatswerte nur auf ±3,2 Pp.",
     "×8", "zu glatt für echte Stichproben"),
]
RH, GAP, Y0 = 1.3, 0.17, 1.62
for i, (g, tag, ttl, desc, num, cap) in enumerate(rows):
    y = Y0 + i * (RH + GAP)
    shape(S.ROUNDED_RECTANGLE, 0.4, y, 12.53, RH, fill=WHITE, line=LB)
    shape(S.OVAL, 0.6, y + 0.14, 0.32, 0.32, fill=DB)
    text(0.6, y + 0.14, 0.32, 0.32, str(i + 1), 12, M, WHITE, "c", "m")
    g(1.25, y + RH / 2 + 0.03, 0.95)
    text(2.05, y + 0.16, 3, 0.22, tag, 10, M, ZB, spacing=100)
    text(2.05, y + 0.38, 7.3, 0.36, ttl, 18, M, DB)
    text(2.05, y + 0.78, 7.4, 0.5, desc, 13, L, DB)
    shape(S.RECTANGLE, 9.65, y + 0.2, 0.02, RH - 0.4, fill=DB)
    text(9.9, y + 0.17, 2.9, 0.6, num, 36, O, ZB, "l", "m")
    text(9.9, y + 0.82, 2.9, 0.3, cap, 12, M, DB)
shape(S.ROUNDED_RECTANGLE, 0.4, 6.14, 12.53, 0.66, fill=DB)
text(0.65, 6.14, 1.9, 0.66, "WIR EMPFEHLEN", 12, M, WHITE, "l", "m")
x = 2.55
for j, step in enumerate(["Erhebung prüfen", "Auf Jahreswerte steuern", "Ursachen klären"]):
    w = 2.45 if j != 1 else 3.0
    pill(x, 6.24, w, step, WHITE, DB, h=0.46, size=14)
    x += w
    if j < 2:
        shape(S.RIGHT_ARROW, x + 0.12, 6.3, 0.5, 0.34, fill=WHITE); x += 0.74
footer("Fiktive Daten. Pp = Prozentpunkte; Spanne = 95-Prozent-Bereich (Normalnäherung);\nDreimonatsfenster = gleitender Schnitt der Monatsschritte.")

# ======================= Folie 3: Datenfundament ========================================================
new_slide("Das Datenfundament baut die IT für das ganze Unternehmen, das liegt nicht in unserer Hand",
          "Die IT baut das Datenfundament für das ganze Unternehmen; wir starten klein mit geprüften Datasets.")
shape(S.ROUNDED_RECTANGLE, 0.4, 1.62, 12.53, 1.4, fill=LB, alpha=30)
g_flask(1.25, 2.32, 0.95)
text(2.05, 1.95, 7.5, 0.4, "Unsere Prototypen", 20, M, DB)
text(2.05, 2.45, 8.5, 0.35, "Zwei Wege auf kleinen, vorab geprüften Datasets: Fabric und Databricks", 14, L, DB)
pill(11.25, 1.85, 1.45, "in unserer Hand", DB, WHITE)
shape(S.ISOSCELES_TRIANGLE, 6.4, 3.1, 0.55, 0.32, fill=ZB)
text(7.1, 3.12, 5.0, 0.3, "braucht als Grundlage gutes Data Management", 12, L, DB, "l", "m")
shape(S.ROUNDED_RECTANGLE, 0.4, 3.5, 12.53, 2.5, fill=DB)
text(0.68, 3.64, 6, 0.45, "Datenfundament der IT", 22, M, WHITE, "l", "m")
pill(9.2, 3.72, 1.35, "Projekt läuft", LB, DB)
pill(10.7, 3.72, 2.05, "nicht in unserer Hand", WHITE, DB)
text(0.68, 4.17, 11.8, 0.3, "„KI ist ein Strukturverstärker: Gutes Data Management ist die Voraussetzung für erfolgreiche KI.“ (Deck der IT)", 13, L, WHITE)
tiles = [(g_search, "Datenkataloge", "für Auffindbarkeit"), (g_network, "APIs und MCP-Tools", "für Zugänglichkeit"),
         (g_info, "Metadaten", "für Verständlichkeit"), (g_check, "Datenqualität", "für Vertrauenswürdigkeit"),
         (g_people, "Klare Zuständigkeiten", "für Verbesserung")]
TG = 0.2; TW_ = (12.53 - 0.44 - 4 * TG) / 5          # Innenrand 0,22 in, Kachelabstand ~0,5 cm
for i, (g, t1, t2) in enumerate(tiles):
    x = 0.62 + i * (TW_ + TG)
    shape(S.ROUNDED_RECTANGLE, x, 4.65, TW_, 1.15, fill=WHITE, rad=0.1)
    g(x + 0.47, 4.97, 0.46)
    text(x + 0.15, 5.27, TW_ - 0.2, 0.28, t1, 13 if len(t1) > 18 else 14, M, DB)
    text(x + 0.15, 5.54, TW_ - 0.2, 0.25, t2, 12, L, DB)
shape(S.ROUNDED_RECTANGLE, 0.4, 6.12, 12.53, 0.62, fill=DB)
text(0.65, 6.12, 1.7, 0.62, "KONSEQUENZ", 12, M, WHITE, "l", "m")
text(2.45, 6.12, 10.3, 0.62, "Wir warten nicht auf das Fundament, sondern starten klein, mit Datasets, die CAN vorab prüft.", 15, L, WHITE, "l", "m")
footer("Quelle: Inhalt aus dem Deck der IT, Einordnung durch das Team")

# ======================= Folie 4: Werkzeuge / Fundament =================================================
new_slide("Werkzeuge ändern sich. Problemlösung bleibt.",
          "Jede Welle bringt neue Werkzeuge; darunter bleibt die Ebene, die uns ausmacht.")
text(0.4, 1.5, 4, 0.28, "Werkzeuge  ·  ändern sich", 12, M, ZB)
cw = [2.75, 2.7, 2.6, 2.5]; ag = (12.53 - sum(cw)) / 3
styles = [("DDE4E3", DB, g_code, "Programmierung", "Code schreiben"),
          ("DCEAF6", DB, g_lowcode, "Low Code", "Bausteine ziehen"),
          (ZB, WHITE, g_gears, "Automatisierung", "Abläufe verketten"),
          (DB, WHITE, g_head, "KI", "Absicht beschreiben")]
x = 0.4; centers = []
for (fill, c, g, t1, t2), w in zip(styles, cw):
    shape(S.ROUNDED_RECTANGLE, x, 1.85, w, 1.85, fill=fill, rad=0.1)
    g(x + 0.55, 2.42, 0.62)
    text(x + 0.2, 2.95, w - 0.3, 0.35, t1, 18, M, c)
    text(x + 0.2, 3.3, w - 0.3, 0.28, t2, 12, L, c)
    centers.append(x + w / 2)
    if t1 == "KI": pill(x + w - 0.95, 1.97, 0.78, "Heute", WHITE, DB, h=0.26, size=11)
    x += w
    if t1 != "KI":
        shape(S.RIGHT_ARROW, x + 0.1, 2.62, ag - 0.2, 0.3, fill=MB); x += ag
for cxm in centers:
    shape(S.ISOSCELES_TRIANGLE, cxm - 0.17, 3.78, 0.34, 0.26, fill=MB)
shape(S.ROUNDED_RECTANGLE, 0.4, 4.1, 12.53, 2.6, fill=DB, rad=0.12)
text(0.65, 4.25, 3.5, 0.3, "Fundament  ·  bleibt", 13, M, WHITE)
text(8.9, 4.25, 3.8, 0.3, "trägt jedes Werkzeug", 12, L, WHITE, "r")
fund = [(g_target, "Problemverständnis", "Erkennen, was wirklich\nzu lösen ist"),
        (g_star, "Fachwissen", "Wissen, was richtig\nund relevant ist"),
        (g_bulb, "Kreativität", "Neue Wege und\ngute Fragen finden"),
        (g_scales, "Urteilskraft", "Entscheiden, ob das\nErgebnis taugt")]
fg_ = 0.2; fw = (12.53 - 0.44 - 3 * fg_) / 4
for i, (g, t1, t2) in enumerate(fund):
    xx = 0.62 + i * (fw + fg_)
    shape(S.ROUNDED_RECTANGLE, xx, 4.78, fw, 1.7, fill=ZB, rad=0.1)
    g(xx + 0.5, 5.25, 0.6)
    text(xx + 0.2, 5.7, fw - 0.35, 0.3, t1, 16, M, WHITE)
    text(xx + 0.2, 6.0, fw - 0.35, 0.45, t2, 12, L, WHITE)
footer()
prs.save(sys.argv[1])
