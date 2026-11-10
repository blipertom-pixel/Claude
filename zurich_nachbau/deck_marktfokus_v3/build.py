# -*- coding: utf-8 -*-
"""Marktfokus v3: Vorstands-Deck nach skill_v2 (Storyline -> Ghost Deck -> Modell -> Archetypen -> Partner-Review). Fiktive Daten."""
import sys
sys.path.insert(0, "../skill_v2/scripts")
import numpy as np
import deck_lite as D
from deck_lite import de, S, X0, W
import modell as Mo

D.new_deck()
ZB, DB, LB, MB, WH, CONTEXT = D.ZB, D.DB, D.LB, D.MB, D.WHITE, D.CONTEXT
pct = lambda v, n=1: de(v, n) + " %"

# =========================== 1 Titel ===========================================================================
D.slide("Wo der Markt am stärksten wächst, setzen wir 80 Mio. € ein",
        "THESE in einem Satz. Zweck: Der Vorstand soll 80 Mio. € Rahmen für drei Wachstumssegmente beschließen und 10 Mio. € sofort freigeben. "
        "Alle Zahlen sind fiktive Beispieldaten aus einem Modell (modell.py). Lernhinweis: Aufbau und Gründe je Folie stehen in den Notizen.", dark=True, hero=True)
for dd, a in [(5.2, 12), (4.0, 16), (2.8, 22)]:
    D.shape(S.DONUT, 13.333 - dd * 0.62, 7.5 - dd * 0.62, dd, dd, fill=LB, alpha=a).adjustments[0] = 0.1
D.hero_title("Wo der Markt am stärksten wächst,\nsetzen wir 80 Mio. € ein", "Vorlage für den Vorstand\nMarktfokus Gewerbe 2027 bis 2029  ·  10. November 2026")
D.text(X0, D.FOOT_Y, 9, 0.3, "Beispieldaten, fiktiv.", 12, D.L, WH)

# =========================== 2 Antwort zuerst ==================================================================
D.slide("Wir empfehlen 80 Mio. € für drei Wachstumssegmente, zurückverdient 2031, freigegeben in Stufen",
        "ANTWORT ZUERST (Pyramide). Drei Argumente, überschneidungsfrei: Chance, Ertrag, Risiko. Jede Zeile = Behauptung + Satz mit Zahlen + Vergleichspaar als Beleg. "
        "Situation: Der Gewerbemarkt wächst bis 2029 von 45 auf 54 Mrd. €. Komplikation: 69 % des Zuwachses liegen in drei Segmenten, in denen unser Anteil am kleinsten ist; ohne Kurswechsel sinkt unser Gesamtanteil. "
        "Frage: Sollen wir gezielt investieren, und lohnt es sich? Antwort: ja, 80 Mio. € in Tranchen, zurückverdient 2031.")
rows = [("chart-line-up", "Der Markt wächst dort am stärksten",
         [("Gesundheit, Cyber und Logistik liefern ", False), (pct(Mo.F_dz / 9 * 100, 0), True), (" des Marktzuwachses, unser Anteil liegt dort bei nur ", False), (pct(Mo.F_sh), True), (".", False)], "Folie 3 und 4"),
        ("coins", "Der Fokus verdient schneller zurück",
         [("Ab 2029 ", False), (de(Mo.RUN_B) + " Mio. €", True), (" Ergebnis pro Jahr, zurückverdient ", False), (str(Mo.PB_B), True), ("; die breite Streuung erst ", False), (str(Mo.PB_A), True), (".", False)], "Folie 5 und 6"),
        ("shield-check", "Das Risiko ist gestuft",
         [("Vor dem Pilotergebnis fließen nur ", False), ("10 Mio. €", True), (". Vorher prüfen wir die Befragung, die ", False), (f"{Mo.SMOOTH:.0f}-mal", True), (" zu glatt ist.", False)], "Folie 7 und 8")]
RY = [1.55, 3.05, 4.55]
for i, (ic, cl, parts, ref) in enumerate(rows):
    y = RY[i]
    if i: D.rule(X0, y - 0.1, W)
    D.icon(ic, X0 + 0.42, y + 0.6, 0.78)
    D.text(X0 + 1.05, y + 0.05, 5.1, 0.4, cl, 19, D.M, DB)
    D.rich(X0 + 1.05, y + 0.5, 5.0, 0.75, parts, 14)
    D.text(X0 + 1.05, y + 1.1, 3, 0.22, ref, 11, D.M, ZB)
cx = 7.0
D.compare_bars(cx, RY[0] + 0.05, "WACHSTUM P. A., %", [("Fokus (3)", Mo.F_g * 100, ZB), ("übrige (5)", Mo.R_g * 100, CONTEXT)], 13.0, 0.95, 1.4)
D.compare_bars(cx + 3.0, RY[0] + 0.05, "UNSER ANTEIL 2026, %", [("Fokus (3)", Mo.F_sh, ZB), ("übrige (5)", Mo.R_sh, CONTEXT)], 3.5, 0.95, 1.4)
D.compare_bars(cx, RY[1] + 0.05, "ERGEBNIS AB 2029, MIO. € P. A.", [("Fokus", Mo.RUN_B, ZB), ("breit", Mo.RUN_A, CONTEXT)], 21.8, 0.75, 1.6)
D.compare_bars(cx + 3.0, RY[1] + 0.05, "INVESTITION, MIO. €", [("Fokus", 80, ZB), ("breit", 140, CONTEXT)], 140, 0.75, 1.6, fmt=lambda v: f"{v:.0f}")
D.text(cx, RY[2] + 0.05, 5.5, 0.22, "TRANCHEN, MIO. € (RAHMEN 80)", 11, D.M, ZB, spacing=30)
tx = cx; tw = 5.6
for k, (_, _, amt) in enumerate(Mo.PH):
    wseg = tw * amt / 80
    D.shape(S.RECTANGLE, tx, RY[2] + 0.4, wseg - 0.03, 0.3, fill=DB if k < 2 else CONTEXT)
    if amt >= 30: D.text(tx, RY[2] + 0.4, wseg - 0.03, 0.3, str(amt), 12, D.M, DB, "c", "m")
    tx += wseg
