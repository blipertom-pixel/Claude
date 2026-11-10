# -*- coding: utf-8 -*-
"""Nachbau Folie 2: drei Argumentzeilen mit Piktogrammen, ohne Diagramm.
Schriftnamen bleiben "Zurich Sans Light/Medium" und "Ogg" -> auf einem Rechner mit den Originalschriften
erscheint sofort die echte Typo; ohne sie greifen Ersatzschriften (Inter / Cormorant Garamond)."""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE as S
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_TICK_LABEL_POSITION
from pptx.oxml.ns import qn
from lxml import etree

DB, ZB, MB, LB, WHITE = "23366F", "2167AE", "5495CF", "91BFE3", "FFFFFF"
L, M, O = "Zurich Sans Light", "Zurich Sans Medium", "Ogg"
rgb = RGBColor.from_string

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
s = prs.slides.add_slide(prs.slide_layouts[6])


def shape(kind, x, y, w, h, fill=None, line=None, lw=1.0, rad=None, alpha=None):
    sp = s.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    sp.shadow.inherit = False
    st = sp._element.find(qn('p:style'))
    if st is not None: sp._element.remove(st)
    if kind == S.ROUNDED_RECTANGLE:
        sp.adjustments[0] = (rad or 0.12) / min(w, h)
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
    return sp


def text(x, y, w, h, t, size=14, font=L, color=DB, align="l", anchor="t", spacing=None):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE}[anchor]
    p = tf.paragraphs[0]
    p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[align]
    r = p.add_run(); r.text = t
    r.font.size = Pt(size); r.font.name = font; r.font.color.rgb = rgb(color)
    if spacing:
        r._r.get_or_add_rPr().set("spc", str(spacing))
    return tb


def logo_and_tracker(num, label):
    shape(S.OVAL, 11.45, 0.42, 0.4, 0.4, fill=ZB)
    text(11.45, 0.42, 0.4, 0.4, "Z", 16, M, WHITE, "c", "m")
    text(11.95, 0.42, 1.1, 0.4, "ZURICH", 15, M, ZB, "l", "m", spacing=100)

PIC_BG, PIC_FG = "A9CBEA", ZB

def icon_trend(cx, cy, d):
    shape(S.OVAL, cx - d/2, cy - d/2, d, d, fill=PIC_BG)
    pts = [(-.30, .16), (-.14, -.04), (0, .08), (.14, -.12), (.30, .06)]
    fb = s.shapes.build_freeform(Inches(cx + pts[0][0]*d), Inches(cy + pts[0][1]*d))
    fb.add_line_segments([(Inches(cx + a*d), Inches(cy + b*d)) for a, b in pts[1:]], close=False)
    f = fb.convert_to_shape(); f.fill.background(); f.line.color.rgb = rgb(DB); f.line.width = Pt(2.5)
    f._element.remove(f._element.find(qn('p:style')))
    f.line.color.rgb = rgb(DB); f.line.width = Pt(2.5)

def icon_hourglass(cx, cy, d):
    shape(S.OVAL, cx - d/2, cy - d/2, d, d, fill=PIC_BG)
    shape(S.FLOWCHART_COLLATE, cx - d*.2, cy - d*.3, d*.4, d*.6, fill=PIC_FG)
    shape(S.RECTANGLE, cx - d*.26, cy - d*.33, d*.52, d*.05, fill=DB)
    shape(S.RECTANGLE, cx - d*.26, cy + d*.28, d*.52, d*.05, fill=DB)

def icon_scales(cx, cy, d):
    shape(S.OVAL, cx - d/2, cy - d/2, d, d, fill=PIC_BG)
    shape(S.RECTANGLE, cx - d*.015, cy - d*.3, d*.03, d*.55, fill=DB)
    shape(S.RECTANGLE, cx - d*.3, cy - d*.2, d*.6, d*.03, fill=DB)
    shape(S.RECTANGLE, cx - d*.12, cy + d*.25, d*.24, d*.04, fill=DB)
    for dx in (-.22, .22):
        p = shape(S.FLOWCHART_DELAY, cx + dx*d - d*.09, cy - d*.04, d*.18, d*.22, fill=PIC_FG)
        p.rotation = 90
        # rotierte 0.22x0.18-Box -> optisch 0.18 breit x 0.22 hoch: Mittelpunkt bleibt gleich

