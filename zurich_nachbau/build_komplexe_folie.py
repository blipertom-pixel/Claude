# -*- coding: utf-8 -*-
"""Schritt 3: komplexere Folie. Titel mit zwei Teilaussagen, je Teilaussage ein Beleg und darunter die Erklärung.
Beide Diagramme folgen EINEM Modell (24 Monatswerte des Anteils -> 21 Dreimonatsfenster). Fiktive Daten."""
import sys, json
import numpy as np
from zcharts import *
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.dml import MSO_LINE
from pptx.enum.chart import XL_MARKER_STYLE, XL_TICK_LABEL_POSITION

d = np.array(json.load(open(sys.argv[2]))["d"])                      # 23 Monatsschritte in Pp
share = 28.0 + np.concatenate([[0], np.cumsum(d)])                    # 24 Monatswerte, Nov 2024 bis Okt 2026
pace = np.array([d[i:i + 3].mean() for i in range(21)])               # 21 Dreimonatsfenster
assert abs(share[-1] - 34.5) < 1e-9 and (d > 0).all()
assert (np.round(pace, 2) <= 0.17).sum() == 2 and abs(pace.mean() - 0.29) < 0.005 and abs(pace.max() - 0.41) < 0.005
growth = (share[-1] / share[0]) ** (12 / 23) - 1
trend = np.exp(12 * np.polyfit(np.arange(24), np.log(share), 1)[0]) - 1
last12 = share[23] / share[11] - 1
assert round(growth * 100, 1) == 11.5 and round(trend * 100, 1) == 12.0 and round(last12 * 100, 1) == 10.5
MN = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
def lab(idx):                                                          # idx 0 = Nov 2024
    m = 10 + idx; return f"{MN[m % 12]} {str(2024 + m // 12)[2:]}"
LOW, PEAK = [6, 20], int(np.argmax(pace))
de = lambda v, n=2: f"{v:.{n}f}".replace(".", ",")

new_slide("Der Anteil wächst klar um 11,5 % pro Jahr, ein Nachlassen des Tempos ist nicht belegt",
          "Situation: Der Anteil stieg in 23 Monaten von 28,0 auf 34,5 %, jeder Monatsschritt zeigt nach oben (11,5 % pro Jahr, Trend 12,0 %, letzte zwölf Monate 10,5 %). "
          "Komplikation: Zuletzt lag das Tempo bei 0,17 statt 0,29 Pp pro Monat. Antwort: Genauso langsam war es schon im August 2025, danach 0,41; "
          "nur 2 von 21 Fenstern liegen so niedrig. Empfehlung: vor der Skalierung Datenbasis prüfen, Tempo weiter beobachten. Fiktive Daten.")

def panel(x, num, claim, head):
    shape(S.ROUNDED_RECTANGLE, x, 1.5, 6.115, 4.5, fill=WHITE, line=LB)
    shape(S.OVAL, x + 0.28, 1.72, 0.36, 0.36, fill=DB); text(x + 0.28, 1.72, 0.36, 0.36, str(num), 13, M, WHITE, "c", "m")
    text(x + 0.8, 1.72, 5.0, 0.36, claim, 19, M, DB, "l", "m")
    text(x + 0.28, 2.25, 5.6, 0.28, head, 11, M, ZB)
    shape(S.RECTANGLE, x + 0.28, 4.5, 5.55, 0.012, fill="D5E3F2")

def line_chart(x, y, w, h, cats, vals, vmin, vmax, grid, name, alt):
    cd = CategoryChartData(number_format="0.00"); cd.categories = cats; cd.add_series(name, [float(v) for v in vals])
    gf = Z.s.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    gf.name = name; gf._element.nvGraphicFramePr.cNvPr.set("descr", alt)
    ch = gf.chart; ch.has_legend = False; ch.has_title = False
    ch.font.size = Pt(12); ch.font.name = L; ch.font.color.rgb = rgb(DB)
    ser = ch.plots[0].series[0]; ser.smooth = False
    ser.format.line.color.rgb = rgb(MB); ser.format.line.width = Pt(2.25)
    ser.marker.style = XL_MARKER_STYLE.CIRCLE; ser.marker.size = 4
    ser.marker.format.fill.solid(); ser.marker.format.fill.fore_color.rgb = rgb(MB); ser.marker.format.line.fill.background()
    va = ch.value_axis; va.minimum_scale, va.maximum_scale = vmin, vmax
    va.has_major_gridlines = grid
    if grid:
        va.major_unit = 0.1
        va.major_gridlines.format.line.color.rgb = rgb("E3EAF2"); va.major_gridlines.format.line.width = Pt(0.75)
    va.format.line.fill.background(); va.tick_label_position = XL_TICK_LABEL_POSITION.NONE; va.major_tick_mark = XL_TICK_MARK.NONE
    ca = ch.category_axis; ca.format.line.color.rgb = rgb(LB); ca.tick_label_position = XL_TICK_LABEL_POSITION.NONE; ca.major_tick_mark = XL_TICK_MARK.NONE
    IX, IY, IW, IH = 0.03, 0.06, 0.94, 0.72
    plot_layout(ch, IX, IY, IW, IH); transparent(ch)
    n = len(vals); pl_, pw_ = x + w * IX, w * IW; pt_, ph_ = y + h * IY, h * IH
    return (lambda i: pl_ + pw_ * (i + .5) / n), (lambda v: pt_ + ph_ * (1 - (v - vmin) / (vmax - vmin))), (pl_, pw_)

