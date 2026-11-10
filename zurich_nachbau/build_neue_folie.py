# -*- coding: utf-8 -*-
"""Neue Folie (Schritt 2): ein Beleg, ein Zeitverlauf, direkte Beschriftung, kein Band. Fiktive Daten."""
import sys
from zcharts import *
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.dml import MSO_LINE
from pptx.enum.chart import XL_MARKER_STYLE, XL_TICK_LABEL_POSITION

new_slide("Das Tempo von 0,17 Pp pro Monat gab es schon einmal, im August 2025, danach stieg es auf 0,41",
          "Situation: Der Anteil wächst klar. Komplikation: Das Tempo war zuletzt mit 0,17 Pp pro Monat niedriger als der Durchschnitt (0,29). "
          "Antwort: Das gleiche Tempo gab es schon im August 2025, danach stieg es auf 0,41. Nur 2 von 21 Dreimonatsfenstern liegen so niedrig. "
          "Nachlassen: möglich, aber nicht belegt. Fiktive Daten.")
months = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
cats = [f"{months[i % 12]} {25 + i // 12}" if i % 3 == 0 else " " for i in range(21)]   # nur Quartalsanfänge beschriftet
vals = [.31, .28, .33, .30, .36, .27, .24, .17, .29, .41, .35, .32, .30, .34, .31, .27, .29, .33, .26, .22, .17]
assert len(vals) == 21 and sum(1 for v in vals if v <= 0.17) == 2 and abs(sum(vals) / 21 - 0.29) < 0.005
LOW = [7, 20]; PEAK = 9

shape(S.ROUNDED_RECTANGLE, 0.4, 1.62, 12.53, 4.05, fill=WHITE, line=LB)
text(0.65, 1.8, 11.8, 0.3, "TEMPO DES ANTEILSWACHSTUMS, PP PRO MONAT (GLEITENDER DREIMONATSSCHNITT, 21 FENSTER)", 12, M, ZB)

FX, FY, FW, FH = 0.55, 2.15, 12.2, 3.45
IX, IY, IW, IH = 0.055, 0.1, 0.93, 0.74
cd = CategoryChartData(number_format="0.00"); cd.categories = cats; cd.add_series("Tempo, Pp pro Monat", vals)
gf = Z.s.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS, Inches(FX), Inches(FY), Inches(FW), Inches(FH), cd)
gf.name = "Liniendiagramm Tempo"
gf._element.nvGraphicFramePr.cNvPr.set("descr", "Liniendiagramm: Tempo des Anteilswachstums in Pp pro Monat, 21 Dreimonatsfenster von Jan 2025 bis Sep 2026. "
    "Tiefstwerte 0,17 im Aug 2025 und im Sep 2026, Höchstwert 0,41 im Okt 2025, Durchschnitt 0,29.")
ch = gf.chart; ch.has_legend = False; ch.has_title = False
ch.font.size = Pt(12); ch.font.name = L; ch.font.color.rgb = rgb(DB)
ser = ch.plots[0].series[0]; ser.smooth = False
ser.format.line.color.rgb = rgb(MB); ser.format.line.width = Pt(2.25)
ser.marker.style = XL_MARKER_STYLE.CIRCLE; ser.marker.size = 5
ser.marker.format.fill.solid(); ser.marker.format.fill.fore_color.rgb = rgb(MB); ser.marker.format.line.fill.background()
for i, size, col in [(7, 12, DB), (20, 12, DB), (9, 9, ZB)]:
    pt = ser.points[i]; pt.marker.style = XL_MARKER_STYLE.CIRCLE; pt.marker.size = size
    pt.marker.format.fill.solid(); pt.marker.format.fill.fore_color.rgb = rgb(col); pt.marker.format.line.fill.background()
va = ch.value_axis; va.minimum_scale, va.maximum_scale, va.major_unit = 0, 0.5, 0.1
va.has_major_gridlines = True
va.major_gridlines.format.line.color.rgb = rgb("E3EAF2"); va.major_gridlines.format.line.width = Pt(0.75)
va.format.line.fill.background(); va.tick_label_position = XL_TICK_LABEL_POSITION.NONE
va.major_tick_mark = XL_TICK_MARK.NONE
ca = ch.category_axis; ca.format.line.color.rgb = rgb(LB); ca.tick_labels.font.size = Pt(12); ca.major_tick_mark = XL_TICK_MARK.NONE
cax = ca._element
skip = parse_xml('<c:tickLblSkip xmlns:c="%s" val="3"/>' % C_NS)
anchor = cax.find(qn("c:noMultiLvlLbl"))
(anchor.addprevious(skip) if anchor is not None else cax.append(skip))
plot_layout(ch, IX, IY, IW, IH); transparent(ch)

pl_, pw_ = FX + FW * IX, FW * IW; pt_, ph_ = FY + FH * IY, FH * IH
X = lambda i: pl_ + pw_ * (i + 0.5) / 21
Y = lambda v: pt_ + ph_ * (1 - v / 0.5)
for v in (0, .1, .2, .3, .4, .5):                          # eigene Achsenzahlen mit Dezimalkomma
    text(pl_ - 0.55, Y(v) - 0.13, 0.45, 0.26, f"{v:.1f}".replace(".", ","), 12, L, DB, "r")
c = Z.s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(pl_), Inches(Y(.17)), Inches(pl_ + pw_), Inches(Y(.17)))
st_ = c._element.find(qn("p:style"))
if st_ is not None: c._element.remove(st_)
c.line.color.rgb = rgb(DB); c.line.width = Pt(1.25); c.line.dash_style = MSO_LINE.DASH; c.name = "Referenz 0,17"
for i_, d_, col_ in [(7, 0.2, DB), (20, 0.2, DB), (9, 0.16, ZB)]:
    v_ = vals[i_]; shape(S.OVAL, X(i_) - d_ / 2, Y(v_) - d_ / 2, d_, d_, fill=col_, name="Markierung")
text(pl_ + 0.12, Y(.17) + 0.05, 2.6, 0.26, "0,17 Pp pro Monat", 13, M, DB)
text(X(7) - 0.8, Y(.17) + 0.2, 1.6, 0.28, "Aug 2025", 13, M, DB, "c")
text(X(20) - 1.5, Y(.17) + 0.2, 1.6, 0.28, "Sep 2026", 13, M, DB, "r")
text(X(9) - 0.9, Y(.41) - 0.36, 1.8, 0.28, "danach 0,41", 13, M, ZB, "c")

shape(S.RECTANGLE, 0.4, 5.85, 12.53, 0.012, fill="D5E3F2")
text(0.4, 6.05, 12.5, 0.5, "Zwei von 21 Fenstern liegen so niedrig. Ein Nachlassen ist möglich, aber nicht belegt.", 20, M, DB)
footer("Fiktive Daten. Pp = Prozentpunkte; 21 Dreimonatsfenster, Jan 2025 bis Sep 2026; Durchschnitt 0,29 Pp pro Monat.")
prs.save(sys.argv[1])
