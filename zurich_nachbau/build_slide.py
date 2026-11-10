# -*- coding: utf-8 -*-
"""1:1-Nachbau der Beispielfolie "69 % des Marktzuwachses ..." ohne Master-Layout.
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


# --- Titel (echter Titel-Platzhalter wäre im Master; hier als Textbox) ---------------------------------
text(0.44, 0.34, 10.3, 0.9, "69 % des Marktzuwachses liegen in drei Segmenten, dort haben wir nur 2,1 % Anteil",
     26, L, ZB)

# --- Logo (Nachbildung: Kreis mit Z + Wortmarke) und Kapitel-Pille ------------------------------------
shape(S.OVAL, 11.45, 0.42, 0.4, 0.4, fill=ZB)
text(11.45, 0.42, 0.4, 0.4, "Z", 16, M, WHITE, "c", "m")
text(11.95, 0.42, 1.1, 0.4, "ZURICH", 15, M, ZB, "l", "m", spacing=100)
shape(S.ROUNDED_RECTANGLE, 11.4, 0.93, 1.5, 0.3, fill="E9EBF0", rad=0.15)
shape(S.OVAL, 11.45, 0.96, 0.24, 0.24, fill=DB)
text(11.45, 0.96, 0.24, 0.24, "1", 10, M, WHITE, "c", "m")
text(11.78, 0.93, 1.1, 0.3, "Der Markt", 11, L, DB, "l", "m")

# --- Karten --------------------------------------------------------------------------------------------
shape(S.ROUNDED_RECTANGLE, 0.4, 1.62, 8.0, 4.4, fill=WHITE, line=LB, lw=1.0)
text(0.65, 1.79, 7.5, 0.3, "MARKTZUWACHS 2026 BIS 2029 JE SEGMENT, MRD. €", 12, M, ZB)

# --- Native Spalten-Grafik (editierbar) ---------------------------------------------------------------
cats = ["Cyber", "Gesundheit", "Logistik", "Handwerk", "Handel", "Industrie", "Gastro", "Freie Berufe"]
vals = [2.2, 2.4, 1.6, 0.9, 0.9, 0.6, 0.2, 0.2]
cd = CategoryChartData(number_format="0.0"); cd.categories = cats; cd.add_series("Marktzuwachs, Mrd. €", vals)
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.5), Inches(2.1), Inches(7.8), Inches(3.8), cd)
ch = gf.chart
ch.has_legend = False; ch.has_title = False
ch.font.size = Pt(12); ch.font.name = L; ch.font.color.rgb = rgb(DB)
pl = ch.plots[0]; pl.gap_width = 45; pl.vary_by_categories = False
ser = pl.series[0]
for i in range(len(vals)):
    pt = ser.points[i]; pt.format.fill.solid()
    pt.format.fill.fore_color.rgb = rgb(ZB if i < 3 else "7FB0E0")
pl.has_data_labels = True
dl = pl.data_labels; dl.number_format = '0.0'; dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END; dl.font.size = Pt(12); dl.font.name = L; dl.font.color.rgb = rgb(DB)
va = ch.value_axis
va.minimum_scale, va.maximum_scale, va.major_unit = 0, 3, 1
va.has_major_gridlines = True
va.major_gridlines.format.line.color.rgb = rgb("E3EAF2"); va.major_gridlines.format.line.width = Pt(0.75)
va.format.line.fill.background(); va.tick_labels.font.size = Pt(12)
va.tick_labels.number_format = '0'; va.tick_labels.number_format_is_linked = False
ca = ch.category_axis; ca.format.line.color.rgb = rgb(LB); ca.tick_labels.font.size = Pt(12)
ca.has_major_gridlines = False
from pptx.enum.chart import XL_TICK_MARK
ca.major_tick_mark = va.major_tick_mark = XL_TICK_MARK.NONE
text_frame_note = gf  # (chart is an editable native object)

# --- Stat-Karten ---------------------------------------------------------------------------------------
def gear_icon(cx, cy, d, bg, fg):
    shape(S.OVAL, cx - d / 2, cy - d / 2, d, d, fill=bg)
    g = shape(S.GEAR_6, cx - d * 0.3, cy - d * 0.3, d * 0.6, d * 0.6, fill=fg)
    shape(S.OVAL, cx - d * 0.09, cy - d * 0.09, d * 0.18, d * 0.18, fill=bg)

def c_icon(cx, cy, d, bg, fg):
    shape(S.OVAL, cx - d / 2, cy - d / 2, d, d, fill=bg)
    shape(S.DONUT, cx - d * 0.34, cy - d * 0.34, d * 0.68, d * 0.68, fill=fg).adjustments[0] = 0.28
    shape(S.RECTANGLE, cx + d * 0.12, cy - d * 0.1, d * 0.26, d * 0.2, fill=bg)
    shape(S.RECTANGLE, cx - d * 0.02, cy - d * 0.06, d * 0.4, d * 0.12, fill=fg)

shape(S.ROUNDED_RECTANGLE, 8.65, 1.62, 4.28, 2.03, fill=DB)
gear_icon(9.17, 2.15, 0.62, "BFD6EE", ZB)
text(9.55, 1.82, 3.2, 0.75, "69 %", 46, O, WHITE, "l", "m")
text(8.95, 2.72, 3.85, 0.8, "des Marktzuwachses von 9,0 Mrd. € liegen in Cyber, Gesundheit und Logistik", 14, L, WHITE)

shape(S.ROUNDED_RECTANGLE, 8.65, 3.85, 4.28, 2.15, fill=LB, alpha=30)
c_icon(9.17, 4.4, 0.62, "BFD6EE", ZB)
text(9.55, 4.07, 3.2, 0.75, "2,1 %", 46, O, ZB, "l", "m")
text(8.95, 5.0, 3.85, 0.8, "ist unser Marktanteil dort. In den übrigen fünf Segmenten liegt er bei 3,5 %.", 14, L, DB)

# --- Einordnungs-Band + Quelle + Fuß -------------------------------------------------------------------
shape(S.ROUNDED_RECTANGLE, 0.4, 6.14, 12.53, 0.66, fill=DB)
text(0.65, 6.14, 1.7, 0.66, "EINORDNUNG", 12, M, WHITE, "l", "m")
text(2.45, 6.14, 10.2, 0.66, "Wir sind dort klein, wo der Markt am stärksten wächst. Das ist der Hebel.", 16, L, WHITE, "l", "m")
text(0.4, 6.93, 10.5, 0.3, "Beispieldaten, fiktiv. Marktzuwachs je Segment 2026 bis 2029; blau = Fokus-Segmente.", 12, L, DB)
text(11.7, 6.95, 0.3, 0.25, "3", 9, L, DB, "r")
text(12.1, 6.95, 0.85, 0.25, "© Zurich", 9, L, DB)

s.notes_slide.notes_text_frame.text = ("Der Markt wächst dort am stärksten, wo wir mit 2,1 % Anteil klein sind "
                                      "(Beispieldaten, fiktiv). Das ist der Hebel.")
prs.save(sys.argv[1])
