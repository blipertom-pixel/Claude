# -*- coding: utf-8 -*-
"""Lern-Deck Marktfokus (fiktiv): 11 Folien nach Ghost Deck (../Methode_Deck_bauen.md, Abschnitt 7).
Alle Zahlen kommen aus EINEM Modell (siehe ../modell_anteil.json und die Konstanten unten)."""
import sys, json
sys.path.insert(0, "..")
import numpy as np
from zcharts import *
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.dml import MSO_LINE
from pptx.enum.chart import XL_MARKER_STYLE, XL_TICK_LABEL_POSITION

# ------------------------------ Modell ---------------------------------------------------------------
cats = ["Gesundheit", "Cyber", "Logistik", "Handwerk", "Handel", "Industrie", "Gastro", "Freie Berufe"]
grow = [2.4, 2.2, 1.6, 0.9, 0.9, 0.6, 0.2, 0.2]          # Marktzuwachs 2026-2029, Mrd. €
share = [2.3, 2.0, 2.0, 3.6, 3.4, 3.8, 3.0, 3.5]         # unser Anteil, %
worth = [round(g * 10) for g in grow]                    # Wert von 1 Pp, Mio. €
F = 3
focus_g, rest_g = sum(grow[:F]), sum(grow[F:])
avg = lambda idx: sum(grow[i] * share[i] for i in idx) / sum(grow[i] for i in idx)
assert abs(sum(grow) - 9.0) < 1e-9 and abs(focus_g - 6.2) < 1e-9 and abs(rest_g - 2.8) < 1e-9
assert round(focus_g / 9 * 100) == 69 and round(avg(range(F)), 1) == 2.1 and round(avg(range(F, 8)), 1) == 3.5
assert sum(worth[:F]) == 62 and sum(worth[F:]) == 28
INV_A, INV_B, PP_A, PP_B = 140, 80, 0.5, 1.5
GAIN_A, GAIN_B = PP_A / 100 * 9000, PP_B / 100 * 6200     # 45 und 93 Mio. €
assert round(GAIN_A) == 45 and round(GAIN_B) == 93
EUR_A, EUR_B = GAIN_A / INV_A, GAIN_B / INV_B
assert round(EUR_A, 2) == 0.32 and round(EUR_B, 2) == 1.16 and EUR_B / EUR_A > 3
BREAK = INV_B / 6200 * 100
assert round(BREAK, 1) == 1.3
SC = [("Vorsichtig", 0.8), ("Basis", 1.5), ("Ambitioniert", 2.2)]
sc_val = [round(p / 100 * 6200) for _, p in SC]
assert sc_val == [50, 93, 136]
PH = [("Datenbasis klären", "Q1 2027", 2), ("Pilot in einem Segment", "Q2 2027", 8),
      ("Auf drei Segmente ausweiten", "Q3 2027", 40), ("Auf Jahreswerte steuern", "Q4 2027", 30)]
assert sum(p[2] for p in PH) == INV_B and sum(p[2] for p in PH[:2]) / INV_B == 0.125
d = np.array(json.load(open("../modell_anteil.json"))["d"])
sh_ts = 28.0 + np.concatenate([[0], np.cumsum(d)])
pace = np.array([d[i:i + 3].mean() for i in range(21)])
assert abs(sh_ts[-1] - 34.5) < 1e-9 and (d > 0).all()
assert (np.round(pace, 2) <= 0.17).sum() == 2 and abs(pace.mean() - 0.29) < 0.005 and abs(pace.max() - 0.41) < 0.005
growth = (sh_ts[-1] / sh_ts[0]) ** (12 / 23) - 1
trend = np.exp(12 * np.polyfit(np.arange(24), np.log(sh_ts), 1)[0]) - 1
last12 = sh_ts[23] / sh_ts[11] - 1
assert round(growth * 100, 1) == 11.5 and round(trend * 100, 1) == 12.0 and round(last12 * 100, 1) == 10.5
de = lambda v, n=1: f"{v:.{n}f}".replace(".", ",")
MN = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
def lab(idx): m = 10 + idx; return f"{MN[m % 12]} {str(2024 + m // 12)[2:]}"      # idx 0 = Nov 2024
LOW, PEAK = [6, 20], int(np.argmax(pace))

# ------------------------------ Helfer ---------------------------------------------------------------
def tracker(n, label):
    shape(S.ROUNDED_RECTANGLE, 11.4, 0.93, 1.5, 0.3, fill="E9EBF0", rad=0.15)
    shape(S.OVAL, 11.45, 0.96, 0.24, 0.24, fill=DB); text(11.45, 0.96, 0.24, 0.24, str(n), 10, M, WHITE, "c", "m")
    text(11.78, 0.93, 1.1, 0.3, label, 11, L, DB, "l", "m")

def band(label, sentence, size=16, y=6.14):
    shape(S.ROUNDED_RECTANGLE, 0.4, y, 12.53, 0.66, fill=DB)
    text(0.65, y, 1.9, 0.66, label, 12, M, WHITE, "l", "m")
    text(2.55, y, 10.2, 0.66, sentence, size, L, WHITE, "l", "m")

def card(x, y, w, h, kind="white"):
    if kind == "dark": return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=DB)
    if kind == "tint": return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=LB, alpha=30)
    return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=WHITE, line=LB)

def rich(x, y, w, h, parts, size=14, color=DB):
    tb = Z.s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True; tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    for txt, bold in parts:
        r = p.add_run(); r.text = txt; r.font.size = Pt(size); r.font.name = M if bold else L; r.font.color.rgb = rgb(color)
    return tb

def dash(x1, y1, x2, y2, color=DB, w=1.25):
    c = Z.s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    st = c._element.find(qn("p:style"))
    if st is not None: c._element.remove(st)
    c.line.color.rgb = rgb(color); c.line.width = Pt(w); c.line.dash_style = MSO_LINE.DASH; return c

def polyline(pts, color, w=2.25):
    fb = Z.s.shapes.build_freeform(Inches(pts[0][0]), Inches(pts[0][1]))
    fb.add_line_segments([(Inches(a), Inches(b)) for a, b in pts[1:]], close=False)
    f = fb.convert_to_shape(); f.fill.background()
    st = f._element.find(qn("p:style"))
    if st is not None: f._element.remove(st)
    f.line.color.rgb = rgb(color); f.line.width = Pt(w); return f

