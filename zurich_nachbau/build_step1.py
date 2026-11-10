# -*- coding: utf-8 -*-
"""Schritt 1: erste Folie, genau EINE Änderung (Klammer über den drei Fokus-Säulen)."""
import sys
from zcharts import *
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
gf = Z.s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.5), Inches(2.15), Inches(7.8), Inches(3.75), cd)
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
FX_, FY_, FW_, FH_ = 0.5, 2.15, 7.8, 3.75
IX_, IY_, IW_, IH_ = 0.06, 0.22, 0.92, 0.62
plot_layout(ch, IX_, IY_, IW_, IH_)
p_left = FX_ + FW_ * IX_; p_w = FW_ * IW_; p_top = FY_ + FH_ * IY_; p_h = FH_ * IH_
yb = p_top + p_h * (1 - 2.4 / 3) - 0.5          # über dem höchsten Fokus-Balken samt Zahl
xb0, xb1 = p_left + 0.08, p_left + p_w * 3 / 8 - 0.08
shape(S.RECTANGLE, xb0, yb, xb1 - xb0, 0.02, fill=DB, name="Klammer Fokus-Segmente")
shape(S.RECTANGLE, xb0, yb, 0.02, 0.14, fill=DB); shape(S.RECTANGLE, xb1 - 0.02, yb, 0.02, 0.14, fill=DB)
text(xb0, yb - 0.34, xb1 - xb0, 0.3, "6,2 von 9,0 Mrd. € = 69\u00a0%", 14, M, DB, "c")
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


prs.save(sys.argv[1])