bx1 = cx + tw * 10 / 80
D.rule(cx, RY[2] + 0.8, bx1 - cx, DB, 0.02); D.shape(S.RECTANGLE, cx, RY[2] + 0.72, 0.02, 0.1, fill=DB); D.shape(S.RECTANGLE, bx1 - 0.02, RY[2] + 0.72, 0.02, 0.1, fill=DB)
D.text(bx1 + 0.1, RY[2] + 0.68, 3.5, 0.26, "10 Mio. € vor dem Pilotergebnis", 11, D.M, DB)
D.band("WIR BITTEN UM", "80 Mio. € Rahmen und 10 Mio. € sofort für Datenprüfung und Pilot in Cyber.")
D.footer("Beispieldaten, fiktiv. Ergebnis = zusätzliche Prämie × Marge; Fokus = Gesundheit, Cyber, Logistik. Belege auf Folie 3 bis 8.")

# =========================== 3 Markt: Dreispalter ==============================================================
D.slide(f"Drei Segmente liefern {Mo.F_dz / 9 * 100:.0f} % des Marktwachstums, genau dort ist unser Anteil am kleinsten",
        "ARGUMENT 1 (Chance). Drei Teilaussagen im Titel (liefern das Wachstum, wachsen schnell, unser Anteil klein) = drei Belege über dieselben acht Segmente. "
        "Die Hervorhebung läuft quer durch alle Spalten. Das Band nennt die Konsequenz, die der Titel nicht sagt: Ohne Kurswechsel sinkt unser Gesamtanteil.", tracker_=(1, "Chance"))
C3 = D.cols(3)
CY, CH = 2.55, 2.45
rowh = CH / 8
D.shape(S.ROUNDED_RECTANGLE, X0, CY - 0.02, W, 3 * rowh + 0.04, fill=LB, alpha=30, rad=0.08, name="Fokus-Zone")
spec = [("chart-line-up", "Marktzuwachs", "Zusätzliche Bruttoprämie 2026 bis 2029, Mrd. €", list(Mo.dz), 3.0, lambda v: de(v),
         [("Gesundheit, Cyber und Logistik liefern ", False), ("6,2 von 9,0 Mrd. €", True), (" des Zuwachses (69\u00a0%).", False)]),
        ("trend-up", "Wachstum pro Jahr", "Wachstum 2026 bis 2029, % pro Jahr", list(Mo.g * 100), 25, lambda v: de(v),
         [("Die drei wachsen mit ", False), (pct(Mo.F_g * 100), True), (" pro Jahr, die übrigen fünf mit ", False), (pct(Mo.R_g * 100), True), (".", False)]),
        ("chart-pie-slice", "Unser Marktanteil", "Unser Anteil am Segment 2026, %", list(Mo.sh), 5.0, lambda v: de(v),
         [("Unser Anteil liegt dort bei ", False), (pct(Mo.F_sh), True), (", in den übrigen fünf bei ", False), (pct(Mo.R_sh), True), (".", False)])]
for k, ((x, w), (ic, hd, desc, vals, vmax, lf, take)) in enumerate(zip(C3, spec)):
    D.shape(S.ROUNDED_RECTANGLE, x, 1.45, w, 0.46, fill=DB, rad=0.08)
    D.icon(ic, x + 0.3, 1.68, 0.34, disc_=False, on_dark=True)
    D.text(x + 0.6, 1.45, w - 0.7, 0.46, hd, 15, D.M, WH, "l", "m")
    D.text(x + 0.05, 1.98, w - 0.1, 0.5, desc, 12, D.L, DB)
    D.bars_h(x, CY, w, CH, Mo.SEG, vals, Mo.FOKUS, vmax, lf, show_cats=(k == 0), cat_w=1.2, alt=f"Balkendiagramm {hd}: {desc}")
    D.rich(x + 0.05, 5.12, w - 0.1, 0.9, take, 14)
D.band("KONSEQUENZ", f"Ohne Kurswechsel sinkt unser Gesamtanteil bis 2029 von {de(Mo.share26)} auf {de(Mo.share29_base)} %.", 16)
D.footer("Beispieldaten, fiktiv. Marktvolumen Gewerbe (Bruttoprämie): 45,0 Mrd. € (2026), 54,0 Mrd. € (2029). Anteile gewichtet nach Marktvolumen.")