def minibars(x, y, title, items, vmax, labw, wbar, fmt, ref=None):
    text(x, y, labw + wbar + 0.5, 0.22, title, 11, M, ZB)
    for k, (lb, v, col) in enumerate(items):
        yy = y + 0.3 + k * 0.38
        text(x, yy, labw, 0.28, lb, 12, L, DB, "l", "m")
        shape(S.RECTANGLE, x + labw, yy + 0.03, wbar * v / vmax, 0.22, fill=col)
        text(x + labw + wbar * v / vmax + 0.07, yy, 0.55, 0.28, fmt(v), 12, M, DB, "l", "m")
    if ref:
        xr = x + labw + wbar * ref[0] / vmax
        dash(xr, y + 0.26, xr, y + 0.3 + len(items) * 0.38 + 0.02)
        text(xr + 0.08, y, 1.9, 0.22, ref[1], 11, M, DB)

MAIN = 0

# ======================= 1  Titel ======================================================================
new_slide("Hero", "Zweck: Der Vorstand soll 80 Mio. € für den Fokus auf drei Segmente freigeben. Alle Zahlen sind fiktive Beispieldaten aus einem gemeinsamen Modell. "
          "Lernhinweis: Dieses Deck folgt der Methode (Antwort zuerst, drei Argumente, Ghost Deck). Die Erklärung je Folie steht in den Notizen.", dark=True)
for k, (dd, a) in enumerate([(5.2, 12), (4.0, 16), (2.8, 22)]):
    shape(S.DONUT, 13.333 - dd * 0.62, 7.5 - dd * 0.62, dd, dd, fill=LB, alpha=a).adjustments[0] = 0.1
set_title("Wir setzen 80 Mio. € auf drei Segmente, in denen der Markt am stärksten wächst", 0.7, 2.2, 8.6, 2.4, 44, WHITE)
text(0.7, 5.0, 9.3, 0.4, "Vorlage für den Vorstand  ·  Marktfokus 2027 bis 2029  ·  10. November 2026", 17, L, WHITE)
text(0.4, 6.93, 9, 0.3, "Beispieldaten, fiktiv.", 12, L, WHITE)

# ======================= 2  Antwort zuerst, jede Behauptung mit ihrem Vergleich ========================
new_slide("Wir setzen 80 Mio. € auf drei Segmente, weil Markt, Rechnung und Datenbasis dafür sprechen",
          "WARUM DIESE FOLIE: Antwort zuerst. Wer nur diese Folie liest, kennt Antwort und Gründe. Jede Behauptung zeigt rechts ihren Vergleich, "
          "damit sie belegt und nicht nur behauptet ist. Die Detailbelege folgen auf Folie 3 bis 7. "
          "Situation: Der Markt wächst bis 2029 um 9,0 Mrd. €. Komplikation: 69 % davon liegen in drei Segmenten mit nur 2,1 % Anteil. "
          "Frage: Wo setzen wir Geld ein, und können wir den Daten trauen? Antwort: 80 Mio. € auf Gesundheit, Cyber, Logistik.")
RH, GAP, Y0 = 1.38, 0.13, 1.5
claims = [(g_trend, "Der Markt wächst dort am stärksten", "Drei Segmente liefern 69 % des Zuwachses, und wir haben dort den kleinsten Anteil.", "Folie 3"),
          (g_scales, "Die Rechnung geht auf", "Je investiertem Euro bringt der Fokus mehr als dreimal so viel wie die breite Streuung.", "Folie 4 und 5"),
          (g_check, "Die Daten tragen", "Der Anteil wächst klar um 11,5 % pro Jahr, ein Nachlassen des Tempos ist nicht belegt.", "Folie 6 und 7")]
for i, (g, claim, proof, ref) in enumerate(claims):
    y = Y0 + i * (RH + GAP)
    card(0.4, y, 12.53, RH)
    g(1.05, y + RH / 2, 0.78)
    text(1.65, y + 0.2, 4.8, 0.36, claim, 19, M, DB)
    text(1.65, y + 0.64, 4.7, 0.6, proof, 13, L, DB)
    text(1.65, y + 1.12, 3, 0.2, ref, 11, M, ZB)
    shape(S.RECTANGLE, 6.65, y + 0.2, 0.015, RH - 0.4, fill="D5E3F2")
mx = 6.95; y1 = Y0 + 0.17
minibars(mx, y1, "MARKTZUWACHS, MRD. €", [("Fokus (3)", focus_g, ZB), ("übrige (5)", rest_g, FOCUS_LIGHT)], 6.2, 0.95, 1.2, lambda v: de(v))
minibars(mx + 3.0, y1, "UNSER ANTEIL, %", [("Fokus (3)", avg(range(F)), ZB), ("übrige (5)", avg(range(F, 8)), FOCUS_LIGHT)], 3.5, 0.95, 1.1, lambda v: de(v))
y2 = Y0 + (RH + GAP) + 0.17
minibars(mx, y2, "MEHR-ANTEIL JE INVESTIERTEM EURO, €", [("Fokus", EUR_B, ZB), ("breit", EUR_A, FOCUS_LIGHT)], 1.3, 0.7, 4.0, lambda v: de(v, 2), ref=(1.0, "1,00 = Einsatz"))
y3 = Y0 + 2 * (RH + GAP) + 0.17
text(mx, y3, 5.5, 0.22, "ANTEIL AM MARKT, %, NOV 2024 BIS OKT 2026", 11, M, ZB)
pts = [(mx + 0.1 + 4.2 * k / 23, y3 + 0.98 - 0.5 * (v - 28.0) / 6.5) for k, v in enumerate(sh_ts)]
polyline(pts, MB)
shape(S.OVAL, pts[0][0] - 0.07, pts[0][1] - 0.07, 0.14, 0.14, fill=ZB); shape(S.OVAL, pts[-1][0] - 0.07, pts[-1][1] - 0.07, 0.14, 0.14, fill=ZB)
text(pts[0][0] - 0.05, pts[0][1] - 0.32, 0.7, 0.24, "28,0", 12, M, DB)
text(pts[-1][0] - 0.2, pts[-1][1] - 0.3, 0.7, 0.24, "34,5", 12, M, DB)
pill(mx + 0.7, y3 + 0.32, 1.9, "+11,5 % pro Jahr", ZB, WHITE, h=0.32, size=12)
band("WIR BITTEN UM", "Freigabe von 80 Mio. € für 2027 bis 2029 und den Start des Piloten im ersten Quartal.")
footer("Beispieldaten, fiktiv. Fokus = Gesundheit, Cyber, Logistik; Anteil gewichtet nach Marktzuwachs; \nMehr-Anteil = Pp-Gewinn × Marktzuwachs ÷ Investition.")