def xlabels(X, idxs, texts, ybase, xmax):
    for i, tx in zip(idxs, texts): text(min(X(i) - 0.5, xmax - 1.0), ybase, 1.0, 0.26, tx, 12, L, DB, "c")

def disc(cx, cy, dd, col): shape(S.OVAL, cx - dd / 2, cy - dd / 2, dd, dd, fill=col, name="Markierung")

# ---------------- linker Beleg: Anteil über 24 Monate
LX, RX = 0.4, 6.815
panel(LX, 1, "Das Wachstum ist klar", "ANTEIL AM MARKT, %, NOV 2024 BIS OKT 2026")
cats = [lab(i) for i in range(24)]
X, Y, (pl_, pw_) = line_chart(LX + 0.2, 2.5, 5.75, 1.95, cats, share, 27, 36, False, "Anteil am Markt, %",
    "Liniendiagramm: Anteil am Markt von 28,0 % im Nov 2024 auf 34,5 % im Okt 2026, jeder Monatsschritt positiv.")
xlabels(X, [0, 6, 12, 18, 23], [lab(i) for i in (0, 6, 12, 18, 23)], 4.07, LX + 6.115 - 0.12)
disc(X(0), Y(share[0]), 0.17, ZB); disc(X(23), Y(share[23]), 0.17, ZB)
text(X(0) - 0.05, Y(share[0]) - 0.38, 0.9, 0.28, de(share[0], 1), 14, M, DB)
text(X(23) - 0.85, Y(share[23]) - 0.38, 0.9, 0.28, de(share[23], 1), 14, M, DB, "r")
pill(X(1), Y(35.2), 1.95, "+11,5 % pro Jahr", ZB, WHITE, h=0.34, size=13)
text(LX + 0.28, 4.6, 5.55, 1.3,
     f"In 23 Monaten stieg der Anteil von 28,0 auf 34,5 %, jeder Monatsschritt zeigt nach oben. "
     f"Trend über alle 24 Monate: {de(trend * 100, 1)} %, letzte zwölf Monate allein: {de(last12 * 100, 1)} %.", 14, L, DB)

# ---------------- rechter Beleg: Tempo über 21 Fenster
panel(RX, 2, "Ein Nachlassen ist nicht belegt", "TEMPO, PP PRO MONAT, GLEITENDER DREIMONATSSCHNITT")
cats2 = [lab(i + 3) for i in range(21)]
X, Y, (pl_, pw_) = line_chart(RX + 0.2, 2.5, 5.75, 1.95, cats2, pace, 0.04, 0.50, False, "Tempo, Pp pro Monat",
    "Liniendiagramm: Tempo des Anteilswachstums in Pp pro Monat, 21 Dreimonatsfenster. Tiefstwerte 0,17 im Aug 2025 und Okt 2026, Höchstwert 0,41 im Nov 2025.")
xlabels(X, [0, 6, 12, 20], [lab(i + 3) for i in (0, 6, 12, 20)], 4.07, RX + 6.115 - 0.12)
c = Z.s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(pl_), Inches(Y(.17)), Inches(pl_ + pw_), Inches(Y(.17)))
st_ = c._element.find(qn("p:style")); c._element.remove(st_)
c.line.color.rgb = rgb(DB); c.line.width = Pt(1.25); c.line.dash_style = MSO_LINE.DASH; c.name = "Referenz 0,17"
for i in LOW: disc(X(i), Y(pace[i]), 0.17, DB)
disc(X(PEAK), Y(pace[PEAK]), 0.15, ZB)
text(X(LOW[0]) - 0.9, Y(.17) + 0.14, 1.8, 0.26, f"{lab(LOW[0] + 3)[:3]} 2025 · 0,17", 12, M, DB, "c")
text(X(LOW[1]) - 1.8, Y(.17) + 0.14, 1.9, 0.26, "Okt 2026 · 0,17", 12, M, DB, "r")
text(X(PEAK) - 0.2, Y(pace[PEAK]) - 0.36, 1.6, 0.26, f"danach {de(pace[PEAK])}", 12, M, ZB)
text(RX + 0.28, 4.6, 5.55, 1.3,
     f"Zuletzt stieg der Anteil um 0,17 statt im Schnitt {de(pace.mean())} Pp pro Monat. "
     f"Genauso langsam war es schon im August 2025, danach lag das Tempo bei {de(pace[PEAK])}. Nur 2 von 21 Fenstern sind so niedrig.", 14, L, DB)

shape(S.ROUNDED_RECTANGLE, 0.4, 6.14, 12.53, 0.66, fill=DB)
text(0.65, 6.14, 1.9, 0.66, "WIR EMPFEHLEN", 12, M, WHITE, "l", "m")
text(2.55, 6.14, 10.2, 0.66, "Vor einer Skalierung die Datenbasis prüfen und das Tempo weiter monatlich beobachten.", 16, L, WHITE, "l", "m")
footer("Fiktive Daten. Pp = Prozentpunkte; Wachstum = relatives Wachstum des Anteils (23 Monate = 1,92 Jahre);\nFenster = Schnitt von drei Monatsschritten. Beschriftung der Fenster = Endmonat.")
prs.save(sys.argv[1])
