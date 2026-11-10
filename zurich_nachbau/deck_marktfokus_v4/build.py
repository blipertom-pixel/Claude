# -*- coding: utf-8 -*-
"""Marktfokus v4: neue Bildsprache (editorial). Keine dunklen Folien, kein Balken unten, keine Blöcke rechts, keine getönten Kästen.
Ein großes Bild je Folie, Anmerkungen im Bild, Ogg-Zahlen als Gestaltung, jede Folie mit eigenem Layout. Fiktive Daten aus modell.py."""
import sys, math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skill_v2" / "scripts"))
import numpy as np
import deck_lite as D
import editorial as E
from deck_lite import de, S, ZB, DB, MB, LB, WHITE, L, M, O
import modell as Mo

D.new_deck()
X0, W = E.X0, E.W
pct = lambda v, n=1: de(v, n) + " %"
NB = " "

# ============================ 1 Titel: Band mit Titel ===========================================================
D.slide("Wo der Markt am stärksten wächst, setzen wir 80 Mio. € ein", "Titel. These in einem Satz. Zweck: Beschluss über 80 Mio. € Rahmen und 10 Mio. € sofort. Fiktive Beispieldaten.", hero=True)
E.blue_band(2.0, 2.9)
for r_, a in [(3.4, 30), (2.5, 40), (1.6, 55)]:
    D.shape(S.DONUT, 13.333 - 2.6 - r_ / 2, 3.45 - r_ / 2, r_, r_, fill=WHITE, alpha=a // 3).adjustments[0] = 0.06
D._set_title("Wo der Markt am stärksten wächst,\nsetzen wir 80 Mio. € ein", X0 + 0.3, 2.55, 10.6, 2.1, 40, WHITE)
E.to_front(D.s().shapes.title)
D.text(X0 + 0.3, 5.25, 9, 0.35, "Vorlage für den Vorstand  ·  Marktfokus Gewerbe 2027 bis 2029", 18, M, DB)
D.text(X0 + 0.3, 5.65, 9, 0.35, "10. November 2026  ·  Beispieldaten, fiktiv", 14, L, DB)

# ============================ 2 Antwort zuerst: Band + drei Karten =============================================
E.slide("80 Mio. € für drei Wachstumssegmente: zurückverdient 2031, freigegeben in Stufen",
        "ANTWORT ZUERST. Drei Argumente (Chance, Ertrag, Risiko), je mit einer tragenden Zahl und ihrem Vergleich als Beleg. "
        "SCQA: Markt wächst von 45 auf 54 Mrd. €; 69 % davon dort, wo wir am kleinsten sind; sollen wir gezielt investieren und lohnt es sich? Ja: 80 Mio. € in Tranchen.")
E.blue_band(2.85, 2.0)
cards = [("chart-line-up", "1 · Chance", "Der Markt wächst dort, wo wir klein sind", "69" + NB + "%", "des Marktwachstums liegen in drei Segmenten",
          "UNSER ANTEIL DORT", [("Fokus", Mo.F_sh, ZB, pct(Mo.F_sh)), ("übrige", Mo.R_sh, LB, pct(Mo.R_sh))], 3.5),
         ("coins", "2 · Ertrag", "Der Fokus verdient schneller zurück", str(Mo.PB_B), "zurückverdient, die breite Streuung erst " + str(Mo.PB_A),
          "ERGEBNIS AB 2029, MIO. € P. A.", [("Fokus", Mo.RUN_B, ZB, de(Mo.RUN_B)), ("breit", Mo.RUN_A, LB, de(Mo.RUN_A))], 21.8),
         ("shield-check", "3 · Risiko", "Das Risiko ist gestuft", "10 Mio. €", "fließen vor dem Pilotergebnis, nicht 80",
          "GEBUNDEN, MIO. €", [("vor Pilot", 10, ZB, "10"), ("Rahmen", 80, LB, "80")], 80)]
cw = (W - 2 * 0.35) / 3
for i, (ic, lab, claim, num, cap, ctitle, pair, vmax) in enumerate(cards):
    x = X0 + i * (cw + 0.35)
    E.white_card(x, 1.75, cw, 4.2)
    D.icon(ic, x + 0.5, 2.25, 0.62)
    E.kicker(x + 0.95, 2.13, cw - 1.1, lab)
    D.text(x + 0.35, 2.7, cw - 0.6, 0.7, claim, 17, M, DB)
    E.big(x + 0.35, 3.35, cw - 0.6, num, 48, ZB)
    D.text(x + 0.35, 4.22, cw - 0.6, 0.5, cap, 13, L, DB)
    E.kicker(x + 0.35, 4.85, cw - 0.6, ctitle, DB)
    for k, (nm, v, col, lbl) in enumerate(pair):
        yy = 5.13 + k * 0.32
        D.text(x + 0.35, yy, 0.85, 0.26, nm, 12, L, DB, "l", "m")
        D.shape(S.RECTANGLE, x + 1.2, yy + 0.07, (cw - 2.15) * v / vmax, 0.13, fill=col)
        D.text(x + 1.2 + (cw - 2.15) * v / vmax + 0.07, yy, 0.8, 0.26, lbl, 12, M, DB, "l", "m")
E.statement("Wir bitten um 80 Mio. € Rahmen und 10 Mio. € sofort für Datenprüfung und Pilot in Cyber.", y=6.38, size=17)
E.footer("Beispieldaten, fiktiv. Fokus = Gesundheit, Cyber, Logistik. Belege auf den folgenden Folien.")

# ============================ 3 Portfolio: Wachstum x Anteil, Größe = Zuwachs ==================================
E.slide(f"69{NB}% des Marktwachstums liegen in drei Segmenten, in denen wir am kleinsten sind",
        "ARGUMENT 1 (Chance). 69 % = 6,2 von 9,0 Mrd. € Zuwachs. Portfolio-Darstellung (Beratungsklassiker): x = Wachstum p. a., y = unser Anteil, Kreisfläche = Zuwachs in Mrd. €. "
        "Die drei Fokus-Segmente liegen rechts unten: Markt wächst schnell, wir sind klein. Konsequenz: Ohne Kurswechsel sinkt der Gesamtanteil von 3,1 auf 3,0 %.", chapter="1 · Chance")
PX, PY, PW, PH = X0 + 0.7, 2.0, 11.2, 3.6
xmin, xmax, ymin, ymax = 0, 22, 1.5, 4.3
fx = lambda v: PX + PW * (v - xmin) / (xmax - xmin)
fy = lambda v: PY + PH * (1 - (v - ymin) / (ymax - ymin))
tot_g = (54 / 45) ** (1 / 3) - 1
D.shape(S.RECTANGLE, fx(tot_g * 100), fy(Mo.share26), fx(xmax) - fx(tot_g * 100), fy(ymin) - fy(Mo.share26), fill=LB, alpha=22, name="Zielzone")
E.kicker(fx(14.5), fy(Mo.share26) + 0.15, 4.8, "Hier wächst der Markt, und wir sind klein", ZB)
D.rule(PX, fy(ymin), PW, DB, 0.012); D.vrule(PX, PY, PH, DB, 0.012)
for v in (0, 5, 10, 15, 20): D.text(fx(v) - 0.4, fy(ymin) + 0.08, 0.8, 0.24, pct(v, 0), 11, L, DB, "c")
for v in (2, 3, 4): D.text(PX - 0.62, fy(v) - 0.12, 0.55, 0.24, pct(v, 0), 11, L, DB, "r")
D.text(PX + PW - 4, fy(ymin) + 0.34, 4, 0.24, "Wachstum des Segments pro Jahr, 2026 bis 2029 →", 11, M, DB, "r")
D.text(X0 - 0.05, PY - 0.38, 3.5, 0.24, "↑ Unser Marktanteil 2026", 11, M, DB)
D.dash(fx(tot_g * 100), PY, fx(tot_g * 100), fy(ymin), MB, 1.0); D.dash(PX, fy(Mo.share26), PX + PW, fy(Mo.share26), MB, 1.0)
D.text(fx(tot_g * 100) + 0.06, fy(ymin) - 0.3, 2.8, 0.24, f"Markt gesamt {pct(tot_g * 100)}", 11, L, DB)
D.text(PX + PW - 2.9, fy(Mo.share26) - 0.27, 2.85, 0.24, f"unser Anteil gesamt {pct(Mo.share26)}", 11, L, DB, "r")
rmax = 0.55
order = np.argsort(-Mo.dz)
for i in order:
    r = rmax * math.sqrt(Mo.dz[i] / Mo.dz.max()); cx, cy = fx(Mo.g[i] * 100), fy(Mo.sh[i])
    foc = i in Mo.FOKUS
    sp = D.shape(S.OVAL, cx - r, cy - r, 2 * r, 2 * r, fill=ZB if foc else LB, alpha=None if foc else 75, line=WHITE, lw=1.0, name=f"Segment {Mo.SEG[i]}",
                 alt=f"{Mo.SEG[i]}: Wachstum {de(Mo.g[i] * 100)} %, Anteil {de(Mo.sh[i])} %, Zuwachs {de(Mo.dz[i])} Mrd. €")
    if foc:
        left = Mo.SEG[i] == "Logistik"
        lx = cx - r - 1.97 if left else cx + r + 0.07
        D.text(lx, cy - 0.25, 1.9, 0.26, Mo.SEG[i], 13, M, DB, "r" if left else "l")
        D.text(lx, cy - 0.01, 1.9, 0.24, f"+{de(Mo.dz[i])} Mrd. €", 12, M, ZB, "r" if left else "l")
ccx, ccy = fx(3.0), fy(3.75)
E.leader(ccx + 0.35, ccy - 0.05, fx(5.6), fy(4.05), DB, 0.75)
D.text(fx(5.7), fy(4.05) - 0.14, 4.6, 0.26, "Übrige fünf: zusammen +2,8 Mrd. €, 2,9 % Wachstum p. a.", 11, L, DB)
E.statement(f"Ohne Kurswechsel sinkt unser Gesamtanteil bis 2029 von {de(Mo.share26)} auf {de(Mo.share29_base)}{NB}%.", y=6.4, size=16)
E.footer("Beispieldaten, fiktiv. Kreisfläche = Zuwachs 2026 bis 2029 (Bruttoprämie, gesamt 9,0 Mrd. €, davon 6,2 Mrd. € in Gesundheit, Cyber, Logistik).")

# ============================ 4 Nachfrage: große Kurve + Tempo-Streifen =========================================
E.slide(f"Die Nachfrage wächst klar um {de(Mo.dem_growth * 100)}{NB}% pro Jahr, ein Nachlassen des Tempos ist nicht belegt",
        "ARGUMENT 1 (Chance), Nachfrage. Oben die Kurve (jeder Monat höher), unten der Tempo-Streifen auf derselben Zeitachse: Monatsschritte als schmale Säulen, "
        "Dreimonatsfenster 0,17 Pp nur zweimal (Aug 2025, Okt 2026); nach Aug 2025 folgten 0,41. Fiktive Befragungsdaten.", chapter="1 · Chance")
CX, CW_ = X0, W
X, Y, (pl, pw, pb) = D.lines(CX, 1.65, CW_, 2.9, [str(i) for i in range(24)], [("Nachfrage, %", Mo.dem, ZB, 3.0)], 26.5, 35.5, inner=(0.07, 0.04, 0.83, 0.92), markers=False,
                            alt="Liniendiagramm: Anteil der befragten Gewerbekunden mit Schutzbedarf, von 28,0 % (Nov 2024) auf 34,5 % (Okt 2026), jeder Monat höher.")
pts = [(X(i), Y(v)) for i, v in enumerate(Mo.dem)] + [(X(23), pb), (X(0), pb)]
fb = D.s().shapes.build_freeform(D.Inches(pts[0][0]), D.Inches(pts[0][1])); fb.add_line_segments([(D.Inches(a), D.Inches(b)) for a, b in pts[1:]], close=True)
area = fb.convert_to_shape(); area.fill.solid(); area.fill.fore_color.rgb = D.rgb(LB); area.line.fill.background()
st = area._element.find(D.qn("p:style")); area._element.remove(st) if st is not None else None
from lxml import etree
etree.SubElement(area._element.spPr.find(D.qn("a:solidFill"))[0], D.qn("a:alpha")).set("val", "25000")
area.name = "Fläche unter der Kurve"
D.disc(X(0), Y(Mo.dem[0]), 0.16, ZB); D.disc(X(23), Y(Mo.dem[23]), 0.18, ZB)
E.big(CX, Y(Mo.dem[0]) - 0.95, 1.6, "28,0" + NB + "%", 26, DB)
E.big(X(23) + 0.15, Y(Mo.dem[23]) - 0.3, 1.9, "34,5" + NB + "%", 34, ZB)
E.kicker(X(2), Y(Mo.dem[2]) - 1.25, 4.5, f"+{de(Mo.dem_growth * 100)} % pro Jahr · jeder Monat höher", ZB)
E.leader(X(4), Y(Mo.dem[2]) - 0.98, X(5), Y(Mo.dem[5]) - 0.08, ZB)
D.text(CX, 1.58, 4, 0.24, "Kunden mit Schutzbedarf, % der Befragten".upper(), 10, M, ZB, spacing=100)
# Tempo-Streifen
sy, sh_ = 4.95, 0.75
E.kicker(CX, sy - 0.05, 2.0, "Tempo je Monat", DB)
D.text(CX, sy + 0.2, 0.9, 0.5, "Pp pro Monat, Dreimonats-\nschnitt", 9, L, DB)
for i, v in enumerate(Mo.pace):
    xi = X(i + 2); hh = sh_ * v / 0.45
    low = i in (6, 20)
    D.shape(S.RECTANGLE, xi - 0.07, sy + sh_ - hh + 0.1, 0.14, hh, fill=DB if low else LB, name="Tempo")
    if low or i == int(np.argmax(Mo.pace)): D.text(xi - 0.35, sy + sh_ - hh - 0.14, 0.7, 0.22, de(v, 2), 11, M, DB, "c")
D.rule(X(2) - 0.15, sy + sh_ + 0.1, X(22) - X(2) + 0.3, LB)
for i in (0, 6, 12, 18, 23): D.text(X(i) - 0.45, sy + sh_ + 0.14, 0.9, 0.22, ["Nov 24", "Mai 25", "Nov 25", "Mai 26", "Okt 26"][[0, 6, 12, 18, 23].index(i)], 11, L, DB, "c")
E.statement("Nur zwei von 21 Fenstern sind so langsam wie zuletzt. Nach dem ersten (August 2025) stieg das Tempo auf 0,41.", y=6.48, size=15)
E.footer("Fiktive Daten. Monatliche Befragung von 1.200 Gewerbekunden in Gesundheit, Cyber, Logistik. Pp = Prozentpunkte.")

# ============================ 5 Business Case: J-Kurve als Bild =================================================
E.slide(f"Der Fokus ist {Mo.PB_B} zurückverdient, die breite Streuung trotz 140 Mio. € Einsatz erst {Mo.PB_A}",
        "ARGUMENT 2 (Ertrag). Investition Fokus 80 Mio. €, breit 140 Mio. €. Kumuliertes Ergebnis nach Investition: Ergebnis = zusätzliche Prämie × Marge (Fokus 12 %, breit 7 %). "
        "Die Jahreszahlen der Amortisation stehen groß am Ereignis, nicht in Kästen.", chapter="2 · Ertrag")
yrs = [str(y) for y in Mo.YEARS]; cumA = [r["cum"] for r in Mo.CA]; cumB = [r["cum"] for r in Mo.CB]
X, Y, (pl, pw, pb) = D.lines(X0, 1.65, W, 4.15, yrs, [("Fokus", cumB, ZB, 4.0), ("Breit", cumA, LB, 3.0)], -135, 115, inner=(0.0, 0.03, 0.86, 0.9), markers=False,
                            alt="Liniendiagramm 2027 bis 2035: Fokus erreicht 2031 die Nulllinie und 2035 +90 Mio. €; breite Streuung liegt 2035 noch bei −51 Mio. €.")
D.shape(S.RECTANGLE, pl, Y(0), pw, Y(-135) - Y(0), fill=LB, alpha=12, name="Investitionsphase")
D.rule(pl, Y(0), pw, DB, 0.014)
E.kicker(X(5) - 0.3, Y(0) + 0.12, 5, "unter null: Geld noch nicht zurückverdient", DB)
for i, yv in enumerate(yrs): D.text(X(i) - 0.4, Y(0) - 0.3 if False else pb - 0.02, 0.8, 0.24, yv, 11, L, DB, "c")
ib = Mo.YEARS.index(Mo.PB_B)
D.disc(X(ib), Y(cumB[ib]), 0.24, ZB)
E.leader(X(ib), Y(cumB[ib]) - 0.14, X(ib), Y(cumB[ib]) - 1.05, ZB, 1.0)
E.big(X(ib) - 1.2, Y(cumB[ib]) - 1.95, 2.4, str(Mo.PB_B), 54, ZB, "c")
D.text(X(ib) - 1.2, Y(cumB[ib]) - 1.12, 2.4, 0.26, "Fokus zurückverdient", 13, M, ZB, "c")
D.text(X(8) + 0.15, Y(cumB[-1]) - 0.2, 1.6, 0.3, f"+{de(cumB[-1], 0)} Mio. €", 16, M, ZB)
D.text(X(8) + 0.15, Y(cumA[-1]) - 0.2, 1.6, 0.3, f"{de(cumA[-1], 0)} Mio. €", 16, M, DB)
D.text(X(8) + 0.15, Y(cumA[-1]) + 0.12, 1.75, 0.5, f"breit, zurück erst {Mo.PB_A}", 12, L, DB)
D.text(X(8) + 0.15, Y(cumB[-1]) + 0.12, 1.75, 0.3, "Fokus", 12, L, DB)
it = 2; D.disc(X(it), Y(cumB[it]), 0.14, ZB)
E.statement(f"Am Tiefpunkt 2029 sind netto {de(-Mo.TROUGH_B)} Mio. € gebunden, danach trägt der Fokus {de(Mo.RUN_B)} Mio. € pro Jahr.", y=6.42, size=16)
D.text(X(it) - 1.0, Y(cumB[it]) + 0.12, 2.0, 0.26, f"Tiefpunkt {de(cumB[it])} Mio. €", 12, M, DB, "c")
E.footer("Beispieldaten, fiktiv. Ergebnis = zusätzliche Prämie × Marge; Anteilsgewinn +0,9 Pp (Fokus) bzw. +0,3 Pp (breit), Hochlauf 30/65/100 %, ab 2030 konstant.")

# ============================ 6 Sensitivität: Raster als Bild ==================================================
E.slide("Ab 0,7 Pp Anteilsgewinn und 10 % Marge ist der Fokus spätestens 2033 zurückverdient",
        "ARGUMENT 2 (Ertrag), Robustheit. Raster aus Anteilsgewinn und Marge, Wert = Amortisationsjahr. Der tragfähige Bereich wird zur Bedingung an den Entscheidungspunkten.", chapter="2 · Ertrag")
gx0, gy0, cw, ch = X0 + 1.4, 2.3, 1.45, 0.78
E.kicker(gx0, 1.62, 5 * cw, "Anteilsgewinn bis 2029 →", DB)
D.text(X0, gy0 - 0.33, 1.3, 0.24, "MARGE ↓", 10, M, DB, spacing=120)
for j, p in enumerate(Mo.SENS_PP): D.text(gx0 + j * cw, gy0 - 0.35, cw, 0.28, f"+{de(p)} Pp", 13, M, DB, "c")
for r_, mg in enumerate(Mo.SENS_M):
    D.text(X0, gy0 + r_ * ch, 1.2, ch, f"{mg * 100:.0f}{NB}%", 14, M, DB, "l", "m")
    for j, yv in enumerate(Mo.SENS[r_]):
        ok = Mo.SENS_PP[j] >= 0.7 and mg >= 0.10
        fill, col = (ZB, WHITE) if yv <= 2031 else ((LB, DB) if yv <= 2033 else ("F1F3F4", DB))
        D.shape(S.RECTANGLE, gx0 + j * cw + 0.04, gy0 + r_ * ch + 0.04, cw - 0.08, ch - 0.08, fill=fill)
        D.text(gx0 + j * cw, gy0 + r_ * ch, cw, ch, str(yv), 20, O, col, "c", "m")
bj, br = Mo.SENS_PP.index(0.9), Mo.SENS_M.index(0.12)
D.shape(S.RECTANGLE, gx0 + bj * cw, gy0 + br * ch, cw, ch, line=DB, lw=3, name="Basisfall")
D.dash(gx0 + cw, gy0 + ch, gx0 + 5 * cw, gy0 + ch, DB, 1.75); D.dash(gx0 + cw, gy0 + ch, gx0 + cw, gy0 + 4 * ch, DB, 1.75)
RX = gx0 + 5 * cw + 0.55
for k, (ic, h_, t_) in enumerate([("target", "Basisfall", f"0,9 Pp und 12{NB}% Marge: zurückverdient {Mo.PB_B} (gerahmt)"),
                                  ("flag-banner", "Tragfähiger Bereich", "Gestrichelt: ab 0,7 Pp und ab 10 % Marge, alle Felder bis 2033"),
                                  ("warning", "Darunter", "Pilot unter 0,7 Pp oder Marge unter 10 %: Stopp nach 10 Mio. €")]):
    yy = 2.0 + k * 1.15
    D.icon(ic, RX + 0.22, yy + 0.2, 0.44, disc_=False)
    D.text(RX + 0.6, yy, W + X0 - RX - 0.6, 0.3, h_, 15, M, DB)
    D.text(RX + 0.6, yy + 0.32, W + X0 - RX - 0.6, 0.7, t_, 13, L, DB)
for k, (fill, lab_) in enumerate([(ZB, "bis 2031"), (LB, "2032 bis 2033"), ("F1F3F4", "ab 2034")]):
    D.shape(S.RECTANGLE, gx0 + k * 1.9, 5.6, 0.26, 0.2, fill=fill, line=LB, lw=0.5); D.text(gx0 + 0.34 + k * 1.9, 5.55, 1.5, 0.3, lab_, 12, L, DB, "l", "m")
E.statement("Diese Schwellen sind die Kriterien am Entscheidungspunkt nach dem Pilot.", y=6.3, size=16)
E.footer("Beispieldaten, fiktiv. Amortisationsjahr = erstes Jahr mit kumuliertem Ergebnis ≥ Investition; übrige Annahmen wie Folie 5.")

# ============================ 7 Datenqualität: zwei Zahlen + Band ==============================================
E.slide(f"Die Befragung schwankt {Mo.SMOOTH:.0f}-mal weniger, als es bei 1.200 Befragten zu erwarten wäre",
        "ARGUMENT 3 (Risiko), stärkster Einwand: Sind die Daten echt? Erwartete Streuung einer Monatsänderung aus dem Stichprobenfehler 1,89 Pp, tatsächlich 0,08 Pp. "
        "Vermutete Ursachen (nicht belegt): Glättung, Gewichtung, festes Panel. Konsequenz: Erhebung vor dem Pilot prüfen, auf Jahreswerte steuern.", chapter="3 · Risiko")
E.big(X0, 1.55, 3.2, de(Mo.obs_sd, 2) + " Pp", 50, ZB)
D.text(X0, 2.45, 3.3, 0.5, "tatsächliche Streuung der\nMonatsänderung", 13, L, DB)
E.big(X0 + 3.7, 1.55, 3.2, de(Mo.noise_diff, 2) + " Pp", 50, DB)
D.text(X0 + 3.7, 2.45, 3.6, 0.5, "erwartet allein aus dem\nStichprobenfehler (1.200 Befragte)", 13, L, DB)
E.big(X0 + 7.6, 1.45, 2.4, f"{Mo.SMOOTH:.0f}×", 66, ZB)
D.text(X0 + 7.6, 2.45, 4.4, 0.5, "zu glatt für echte Stichproben.\nMögliche Ursachen: Glättung, Gewichtung, festes Panel", 13, L, DB)
band95 = 1.96 * Mo.noise_diff; mu = Mo.d.mean()
X, Y = D.columns(X0, 3.2, W, 2.75, [str(i) for i in range(23)], list(Mo.d), [ZB] * 23, -4.3, 4.6, None, inner=(0.0, 0.02, 1.0, 0.96), gap=80, cat_labels=False,
                 alt="Säulendiagramm: 23 Monatsänderungen zwischen 0,17 und 0,45 Pp innerhalb eines Zufallsbands von ±3,7 Pp.")
D.shape(S.RECTANGLE, X0, Y(mu + band95), W, Y(mu - band95) - Y(mu + band95), fill=LB, alpha=20, name="Zufallsband")
D.rule(X0, Y(mu + band95), W, MB); D.rule(X0, Y(mu - band95), W, MB)
D.text(X0 + 0.05, Y(mu + band95) + 0.05, 7, 0.24, f"Bereich, in dem Monatsänderungen allein durch Zufall liegen würden: ±{de(band95)} Pp", 11, M, ZB)
D.text(X0 + W - 5.6, Y(mu) - 0.42, 5.6, 0.24, "tatsächliche Monatsänderungen, alle 0,17 bis 0,45 Pp", 11, M, DB, "r")
E.statement("Wir prüfen die Erhebung, bevor Geld in den Pilot fließt, und steuern auf Jahres- statt Monatswerte.", y=6.4, size=16)
E.footer(f"Fiktive Daten. Erwartete Streuung = √2 × Stichprobenfehler (Anteil ≈ {Mo.p_mid * 100:.0f} %, n = 1.200); Bereich = ±1,96 × {de(Mo.noise_diff, 2)} Pp um die mittlere Änderung.")

# ============================ 8 Fahrplan: Kapital-Treppe =======================================================
E.slide("Vor dem Pilotergebnis sind nur 10 Mio. € gebunden, jede weitere Tranche braucht eine Freigabe",
        "ARGUMENT 3 (Risiko), Umsetzung. Treppe des gebundenen Kapitals über die Zeit (Quartale 2027 bis 2029). Rauten = Entscheidungspunkte am Phasenende mit Kriterium. "
        "Stopp nach höchstens 2, 10 oder 50 Mio. €.", chapter="3 · Risiko")
q0, qw = X0 + 0.2, (W - 0.4) / 12
spans = [(0, 1), (1, 4), (4, 8), (8, 12)]
base_y, hmax = 5.15, 2.55
cum = [2, 10, 50, 80]
gates = ["Erhebung belastbar?", "Pilot auf Kurs zu ≥ 0,7 Pp?", "Marge ≥ 10 %?", "Fortführen?"]
for k, ((a, b), (nm, per, amt)) in enumerate(zip(spans, Mo.PH)):
    x1, x2 = q0 + a * qw, q0 + b * qw; hh = hmax * cum[k] / 80
    D.shape(S.RECTANGLE, x1, base_y - hh, x2 - x1 - 0.04, hh, fill=ZB if k < 2 else LB, alpha=None if k < 2 else 70, name=f"Phase {k + 1}")
    lab = f"{cum[k]} Mio. €" if k == 3 else str(cum[k])
    D.text(x1 + 0.08, base_y - hh - 0.42, 1.6 if k else 0.8, 0.36, lab, 20 if k >= 2 else 16, O, ZB if k < 2 else DB)
    D.text(x1, base_y + 0.1, x2 - x1, 0.25, per.upper(), 9, M, ZB, "l", spacing=60)
    D.text(x1, base_y + 0.34, x2 - x1 - 0.05, 0.5, nm, 11 if k == 0 else 12, M, DB)
    D.shape(S.DIAMOND, x2 - 0.2, base_y - hh - 0.16, 0.32, 0.32, fill=DB, name=f"Entscheidungspunkt {k + 1}", alt=gates[k])
gl = [(1, "Erhebung belastbar?"), (4, "Pilot auf Kurs zu ≥ 0,7 Pp?"), (8, "Marge ≥ 10 %?"), (12, "Fortführen?")]
for k, (q, t_) in enumerate(gl):
    gx = q0 + q * qw - 0.04
    yv = base_y - hmax * cum[k] / 80
    D.dash(gx, 2.05, gx, yv - 0.2, MB, 0.9)
    al = "r" if q == 12 else "c"
    bx = gx - 2.4 if q == 12 else gx - 1.3
    D.text(bx, 1.72, 2.6 if q != 12 else 2.4, 0.3, t_, 12, M, DB, al)
E.kicker(q0 + 1 * qw + 0.1, base_y - hmax * 10 / 80 - 0.75, 4, "10 Mio. € bis zum Pilotergebnis", ZB)
D.rule(q0, base_y, W - 0.4, DB, 0.015)
E.statement("Scheitert ein Entscheidungspunkt, stoppen wir nach höchstens 2, 10 oder 50 Mio. € statt nach 80.", y=6.45, size=16)
E.footer("Beispieldaten, fiktiv. Tranchen 2, 8, 40, 30 Mio. € (Annahme); Kriterien aus Folie 6 und 7.")

# ============================ 9 Entscheidung: Band + drei Karten ===============================================
E.slide("Wir bitten um 80 Mio. € Rahmen und 10 Mio. € sofort, damit wir im ersten Quartal starten",
        "ENTSCHEIDUNG: drei Beschlüsse, konsistent mit Folie 2. Entscheider und Termin unbekannt: [DATA NEEDED].")
E.blue_band(3.0, 1.9)
asks = [("hand-coins", "Beschluss 1", "10 Mio. €", "sofort freigeben", "Tranche 1 und 2: Erhebung prüfen (2) und Pilot in Cyber (8)"),
        ("seal-check", "Beschluss 2", "80 Mio. €", "als Rahmen zusagen", "Weitere 70 Mio. € nur nach bestandenen Entscheidungspunkten"),
        ("users-three", "Beschluss 3", "3", "Entscheider benennen", "für die drei Entscheidungspunkte mit Geldwirkung, nach den Kriterien von Folie 6 und 7")]
for i, (ic, lab, big_, head_, d_) in enumerate(asks):
    x = X0 + i * (cw_ := (W - 0.7) / 3) + i * 0.35
    E.white_card(x, 1.85, cw_, 3.85)
    D.icon(ic, x + 0.55, 2.4, 0.7)
    E.kicker(x + 1.05, 2.28, cw_ - 1.2, lab)
    E.big(x + 0.35, 2.85, cw_ - 0.6, big_, 44, ZB)
    D.text(x + 0.35, 3.72, cw_ - 0.6, 0.35, head_, 17, M, DB)
    D.rule(x + 0.35, 4.2, 0.6, ZB, 0.035)
    D.text(x + 0.35, 4.38, cw_ - 0.65, 1.2, d_, 14, L, DB)
D.text(X0, 6.05, W, 0.3, "Entscheider und Termin: [DATA NEEDED: Gremium und Termin der Entscheidung]", 14, M, DB)
E.footer("Beispieldaten, fiktiv. Tranchen und Entscheidungspunkte: Folie 8.")

# ============================ 10 Anhang: roter Faden ===========================================================
E.slide("Jede Folie belegt ein Argument, und die drei Argumente tragen die Empfehlung",
        "LERNFOLIE (Pyramidenprinzip): Frage → Antwort → drei überschneidungsfreie Argumente → Belegfolien mit Folientyp.", chapter="Anhang")
E.kicker(X0, 1.6, W, "Frage: Sollen wir gezielt in die Wachstumssegmente investieren, und lohnt es sich?", DB)
D.text(X0, 1.95, W, 0.5, "80 Mio. € für drei Wachstumssegmente, zurückverdient 2031, freigegeben in Stufen", 22, L, ZB)
D.rule(X0, 2.6, W, ZB, 0.02)
c3 = (W - 0.8) / 3
items = [("chart-line-up", "1 · Chance", "Der Markt wächst dort, wo wir klein sind", [("3", "Portfolio: Wachstum × Anteil"), ("4", "Kurve + Tempo-Streifen")]),
         ("coins", "2 · Ertrag", "Der Fokus verdient schneller zurück", [("5", "J-Kurve: kumuliertes Ergebnis"), ("6", "Raster: Sensitivität")]),
         ("shield-check", "3 · Risiko", "Das Risiko ist gestuft", [("7", "Zahlenpaar + Zufallsband"), ("8", "Kapital-Treppe mit Rauten")])]
for k, (ic, lab, cl, sl) in enumerate(items):
    x = X0 + k * (c3 + 0.4)
    D.vrule(x + 0.25, 2.62, 0.35, ZB, 0.02)
    D.icon(ic, x + 0.25, 3.35, 0.5, disc_=False)
    E.kicker(x + 0.65, 3.12, c3 - 0.7, lab)
    D.text(x + 0.65, 3.38, c3 - 0.7, 0.6, cl, 16, M, DB)
    for j, (n, d_) in enumerate(sl):
        yy = 4.25 + j * 0.62
        D.rule(x, yy - 0.06, c3, LB)
        E.big(x, yy, 0.6, n, 24, ZB)
        D.text(x + 0.6, yy + 0.06, c3 - 0.6, 0.3, d_, 13, L, DB)
E.statement("Folie 2 gibt die Antwort zuerst, Folie 9 bittet um die Entscheidung, alles dazwischen belegt ein Argument.", y=6.2, size=15)
E.footer("Lernfolie. Methode: skill_v2/references/storyline.md.")

# ============================ 11 Anhang: Annahmen =============================================================
E.slide("Alle Werte folgen aus sieben Annahmen, die wir offenlegen", "ANHANG: Methode. Jede Zahl kommt aus modell.py; asserts prüfen die Aussagen vor dem Bauen.", chapter="Anhang")
ass = [("Marktvolumen", "Gewerbe-Bruttoprämie 45,0 Mrd. € (2026) und 54,0 Mrd. € (2029) in acht Segmenten, Verlauf geometrisch."),
       ("Unser Anteil", "2026 je Segment fest; ohne Kurswechsel konstant; Gruppenwerte gewichtet nach Marktvolumen."),
       ("Anteilsgewinn", "Fokus +0,9 Pp auf drei Segmente, breit +0,3 Pp auf alle acht; Hochlauf 30 / 65 / 100 %."),
       ("Marge", "Ergebnis = zusätzliche Prämie × Marge: Fokus 12 %, breit 7 %; ab 2030 konstant."),
       ("Investition", "Fokus 80 Mio. € in Tranchen 2 / 8 / 40 / 30; breit 140 Mio. € (30 / 60 / 50)."),
       ("Befragung", "Monatlich 1.200 Gewerbekunden der Fokus-Segmente; Anteil mit Schutzbedarf."),
       ("Rechenwege", "Wachstum relativ (23 Monate = 1,92 Jahre); Amortisation = erstes Jahr mit kumuliertem Ergebnis ≥ 0.")]
for i, (k, v) in enumerate(ass):
    col, row = i % 2, i // 2
    x = X0 + col * (W / 2 + 0.2); y = 1.75 + row * 1.08
    D.rule(x, y - 0.08, W / 2 - 0.2, LB)
    E.big(x, y, 0.6, str(i + 1), 28, ZB)
    D.text(x + 0.6, y + 0.05, W / 2 - 0.9, 0.3, k, 15, M, DB)
    D.text(x + 0.6, y + 0.36, W / 2 - 0.9, 0.6, v, 13, L, DB)
E.footer("Beispieldaten, fiktiv. Pp = Prozentpunkte.")

# ============================ 12 Anhang: Segmentdaten (Tabelle ohne Kästen) ====================================
E.slide("Cyber wächst am schnellsten (20 % pro Jahr), dort ist unser Anteil am niedrigsten (2,0 %)", "ANHANG: Werte nachschlagen.", chapter="Anhang")
hdr = ["Segment", "Markt 2026", "Markt 2029", "Zuwachs", "Wachstum p. a.", "Anteil 2026"]
units = ["", "Mrd. €", "Mrd. €", "Mrd. €", "%", "%"]
cwid = [3.13, 1.8, 1.8, 1.8, 1.8, 1.8]
xs = [X0 + sum(cwid[:j]) for j in range(6)]
for j, (h_, u) in enumerate(zip(hdr, units)):
    D.text(xs[j], 1.6, cwid[j] - 0.1, 0.26, h_, 13, M, ZB, "l" if j == 0 else "r")
    D.text(xs[j], 1.88, cwid[j] - 0.1, 0.22, u, 11, L, DB, "l" if j == 0 else "r")
D.rule(X0, 2.18, W, ZB, 0.02)
rows_ = [[Mo.SEG[i], de(Mo.m26[i]), de(Mo.m29[i]), de(Mo.dz[i]), de(Mo.g[i] * 100), de(Mo.sh[i])] for i in range(8)]
rows_ += [["Fokus (3)", de(Mo.m26[Mo.FOKUS].sum()), de(Mo.m29[Mo.FOKUS].sum()), de(Mo.F_dz), de(Mo.F_g * 100), de(Mo.F_sh)],
          ["Übrige (5)", de(Mo.m26[Mo.REST].sum()), de(Mo.m29[Mo.REST].sum()), de(Mo.R_dz), de(Mo.R_g * 100), de(Mo.R_sh)]]
for i, r in enumerate(rows_):
    y = 2.28 + i * 0.4 + (0.12 if i >= 8 else 0)
    if i == 8: D.rule(X0, y - 0.08, W, ZB, 0.015)
    foc = i in (0, 1, 2, 8)
    if foc and i < 8: D.shape(S.RECTANGLE, X0 - 0.15, y + 0.06, 0.06, 0.26, fill=ZB, name="Fokus-Marke")
    for j, v in enumerate(r):
        D.text(xs[j], y, cwid[j] - 0.1, 0.38, v, 14, M if foc else L, DB, "l" if j == 0 else "r", "m")
    if i < 9: D.rule(X0, y + 0.39, W, "E3EAF2")
E.footer("Beispieldaten, fiktiv. Blaue Marke: Fokus-Segmente.")
D.save(sys.argv[1])