# ======================= 3  Dreispalter (freigegeben) ==================================================
new_slide("Dort, wo der Markt am stärksten wächst, ist unser Anteil am kleinsten und jeder Prozentpunkt am meisten wert",
          "WARUM DIESE FOLIE: Argument 1 (Warum dort?). Der Titel enthält drei Teilaussagen (wächst, Anteil klein, Prozentpunkt wertvoll), also drei Belege über dieselben acht Segmente. "
          "Die Hervorhebung läuft quer durch alle Spalten, damit man die Fokus-Segmente über alle drei Sichten verfolgt. "
          "Gemeinsames Modell: Wert von 1 Pp = Marktzuwachs × 1 %. Fiktive Daten.")
tracker(1, "Warum dort")
CW = (12.53 - 2 * 0.25) / 3
COLX = [0.4 + i * (CW + 0.25) for i in range(3)]
CY, CH_ = 2.62, 2.8; PY_, PH_ = 0.02, 0.96
rows_top = CY + CH_ * PY_; row_h = CH_ * PH_ / 8
shape(S.ROUNDED_RECTANGLE, 0.4, rows_top - 0.02, 12.53, F * row_h + 0.04, fill=LB, alpha=30, rad=0.08, name="Fokus-Zone")
cols = [(g_trend, "Marktzuwachs", "Zusätzliches Marktvolumen je Segment 2026 bis 2029, Mrd. €", grow, 3.0, "0.0", lambda v: de(v),
         [("Gesundheit, Cyber und Logistik liefern ", False), ("6,2 von 9,0 Mrd. €", True), (" des Zuwachses, das sind ", False), ("69 %", True), (".", False)]),
        (g_c, "Unser Marktanteil", "Unser Anteil am Segment, %", share, 5.0, "0.0", lambda v: de(v),
         [("In den drei Wachstumssegmenten liegt unser Anteil bei ", False), ("2,1 %", True), (", in den übrigen fünf bei ", False), ("3,5 %", True), (".", False)]),
        (g_scales, "Wert eines Prozentpunkts", "Mehr-Anteil von 1 Pp am Zuwachs 2026 bis 2029, Mio. €", worth, 30, "0", lambda v: f"{v:.0f}",
         [("Ein Prozentpunkt ist in den drei Fokus-Segmenten ", False), ("62 Mio. €", True), (" wert, in den übrigen fünf zusammen ", False), ("28 Mio. €", True), (".", False)])]
for k, (x, (gi, hd, desc, vals, vmax, fmt, lf, take)) in enumerate(zip(COLX, cols)):
    shape(S.ROUNDED_RECTANGLE, x, 1.45, CW, 0.46, fill=DB, rad=0.08)
    gi(x + 0.36, 1.68, 0.34)
    text(x + 0.68, 1.45, CW - 0.8, 0.46, hd, 15, M, WHITE, "l", "m")
    text(x + 0.05, 2.0, CW - 0.1, 0.55, desc, 13, L, DB)
    inner = (0.30, PY_, 0.52, PH_) if k == 0 else (0.02, PY_, 0.80, PH_)
    hbar(x, CY, CW, CH_, cats, vals, F, vmax, fmt, k == 0, inner, f"Balkendiagramm {hd}, {desc}", labels=False)
    pl_ = x + CW * inner[0]; pw_ = CW * inner[2]
    for i, v in enumerate(vals):
        yc = CY + CH_ * PY_ + row_h * (i + 0.5)
        text(pl_ + pw_ * v / vmax + 0.08, yc - 0.13, 0.7, 0.26, lf(v), 13, M if i < F else L, DB)
    rich(x + 0.05, 5.62, CW - 0.1, 1.2, take, 14)
footer("Beispieldaten, fiktiv. Anteil = Durchschnitt je Gruppe, gewichtet nach Marktzuwachs;\nWert von 1 Pp = Marktzuwachs × 1 %. Pp = Prozentpunkte.")

# ======================= 4  Optionen ===================================================================
new_slide("Der Fokus bringt je investiertem Euro mehr als dreimal so viel wie die breite Streuung",
          "WARUM DIESE FOLIE: Argument 2 (Lohnt es sich?). Die Aufgabe des Betrachters wechselt von 'Segmente vergleichen' zu 'Optionen bewerten': Kriterien mal Optionen, Empfehlung markiert. "
          "Beitrag je Euro = Mehr-Anteil ÷ Investition: Option A 45 ÷ 140 = 0,32; Option B 93 ÷ 80 = 1,16 (3,6-fach). Das Risiko steht als Symbol und Wort, nicht nur als Farbe. Fiktive Daten.")
tracker(2, "Lohnt es sich")
LX_, LW_, CWD, CG_ = 0.4, 3.0, 2.98, 0.165
colx = [LX_ + LW_ + CG_ + i * (CWD + CG_) for i in range(3)]
heads = [(g_network, "Option A", "Breit wachsen", "alle acht Segmente"), (g_target, "Option B", "Fokus auf 3 Segmente", "Gesundheit, Cyber, Logistik"),
         (g_hourglass, "Option C", "Bestand halten", "keine neue Investition")]
HY, HH, RY, RHH = 1.5, 1.0, 2.62, 0.84
for i, (x, (gi, o, n, dsc)) in enumerate(zip(colx, heads)):
    rec = i == 1
    shape(S.ROUNDED_RECTANGLE, x, HY, CWD, HH, fill=DB if rec else "DDE4E3", rad=0.1)
    gi(x + 0.42, HY + 0.5, 0.5)
    text(x + 0.82, HY + 0.12, CWD - 0.9, 0.25, o.upper(), 11, M, WHITE if rec else ZB, spacing=100)
    text(x + 0.82, HY + 0.37, CWD - 0.85, 0.3, n, 13, M, WHITE if rec else DB)
    text(x + 0.82, HY + 0.68, CWD - 0.9, 0.25, dsc, 11, L, WHITE if rec else DB)