# =========================== 4 Nachfrage: zwei Belege ==========================================================
D.slide(f"Die Nachfrage wächst klar um {de(Mo.dem_growth * 100)} % pro Jahr, ein Nachlassen des Tempos ist nicht belegt",
        "ARGUMENT 1 (Chance), zweiter Beleg: Kundennachfrage. Zwei Teilaussagen = zwei Belege mit Erklärung darunter. "
        f"Anteil der befragten Gewerbekunden in den Fokus-Segmenten, die Schutz anfragen oder planen: 28,0 auf 34,5 % in 23 Monaten ({de(Mo.dem_growth * 100)} % p. a.; Trend {de(Mo.dem_trend * 100)} %; letzte zwölf Monate {de(Mo.dem_last12 * 100)} %). "
        "Tempo zuletzt 0,17 statt 0,29 Pp pro Monat, genauso niedrig schon im Aug 2025, danach 0,41. Das Band leitet zum Risiko über (Folie 7).", tracker_=(1, "Chance"))
(LX, LW), (RX, RW) = D.cols(2, gap=0.5)
D.vrule(X0 + W / 2, 1.5, 4.35)
D.claim(LX, 1.45, LW, "Das Wachstum ist klar", "trend-up")
D.header(LX, 2.0, LW, "KUNDEN MIT SCHUTZBEDARF, % DER BEFRAGTEN")
X, Y, (pl, pw, pb) = D.lines(LX, 2.42, LW, 1.85, [f"m{i}" for i in range(24)], [("Nachfrage, %", Mo.dem, MB, 2.25)], 27, 36,
                            alt="Liniendiagramm: Anteil der befragten Gewerbekunden mit Schutzbedarf, 28,0 % (Nov 2024) bis 34,5 % (Okt 2026), jeder Monat höher.")
lab = lambda idx: f"{['Jan','Feb','Mär','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez'][(10 + idx) % 12]} {str(2024 + (10 + idx) // 12)[2:]}"
D.xlabels(X, [0, 6, 12, 18, 23], [lab(i) for i in (0, 6, 12, 18, 23)], pb + 0.06, xmax=LX + LW)
D.disc(X(0), Y(Mo.dem[0]), 0.16, ZB); D.disc(X(23), Y(Mo.dem[23]), 0.16, ZB)
D.text(X(0) - 0.05, Y(Mo.dem[0]) - 0.36, 0.8, 0.26, de(Mo.dem[0]), 14, D.M, DB)
D.text(X(23) - 0.8, Y(Mo.dem[23]) - 0.36, 0.8, 0.26, de(Mo.dem[23]), 14, D.M, DB, "r")
D.pill(X(1), Y(35.3), 1.95, f"+{de(Mo.dem_growth * 100)} % pro Jahr", ZB, WH, h=0.32, size=12)
D.rich(LX, 4.65, LW, 1.3, [("In 23 Monaten von 28,0 auf 34,5 %, ", False), ("jeder Monat höher", True), (f". Trend über alle 24 Monate {pct(Mo.dem_trend * 100)}, letzte zwölf Monate {pct(Mo.dem_last12 * 100)}.", False)], 14)
D.claim(RX, 1.45, RW, "Ein Nachlassen ist nicht belegt", "hourglass")
D.header(RX, 2.0, RW, "TEMPO, PP PRO MONAT, DREIMONATSSCHNITT")
X, Y, (pl, pw, pb) = D.lines(RX, 2.42, RW, 1.85, [f"w{i}" for i in range(21)], [("Tempo, Pp", Mo.pace, MB, 2.25)], 0.04, 0.5,
                            alt="Liniendiagramm: Tempo in Pp pro Monat, 21 Dreimonatsfenster; Tiefstwerte 0,17 im Aug 2025 und Okt 2026, Höchstwert 0,41 im Nov 2025.")
D.xlabels(X, [0, 6, 12, 20], [lab(i + 3) for i in (0, 6, 12, 20)], pb + 0.06, xmax=RX + RW)
D.dash(pl, Y(0.17), pl + pw, Y(0.17))
for i in (6, 20): D.disc(X(i), Y(Mo.pace[i]), 0.16, DB)
pk = int(np.argmax(Mo.pace)); D.disc(X(pk), Y(Mo.pace[pk]), 0.14, ZB)
D.text(X(6) - 0.9, Y(0.17) + 0.1, 1.8, 0.26, "Aug 25 · 0,17", 12, D.M, DB, "c")
D.text(X(20) - 1.75, Y(0.17) + 0.1, 1.8, 0.26, "Okt 26 · 0,17", 12, D.M, DB, "r")
D.text(X(pk) - 0.2, Y(Mo.pace[pk]) - 0.34, 1.6, 0.26, f"danach {de(Mo.pace[pk], 2)}", 12, D.M, ZB)
D.rich(RX, 4.65, RW, 1.3, [("Zuletzt 0,17 statt im Schnitt ", False), (de(Mo.pace.mean(), 2) + " Pp", True), (" pro Monat. Genauso langsam war es schon im August 2025, danach 0,41. ", False), ("Nur 2 von 21", True), (" Fenstern sind so niedrig.", False)], 14)
D.band("ABER", "Die Befragung ist auffällig glatt. Bevor wir auf Monatswerte steuern, prüfen wir sie (Folie 7).", 15)
D.footer("Fiktive Daten. Monatliche Befragung von 1.200 Gewerbekunden in den Fokus-Segmenten. Pp = Prozentpunkte;\nFenster = Schnitt von drei Monatsschritten, beschriftet mit dem Endmonat.")

