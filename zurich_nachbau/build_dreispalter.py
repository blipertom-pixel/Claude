# -*- coding: utf-8 -*-
"""Schritt 4: Dreispalten-Folie (Struktur nach Screenshot): drei parallele Belege über dieselben Zeilen,
Hervorhebung über alle Spalten, Takeaway je Spalte mit fetten Schlüsselwörtern. Fiktive Daten, ein Modell."""
import sys
from zcharts import *

cats = ["Gesundheit", "Cyber", "Logistik", "Handwerk", "Handel", "Industrie", "Gastro", "Freie Berufe"]
grow = [2.4, 2.2, 1.6, 0.9, 0.9, 0.6, 0.2, 0.2]
share = [2.3, 2.0, 2.0, 3.6, 3.4, 3.8, 3.0, 3.5]
worth = [round(g * 10) for g in grow]
F = 3
assert abs(sum(grow) - 9.0) < 1e-9 and abs(sum(grow[:F]) - 6.2) < 1e-9 and round(sum(grow[:F]) / 9.0 * 100) == 69
avg = lambda idx: sum(grow[i] * share[i] for i in idx) / sum(grow[i] for i in idx)
assert round(avg(range(F)), 1) == 2.1 and round(avg(range(F, 8)), 1) == 3.5
assert sum(worth[:F]) == 62 and sum(worth[F:]) == 28
de = lambda v, n=1: f"{v:.{n}f}".replace(".", ",")

new_slide("Dort, wo der Markt am stärksten wächst, ist unser Anteil am kleinsten und jeder Prozentpunkt am meisten wert",
          "Situation: Der Markt wächst bis 2029 um 9,0 Mrd. €. Komplikation: 6,2 davon (69 %) entfallen auf Gesundheit, Cyber und Logistik, wo unser Anteil 2,1 % beträgt "
          "(übrige fünf: 3,5 %). Antwort: Dort ist ein Prozentpunkt Mehr-Anteil 62 Mio. € wert, in den übrigen fünf zusammen 28 Mio. €. Fiktive Daten, ein gemeinsames Modell.")

CW = (12.53 - 2 * 0.25) / 3
COLX = [0.4 + i * (CW + 0.25) for i in range(3)]
CY, CH_ = 2.62, 2.8
PY, PH = 0.02, 0.96
rows_top = CY + CH_ * PY; row_h = CH_ * PH / 8
shape(S.ROUNDED_RECTANGLE, 0.4, rows_top - 0.02, 12.53, F * row_h + 0.04, fill=LB, alpha=30, rad=0.08, name="Fokus-Zone")

def rich(x, y, w, h, parts, size=14):
    tb = Z.s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    for txt, bold in parts:
        r = p.add_run(); r.text = txt; r.font.size = Pt(size); r.font.name = M if bold else L; r.font.color.rgb = rgb(DB)
    return tb

cols = [("Marktzuwachs", "Zusätzliches Marktvolumen je Segment 2026 bis 2029, Mrd. €", grow, 3.0, "0.0", lambda v: de(v),
         [("Gesundheit, Cyber und Logistik liefern ", False), ("6,2 von 9,0 Mrd. €", True), (" des Zuwachses, das sind ", False), ("69 %", True), (".", False)]),
        ("Unser Marktanteil", "Unser Anteil am Segment, %", share, 5.0, "0.0", lambda v: de(v),
         [("In den drei Wachstumssegmenten liegt unser Anteil bei ", False), ("2,1 %", True), (", in den übrigen fünf bei ", False), ("3,5 %", True), (".", False)]),
        ("Wert eines Prozentpunkts", "Mehr-Anteil von 1 Pp am Zuwachs 2026 bis 2029, Mio. €", worth, 30, "0", lambda v: f"{v:.0f}",
         [("Ein Prozentpunkt ist in den drei Fokus-Segmenten ", False), ("62 Mio. €", True), (" wert, in den übrigen fünf zusammen ", False), ("28 Mio. €", True), (".", False)])]
for k, (x, (hd, desc, vals, vmax, fmt, lf, take)) in enumerate(zip(COLX, cols)):
    shape(S.ROUNDED_RECTANGLE, x, 1.45, CW, 0.42, fill=DB, rad=0.08)
    text(x + 0.18, 1.45, CW - 0.3, 0.42, hd, 15, M, WHITE, "l", "m")
    text(x + 0.05, 1.98, CW - 0.1, 0.55, desc, 13, L, DB)
    inner = (0.30, PY, 0.52, PH) if k == 0 else (0.02, PY, 0.80, PH)
    hbar(x, CY, CW, CH_, cats, vals, F, vmax, fmt, k == 0, inner, f"Balkendiagramm {hd}, {desc}", labels=False)
    pl_ = x + CW * inner[0]; pw_ = CW * inner[2]
    for i, v in enumerate(vals):
        yc = CY + CH_ * PY + row_h * (i + 0.5)
        text(pl_ + pw_ * v / vmax + 0.08, yc - 0.13, 0.7, 0.26, lf(v), 13, M if i < F else L, DB)
    rich(x + 0.05, 5.62, CW - 0.1, 1.2, take, 14)
footer("Beispieldaten, fiktiv. Anteil = Durchschnitt je Gruppe, gewichtet nach Marktzuwachs;\nWert von 1 Pp = Marktzuwachs × 1 %. Pp = Prozentpunkte.")
prs.save(sys.argv[1])