pill(colx[1] + CWD - 1.18, HY + 0.1, 1.05, "Empfohlen", LB, DB, h=0.28, size=11) if False else None
labels = [("Mehr-Anteil bis 2029", "Pp-Gewinn × Marktzuwachs"), ("Investition 2027 bis 2029", None),
          ("Beitrag je investiertem Euro", "Mehr-Anteil ÷ Investition; 1,00 = Einsatz kommt zurück"), ("Umsetzungsrisiko", None)]
cells = [[("45 Mio. €", "+0,5 Pp auf 9,0 Mrd. €"), ("93 Mio. €", "+1,5 Pp auf 6,2 Mrd. €"), ("0 Mio. €", "Anteil unverändert")],
         [("140 Mio. €", ""), ("80 Mio. €", ""), ("0 Mio. €", "")], None,
         [("hoch", "acht Segmente parallel"), ("mittel", "drei Segmente, mit Pilot"), ("niedrig", "Anteil nicht gesichert")]]
risk_fill = {"hoch": 1.0, "mittel": 0.5, "niedrig": 0.0}
for r, (lb, sub) in enumerate(labels):
    y = RY + r * RHH
    text(LX_ + 0.05, y + 0.12, LW_ - 0.2, 0.3, lb, 14, M, DB)
    if sub: text(LX_ + 0.05, y + 0.42, LW_ - 0.15, 0.4, sub, 11, L, DB)
    shape(S.RECTANGLE, LX_, y + RHH - 0.01, LW_ + CG_ + 3 * CWD + 2 * CG_, 0.012, fill="D5E3F2")
    for i, x in enumerate(colx):
        if r == 2:
            v = [EUR_A, EUR_B, None][i]
            if v is None:
                text(x + 0.2, y + 0.18, CWD - 0.4, 0.45, "kein Beitrag", 20, O, DB, "l", "m")
            else:
                text(x + 0.2, y + 0.03, CWD - 0.4, 0.42, de(v, 2) + " €", 26 if i == 1 else 22, O, ZB if i == 1 else DB, "l", "m")
                shape(S.RECTANGLE, x + 0.2, y + 0.52, 2.5 * v / 1.2, 0.17, fill=ZB if i == 1 else FOCUS_LIGHT)
            if v is not None: shape(S.RECTANGLE, x + 0.2 + 2.5 / 1.2 - 0.008, y + 0.47, 0.016, 0.27, fill=DB)       # Marke 1,00
        elif r == 3:
            v, dsc = cells[3][i]; f = risk_fill[v]
            shape(S.OVAL, x + 0.2, y + 0.17, 0.26, 0.26, fill=DB if f == 1 else WHITE, line=DB, lw=1.5)
            if f == 0.5:
                ch_ = shape(S.CHORD, x + 0.2, y + 0.17, 0.26, 0.26, fill=DB); ch_.adjustments[0] = 54; ch_.adjustments[1] = 162
            text(x + 0.58, y + 0.12, CWD - 0.7, 0.3, v, 16, M, DB)
            text(x + 0.58, y + 0.43, CWD - 0.7, 0.3, dsc, 12, L, DB)
        else:
            v, dsc = cells[r][i]
            text(x + 0.2, y + 0.07, CWD - 0.4, 0.5, v, 26 if i == 1 else 22, O, ZB if i == 1 else DB, "l", "m")
            if dsc: text(x + 0.2, y + 0.56, CWD - 0.4, 0.22, dsc, 12, L, DB)
shape(S.ROUNDED_RECTANGLE, colx[1] - 0.06, HY - 0.04, CWD + 0.12, RY + 4 * RHH - HY + 0.08, line=ZB, lw=2.5, rad=0.12, name="Empfehlungsrahmen")
band("EMPFEHLUNG", "Option B: höchster Ertrag je Euro, mittleres Risiko und 60 Mio. € weniger Investition als Option A.", 15)
footer("Beispieldaten, fiktiv. Mehr-Anteil = Pp-Gewinn × Marktzuwachs 2026 bis 2029 \n(A: 0,5 Pp × 9,0 Mrd. €; B: 1,5 Pp × 6,2 Mrd. €). Pp = Prozentpunkte.")

# ======================= 5  Szenarien ==================================================================
new_slide("Die Investition rechnet sich ab 1,3 Prozentpunkten Mehr-Anteil, im Basisfall erreichen wir 1,5",
          "WARUM DIESE FOLIE: Argument 2 (Lohnt es sich?), zweite Hälfte. Folie 4 zeigt die Rechnung im Basisfall; diese Folie beantwortet die eigene Frage 'Hält sie bei Unsicherheit?'. "
          "Betrachteraufgabe: Balken gegen eine Schwelle lesen (Säulen mit Linie). Szenarien sind Fortschreibungen, keine Prognosen. "
          "Break-even 80 ÷ 6.200 = 1,29 Pp. Vorsichtig +0,8 Pp = 50, Basis +1,5 = 93, ambitioniert +2,2 = 136 Mio. €. Fiktive Daten.")
tracker(2, "Lohnt es sich")
card(0.4, 1.5, 8.5, 4.5)
text(0.65, 1.7, 7.5, 0.3, "MEHR-ANTEIL BIS 2029 JE SZENARIO, MIO. € (OPTION B)", 12, M, ZB)
sc_cats = [f"{n}  +{de(p)} Pp" for n, p in SC]
cd = CategoryChartData(number_format='0'); cd.categories = sc_cats; cd.add_series("Mehr-Anteil, Mio. €", sc_val)
FX, FY, FW, FH = 0.5, 2.1, 8.3, 3.8; IX, IY, IW, IH = 0.04, 0.1, 0.92, 0.72
gf = Z.s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(FX), Inches(FY), Inches(FW), Inches(FH), cd)
gf.name = "Säulendiagramm Szenarien"
gf._element.nvGraphicFramePr.cNvPr.set("descr", "Säulendiagramm: Mehr-Anteil bis 2029 in Mio. Euro. Vorsichtig 50, Basis 93, ambitioniert 136; Investition 80 als Linie.")
ch = gf.chart; ch.has_legend = False; ch.has_title = False
ch.font.size = Pt(13); ch.font.name = L; ch.font.color.rgb = rgb(DB)
pl = ch.plots[0]; pl.gap_width = 70; pl.vary_by_categories = False
for i, v in enumerate(sc_val):
    pt = pl.series[0].points[i]; pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(ZB if v >= 80 else FOCUS_LIGHT)