# =========================== 5 Business Case ==================================================================
D.slide(f"Der Fokus ist {Mo.PB_B} zurückverdient, die breite Streuung trotz 140 Mio. € Einsatz erst {Mo.PB_A}",
        "ARGUMENT 2 (Ertrag). Ob sich etwas rechnet, zeigt der kumulierte Ergebnisbeitrag nach Investition, nicht das Prämienvolumen (Fehler der Vorversion). "
        "Kurve: Investition je Tranche, Ergebnis = zusätzliche Prämie × Marge. Fokus: +0,9 Pp auf 20,2 Mrd. € (2029) = 182 Mio. € Prämie, Marge 12 % = 21,8 Mio. € pro Jahr. "
        "Breit: +0,3 Pp auf 54,0 Mrd. € = 162 Mio. €, Marge 7 % = 11,3 Mio. €. Tiefster Punkt Fokus 2029: −40,5 Mio. €.", tracker_=(2, "Ertrag"))
(LX, LW), (RX, RW) = D.split(8.2)
D.header(LX, 1.5, LW, "KUMULIERTES ERGEBNIS NACH INVESTITION, MIO. €", "coins")
yrs = [str(y) for y in Mo.YEARS]
cumA = [r["cum"] for r in Mo.CA]; cumB = [r["cum"] for r in Mo.CB]
X, Y, (pl, pw, pb) = D.lines(LX, 2.0, LW, 3.75, yrs, [("Fokus", cumB, ZB, 3.25), ("Breit", cumA, LB, 2.5)], -130, 110, inner=(0.02, 0.05, 0.84, 0.86),
                            alt="Liniendiagramm: kumuliertes Ergebnis nach Investition 2027 bis 2035. Fokus: Tiefpunkt −40,5 Mio. € 2029, positiv ab 2031, +90 Mio. € 2035. Breit: −118,7 Mio. € 2029, −50,7 Mio. € 2035.")
D.dash(pl, Y(0), pl + pw, Y(0), DB, 1.0)
D.text(X(4) - 0.2, Y(0) + 0.05, 2.4, 0.26, "0 = Investition zurückverdient", 11, D.L, DB)
for i, yv in enumerate(yrs):
    if i % 2 == 0 or i == len(yrs) - 1: D.text(X(i) - 0.4, pb + 0.06, 0.8, 0.26, yv, 12, D.L, DB, "c")
D.text(X(8) + 0.12, Y(cumB[-1]) - 0.15, 1.25, 0.3, f"Fokus +{de(cumB[-1], 0)}", 13, D.M, ZB)
D.text(X(8) + 0.12, Y(cumA[-1]) - 0.15, 1.25, 0.3, f"Breit {de(cumA[-1], 0)}", 13, D.M, DB)
ib = Mo.YEARS.index(Mo.PB_B); D.disc(X(ib), Y(cumB[ib]), 0.18, ZB)
D.text(X(ib) - 0.95, Y(cumB[ib]) - 0.62, 1.9, 0.3, f"{Mo.PB_B}: zurückverdient", 13, D.M, ZB, "c")
it = 2; D.disc(X(it), Y(cumB[it]), 0.14, ZB)
D.text(X(it) - 0.9, Y(cumB[it]) + 0.12, 1.8, 0.28, f"Tiefpunkt {de(cumB[it])}", 12, D.M, DB, "c")
D.card(RX, 1.5, RW, 2.1, "dark")
D.icon("coins", RX + 0.5, 2.05, 0.6, on_dark=True)
D.text(RX + 0.95, 1.7, RW - 1.1, 0.75, str(Mo.PB_B), 44, D.O, WH, "l", "m")
D.text(RX + 0.3, 2.62, RW - 0.5, 0.9, f"Fokus zurückverdient; ab 2029 {de(Mo.RUN_B)} Mio. € Ergebnis pro Jahr aus 80 Mio. € Einsatz", 14, D.L, WH)
D.card(RX, 3.8, RW, 2.1, "tint")
D.icon("hourglass", RX + 0.5, 4.35, 0.6)
D.text(RX + 0.95, 4.0, RW - 1.1, 0.75, str(Mo.PB_A), 44, D.O, ZB, "l", "m")
D.text(RX + 0.3, 4.92, RW - 0.5, 0.9, f"breite Streuung: {de(Mo.RUN_A)} Mio. € pro Jahr aus 140 Mio. € Einsatz", 14, D.L, DB)
D.takeaway(f"Am Tiefpunkt 2029 sind netto {de(-Mo.TROUGH_B)} Mio. € gebunden, danach trägt der Fokus {de(Mo.RUN_B)} Mio. € pro Jahr.", size=17)
D.footer("Beispieldaten, fiktiv. Ergebnis = zusätzliche Prämie × Marge (Fokus 12 %, breit 7 %); Anteilsgewinn +0,9 bzw. +0,3 Pp,\nHochlauf 30/65/100 %, ab 2030 konstant ohne weiteres Marktwachstum (vorsichtig). Werte gerundet.")

# =========================== 6 Sensitivität ===================================================================
D.slide("Ab 0,7 Pp Anteilsgewinn und 10 % Marge ist der Fokus spätestens 2033 zurückverdient",
        "ARGUMENT 2 (Ertrag), Robustheit: Hält die Rechnung, wenn Annahmen schlechter sind? Matrix aus Anteilsgewinn und Marge, Wert = Amortisationsjahr. "
        "Betrachteraufgabe: Bereich ablesen, in dem die Entscheidung trägt. Die Schwellen werden die Kriterien an den Entscheidungspunkten (Folie 8).", tracker_=(2, "Ertrag"))
