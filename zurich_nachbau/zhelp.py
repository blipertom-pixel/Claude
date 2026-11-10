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
DARK = False


def new_slide(title, notes, title_w=10.3, dark=False):
    """Titel zuerst (Lesereihenfolge), dann Logo; feste Ränder 0,4 in (~1 cm). dark = Dark-Blue-Ground (Entscheidungsfolie)."""
    global s, PAGE, DARK
    PAGE += 1; DARK = dark
    s = prs.slides.add_slide(prs.slide_layouts[6])
    if dark:
        s.background.fill.solid(); s.background.fill.fore_color.rgb = rgb(DB)
    text(0.44, 0.34, title_w, 0.9, title, 26, L, WHITE if dark else ZB).name = "Titel"
    shape(S.OVAL, 11.45, 0.42, 0.4, 0.4, fill=WHITE if dark else ZB, name="Logo (Nachbildung)", alt="Zurich Logo")
    text(11.45, 0.42, 0.4, 0.4, "Z", 16, M, ZB if dark else WHITE, "c", "m")
    text(11.95, 0.42, 1.1, 0.4, "ZURICH", 15, M, WHITE if dark else ZB, "l", "m", spacing=100)
    s.notes_slide.notes_text_frame.text = notes


def footer(src=None):
    c = WHITE if DARK else DB
    if src: text(0.4, 6.93, 11.0, 0.45, src, 12, L, c).name = "Quelle"
    text(11.9, 6.95, 0.3, 0.25, str(PAGE), 10, L, c, "r")
    text(12.3, 6.95, 0.65, 0.25, "© Zurich", 10, L, c)


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