pl.has_data_labels = True
dl = pl.data_labels; dl.number_format = '0'; dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END; dl.font.size = Pt(14); dl.font.name = L; dl.font.color.rgb = rgb(DB)
va = ch.value_axis; va.minimum_scale, va.maximum_scale = 0, 160; va.has_major_gridlines = False; va.visible = False
ca = ch.category_axis; ca.major_tick_mark = XL_TICK_MARK.NONE; ca.format.line.color.rgb = rgb(LB); ca.tick_labels.font.size = Pt(13)
plot_layout(ch, IX, IY, IW, IH); transparent(ch)
ly = FY + FH * (IY + IH * (1 - 80 / 160))
shape(S.RECTANGLE, FX + FW * IX, ly - 0.006, FW * IW, 0.012, fill=DB, name="Linie Investition 80 Mio. €")
text(FX + FW * IX + 0.05, ly - 0.36, 3.2, 0.3, "Investition 80 Mio. €", 13, M, DB)
card(9.15, 1.5, 3.78, 2.15, "dark")
g_target(9.62, 2.05, 0.6)
text(10.1, 1.72, 2.7, 0.75, "1,3 Pp", 40, O, WHITE, "l", "m")
text(9.4, 2.65, 3.3, 0.9, "Break-even: 80 Mio. € geteilt durch 6,2 Mrd. € Marktzuwachs", 14, L, WHITE)
card(9.15, 3.85, 3.78, 2.15, "tint")
g_hourglass(9.62, 4.38, 0.6)
text(10.1, 4.05, 2.7, 0.75, "−30 Mio. €", 30, O, ZB, "l", "m")
text(9.4, 4.95, 3.3, 0.9, "Lücke im vorsichtigen Fall: 50 statt 80 Mio. € Mehr-Anteil", 14, L, DB)
band("EINORDNUNG", "Das Risiko bleibt begrenzt: Große Ausgaben fließen erst nach dem Entscheidungspunkt zum Pilot (Folie 7).", 15)
footer("Beispieldaten, fiktiv. Szenarien sind Fortschreibungen, keine Prognosen. Mehr-Anteil = Pp-Gewinn × 6,2 Mrd. € Marktzuwachs;\nkein Ergebnis.")

# ======================= 6  Zwei Belege (freigegeben) ==================================================
new_slide("Der Anteil wächst klar um 11,5 % pro Jahr, ein Nachlassen des Tempos ist nicht belegt",
          "WARUM DIESE FOLIE: Argument 3 (Verlässlich und machbar?). Zwei Teilaussagen im Titel, also zwei Belege nebeneinander mit je einer Erklärung darunter. "
          "Zugleich das wichtigste Gegenargument: Wer sagt 'Wachstum lässt nach', sieht hier, dass dasselbe Tempo schon im August 2025 vorkam. "
          "Situation: Anteil 28,0 auf 34,5 % in 23 Monaten, jeder Schritt positiv (11,5 % p. a.; Trend 12,0 %; letzte zwölf Monate 10,5 %). "
          "Komplikation: Zuletzt 0,17 statt 0,29 Pp pro Monat. Antwort: Gleich langsam im August 2025, danach 0,41; nur 2 von 21 Fenstern. Fiktive Daten.")
tracker(3, "Verlässlich")
def panel(x, gi, claim, head):
    card(x, 1.5, 6.115, 4.5)
    gi(x + 0.5, 1.9, 0.5)
    text(x + 0.9, 1.72, 5.0, 0.36, claim, 19, M, DB, "l", "m")
    text(x + 0.28, 2.25, 5.6, 0.28, head, 11, M, ZB)
    shape(S.RECTANGLE, x + 0.28, 4.5, 5.55, 0.012, fill="D5E3F2")
def line_chart(x, y, w, h, cats_, vals, vmin, vmax, name, alt):
    cd = CategoryChartData(number_format="0.00"); cd.categories = cats_; cd.add_series(name, [float(v) for v in vals])
    gf = Z.s.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    gf.name = name; gf._element.nvGraphicFramePr.cNvPr.set("descr", alt)
    ch = gf.chart; ch.has_legend = False; ch.has_title = False
    ch.font.size = Pt(12); ch.font.name = L; ch.font.color.rgb = rgb(DB)
    ser = ch.plots[0].series[0]; ser.smooth = False
    ser.format.line.color.rgb = rgb(MB); ser.format.line.width = Pt(2.25)
    ser.marker.style = XL_MARKER_STYLE.CIRCLE; ser.marker.size = 4
    ser.marker.format.fill.solid(); ser.marker.format.fill.fore_color.rgb = rgb(MB); ser.marker.format.line.fill.background()
    va = ch.value_axis; va.minimum_scale, va.maximum_scale = vmin, vmax; va.has_major_gridlines = False
    va.format.line.fill.background(); va.tick_label_position = XL_TICK_LABEL_POSITION.NONE; va.major_tick_mark = XL_TICK_MARK.NONE
    ca = ch.category_axis; ca.format.line.color.rgb = rgb(LB); ca.tick_label_position = XL_TICK_LABEL_POSITION.NONE; ca.major_tick_mark = XL_TICK_MARK.NONE
    IX_, IY_, IW_, IH_ = 0.03, 0.06, 0.94, 0.72
    plot_layout(ch, IX_, IY_, IW_, IH_); transparent(ch)
    n = len(vals); pl_, pw_ = x + w * IX_, w * IW_; pt_, ph_ = y + h * IY_, h * IH_
    return (lambda i: pl_ + pw_ * (i + .5) / n), (lambda v: pt_ + ph_ * (1 - (v - vmin) / (vmax - vmin))), (pl_, pw_)
def xlabels(X, idxs, texts, ybase, xmax):
    for i, tx in zip(idxs, texts): text(min(X(i) - 0.5, xmax - 1.0), ybase, 1.0, 0.26, tx, 12, L, DB, "c")