# --- Kopf ------------------------------------------------------------------------------------------------
text(0.44, 0.34, 10.3, 0.9, "Das Interesse wächst klar um 11,5 % pro Jahr; vor einer Skalierung prüfen wir die Datenbasis.", 26, L, ZB)
logo_and_tracker(1, "")

# --- Drei Argumentzeilen -------------------------------------------------------------------------------
rows = [
    (icon_trend, "Das Wachstum ist klar",
     "Der Anteil stieg von 28,0 % auf 34,5 %; alle 23 Monatsschritte zeigen nach oben, drei Rechenwege liefern 11,5 bis 12,3 %.",
     "+11,5 %", "pro Jahr, Spanne 5,5 bis 17,8 %"),
    (icon_hourglass, "Ein Nachlassen ist möglich, aber nicht belegt",
     "Zuletzt 0,17 statt 0,30 Pp pro Monat; so niedrig war das Tempo schon im Aug 2025, danach stieg es auf 0,41.",
     "2 von 21", "Dreimonatsfenster so langsam"),
    (icon_scales, "Erst die Datenbasis, dann die Steuerung",
     "Die Kurve ist 8-mal glatter, als Zufall erlaubt; Jahreswerte sind auf ±0,9 Pp genau, Monatswerte nur auf ±3,2 Pp.",
     "×8", "zu glatt für echte Stichproben"),
]
RH, GAP, Y0 = 1.36, 0.10, 1.62
for i, (icon, ttl, desc, num, cap) in enumerate(rows):
    y = Y0 + i * (RH + GAP)
    shape(S.ROUNDED_RECTANGLE, 0.4, y, 12.53, RH, fill=WHITE, line=LB, lw=1.0)
    icon(1.2, y + RH/2, 1.0)
    shape(S.OVAL, 0.62, y + 0.12, 0.34, 0.34, fill=DB)
    text(0.62, y + 0.12, 0.34, 0.34, str(i + 1), 12, M, WHITE, "c", "m")
    text(2.05, y + 0.22, 7.3, 0.4, ttl, 18, M, DB)
    text(2.05, y + 0.68, 7.3, 0.6, desc, 13, L, DB)
    shape(S.RECTANGLE, 9.65, y + 0.2, 0.02, RH - 0.4, fill=DB)
    text(9.9, y + 0.2, 2.9, 0.6, num, 36, O, ZB, "l", "m")
    text(9.9, y + 0.85, 2.9, 0.4, cap, 12, M, DB)

# --- Empfehlungsband mit Pfeil-Kette ---------------------------------------------------------------------
shape(S.ROUNDED_RECTANGLE, 0.4, 6.14, 12.53, 0.66, fill=DB)
text(0.65, 6.14, 1.9, 0.66, "WIR EMPFEHLEN", 12, M, WHITE, "l", "m")
x = 2.55
for j, step in enumerate(["Erhebung prüfen", "Auf Jahreswerte steuern", "Ursachen klären"]):
    w = 2.45 if j != 1 else 3.0
    shape(S.ROUNDED_RECTANGLE, x, 6.24, w, 0.46, fill=WHITE, rad=0.23)
    text(x, 6.24, w, 0.46, step, 14, M, DB, "c", "m")
    x += w
    if j < 2:
        shape(S.RIGHT_ARROW, x + 0.12, 6.3, 0.5, 0.34, fill=WHITE)
        x += 0.74
text(0.4, 6.93, 11.45, 0.3, "Fiktive Daten. Pp = Prozentpunkte; Spanne = 95-Prozent-Bereich (Normalnäherung); Dreimonatsfenster = gleitender Schnitt der Monatsschritte.", 11, L, DB)
text(11.9, 6.95, 0.3, 0.25, "4", 9, L, DB, "r")
text(12.3, 6.95, 0.65, 0.25, "© Zurich", 9, L, DB)
s.notes_slide.notes_text_frame.text = "Wachstum klar belegt; Nachlassen möglich, aber nicht belegt; erst Datenbasis klären, dann steuern (fiktive Daten)."
prs.save(sys.argv[1])
