# -*- coding: utf-8 -*-
"""Nachbau Folien 3+4: Datenfundament (Karten + Kacheln) und Werkzeuge/Fundament, ohne Diagramm.
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
def new_slide():
    global s
    s = prs.slides.add_slide(prs.slide_layouts[6]); return s
s = new_slide()


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


BG, TRI = "BFD6EE", MB

def disc(cx, cy, d, bg=BG):
    shape(S.OVAL, cx - d/2, cy - d/2, d, d, fill=bg)

def poly(pts, cx, cy, d, fg, w=2.2, close=False):
    fb = s.shapes.build_freeform(Inches(cx + pts[0][0]*d), Inches(cy + pts[0][1]*d))
    fb.add_line_segments([(Inches(cx + a*d), Inches(cy + b*d)) for a, b in pts[1:]], close=close)
    f = fb.convert_to_shape(); f.fill.background()
    st = f._element.find(qn('p:style'))
    if st is not None: f._element.remove(st)
    f.line.color.rgb = rgb(fg); f.line.width = Pt(w); return f

def g_flask(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    t = shape(S.ISOSCELES_TRIANGLE, cx - d*.2, cy - d*.05, d*.4, d*.38, fill=fg)
    shape(S.RECTANGLE, cx - d*.07, cy - d*.3, d*.14, d*.28, fill=fg)
    shape(S.RECTANGLE, cx - d*.12, cy - d*.32, d*.24, d*.04, fill=DB)

def g_search(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    shape(S.DONUT, cx - d*.28, cy - d*.3, d*.46, d*.46, fill=fg).adjustments[0] = 0.18
    poly([(.15, .13), (.3, .3)], cx, cy, d, fg, 3.5)

def g_network(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    P = [(-.18, .12), (.2, .16), (0, -.2)]
    for a, b in P: poly([(0, 0), (a, b)], cx, cy, d, DB, 1.2)
    shape(S.OVAL, cx - d*.07, cy - d*.07, d*.14, d*.14, fill=DB)
    for a, b in P: shape(S.OVAL, cx + a*d - d*.07, cy + b*d - d*.07, d*.14, d*.14, fill=fg)

def g_info(cx, cy, d, bg="BFD6EE", fg=ZB):
    shape(S.OVAL, cx - d/2, cy - d/2, d, d, fill=fg)
    shape(S.OVAL, cx - d*.05, cy - d*.3, d*.1, d*.1, fill=WHITE)
    shape(S.RECTANGLE, cx - d*.04, cy - d*.14, d*.08, d*.4, fill=WHITE)

def g_check(cx, cy, d, bg="BFD6EE", fg=ZB):
    shape(S.OVAL, cx - d/2, cy - d/2, d, d, fill=bg if bg != "BFD6EE" else "A9CBEA")
    poly([(-.22, .02), (-.06, .18), (.24, -.16)], cx, cy, d, fg, 3.5)

def g_people(cx, cy, d, bg=BG, fg=DB):
    disc(cx, cy, d, bg)
    for dx, dy, r in [(-.2, 0, .13), (.2, 0, .13), (0, -.1, .16)]:
        shape(S.OVAL, cx + dx*d - r*d, cy + dy*d - r*d - .05*d, 2*r*d, 2*r*d, fill=fg)
        shape(S.ROUNDED_RECTANGLE, cx + dx*d - r*1.6*d, cy + dy*d + r*.7*d, r*3.2*d, r*1.5*d, fill=ZB, rad=0.06)

def g_code(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    shape(S.ROUNDED_RECTANGLE, cx - d*.3, cy - d*.25, d*.6, d*.5, fill=WHITE, rad=0.05)
    text(cx - d*.3, cy - d*.25, d*.6, d*.5, "</>", 12, M, fg, "c", "m")

def g_lowcode(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    for i, w in enumerate((.5, .36, .44)):
        shape(S.ROUNDED_RECTANGLE, cx - d*.25, cy - d*.24 + i*d*.17, d*w, d*.11, fill=fg, rad=0.03)
    shape(S.OVAL, cx + d*.1, cy + d*.02, d*.2, d*.24, fill=DB)

def g_gears(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    shape(S.GEAR_6, cx - d*.3, cy - d*.3, d*.38, d*.38, fill=fg)
    shape(S.GEAR_6, cx - d*.02, cy - d*.02, d*.32, d*.32, fill=DB)

def g_head(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    shape(S.OVAL, cx - d*.2, cy - d*.3, d*.4, d*.44, fill=fg)
    shape(S.ROUNDED_RECTANGLE, cx - d*.3, cy + d*.12, d*.6, d*.22, fill=DB, rad=0.08)

def g_puzzle(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    shape(S.PLAQUE, cx - d*.32, cy - d*.22, d*.34, d*.34, fill=fg)
    shape(S.OVAL, cx + d*.02, cy - d*.2, d*.24, d*.24, fill=DB)
    shape(S.ROUNDED_RECTANGLE, cx - d*.02, cy + d*.08, d*.34, d*.2, fill=DB, rad=0.08)

def g_star(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    shape(S.OVAL, cx - d*.16, cy - d*.14, d*.32, d*.32, fill=DB)
    shape(S.ROUNDED_RECTANGLE, cx - d*.26, cy + d*.2, d*.52, d*.16, fill=DB, rad=0.08)
    for dx in (-.2, 0, .2):
        shape(S.STAR_5_POINT, cx + dx*d - d*.05, cy - d*.34 + (0 if dx else -.04*d), d*.1, d*.1, fill=WHITE)

def g_bulb(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    shape(S.OVAL, cx - d*.2, cy - d*.3, d*.4, d*.42, fill=fg)
    shape(S.RECTANGLE, cx - d*.09, cy + d*.1, d*.18, d*.14, fill=DB)

def g_scales(cx, cy, d, bg=BG, fg=ZB):
    disc(cx, cy, d, bg)
    shape(S.RECTANGLE, cx - d*.015, cy - d*.3, d*.03, d*.55, fill=DB)
    shape(S.RECTANGLE, cx - d*.3, cy - d*.2, d*.6, d*.03, fill=DB)
    shape(S.RECTANGLE, cx - d*.12, cy + d*.25, d*.24, d*.04, fill=DB)
    for dx in (-.22, .22):
        shape(S.FLOWCHART_DELAY, cx + dx*d - d*.09, cy - d*.04, d*.18, d*.22, fill=fg).rotation = 90

def logo():
    shape(S.OVAL, 11.45, 0.42, 0.4, 0.4, fill=ZB)
    text(11.45, 0.42, 0.4, 0.4, "Z", 16, M, WHITE, "c", "m")
    text(11.95, 0.42, 1.1, 0.4, "ZURICH", 15, M, ZB, "l", "m", spacing=100)

def pill(x, y, w, t, fill, color, h=0.32, size=12):
    shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=fill, rad=h/2)
    text(x, y, w, h, t, size, M, color, "c", "m")

def footer(n, src=None):
    if src: text(0.4, 6.93, 9.5, 0.3, src, 11, L, DB)
    text(11.9, 6.95, 0.3, 0.25, str(n), 9, L, DB, "r")
    text(12.3, 6.95, 0.65, 0.25, "© Zurich", 9, L, DB)

# ============================== Folie A: Datenfundament ================================================
text(0.44, 0.34, 10.3, 0.9, "Das Datenfundament baut die IT für das ganze Unternehmen, das liegt nicht in unserer Hand", 26, L, ZB)
logo()
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
text(0.68, 4.17, 11.5, 0.3, "„KI ist ein Strukturverstärker: Gutes Data Management ist die Voraussetzung für erfolgreiche KI.“ (Deck der IT)", 13, L, WHITE)
tiles = [(g_search, "Datenkataloge", "für Auffindbarkeit"), (g_network, "APIs und MCP-Tools", "für Zugänglichkeit"),
         (g_info, "Metadaten", "für Verständlichkeit"), (g_check, "Datenqualität", "für Vertrauenswürdigkeit"),
         (g_people, "Klare Zuständigkeiten", "für Verbesserung")]
TW_, TG = 2.3, 0.145
for i, (g, t1, t2) in enumerate(tiles):
    x = 0.6 + i * (TW_ + TG)
    shape(S.ROUNDED_RECTANGLE, x, 4.65, TW_, 1.15, fill=WHITE, rad=0.1)
    g(x + 0.5, 4.97, 0.46)
    text(x + 0.18, 5.27, TW_ - 0.3, 0.28, t1, 13 if len(t1) > 18 else 14, M, DB)
    text(x + 0.18, 5.54, TW_ - 0.3, 0.25, t2, 11, L, DB)
shape(S.ROUNDED_RECTANGLE, 0.4, 6.12, 12.53, 0.62, fill=DB)
text(0.65, 6.12, 1.7, 0.62, "KONSEQUENZ", 12, M, WHITE, "l", "m")
text(2.45, 6.12, 10.3, 0.62, "Wir warten nicht auf das Fundament, sondern starten klein, mit Datasets, die CAN vorab prüft.", 15, L, WHITE, "l", "m")
footer(5, "Quelle: Inhalt aus dem Deck der IT, Einordnung durch das Team")
s.notes_slide.notes_text_frame.text = "Die IT baut das Datenfundament für das ganze Unternehmen; wir starten klein mit geprüften Datasets."

# ============================== Folie B: Werkzeuge / Fundament =========================================
new_slide()
text(0.44, 0.34, 10.3, 0.5, "Werkzeuge ändern sich. Problemlösung bleibt.", 26, L, ZB)
logo()
text(0.4, 1.5, 4, 0.28, "Werkzeuge  ·  ändern sich", 12, M, ZB)
cw = [2.75, 2.7, 2.6, 2.5]; ag = (12.53 - sum(cw)) / 3
styles = [("DDE4E3", DB, DB, g_code, "Programmierung", "Code schreiben"),
          ("DCEAF6", DB, DB, g_lowcode, "Low Code", "Bausteine ziehen"),
          (ZB, WHITE, WHITE, g_gears, "Automatisierung", "Abläufe verketten"),
          (DB, WHITE, WHITE, g_head, "KI", "Absicht beschreiben")]
x = 0.4; centers = []
for (fill, c1, c2, g, t1, t2), w in zip(styles, cw):
    shape(S.ROUNDED_RECTANGLE, x, 1.85, w, 1.85, fill=fill, rad=0.1)
    g(x + 0.55, 2.42, 0.62, "BFD6EE", ZB if fill in ("DDE4E3", "DCEAF6", ZB) else ZB)
    text(x + 0.2, 2.95, w - 0.3, 0.35, t1, 18, M, c1)
    text(x + 0.2, 3.3, w - 0.3, 0.28, t2, 12, L, c2)
    centers.append(x + w / 2)
    if t1 == "KI": pill(x + w - 0.95, 1.97, 0.78, "Heute", WHITE, DB, h=0.26, size=11)
    x += w
    if t1 != "KI":
        shape(S.RIGHT_ARROW, x + 0.1, 2.62, ag - 0.2, 0.3, fill=MB)
        x += ag
for cxm in centers:
    shape(S.ISOSCELES_TRIANGLE, cxm - 0.17, 3.78, 0.34, 0.26, fill=MB)
shape(S.ROUNDED_RECTANGLE, 0.4, 4.1, 12.53, 2.6, fill=DB, rad=0.12)
text(0.65, 4.25, 3.5, 0.3, "Fundament  ·  bleibt", 13, M, WHITE)
text(8.9, 4.25, 3.8, 0.3, "trägt jedes Werkzeug", 12, L, WHITE, "r")
fund = [(g_puzzle, "Problemverständnis", "Erkennen, was wirklich zu lösen ist"),
        (g_star, "Fachwissen", "Wissen, was richtig und relevant ist"),
        (g_bulb, "Kreativität", "Neue Wege und gute Fragen finden"),
        (g_scales, "Urteilskraft", "Entscheiden, ob das Ergebnis taugt")]
fw, fg_ = 2.92, 0.15
for i, (g, t1, t2) in enumerate(fund):
    xx = 0.6 + i * (fw + fg_)
    shape(S.ROUNDED_RECTANGLE, xx, 4.78, fw, 1.7, fill=ZB, rad=0.1)
    g(xx + 0.5, 5.25, 0.6, "BFD6EE", ZB)
    text(xx + 0.2, 5.7, fw - 0.35, 0.3, t1, 16, M, WHITE)
    text(xx + 0.2, 6.0, fw - 0.35, 0.45, t2, 12, L, WHITE)
footer(6)
s.notes_slide.notes_text_frame.text = "Jede Welle bringt neue Werkzeuge; darunter bleibt die Ebene, die uns ausmacht."
prs.save(sys.argv[1])