def disc(cx, cy, dd, col): shape(S.OVAL, cx - dd / 2, cy - dd / 2, dd, dd, fill=col, name="Markierung")
LX, RX = 0.4, 6.815
panel(LX, g_trend, "Das Wachstum ist klar", "ANTEIL AM MARKT, %, NOV 2024 BIS OKT 2026")
X, Y, (pl_, pw_) = line_chart(LX + 0.2, 2.5, 5.75, 1.95, [lab(i) for i in range(24)], sh_ts, 27, 36, "Anteil am Markt, %",
    "Liniendiagramm: Anteil am Markt von 28,0 % im Nov 2024 auf 34,5 % im Okt 2026, jeder Monatsschritt positiv.")
xlabels(X, [0, 6, 12, 18, 23], [lab(i) for i in (0, 6, 12, 18, 23)], 4.07, LX + 6.115 - 0.12)
disc(X(0), Y(sh_ts[0]), 0.17, ZB); disc(X(23), Y(sh_ts[23]), 0.17, ZB)
text(X(0) - 0.05, Y(sh_ts[0]) - 0.38, 0.9, 0.28, de(sh_ts[0], 1), 14, M, DB)
text(X(23) - 0.85, Y(sh_ts[23]) - 0.38, 0.9, 0.28, de(sh_ts[23], 1), 14, M, DB, "r")
pill(X(1), Y(35.2), 1.95, "+11,5 % pro Jahr", ZB, WHITE, h=0.34, size=13)
text(LX + 0.28, 4.6, 5.55, 1.3, f"In 23 Monaten stieg der Anteil von 28,0 auf 34,5 %, jeder Monatsschritt zeigt nach oben. "
     f"Trend über alle 24 Monate: {de(trend * 100, 1)} %, letzte zwölf Monate allein: {de(last12 * 100, 1)} %.", 14, L, DB)
panel(RX, g_hourglass, "Ein Nachlassen ist nicht belegt", "TEMPO, PP PRO MONAT, GLEITENDER DREIMONATSSCHNITT")
X, Y, (pl_, pw_) = line_chart(RX + 0.2, 2.5, 5.75, 1.95, [lab(i + 3) for i in range(21)], pace, 0.04, 0.50, "Tempo, Pp pro Monat",
    "Liniendiagramm: Tempo in Pp pro Monat, 21 Dreimonatsfenster. Tiefstwerte 0,17 im Aug 2025 und Okt 2026, Höchstwert 0,41 im Nov 2025.")
xlabels(X, [0, 6, 12, 20], [lab(i + 3) for i in (0, 6, 12, 20)], 4.07, RX + 6.115 - 0.12)
dash(pl_, Y(.17), pl_ + pw_, Y(.17))
for i in LOW: disc(X(i), Y(pace[i]), 0.17, DB)
disc(X(PEAK), Y(pace[PEAK]), 0.15, ZB)
text(X(LOW[0]) - 0.9, Y(.17) + 0.14, 1.8, 0.26, "Aug 2025 · 0,17", 12, M, DB, "c")
text(X(LOW[1]) - 1.8, Y(.17) + 0.14, 1.9, 0.26, "Okt 2026 · 0,17", 12, M, DB, "r")
text(X(PEAK) - 0.2, Y(pace[PEAK]) - 0.36, 1.6, 0.26, f"danach {de(pace[PEAK], 2)}", 12, M, ZB)
text(RX + 0.28, 4.6, 5.55, 1.3, f"Zuletzt stieg der Anteil um 0,17 statt im Schnitt {de(pace.mean(), 2)} Pp pro Monat. "
     f"Genauso langsam war es schon im August 2025, danach lag das Tempo bei {de(pace[PEAK], 2)}. Nur 2 von 21 Fenstern sind so niedrig.", 14, L, DB)
band("WIR EMPFEHLEN", "Vor einer Skalierung die Datenbasis prüfen und das Tempo weiter monatlich beobachten.")
footer("Fiktive Daten. Pp = Prozentpunkte; Wachstum = relatives Wachstum des Anteils (23 Monate = 1,92 Jahre);\nFenster = Schnitt von drei Monatsschritten. Beschriftung der Fenster = Endmonat.")

# ======================= 7  Fahrplan mit Entscheidungspunkten und Tranchen =============================
new_slide("Vor jeder Ausgabe steht ein Entscheidungspunkt, bis zur Ausweitung sind erst 12,5 % der 80 Mio. € gebunden",
          "WARUM DIESE FOLIE: Argument 3 (Machbar). Betrachteraufgabe: einen Ablauf verstehen, also Phasen, Entscheidungspunkte und Geld in einer Zeitleiste. "
          "Die Budgetzeile belegt den Titel: 2 + 8 = 10 Mio. € sind vor dem dritten Entscheidungspunkt gebunden, das sind 12,5 % von 80. "
          "Raute = Entscheidungspunkt, Pfeil = Phase. Die Tranchen (2, 8, 40, 30) sind fiktive Annahmen.")
tracker(3, "Verlässlich")
LBLW = 1.55; colw = (12.53 - LBLW - 3 * 0.1) / 4
xs = [0.4 + LBLW + i * (colw + 0.1) for i in range(4)]
shades = [LB, MB, ZB, DB]
gl = [g_check, g_flask, g_gear1, g_trend]
what = ["Erhebung und Monatswerte prüfen", "Fabric- und Databricks-Dataset in einem Segment testen", "Cyber, Gesundheit, Logistik anbinden", "Budget an Jahreswerten ausrichten"]
res = ["Belastbare Datenbasis", "Messbarer Anteilsgewinn", "Drei Segmente live", "Steuerung im Regelbetrieb"]
gate = ["Erhebung belastbar?", "Gewinn über Zufall?", "Ertrag je Euro hält?", "Dauerbetrieb freigeben?"]
for i, x in enumerate(xs):
    shape(S.PENTAGON, x, 1.5, colw + (0.1 if i < 3 else 0), 0.9, fill=shades[i])
    dk = i == 0
    text(x + 0.22, 1.58, colw - 0.9, 0.25, PH[i][1].upper(), 11, M, DB if dk else WHITE, spacing=100)
    text(x + 0.22, 1.83, colw - 0.6, 0.55, PH[i][0], 14, M, DB if dk else WHITE)
LANES = [("Was passiert", 2.5), ("Ergebnis", 3.5), ("Entscheidung", 4.3), ("Freigabe, Mio. €", 5.1)]
for lb_, y in LANES:
    shape(S.RECTANGLE, 0.4, y, 12.53, 0.01, fill="D5E3F2")
    text(0.4, y + 0.12, LBLW - 0.15, 0.3, lb_, 13, M, ZB)