(LX, LW), (RX, RW) = D.split(8.2)
D.header(LX, 1.5, LW, "AMORTISATIONSJAHR DES FOKUS JE ANTEILSGEWINN UND MARGE", "scales")
gx0, gy0, cw, chh = LX + 1.35, 2.6, 1.32, 0.6
D.text(gx0, 1.95, 5 * cw, 0.26, "Anteilsgewinn bis 2029 →", 12, D.M, DB, "c")
D.text(LX, gy0 - 0.36, 1.25, 0.3, "Marge ↓", 12, D.M, DB)
for j, p in enumerate(Mo.SENS_PP): D.text(gx0 + j * cw, gy0 - 0.34, cw, 0.28, f"+{de(p)} Pp", 13, D.M, DB, "c")
for r_, mg in enumerate(Mo.SENS_M):
    D.text(LX, gy0 + r_ * chh, 1.2, chh, f"{mg * 100:.0f} %", 13, D.M, DB, "l", "m")
    for j, yv in enumerate(Mo.SENS[r_]):
        fill, col = (ZB, WH) if yv <= 2031 else ((LB, DB) if yv <= 2033 else ("ECEEEF", DB))
        D.shape(S.RECTANGLE, gx0 + j * cw + 0.03, gy0 + r_ * chh + 0.03, cw - 0.06, chh - 0.06, fill=fill)
        D.text(gx0 + j * cw, gy0 + r_ * chh, cw, chh, str(yv), 16, D.M, col, "c", "m")
bj, br = Mo.SENS_PP.index(0.9), Mo.SENS_M.index(0.12)
D.shape(S.RECTANGLE, gx0 + bj * cw, gy0 + br * chh, cw, chh, line=DB, lw=3, name="Basisfall")
D.text(gx0 + bj * cw, gy0 + 4 * chh + 0.05, cw, 0.26, "Basisfall", 12, D.M, DB, "c")
x0s, x1s = gx0 + 1 * cw, gx0 + 5 * cw; y0s, y1s = gy0 + 1 * chh, gy0 + 4 * chh
D.dash(x0s, y0s, x1s, y0s, DB, 1.5); D.dash(x0s, y0s, x0s, y1s, DB, 1.5)
D.text(gx0 + 1 * cw, gy0 + 4 * chh + 0.32, 4 * cw, 0.26, "gestrichelt: ab 0,7 Pp und ab 10 % Marge, alle Felder bis 2033", 12, D.L, DB, "c")
for k, (fill, lab_, tcol) in enumerate([(ZB, "bis 2031", WH), (LB, "2032 bis 2033", DB), ("ECEEEF", "ab 2034", DB)]):
    D.shape(S.RECTANGLE, LX + 1.35 + k * 1.9, 5.72, 0.3, 0.22, fill=fill, line=LB, lw=0.5); D.text(LX + 1.72 + k * 1.9, 5.68, 1.5, 0.3, lab_, 12, D.L, DB, "l", "m")
D.card(RX, 1.5, RW, 4.4, "tint")
D.icon("flag-banner", RX + 0.5, 2.05, 0.6)
D.text(RX + 0.3, 2.5, RW - 0.5, 0.35, "Schwellen werden Kriterien", 17, D.M, DB)
D.rich(RX + 0.3, 2.95, RW - 0.5, 2.8, [("Im Basisfall (0,9 Pp, 12 %) ist der Fokus ", False), (str(Mo.PB_B), True), (" zurückverdient. ", False),
       ("Kritisch wird es nur unter ", False), ("0,7 Pp", True), (" oder unter ", False), ("10 %", True), (" Marge. Genau diese Werte prüfen wir nach dem Pilot, bevor 40 Mio. € fließen.", False)], 14)
D.band("KONSEQUENZ", "Liegt der Pilot unter 0,7 Pp oder die Marge unter 10 %, stoppen wir nach 10 Mio. €.", 15)
D.footer("Beispieldaten, fiktiv. Amortisationsjahr = erstes Jahr mit kumuliertem Ergebnis ≥ Investition; übrige Annahmen wie Folie 5.")

# =========================== 7 Datenqualität ==================================================================
D.slide(f"Die Befragung schwankt {Mo.SMOOTH:.0f}-mal weniger, als es bei 1.200 Befragten zu erwarten wäre",
        "ARGUMENT 3 (Risiko). Der wichtigste Einwand gegen Folie 4: Sind die Daten echt? Bei 1.200 Befragten müssten Monatswerte allein durch Zufall um etwa 1,9 Pp schwanken; "
        "sie schwanken um 0,08 Pp. Das deutet auf Glättung, Gewichtung oder ein festes Panel (Vermutung, nicht belegt). Konsequenz: Erhebung prüfen, auf Jahreswerte steuern.", tracker_=(3, "Risiko"))
(LX, LW), (RX, RW) = D.split(8.2)
D.header(LX, 1.5, LW, "MONATLICHE VERÄNDERUNG DER NACHFRAGE, PP", "database")
band95 = 1.96 * Mo.noise_diff; mu = Mo.d.mean()
X, Y = D.columns(LX, 2.0, LW, 3.75, [f"m{i}" for i in range(23)], list(Mo.d), [ZB] * 23, -4.4, 4.6, None, inner=(0.02, 0.05, 0.96, 0.86), gap=60, cat_labels=False,
                 alt="Säulendiagramm: 23 monatliche Veränderungen der Nachfrage zwischen 0,17 und 0,45 Pp, verglichen mit dem Zufallsband von ±3,7 Pp.")