for i, x in enumerate(xs):
    gl[i](x + 0.34, 3.0, 0.46)
    text(x + 0.7, 2.66, colw - 0.75, 0.8, what[i], 13, L, DB)
    text(x + 0.2, 3.66, colw - 0.3, 0.6, res[i], 14, M, DB)
    shape(S.DIAMOND, x + 0.2, 4.45, 0.32, 0.32, fill=DB, name=f"Entscheidungspunkt {i + 1}", alt=f"Entscheidungspunkt vor Phase {i + 1}")
    text(x + 0.62, 4.4, colw - 0.7, 0.45, gate[i], 13, M, DB, "l", "m")
    amt = PH[i][2]; wbar = (colw - 1.1) * amt / 40
    shape(S.RECTANGLE, x + 0.2, 5.28, max(wbar, 0.05), 0.28, fill=DB if i < 2 else ZB)
    text(x + 0.3 + max(wbar, 0.05), 5.26, 1.0, 0.32, f"{amt}", 15, M, DB, "l", "m")
bx0, bx1 = xs[0] + 0.2, xs[1] + colw - 0.2
shape(S.RECTANGLE, bx0, 5.68, bx1 - bx0, 0.02, fill=DB); shape(S.RECTANGLE, bx0, 5.68, 0.02, 0.1, fill=DB); shape(S.RECTANGLE, bx1 - 0.02, 5.68, 0.02, 0.1, fill=DB)
text(bx0, 5.76, bx1 - bx0, 0.24, "10 Mio. € = 12,5 % bis zur Ausweitung", 12, M, DB, "c")
band("EINORDNUNG", "Ein bestandener Entscheidungspunkt gibt jeweils nur die nächste Tranche frei.")
footer("Beispieldaten, fiktiv. Tranchen 2, 8, 40 und 30 Mio. € sind Annahmen. Rauten = Entscheidungspunkte.")

# ======================= 8  Entscheidung ===============================================================
new_slide("Wir bitten um drei Entscheidungen, damit der Pilot im ersten Quartal startet",
          "WARUM DIESE FOLIE: Das Deck endet mit der Entscheidung: was, wer, bis wann. Jede Karte entspricht einem Argument. "
          "Entscheider und Termin sind nicht bekannt und stehen als [DATA NEEDED]. Fiktive Daten.", dark=True)
asks = [(g_gear1, "80 Mio. € in Tranchen freigeben", "Option B für Gesundheit, Cyber und Logistik, ausgezahlt in vier Tranchen von 2 bis 40 Mio. €", "80 Mio. €", "Rahmen 2027 bis 2029"),
        (g_check, "Entscheidungspunkt 1 festlegen", "Vor dem Pilot prüfen wir, ob die Erhebung belastbar ist", "Q1 2027", "Pilot nur bei bestandener Prüfung"),
        (g_hourglass, "Das Tempo weiter beobachten", "Bei Bestätigung des Rückgangs bewerten wir neu, vor der Ausweitung", "2 von 21", "Fenster so langsam wie zuletzt")]
cw3 = (12.53 - 2 * 0.25) / 3
for i, (g, t_, d_, big, cap) in enumerate(asks):
    x = 0.4 + i * (cw3 + 0.25)
    shape(S.ROUNDED_RECTANGLE, x, 1.6, cw3, 4.45, fill=ZB, rad=0.14)
    shape(S.OVAL, x + 0.3, 1.88, 0.5, 0.5, fill=WHITE); text(x + 0.3, 1.88, 0.5, 0.5, str(i + 1), 18, M, ZB, "c", "m")
    g(x + cw3 - 0.75, 2.13, 0.8)
    text(x + 0.3, 2.7, cw3 - 0.6, 0.75, t_, 20, M, WHITE)
    text(x + 0.3, 3.45, cw3 - 0.6, 0.9, d_, 14, L, WHITE)
    shape(S.RECTANGLE, x + 0.3, 4.4, cw3 - 0.6, 0.015, fill=WHITE)
    text(x + 0.3, 4.52, cw3 - 0.6, 0.8, big, 40, O, WHITE, "l", "m")
    text(x + 0.3, 5.4, cw3 - 0.6, 0.3, cap, 12, M, WHITE)
text(0.4, 6.35, 12.0, 0.3, "Entscheider und Termin: [DATA NEEDED: Gremium und Termin der Entscheidung]", 15, M, WHITE)
footer("Beispieldaten, fiktiv. Pp = Prozentpunkte. Tranchen siehe Folie 7.")

# ======================= 9  Anhang: Der rote Faden =====================================================
new_slide("Jede Folie belegt ein Argument, und die drei Argumente tragen die Kernaussage",
          "LERNFOLIE: So ist das Deck gebaut (Pyramidenprinzip). Oben die Kernaussage, darunter drei Argumente, darunter die Folien, die sie belegen. "
          "Folie 2 gibt die Antwort zuerst, Folie 8 bittet um die Entscheidung. Die Frage oben ist die Komplikation aus der Ausgangslage.")
tracker("A", "Anhang")
text(0.4, 1.45, 12.5, 0.3, "Frage: Wo setzen wir Geld ein, und können wir den Daten trauen?", 14, M, ZB, "c")
shape(S.ROUNDED_RECTANGLE, 1.9, 1.85, 9.53, 0.95, fill=DB)
text(2.2, 1.85, 8.9, 0.95, "Kernaussage: 80 Mio. € auf drei Segmente, weil Markt, Rechnung und Datenbasis dafür sprechen", 19, M, WHITE, "l", "m")
AW = 3.95; AG = 0.34; ax = [0.4 + i * (AW + AG) for i in range(3)]
shape(S.RECTANGLE, 6.665 - 0.007, 2.8, 0.014, 0.2, fill=DB)
shape(S.RECTANGLE, ax[0] + AW / 2, 3.0, ax[2] - ax[0], 0.014, fill=DB)
for x in ax: shape(S.RECTANGLE, x + AW / 2 - 0.007, 3.0, 0.014, 0.2, fill=DB)
args = [(g_trend, "1  Warum dort?", "Der Markt wächst dort am stärksten", [("Folie 3", "Dreispalter: wächst, Anteil, Wert")]),
        (g_scales, "2  Lohnt es sich?", "Die Rechnung geht auf", [("Folie 4", "Optionen: Matrix, Beitrag je Euro"), ("Folie 5", "Szenarien: Schwelle bei 1,3 Pp")]),
        (g_check, "3  Verlässlich und machbar?", "Die Daten tragen, der Weg ist gestuft", [("Folie 6", "Zwei Belege: Wachstum, Tempo"), ("Folie 7", "Fahrplan mit Entscheidungspunkten")])]
for x, (gi, h_, cl, sl) in zip(ax, args):
    shape(S.ROUNDED_RECTANGLE, x, 3.2, AW, 1.0, fill=ZB, rad=0.1)
    gi(x + 0.55, 3.7, 0.6)
    text(x + 1.0, 3.3, AW - 1.1, 0.3, h_, 14, M, WHITE)
    text(x + 1.0, 3.62, AW - 1.1, 0.5, cl, 13, L, WHITE)
    for k, (fo, ds) in enumerate(sl):
        yy = 4.4 + k * 0.7
        shape(S.ROUNDED_RECTANGLE, x, yy, AW, 0.6, fill=LB, alpha=30, rad=0.08)
        text(x + 0.2, yy, 0.9, 0.6, fo, 13, M, ZB, "l", "m")
        text(x + 1.1, yy, AW - 1.2, 0.6, ds, 13, L, DB, "l", "m")
rich(0.4, 5.95, 12.5, 0.4, [("Folie 2", True), (" gibt die Antwort zuerst, ", False), ("Folie 8", True), (" bittet um die Entscheidung, alles dazwischen belegt ein Argument.", False)], 15)
footer("Lernfolie zur Methode (Methode_Deck_bauen.md): Kernaussage, drei Argumente, Folien als Belege.")

# ======================= 10  Anhang: Segmentdaten ======================================================
new_slide("Ein Prozentpunkt Anteil ist in Gesundheit 24 Mio. € wert, in Gastro nur 2 Mio. €",
          "ANHANG: Beleg auf Nachfrage. Betrachteraufgabe: exakte Werte nachschlagen, also eine Tabelle. Wert von 1 Pp = Marktzuwachs × 1 %. Fiktive Daten.")
tracker("A", "Anhang")
gt = Z.s.shapes.add_table(9, 4, Inches(0.4), Inches(1.5), Inches(12.53), Inches(4.4))
gt.name = "Tabelle Segmentdaten"; tbl = gt.table; tbl.first_row = True
for j, w in enumerate((3.4, 3.1, 3.0, 3.03)): tbl.columns[j].width = Inches(w)
tbl.rows[0].height = Inches(0.52)
for i in range(1, 9): tbl.rows[i].height = Inches(0.485)
def setc(c, t, size, font, color, fill, align):
    c.fill.solid(); c.fill.fore_color.rgb = rgb(fill)
    c.margin_left = c.margin_right = Inches(0.15); c.margin_top = c.margin_bottom = Inches(0.03)
    c.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = c.text_frame.paragraphs[0]; p.alignment = {"l": PP_ALIGN.LEFT, "r": PP_ALIGN.RIGHT}[align]
    r = p.add_run(); r.text = t; r.font.size = Pt(size); r.font.name = font; r.font.color.rgb = rgb(color)
for j, h_ in enumerate(["Segment", "Marktzuwachs 2026 bis 2029, Mrd. €", "Unser Marktanteil, %", "Wert von 1 Pp, Mio. €"]):
    setc(tbl.cell(0, j), h_, 13, M, WHITE, DB, "l" if j == 0 else "r")
for i in range(8):
    fill = "DCEAF6" if i < F else WHITE
    for j, v in enumerate((cats[i], de(grow[i]), de(share[i]), str(worth[i]))):
        setc(tbl.cell(i + 1, j), v, 14, M if (j == 0 and i < F) else L, DB, fill, "l" if j == 0 else "r")
band("EINORDNUNG", "Die drei Fokus-Segmente sind je Prozentpunkt 62 Mio. € wert, die übrigen fünf zusammen 28 Mio. €.", 15)
footer("Beispieldaten, fiktiv. Wert von 1 Pp = Marktzuwachs × 1 %. Pp = Prozentpunkte.")

# ======================= 11  Anhang: Annahmen ==========================================================
new_slide("Alle Werte folgen aus sechs Annahmen, die wir offenlegen",
          "ANHANG: Methode. Betrachteraufgabe: die Herleitung prüfen. Strukturierte Textfolie, jede Annahme in einer Zeile. Fiktive Daten.")
tracker("A", "Anhang")
ass = [("Marktzuwachs", "Zuwachs je Segment 2026 bis 2029, Summe 9,0 Mrd. €, davon 6,2 Mrd. € in den drei Fokus-Segmenten."),
       ("Marktanteil", "Durchschnitt je Gruppe, gewichtet nach Marktzuwachs: Fokus 2,1 %, übrige fünf 3,5 %."),
       ("Mehr-Anteil", "Pp-Gewinn × Marktzuwachs. Option A: +0,5 Pp auf 9,0 Mrd. €; Option B: +1,5 Pp auf 6,2 Mrd. €. Kein Ergebnis."),
       ("Szenarien", "Fortschreibung des Pp-Gewinns (+0,8, +1,5, +2,2 Pp), keine Prognose. Break-even bei 80 Mio. €: 1,3 Pp."),
       ("Wachstumsrate", "Relatives Wachstum des Anteils (28,0 auf 34,5 % in 23 Monaten = 1,92 Jahre); Spanne = Trend und letzte zwölf Monate."),
       ("Tranchen", "Aufteilung der 80 Mio. € auf vier Phasen (2, 8, 40, 30 Mio. €) ist eine Annahme für dieses Beispiel.")]
for i, (k, v) in enumerate(ass):
    y = 1.5 + i * 0.78
    card(0.4, y, 12.53, 0.68, "tint")
    shape(S.OVAL, 0.6, y + 0.16, 0.36, 0.36, fill=DB); text(0.6, y + 0.16, 0.36, 0.36, str(i + 1), 13, M, WHITE, "c", "m")
    text(1.2, y, 2.4, 0.68, k, 16, M, DB, "l", "m")
    text(3.7, y, 9.1, 0.68, v, 13, L, DB, "l", "m")
footer("Beispieldaten, fiktiv. Pp = Prozentpunkte.")
prs.save(sys.argv[1])