x_l, x_r = X(0) - 0.15, X(22) + 0.15
D.shape(S.RECTANGLE, x_l, Y(mu + band95), x_r - x_l, Y(mu - band95) - Y(mu + band95), fill=LB, alpha=25, name="Zufallsband")
D.dash(x_l, Y(mu + band95), x_r, Y(mu + band95), MB, 1.0); D.dash(x_l, Y(mu - band95), x_r, Y(mu - band95), MB, 1.0)
D.dash(x_l, Y(0), x_r, Y(0), DB, 0.75)
D.text(x_l + 0.05, Y(mu + band95) + 0.05, 7.6, 0.28, f"Erwartete Schwankung aus Zufall bei 1.200 Befragten: ±{de(band95)} Pp (95 %)", 12, D.M, ZB)
D.text(x_l + 0.05, Y(mu) - 0.62, 6.5, 0.28, f"Tatsächlich: alle 23 Monate zwischen {de(Mo.d.min(), 2)} und {de(Mo.d.max(), 2)} Pp", 13, D.M, DB)
D.text(LX, 5.6, 3, 0.26, "Nov 24", 12, D.L, DB); D.text(LX + LW - 1.0, 5.6, 1.0, 0.26, "Okt 26", 12, D.L, DB, "r")
D.card(RX, 1.5, RW, 2.05, "tint")
D.text(RX + 0.3, 1.65, RW - 0.5, 0.7, f"{de(Mo.obs_sd, 2)} Pp", 36, D.O, ZB, "l", "m")
D.text(RX + 0.3, 2.4, RW - 0.5, 1.0, "tatsächliche Streuung der Monatsänderungen (Standardabweichung)", 14, D.L, DB)
D.card(RX, 3.75, RW, 2.15, "line")
D.text(RX + 0.3, 3.9, RW - 0.5, 0.7, f"{de(Mo.noise_diff, 2)} Pp", 36, D.O, DB, "l", "m")
D.text(RX + 0.3, 4.65, RW - 0.5, 1.2, "erwartet allein aus dem Stichprobenfehler. Mögliche Ursachen (Vermutung): Glättung, Gewichtung, festes Panel", 14, D.L, DB)
D.band("WIR EMPFEHLEN", "Die Erhebung vor dem Pilot prüfen und das Budget auf Jahres- statt Monatswerte steuern.", 15)
D.footer(f"Fiktive Daten. Erwartete Streuung einer Monatsänderung = √2 × Stichprobenfehler (Anteil ≈ {Mo.p_mid * 100:.0f} %, n = 1.200) = {de(Mo.noise_diff, 2)} Pp;\n95-%-Band = ±1,96 × {de(Mo.noise_diff, 2)} Pp um die mittlere Änderung.")

# =========================== 8 Fahrplan ======================================================================
D.slide("Vor dem Pilotergebnis fließen nur 10 Mio. €, jede weitere Tranche braucht eine Freigabe",
        "ARGUMENT 3 (Risiko), Umsetzung. Betrachteraufgabe: Ablauf verstehen. Pfeil = Phase, Raute = Entscheidungspunkt am Phasenende mit Kriterium aus Folie 6 und 7, "
        "Balken = Tranche, die erst danach frei wird. Stoppt ein Entscheidungspunkt, sind höchstens 2, 10 oder 50 Mio. € eingesetzt.", tracker_=(3, "Risiko"))
LBW = 1.55; cw4 = (W - LBW - 3 * 0.1) / 4
xs = [X0 + LBW + i * (cw4 + 0.1) for i in range(4)]
shades = [LB, MB, ZB, DB]
icons_ = ["magnifying-glass", "flask", "target", "steps"]
what = ["Erhebung prüfen, auf Jahreswerte umstellen", "Fokus-Angebot in Cyber testen", "Gesundheit und Logistik anbinden", "Vertrieb skalieren, Ziele steuern"]
res = ["Belastbare Datenbasis", "Anteilsgewinn im Pilot gemessen", "Drei Segmente live", "Regelbetrieb"]
gate = ["Erhebung belastbar?", "Kurs ≥ 0,7 Pp?", "Marge ≥ 10 %?", "Fortführen?"]
for i, x in enumerate(xs):
    D.shape(S.PENTAGON, x, 1.45, cw4 + (0.1 if i < 3 else 0), 0.85, fill=shades[i])
    dk = i == 0
    D.text(x + 0.22, 1.52, cw4 - 0.8, 0.25, Mo.PH[i][1].upper(), 11, D.M, DB if dk else WH, spacing=80)
    D.text(x + 0.22, 1.77, cw4 - 0.55, 0.5, Mo.PH[i][0], 14, D.M, DB if dk else WH)
for lb_, y in [("Was passiert", 2.42), ("Ergebnis", 3.3), ("Entscheidungs-\npunkt", 3.98), ("Tranche, Mio. €", 4.82)]:
    D.rule(X0, y, W); D.text(X0, y + 0.1, LBW - 0.15, 0.5, lb_, 13, D.M, ZB)
for i, x in enumerate(xs):
    D.icon(icons_[i], x + 0.32, 2.86, 0.48)
    D.text(x + 0.66, 2.52, cw4 - 0.7, 0.75, what[i], 13, D.L, DB)
    D.text(x + 0.2, 3.44, cw4 - 0.3, 0.5, res[i], 14, D.M, DB)
    D.shape(S.DIAMOND, x + 0.2, 4.2, 0.32, 0.32, fill=DB, name=f"Entscheidungspunkt {i + 1}", alt=f"Entscheidungspunkt am Ende von Phase {i + 1}: {gate[i]}")
    D.text(x + 0.62, 4.1, cw4 - 0.7, 0.5, gate[i], 14, D.M, DB, "l", "m")
    amt = Mo.PH[i][2]; wb = (cw4 - 1.0) * amt / 40
    D.shape(S.RECTANGLE, x + 0.2, 4.98, max(wb, 0.05), 0.26, fill=DB if i < 2 else ZB)
    D.text(x + 0.3 + max(wb, 0.05), 4.96, 0.8, 0.3, str(amt), 15, D.M, DB, "l", "m")
    D.text(x + 0.2, 5.28, cw4 - 0.3, 0.22, "mit dem Beschluss" if i == 0 else f"frei nach Entscheidungspunkt {i}", 11, D.L, DB)
D.bracket(xs[0] + 0.2, xs[1] + cw4 - 0.2, 5.62, "10 Mio. € bis zum Pilotergebnis", 12)
D.band("KONSEQUENZ", f"Scheitert ein Entscheidungspunkt, stoppen wir nach höchstens {Mo.STOP[0]}, {Mo.STOP[1]} oder {Mo.STOP[2]} Mio. € statt nach 80.", 15)
D.footer("Beispieldaten, fiktiv. Tranchen 2, 8, 40 und 30 Mio. € sind Annahmen. Kriterien aus Folie 6 und 7.")

# =========================== 9 Entscheidung =================================================================
D.slide("Wir bitten um 80 Mio. € Rahmen und 10 Mio. € sofort, damit wir im ersten Quartal starten",
        "ENTSCHEIDUNG: was, wer, bis wann. Drei Beschlüsse: erste Freigabe (Tranche 1 und 2), Rahmenzusage mit Entscheidungspunkten, Lenkungskreis. "
        "Entscheider und Termin sind nicht bekannt und stehen als [DATA NEEDED].", dark=True)
asks = [("hand-coins", "10 Mio. € sofort", "Tranche 1 und 2: Erhebung prüfen (2) und Pilot in Cyber (8)", "10 Mio. €", "Start im ersten Quartal 2027"),
        ("seal-check", "Rahmen zusagen", "Weitere 70 Mio. € nur nach bestandenen Entscheidungspunkten", "80 Mio. €", "Rahmen 2027 bis 2029"),
        ("users-three", "Gremium benennen", "Entscheidet an den Entscheidungspunkten nach den Kriterien von Folie 6 und 7", "3", "Entscheidungspunkte mit Geldwirkung")]
for i, ((x, w), (ic, t_, d_, big, cap)) in enumerate(zip(D.cols(3), asks)):
    D.card(x, 1.55, w, 4.45, "blue")
    D.badge(x + 0.55, 2.1, i + 1, 0.5, fill=WH, color=ZB, size=18)
    D.icon(ic, x + w - 0.75, 2.1, 0.8, on_dark=True)
    D.text(x + 0.3, 2.7, w - 0.6, 0.45, t_, 22, D.M, WH)
    D.text(x + 0.3, 3.3, w - 0.6, 0.95, d_, 14, D.L, WH)
    D.rule(x + 0.3, 4.4, w - 0.6, WH, 0.015)
    D.text(x + 0.3, 4.52, w - 0.6, 0.8, big, 40, D.O, WH, "l", "m")
    D.text(x + 0.3, 5.4, w - 0.6, 0.3, cap, 12, D.M, WH)
D.text(X0, 6.32, 12.0, 0.3, "Entscheider und Termin: [DATA NEEDED: Gremium und Termin der Entscheidung]", 15, D.M, WH)
D.footer("Beispieldaten, fiktiv. Tranchen und Entscheidungspunkte: Folie 8.")

# =========================== 10 Anhang: roter Faden ==========================================================
D.slide("Jede Folie belegt ein Argument, und die drei Argumente tragen die Empfehlung",
        "LERNFOLIE (Pyramidenprinzip). Oben die Frage, darunter die Antwort, darunter drei überschneidungsfreie Argumente (Chance, Ertrag, Risiko), darunter je zwei Belegfolien. "
        "Der Folientyp folgt der Aufgabe des Betrachters.", tracker_=("A", "Anhang"))
D.text(1.9, 1.45, 9.53, 0.3, "Frage: Sollen wir gezielt in die Wachstumssegmente investieren, und lohnt es sich?", 14, D.M, ZB)
D.shape(S.ROUNDED_RECTANGLE, 1.9, 1.85, 9.53, 0.85, fill=DB)
D.text(2.2, 1.85, 8.9, 0.85, "Antwort: 80 Mio. € für drei Wachstumssegmente, zurückverdient 2031, freigegeben in Stufen", 18, D.M, WH, "l", "m")
C3 = D.cols(3, gap=0.34)
D.vrule(X0 + W / 2, 2.7, 0.2, DB, 0.014); D.rule(C3[0][0] + C3[0][1] / 2, 2.9, C3[2][0] - C3[0][0], DB, 0.014)
args = [("chart-line-up", "1  Chance", "Der Markt wächst dort am stärksten", [("Folie 3", "Dreispalter: Zuwachs, Wachstum, Anteil"), ("Folie 4", "Zwei Belege: Nachfrage und Tempo")]),
        ("coins", "2  Ertrag", "Der Fokus verdient schneller zurück", [("Folie 5", "Kurve: kumuliertes Ergebnis"), ("Folie 6", "Matrix: Sensitivität")]),
        ("shield-check", "3  Risiko", "Das Risiko ist gestuft", [("Folie 7", "Abweichung: Daten zu glatt"), ("Folie 8", "Fahrplan: Tranchen, Stopp")])]
for (x, w), (ic, h_, cl, sl) in zip(C3, args):
    D.vrule(x + w / 2, 2.9, 0.2, DB, 0.014)
    D.card(x, 3.1, w, 1.0, "blue")
    D.icon(ic, x + 0.5, 3.6, 0.6, on_dark=True)
    D.text(x + 0.95, 3.2, w - 1.05, 0.3, h_, 15, D.M, WH)
    D.text(x + 0.95, 3.52, w - 1.05, 0.5, cl, 13, D.L, WH)
    for k, (fo, ds) in enumerate(sl):
        yy = 4.3 + k * 0.7
        D.card(x, yy, w, 0.6, "tint")
        D.text(x + 0.2, yy, 0.85, 0.6, fo, 13, D.M, ZB, "l", "m")
        D.text(x + 1.05, yy, w - 1.15, 0.6, ds, 13, D.L, DB, "l", "m")
D.takeaway("Folie 2 gibt die Antwort zuerst, Folie 9 bittet um die Entscheidung, alles dazwischen belegt ein Argument.", size=16)
D.footer("Lernfolie: Methode siehe skill_v2/references/storyline.md.")

# =========================== 11 Anhang: Annahmen =============================================================
D.slide("Alle Werte folgen aus sieben Annahmen, die wir offenlegen",
        "ANHANG: Methode. Jede Zahl im Deck kommt aus modell.py; asserts prüfen die Aussagen vor dem Bauen.", tracker_=("A", "Anhang"))
ass = [("Marktvolumen", "Gewerbe-Bruttoprämie 45,0 Mrd. € (2026) und 54,0 Mrd. € (2029) in acht Segmenten; Verlauf geometrisch."),
       ("Unser Anteil", "2026 je Segment fest; ohne Kurswechsel konstant. Gruppenwerte gewichtet nach Marktvolumen."),
       ("Anteilsgewinn", "Fokus +0,9 Pp auf die drei Segmente, breit +0,3 Pp auf alle acht; Hochlauf 30 / 65 / 100 % (2027 bis 2029)."),
       ("Marge", "Ergebnis = zusätzliche Prämie × Marge: Fokus 12 %, breit 7 %; ab 2030 konstant, ohne weiteres Wachstum."),
       ("Investition", "Fokus 80 Mio. € in Tranchen 2 / 8 / 40 / 30; breit 140 Mio. € (30 / 60 / 50)."),
       ("Befragung", "Monatlich 1.200 Gewerbekunden der Fokus-Segmente; Anteil mit Schutzbedarf 28,0 auf 34,5 %."),
       ("Rechenwege", "Wachstum p. a. relativ (23 Monate = 1,92 Jahre); Amortisation = erstes Jahr mit kumuliertem Ergebnis ≥ 0.")]
for i, (k, v) in enumerate(ass):
    y = 1.5 + i * 0.64
    D.card(X0, y, W, 0.56, "tint")
    D.badge(X0 + 0.3, y + 0.28, i + 1, 0.34)
    D.text(X0 + 0.7, y, 2.4, 0.56, k, 15, D.M, DB, "l", "m")
    D.text(X0 + 3.2, y, W - 3.4, 0.56, v, 13, D.L, DB, "l", "m")
D.footer("Beispieldaten, fiktiv. Pp = Prozentpunkte.")

# =========================== 12 Anhang: Segmenttabelle =======================================================
D.slide("Cyber wächst am schnellsten (20 % pro Jahr), dort ist unser Anteil am niedrigsten (2,0 %)",
        "ANHANG: Beleg auf Nachfrage. Betrachteraufgabe: exakte Werte nachschlagen, also Tabelle.", tracker_=("A", "Anhang"))
rows_ = [[Mo.SEG[i], de(Mo.m26[i]), de(Mo.m29[i]), de(Mo.dz[i]), de(Mo.g[i] * 100), de(Mo.sh[i])] for i in range(8)]
rows_ += [["Fokus (3)", de(Mo.m26[Mo.FOKUS].sum()), de(Mo.m29[Mo.FOKUS].sum()), de(Mo.F_dz), de(Mo.F_g * 100), de(Mo.F_sh)],
          ["Übrige (5)", de(Mo.m26[Mo.REST].sum()), de(Mo.m29[Mo.REST].sum()), de(Mo.R_dz), de(Mo.R_g * 100), de(Mo.R_sh)]]
D.table(X0, 1.5, W, 4.5, ["Segment", "Markt 2026, Mrd. €", "Markt 2029, Mrd. €", "Zuwachs, Mrd. €", "Wachstum p. a., %", "Unser Anteil 2026, %"],
        rows_, [2.83, 1.94, 1.94, 1.94, 1.94, 1.94], ["l", "r", "r", "r", "r", "r"], focus_rows=(0, 1, 2, 8), size=13, name="Tabelle Segmentdaten")
D.footer("Beispieldaten, fiktiv. Hell hinterlegt: Fokus-Segmente. Pp = Prozentpunkte.")
D.save(sys.argv[1])
