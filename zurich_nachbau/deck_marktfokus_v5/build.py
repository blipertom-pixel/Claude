# -*- coding: utf-8 -*-
"""Marktfokus v5: komplett neu nach Review der Folien 1 bis 9 (Feedback 10.11.2026). Fiktive Daten aus modell.py.
Regeln: keine dunklen Folien, kein Band unten, keine Blöcke rechts, keine getönten Kästen, kein Diagramm ohne eigene Aussage."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skill_v2" / "scripts"))
import deck_lite as D
import editorial as E
from deck_lite import S, ZB, DB, MB, LB, WHITE, L, M, O
import modell as Mo
from modell import de

D.new_deck()
X0, W = E.X0, E.W
R = X0 + W
NB = " "
GREY = "8C96A8"
pct = lambda v, n=1: de(v, n) + NB + "%"
mio = lambda v: de(v, 0) + NB + "Mio. €"

def pair(x, y, w, title, rows, vmax, lab_w=1.0):
    E.kicker(x, y, w, title, DB)
    for k, (nm, v, col, lbl) in enumerate(rows):
        yy = y + 0.3 + k * 0.32
        D.text(x, yy, lab_w, 0.26, nm, 12, L, DB, "l", "m")
        bw = (w - lab_w - 0.75) * v / vmax
        D.shape(S.RECTANGLE, x + lab_w, yy + 0.06, bw, 0.14, fill=col)
        D.text(x + lab_w + bw + 0.07, yy, 0.8, 0.26, lbl, 12, M, DB, "l", "m")

# ================= 1 Titel =================================================================================
D.slide("Wo der Markt am stärksten wächst, setzen wir 80 Mio. € ein",
        "Titel. These in einem Satz. Zweck: Beschluss über 80 Mio. € in drei Stufen, 10 Mio. € sofort. Alle Zahlen sind fiktive Beispieldaten.", hero=True)
E.blue_band(2.0, 2.9)
for r_, a in [(3.4, 10), (2.5, 13), (1.6, 18)]:
    D.shape(S.DONUT, 13.333 - 2.0 - r_ / 2, 3.45 - r_ / 2, r_, r_, fill=WHITE, alpha=a).adjustments[0] = 0.06
for k, ic in enumerate(["shield-check", "heartbeat", "truck"]):
    D.icon(ic, 10.71 + k * 0.62, 3.45, 0.5, disc_=False, on_dark=True)
D._set_title("Wo der Markt am stärksten wächst,\nsetzen wir 80 Mio. € ein", X0 + 0.3, 2.6, 9.6, 2.1, 38, WHITE)
E.to_front(D.s().shapes.title)
D.text(X0 + 0.3, 5.25, 9.5, 0.35, "Vorlage zur Entscheidung  ·  Vorstand  ·  Marktfokus Gewerbe 2027 bis 2029", 17, M, DB)
D.text(X0 + 0.3, 5.65, 9, 0.35, "10. November 2026  ·  Beispieldaten, fiktiv", 14, L, DB)

# ================= 2 Antwort zuerst =======================================================================
E.slide(f"Wir setzen 80 Mio. € auf drei Wachstumssegmente, in denen Beratung zählt, zurückverdient {Mo.PB_BASE}",
        "ANTWORT ZUERST. Situation: Der Gewerbemarkt wächst bis 2029 von 49,5 auf 60,7 Mrd. €. Komplikation: 58 % des Zuwachses liegen in drei Segmenten, "
        "in denen unser Anteil am kleinsten ist; ohne Kurswechsel wachsen wir langsamer als der Markt. Frage: Lohnt sich ein gezielter Einsatz? "
        "Antwort: ja, drei Gründe (Markt, Kunde, Ertrag), jede Karte mit ihrem Vergleich als Beleg. Details Folie 3 bis 9.", title_w=10.3)
E.blue_band(2.75, 2.0)
cw = (W - 2 * 0.35) / 3
cards = [("chart-line-up", "1 · Markt", "Der Markt wächst dort,\nwo wir klein sind", pct(Mo.F_dz_share * 100, 0), "des Marktzuwachses bis 2029\nliegen in drei Segmenten",
          "UNSER ANTEIL 2026", [("Fokus", Mo.F_sh, ZB, pct(Mo.F_sh)), ("übrige", Mo.R_sh, LB, pct(Mo.R_sh))], 3.6),
         ("handshake", "2 · Kunde", "Dort zählt Beratung\nmehr als der Preis", f"{Mo.R_FOK[0]}{NB}%", "nennen Beratung als\nHauptgrund für den Abschluss",
          "HAUPTGRUND, FOKUS-SEGMENTE", [("Beratung", Mo.R_FOK[0], ZB, f"{Mo.R_FOK[0]}{NB}%"), ("Preis", Mo.R_FOK[2], LB, f"{Mo.R_FOK[2]}{NB}%")], 41),
         ("coins", "3 · Ertrag", "Der Einsatz ist früh\nzurückverdient", str(Mo.PB_BASE), f"Amortisation im Basisfall,\nim vorsichtigen Fall {Mo.PB_CAUT}",
          "KUMULIERT BIS 2035, MIO. €", [("Basisfall", Mo.BASE[-1]["cum"], ZB, "+" + de(Mo.BASE[-1]["cum"], 0)), ("vorsichtig", Mo.CAUT[-1]["cum"], LB, "+" + de(Mo.CAUT[-1]["cum"], 0))], Mo.BASE[-1]["cum"])]
for i, (ic, lab, claim, num, cap, ctitle, rows, vmax) in enumerate(cards):
    x = X0 + i * (cw + 0.35)
    E.white_card(x, 1.75, cw, 4.15)
    D.icon(ic, x + 0.55, 2.27, 0.66)
    E.kicker(x + 1.05, 2.15, cw - 1.2, lab)
    D.text(x + 0.35, 2.72, cw - 0.6, 0.62, claim, 16, M, DB)
    E.big(x + 0.35, 3.3, cw - 0.6, num, 46, ZB)
    D.text(x + 0.35, 4.12, cw - 0.6, 0.5, cap, 12, L, DB)
    pair(x + 0.35, 4.82, cw - 0.6, ctitle, rows, vmax, lab_w=1.0)
E.statement("Wir bitten um 80 Mio. € in drei Stufen und 10 Mio. € sofort für den Pilot in Cyber.", y=6.38, size=17)
E.footer("Anmerkung: Beispieldaten, fiktiv; Fokus = Cyber, Gesundheit, Logistik. Quelle: Marktstudie 2026; Kundenbefragung 2026 (n = 1.200); Szenariomodell")

# ================= 3 Markt: Mekko ==========================================================================
E.slide(f"{pct(Mo.F_dz_share * 100, 0)} des Marktzuwachses liegen in drei Segmenten, in denen unser Anteil am niedrigsten ist",
        "ARGUMENT 1 (Markt). Ein Bild mit zwei Dimensionen: Breite = Zuwachs 2026 bis 2029 (wo das Geld hinzukommt), Höhe = unser Anteil. "
        "Links die breiten, niedrigen Säulen = viel Wachstum, wenig Anteil. Ersetzt die alten Folien 3 und 4 (Kleinlinien ohne Aussage, doppelte Mini-Diagramme).", chapter="Markt")
E.kicker(X0, 1.6, W, "Breite = Marktzuwachs 2026 bis 2029  ·  Höhe = unser Marktanteil 2026", DB)
grp = [(0, "Cyber"), (1, "Gesundheit"), (2, "Logistik"), (3, "Handwerk"), (4, "Freie Berufe")]
idx_r = [5, 6, 7]
items = [(nm, Mo.dz[i], Mo.sh[i], i in Mo.FOKUS) for i, nm in grp]
items.append(("Übrige drei", Mo.dz[idx_r].sum(), (Mo.m26[idx_r] * Mo.sh[idx_r]).sum() / Mo.m26[idx_r].sum(), False))
px, pw, base, sc = X0 + 0.45, W - 0.45, 5.3, 0.62
tot = sum(it[1] for it in items)
for v in (0, 1, 2, 3, 4):
    D.text(X0 - 0.15, base - v * sc - 0.12, 0.5, 0.24, f"{v}{NB}%", 10, L, GREY, "r")
x = px; fx = []
for nm, dz, s_, foc in items:
    w = pw * dz / tot; h = s_ * sc
    D.shape(S.RECTANGLE, x + 0.02, base - h, w - 0.04, h, fill=ZB if foc else LB, name=f"Säule {nm}", alt=f"{nm}: Zuwachs {de(dz)} Mrd. €, Anteil {de(s_)} %")
    ly = base - h + 0.08
    yl = base - Mo.share26 * sc
    if yl - 0.35 < base - h < yl + 0.1: ly = yl + 0.07
    D.text(x, ly, w, 0.3, pct(s_), 15, M, WHITE if foc else DB, "c")
    D.text(x, base + 0.08, w, 0.26, nm, 12, M if foc else L, DB, "c")
    D.text(x, base + 0.33, w, 0.24, f"+{de(dz)} Mrd. €", 11, L, DB, "c")
    fx.append((x, w)); x += w
D.rule(px, base, pw, DB, 0.014)
ya = base - Mo.share26 * sc
D.dash(px, ya, px + pw, ya, DB, 1.25)
D.text(px + 0.1, ya - 0.3, 4.2, 0.26, f"unser Anteil über alle Segmente {pct(Mo.share26)}", 12, M, DB)
bx0, bx1 = fx[0][0] + 0.02, fx[2][0] + fx[2][1] - 0.02
E_br = 2.6
D.rule(bx0, E_br, bx1 - bx0, ZB, 0.025); D.shape(S.RECTANGLE, bx0, E_br, 0.025, 0.14, fill=ZB); D.shape(S.RECTANGLE, bx1 - 0.025, E_br, 0.025, 0.14, fill=ZB)
D.text(bx0, E_br - 0.42, bx1 - bx0, 0.34, f"{pct(Mo.F_dz_share * 100, 0)} des Zuwachses ({de(Mo.dz[Mo.FOKUS].sum())} Mrd. €), unser Anteil dort {pct(Mo.F_sh)}", 15, M, ZB, "c")
yF = base - Mo.F_sh * sc
xg = fx[2][0] + fx[2][1] + 0.12
D.vrule(xg, ya, yF - ya, DB, 0.025)
D.shape(S.RECTANGLE, xg - 0.06, ya, 0.14, 0.02, fill=DB); D.shape(S.RECTANGLE, xg - 0.06, yF - 0.02, 0.14, 0.02, fill=DB)
D.text(xg - 4.6, ya + 0.06, 4.5, 0.28, f"Lücke {de(Mo.GAP_PP)} Pp = {mio(Mo.PRIZE)} Beitrag pro Jahr ab 2029", 13, M, DB, "r")
E.statement(f"Ohne Kurswechsel sinkt unser Gesamtanteil bis 2029 von {pct(Mo.share26)} auf {pct(Mo.share29_ohne)}.", y=6.38, size=16)
E.footer(f"Anmerkung: Beispieldaten, fiktiv; übrige drei = Industrie, Handel, Gastro; Lücke bewertet am Fokusmarkt 2029 ({de(Mo.m29[Mo.FOKUS].sum())} Mrd. €). Quelle: Marktstudie 2026, Bruttoprämie Gewerbe")

# ================= 4 Auswahl: Filter =======================================================================
E.slide("Von acht Segmenten erfüllen nur Cyber, Gesundheit und Logistik alle drei Kriterien",
        "AUSWAHL. Ersetzt Venn-Diagramm und Rangtabelle (alte Folien 5 und 6): ein Filter in drei Stufen. Spalte für Spalte fällt weg, wer die Schwelle verfehlt. "
        "Marktanteil ist kein Auswahlkriterium mehr (niedriger Anteil kann auch Schwäche heißen), sondern die Chance aus Folie 3. Handwerk scheitert nur an der Combined Ratio.", chapter="Auswahl")
order = [0, 1, 2, 3, 4, 5, 6, 7]
cols_ = [("Segment", None, 2.4), ("Wachstum p. a.", f"über Markt ({pct(Mo.mkt_g * 100)})", 2.75), ("Beratungsbedarf", "mindestens 60 % der Kunden", 2.75),
         ("Combined Ratio", "unter 95 %", 2.75), ("", None, 1.48)]
xs = [X0]; [xs.append(xs[-1] + c[2]) for c in cols_[:-1]]
counts = [8, len(Mo.STEP1), len(Mo.STEP2), len(Mo.STEP3)]
for j, (h_, sub, w) in enumerate(cols_[:4]):
    E.big(xs[j], 1.5, 0.9, str(counts[j]), 34, ZB if j == 3 else DB)
    D.text(xs[j] + 0.62 if counts[j] < 10 else xs[j] + 0.8, 1.73, 1.8, 0.26, "Segmente" if j == 0 else "bleiben", 12, L, DB)
    if j: D.text(xs[j] - 0.28, 1.68, 0.3, 0.3, "→", 16, M, ZB)
    if h_ != "Segment":
        D.text(xs[j], 2.15, w - 0.2, 0.26, h_, 13, M, DB)
        D.text(xs[j], 2.4, w - 0.2, 0.24, sub, 11, L, DB)
D.rule(X0, 2.72, W, DB, 0.015)
vals = [lambda i: pct(Mo.g[i] * 100), lambda i: f"{Mo.ber[i]}{NB}%", lambda i: pct(Mo.cr[i])]
passes = [lambda i: i in Mo.STEP1, lambda i: i in Mo.STEP2, lambda i: i in Mo.STEP3]
for r_, i in enumerate(order):
    y = 2.8 + r_ * 0.39
    foc = i in Mo.FOKUS
    dropped_at = next((k for k in range(3) if not passes[k](i)), None)
    if foc: D.shape(S.RECTANGLE, X0 - 0.16, y + 0.06, 0.06, 0.27, fill=ZB, name="Fokus-Marke")
    D.text(X0, y, 2.3, 0.38, Mo.SEG[i], 14, M if foc else L, DB if dropped_at is None or dropped_at > 0 else GREY, "l", "m")
    for k in range(3):
        cx = xs[k + 1]
        if dropped_at is not None and k > dropped_at:
            D.text(cx, y, 1.0, 0.38, "–", 13, L, GREY, "l", "m"); continue
        ok = passes[k](i)
        D.text(cx, y, 1.0, 0.38, vals[k](i), 14, M if ok else L, DB if ok else GREY, "l", "m")
        if ok: D.icon("check-circle", cx + 1.15, y + 0.19, 0.24, disc_=False)
        else: D.text(cx + 1.0, y, 1.6, 0.38, "verfehlt", 12, M, GREY, "l", "m")
    D.text(xs[4], y, 1.5, 0.38, "im Fokus" if foc else "", 13, M, ZB, "l", "m")
    if r_ < 7: D.rule(X0, y + 0.385, W, "E3EAF2")
E.statement(f"Handwerk verfehlt nur die Combined Ratio ({pct(Mo.cr[3])}): ein Kandidat für später, wenn die Schadenquote sinkt.", y=6.38, size=16)
E.footer("Anmerkung: Beispieldaten, fiktiv; Schwellen sind Vorschläge zur Bestätigung durch den Vorstand. Quelle: Marktstudie 2026; Kundenbefragung 2026 (n = 1.200); Schadenstatistik 2023 bis 2025")

# ================= 5 Kunde ==================================================================================
E.slide(f"In den Fokus-Segmenten schließen {Mo.R_FOK[0]}{NB}% der Kunden wegen der Beratung ab, nur {Mo.R_FOK[2]}{NB}% wegen des Preises",
        "ARGUMENT 2 (Kunde). Links: Wer ist der Kunde, was braucht er, was bieten wir (Persona aus einem Fokus-Segment, nicht aus Handwerk wie in der alten Folie 7). "
        "Rechts: Beleg, wie sich die Kaufgründe zwischen Fokus und übrigen Segmenten unterscheiden (Hantel-Diagramm statt dritter Wiederholung des Beratungsbedarfs).", chapter="Kunde")
LW = 5.75
D.icon("truck", X0 + 0.55, 2.1, 1.0)
D.text(X0 + 1.3, 1.68, LW - 1.3, 0.32, "Sandra K., Geschäftsführerin Spedition", 16, M, DB)
D.text(X0 + 1.3, 2.02, LW - 1.3, 0.26, "120 Beschäftigte, 60 Lkw  ·  Beispielprofil, fiktiv", 12, L, DB)
D.icon("quotes", X0 + 1.42, 2.55, 0.28, disc_=False)
D.text(X0 + 1.65, 2.4, LW - 1.65, 0.7, "Ich brauche jemanden, der Flotte, Lager und Cyber-Risiken zusammen versteht und im Schaden sofort da ist.", 14, L, ZB)
E.kicker(X0, 3.35, 2.6, "Sie braucht", DB); E.kicker(X0 + 3.1, 3.35, 2.65, "Wir bieten", ZB)
needs = [("users-three", "eine Ansprechperson für alle Risiken", "festen Gewerbe-Berater je Kunde"),
         ("timer", "schnelle Hilfe im Schaden", "Regulierung in 48 Stunden"),
         ("puzzle-piece", "Verständnis für ihr Geschäft", "Branchenpakete für Logistik, Cyber, Gesundheit")]
for k, (ic, need, offer) in enumerate(needs):
    y = 3.7 + k * 0.72
    D.rule(X0, y - 0.06, LW, "E3EAF2")
    D.icon(ic, X0 + 0.2, y + 0.27, 0.36, disc_=False)
    D.text(X0 + 0.5, y, 2.3, 0.6, need, 13, L, DB, "l", "m")
    D.text(X0 + 2.83, y, 0.3, 0.6, "→", 14, M, ZB, "l", "m")
    D.text(X0 + 3.1, y, 2.65, 0.6, offer, 13, M, DB, "l", "m")
# rechts: Hantel-Diagramm
RX = X0 + LW + 0.6; RW = R - RX
D.vrule(RX - 0.3, 1.7, 4.2, "E3EAF2")
E.kicker(RX, 1.68, RW, "Hauptgrund für den Abschluss, % der Kunden", DB)
D.disc(RX + 0.08, 2.1, 0.16, ZB); D.text(RX + 0.22, 1.97, 1.8, 0.26, "Fokus-Segmente", 12, M, DB)
D.disc(RX + 2.0, 2.1, 0.16, LB); D.text(RX + 2.14, 1.97, 1.6, 0.26, "übrige fünf", 12, L, DB)
lab_w = 1.75; sx = RX + lab_w; sw = RW - lab_w - 0.25
X = lambda v: sx + sw * v / 45
for k, (rs, a, b) in enumerate(zip(Mo.REASONS, Mo.R_FOK, Mo.R_REST)):
    y = 2.75 + k * 0.92
    D.text(RX, y - 0.15, lab_w - 0.1, 0.3, rs, 13, M if k in (0, 2) else L, DB, "l", "m")
    D.rule(sx, y, sw, "EEF1F4", 0.01)
    D.rule(min(X(a), X(b)), y - 0.012, abs(X(a) - X(b)), MB, 0.03)
    D.disc(X(b), y, 0.2, LB); D.disc(X(a), y, 0.24, ZB)
    up = a >= b
    D.text(X(a) - 0.4, y - 0.42, 0.8, 0.24, f"{a}{NB}%", 12, M, ZB, "c")
    D.text(X(b) - 0.4, y + 0.16, 0.8, 0.24, f"{b}{NB}%", 11, L, DB, "c")
    if k in (0, 2):
        dd = a - b
        D.text(max(X(a), X(b)) + 0.18, y - 0.13, 1.0, 0.26, f"{'+' if dd > 0 else '−'}{abs(dd)} Pp", 12, M, ZB if dd > 0 else DB)
E.statement("Beratung ist unsere Stärke: Vermittler sehen uns dort auf Platz 2 von 14 Versicherern.", y=6.42, size=16)
E.footer("Anmerkung: Beispieldaten, fiktiv; ein Hauptgrund je Kunde; Persona und Zitat sind Beispiele. Quelle: Kundenbefragung 2026 (n = 1.200); Vermittlerbefragung 2026 (n = 412)")

# ================= 6 Beitrag =================================================================================
E.slide(f"Ohne Fokus wachsen wir langsamer als der Markt, mit Fokus kommen 2029 {mio(Mo.B_plus)} Beitrag dazu",
        f"ARGUMENT 3 (Ertrag), Umsatzseite. Brücke von 1.556 auf 2.148 Mio. € mit voller Achse (alte Folie 9 hatte eine abgeschnittene Achse). "
        f"Gestrichelt: so viel hätten wir, wenn wir mit dem Markt wüchsen (+{pct(Mo.mkt_g * 100)} p. a.). Ohne Fokus liegen wir darunter (Anteilsverlust), mit Fokus darüber.", chapter="Ertrag")
E.kicker(X0, 1.6, W, "Beitrag in Mio. € (Bruttoprämie Gewerbe)", DB)
bars = [("Beitrag 2026", 0, Mo.B26, "total"), ("Marktwachstum\nbei gleichem Anteil", Mo.B26, Mo.B29_ohne, "delta"),
        ("2029 ohne Fokus", 0, Mo.B29_ohne, "total"), ("Anteilsgewinn\nFokus (+1,5 Pp)", Mo.B29_ohne, Mo.B29_mit, "deltaF"), ("2029 mit Fokus", 0, Mo.B29_mit, "totalF")]
base, scale = 5.35, 3.15 / 2300
bw, gap = 1.55, (W - 0.6 - 5 * 1.55) / 4
bxs = [X0 + 0.3 + k * (bw + gap) for k in range(5)]
Yv = lambda v: base - v * scale
for k, (nm, a, b, kind) in enumerate(bars):
    col = {"total": LB, "delta": LB, "deltaF": ZB, "totalF": ZB}[kind]
    D.shape(S.RECTANGLE, bxs[k], Yv(b), bw, Yv(a) - Yv(b), fill=col, alpha=None if kind != "delta" else 60, name=nm.replace("\n", " "))
    lbl = de(b, 0) if kind.startswith("total") else f"+{de(b - a, 0)}"
    ly_ = Yv(b) - 0.42 if k != 2 else Yv(Mo.B29_markt) - 0.45
    D.text(bxs[k] - 0.2, ly_, bw + 0.4, 0.36, lbl, 22 if kind.startswith("total") else 18, O, ZB if "F" in kind else DB, "c")
    D.text(bxs[k] - 0.25, base + 0.08, bw + 0.5, 0.5, nm, 12, M if "F" in kind else L, DB, "c")
    if k < 4:
        nxt = b if kind != "total" else b
        D.rule(bxs[k] + bw, Yv(b), gap, GREY, 0.01)
D.rule(X0, base, W, DB, 0.014)
ym = Yv(Mo.B29_markt)
D.dash(bxs[2] - 0.08, ym, bxs[2] + bw + 0.08, ym, DB, 1.5)
xq = bxs[2] + bw + 0.14
D.vrule(xq, ym, Yv(Mo.B29_ohne) - ym, DB, 0.025)
D.shape(S.RECTANGLE, xq - 0.06, ym, 0.14, 0.02, fill=DB); D.shape(S.RECTANGLE, xq - 0.06, Yv(Mo.B29_ohne) - 0.02, 0.14, 0.02, fill=DB)
D.text(xq + 0.1, Yv(Mo.B29_ohne) + 0.08, gap - 0.15, 0.75, f"−{de(Mo.B29_markt - Mo.B29_ohne, 0)} zum\nMarkt\n({de(Mo.B29_markt, 0)})", 11, M, DB)
D.text(bxs[2], Yv(Mo.B29_ohne) + 0.12, bw, 0.5, f"+{pct(Mo.g_ohne * 100)} p. a.\nAnteil {pct(Mo.share29_ohne)}", 12, M, DB, "c")
D.text(bxs[4], Yv(Mo.B29_mit) + 0.08, bw, 0.5, f"+{pct(Mo.g_mit * 100)} p. a.\nAnteil {pct(Mo.share29_mit)}", 12, M, WHITE, "c")
D.text(bxs[0], Yv(Mo.B26) + 0.08, bw, 0.3, f"Anteil {pct(Mo.share26)}", 12, M, DB, "c")
E.statement(f"Ohne Fokus fehlen 2029 {mio(Mo.B29_markt - Mo.B29_ohne)} zum Marktwachstum, mit Fokus liegen wir {mio(Mo.B29_mit - Mo.B29_markt)} darüber.", y=6.42, size=16)
E.footer(f"Anmerkung: Beispieldaten, fiktiv; ohne Fokus: Anteile je Segment konstant; mit Fokus: +1,5 Pp in den drei Segmenten; gestrichelt: Wachstum mit dem Markt (+{pct(Mo.mkt_g * 100)} p. a.). Quelle: Marktstudie 2026; Szenariomodell")

# ================= 7 Ergebnis ================================================================================
E.slide(f"Der Fokus ist im Basisfall {Mo.PB_BASE} zurückverdient, im vorsichtigen Fall {Mo.PB_CAUT}",
        f"ARGUMENT 3 (Ertrag), Ergebnisseite. Kumuliertes Mehrergebnis nach Investition, nur dem Fokus zugerechnet: zusätzlicher Beitrag × (1 − Combined Ratio der Fokus-Segmente "
        f"{pct(Mo.cr_f)}). Keine Verwaltungskosten-Effekte eingerechnet (die waren in der alten Fassung nicht dem Fokus zuzuordnen). Vorsichtig: +1,0 Pp, Marge 5 %.", chapter="Ertrag")
E.kicker(X0, 1.6, W, "Kumuliertes Mehrergebnis nach Investition, Mio. €", DB)
yrs = [str(r["year"]) for r in Mo.BASE]
cb = [r["cum"] for r in Mo.BASE]; cc = [r["cum"] for r in Mo.CAUT]
X, Y, (pl, pw_, pb) = D.lines(X0, 1.95, W - 1.7, 3.85, yrs, [("Basisfall", cb, ZB, 4.0), ("Vorsichtig", cc, MB, 2.5)], -75, 145,
                             inner=(0.0, 0.02, 1.0, 0.92), markers=False,
                             alt=f"Liniendiagramm 2027 bis 2035: Basisfall Tiefpunkt {de(Mo.TROUGH)} Mio. €, ab {Mo.PB_BASE} positiv, 2035 +{de(cb[-1], 0)}; vorsichtig ab {Mo.PB_CAUT} positiv.")
D.shape(S.RECTANGLE, pl, Y(0), pw_, Y(-75) - Y(0), fill=LB, alpha=14, name="Investitionsphase")
D.rule(pl, Y(0), pw_, DB, 0.014)
for i, yv in enumerate(yrs): D.text(X(i) - 0.4, pb + 0.05, 0.8, 0.24, yv, 11, L, DB, "c")
for yrp, ser, col, up in ((Mo.PB_BASE, cb, ZB, True), (Mo.PB_CAUT, cc, MB, False)):
    i = Mo.YEARS.index(yrp); D.disc(X(i), Y(ser[i]), 0.22, col)
    if up:
        E.leader(X(i), Y(ser[i]) - 0.13, X(i), Y(ser[i]) - 0.95, ZB, 1.0)
        E.big(X(i) - 1.1, Y(ser[i]) - 1.78, 2.2, str(yrp), 48, ZB, "c")
    else:
        E.leader(X(i), Y(ser[i]) + 0.13, X(i), Y(ser[i]) + 0.55, MB, 1.0)
        E.big(X(i) - 1.1, Y(ser[i]) + 0.5, 2.2, str(yrp), 30, DB, "c")
lx = X(8) + 0.2
D.text(lx, Y(0) + 0.05, 1.7, 0.4, "unter der Linie: Einsatz\nnoch nicht zurück", 10, L, DB)
D.text(lx, Y(cb[-1]) - 0.25, 1.6, 0.3, f"+{de(cb[-1], 0)}", 18, M, ZB); D.text(lx, Y(cb[-1]) + 0.05, 1.6, 0.26, "Basisfall", 12, M, ZB)
D.text(lx, Y(cc[-1]) - 0.25, 1.6, 0.3, f"+{de(cc[-1], 0)}", 18, M, DB); D.text(lx, Y(cc[-1]) + 0.05, 1.6, 0.26, "vorsichtig", 12, L, DB)
D.rule(X0, 6.25, 0.35, ZB, 0.05); D.text(X0 + 0.45, 6.12, 5.6, 0.28, f"Basisfall: +1,5 Pp Anteil, Marge {pct(100 - Mo.cr_f)} (Combined Ratio {pct(Mo.cr_f)})", 13, M, DB)
D.rule(X0 + 6.3, 6.25, 0.35, MB, 0.035); D.text(X0 + 6.75, 6.12, 5.4, 0.28, "Vorsichtig: +1,0 Pp Anteil, Marge 5,0 %", 13, L, DB)
D.text(X0, 6.45, W, 0.28, f"Am Tiefpunkt 2029 sind netto {de(-Mo.TROUGH)} Mio. € gebunden; ab 2029 bringt der Fokus im Basisfall rund {mio(Mo.RES29)} Mehrergebnis pro Jahr.", 13, L, DB)
E.footer("Anmerkung: Beispieldaten, fiktiv; Mehrergebnis = zusätzlicher Beitrag × (1 − Combined Ratio); Einsatz 10 / 40 / 30 Mio. € (2027 bis 2029); Hochlauf 20 / 55 / 100 %; Märkte ab 2033 konstant. Quelle: Szenariomodell")

# ================= 8 Risiken ===================================================================================
E.slide(f"Keines der vier Hauptrisiken verschiebt die Amortisation über {max(Mo.RISK_PB)} hinaus, jedes zeigt sich vor der nächsten Stufe",
        "RISIKEN. Jedes Risiko einzeln im Modell gerechnet (übrige Annahmen wie Basisfall). Rechts die Wirkung auf das Amortisationsjahr als Punktdiagramm: Basisfall 2031 gestrichelt. "
        "Die Spalte Frühindikator zeigt, an welchem Entscheidungspunkt wir das Risiko sehen, bevor die nächste Tranche fließt.", chapter="Risiken")
cols_r = [("Risiko", 3.3), ("Gegenmaßnahme", 3.25), ("Frühindikator", 2.5), ("Amortisation", 3.08)]
xr = [X0]; [xr.append(xr[-1] + c[1]) for c in cols_r[:-1]]
for j, (h_, w) in enumerate(cols_r):
    E.kicker(xr[j] + (0.55 if j == 0 else 0), 1.7, w - 0.2, h_, DB)
D.rule(X0, 2.02, W, DB, 0.015)
ax0, ax1, y0, y1 = xr[3] + 0.1, R - 0.15, 2030, 2035
AX = lambda yv: ax0 + (ax1 - ax0) * (yv - y0) / (y1 - y0)
icons_r = ["chart-pie-slice", "scales", "users-three", "stack"]
counter = [("Pilot in einem Segment, Ausweitung nur bei Erfolg", "Anteil im Pilot nach 9 Monaten", "Entscheidungspunkt 1"),
           ("Tarifierung je Segment, Annahmerichtlinien", "Combined Ratio im Neugeschäft", "Entscheidungspunkt 2"),
           ("Berater ab Q4 2026 rekrutieren, Vermittler einbinden", "Besetzte Stellen je Quartal", "laufend"),
           ("Neugeschäft getrennt messen, Provision nur für Neukunden", "Anteil Umdeckungen aus Bestand", "Entscheidungspunkt 1")]
ry0, rh = 2.12, 0.92
for k, ((nm, _), pb, (cm, ind, gate)) in enumerate(zip(Mo.RISKS, Mo.RISK_PB, counter)):
    y = ry0 + k * rh
    D.icon(icons_r[k], X0 + 0.22, y + 0.42, 0.42)
    D.text(X0 + 0.55, y + 0.08, cols_r[0][1] - 0.7, 0.7, nm, 14, M, DB, "l", "m")
    D.text(xr[1], y + 0.08, cols_r[1][1] - 0.25, 0.7, cm, 13, L, DB, "l", "m")
    D.text(xr[2], y + 0.08, cols_r[2][1] - 0.2, 0.5, ind, 13, L, DB)
    D.text(xr[2], y + 0.6, cols_r[2][1] - 0.2, 0.24, gate, 11, M, ZB)
    D.rule(ax0, y + 0.42, ax1 - ax0, "E3EAF2", 0.012)
    D.rule(AX(Mo.PB_BASE), y + 0.405, AX(pb) - AX(Mo.PB_BASE), MB, 0.035)
    D.disc(AX(pb), y + 0.42, 0.22, ZB)
    D.text(AX(pb) + 0.16, y + 0.29, 0.8, 0.26, str(pb), 13, M, DB)
    D.rule(X0, y + rh - 0.02, W, "E3EAF2")
yb = ry0 + 4 * rh
D.dash(AX(Mo.PB_BASE), ry0 + 0.05, AX(Mo.PB_BASE), yb - 0.05, DB, 1.25)
D.dash(AX(Mo.PB_CAUT), ry0 + 0.05, AX(Mo.PB_CAUT), yb - 0.05, GREY, 1.0)
for yv in range(y0, y1 + 1): D.text(AX(yv) - 0.3, yb + 0.02, 0.6, 0.22, str(yv), 10, L, DB, "c")
D.text(AX(Mo.PB_BASE) - 1.0, yb + 0.24, 2.0, 0.22, "Basisfall", 10, M, DB, "c")
D.text(AX(Mo.PB_CAUT) - 1.0, yb + 0.24, 2.0, 0.22, "alle schlecht", 10, L, GREY, "c")
E.statement(f"Treten alle Risiken zugleich ein (vorsichtiger Fall), ist der Einsatz {Mo.PB_CAUT} zurückverdient, nicht verloren.", y=6.42, size=16)
E.footer("Anmerkung: Beispieldaten, fiktiv; jedes Risiko einzeln gerechnet, übrige Annahmen wie Basisfall (Folie 7). Quelle: Szenariomodell")

# ================= 8 Umsetzung ===============================================================================
E.slide("Bis zum Pilotergebnis stehen nur 10 Mio. € im Risiko, jede weitere Stufe braucht eine Freigabe",
        "UMSETZUNG. Treppe = Geld, das zu jedem Zeitpunkt höchstens im Risiko steht. Rauten = Entscheidungspunkte am Ende einer Stufe, mit messbarem Kriterium. "
        "Scheitert ein Entscheidungspunkt, stoppen wir nach 10 oder 50 statt 80 Mio. €.", chapter="Umsetzung")
q0, qw = X0 + 0.1, (W - 0.2) / 12
spans = [(0, 4), (4, 8), (8, 12)]
base, hmax = 5.0, 2.45
gates = [("Entscheidungspunkt 1 · Oktober 2027", "Ist unser Anteil in Cyber im Pilot um mindestens 0,5 Pp gestiegen?"),
         ("Entscheidungspunkt 2 · Dezember 2028", "Liegt die Combined Ratio im Neugeschäft unter 95 %?")]
what = ["Branchenpaket Cyber, 25 Gewerbe-Berater, Schadenservice 48 Stunden", "Pakete Gesundheit und Logistik, Vertrieb auf 80 Berater", "Alle drei Segmente im Regelbetrieb, Steuerung auf Jahreswerte"]
for k, ((a, b), (nm, per, amt)) in enumerate(zip(spans, Mo.STAGES)):
    x1, x2 = q0 + a * qw, q0 + b * qw; hh = hmax * Mo.AT_RISK[k] / 80
    D.shape(S.RECTANGLE, x1, base - hh, x2 - x1 - 0.05, hh, fill=ZB if k == 0 else LB, alpha=None if k == 0 else 75, name=f"Stufe {k + 1}")
    ty = base - hh - 0.78 if k == 0 else base - hh + 0.08
    E.big(x1 + 0.12, ty, 3.2, mio(Mo.AT_RISK[k]), 22, ZB if k == 0 else DB)
    D.text(x1 + 0.12, ty + 0.44, 3.2, 0.24, f"im Risiko, davon {amt} Mio. € in dieser Stufe", 11, L, DB)
    E.kicker(x1, base + 0.1, x2 - x1, f"Stufe {k + 1}  ·  {per}", ZB)
    D.text(x1, base + 0.36, x2 - x1 - 0.2, 0.3, nm, 14, M, DB)
    D.text(x1, base + 0.66, x2 - x1 - 0.25, 0.5, what[k], 12, L, DB)
for k, (gh, gq) in enumerate(gates):
    gx = q0 + spans[k][1] * qw - 0.05
    yv = base - hmax * Mo.AT_RISK[k] / 80
    D.shape(S.DIAMOND, gx - 0.17, yv - 0.17, 0.34, 0.34, fill=DB, name=f"Entscheidungspunkt {k + 1}", alt=gq)
    ty = 1.68
    D.dash(gx, ty + 0.05, gx, yv - 0.2, MB, 0.9)
    D.text(gx + 0.15, ty, 3.75, 0.26, gh, 12, M, ZB)
    D.text(gx + 0.15, ty + 0.27, 3.75, 0.55, gq, 13, M, DB)
D.rule(q0, base, W - 0.2, DB, 0.015)
E.statement("Scheitert ein Entscheidungspunkt, stoppen wir nach 10 oder 50 Mio. € statt nach 80.", y=6.42, size=16)
E.footer("Anmerkung: Beispieldaten, fiktiv; Stufen 10 / 40 / 30 Mio. €; Kriterien aus Folie 4 (Combined Ratio) und Folie 8 (Anteilsgewinn). Quelle: Szenariomodell")

# ================= 9 Entscheidung =============================================================================
E.slide("Wir bitten heute um drei Beschlüsse, damit der Pilot in Cyber im Februar 2027 startet",
        "ENTSCHEIDUNG. Drei Beschlüsse, konsistent mit Folie 2 und 9. Namen und Termine sind Beispiele.")
E.blue_band(3.0, 1.9)
asks = [("hand-coins", "Beschluss 1", "10 Mio. €", "sofort freigeben", "für den Pilot in Cyber, Februar bis Oktober 2027"),
        ("seal-check", "Beschluss 2", "80 Mio. €", "als Rahmen zusagen", "weitere 70 Mio. € nur nach bestandenen Entscheidungspunkten"),
        ("users-three", "Beschluss 3", "2", "Entscheider benennen", "für die zwei Entscheidungspunkte: CFO, Leitung Gewerbe, Leitung Vertrieb")]
cw_ = (W - 0.7) / 3
for i, (ic, lab, big_, head_, d_) in enumerate(asks):
    x = X0 + i * (cw_ + 0.35)
    E.white_card(x, 1.85, cw_, 3.85)
    D.icon(ic, x + 0.55, 2.4, 0.7)
    E.kicker(x + 1.05, 2.28, cw_ - 1.2, lab)
    E.big(x + 0.35, 2.85, cw_ - 0.6, big_, 44, ZB)
    D.text(x + 0.35, 3.72, cw_ - 0.6, 0.35, head_, 17, M, DB)
    D.rule(x + 0.35, 4.2, 0.6, ZB, 0.035)
    D.text(x + 0.35, 4.38, cw_ - 0.65, 1.2, d_, 14, L, DB)
D.icon("calendar-check", X0 + 0.2, 6.2, 0.36, disc_=False)
D.text(X0 + 0.5, 6.05, W, 0.3, "Nächster Bericht an den Vorstand: November 2027, nach Entscheidungspunkt 1.", 15, M, DB)
E.footer("Anmerkung: Beispieldaten, fiktiv; Namen und Termine sind Vorschläge. Stufen und Entscheidungspunkte: Folie 9")

# ================= 10 Anhang: Segmentdaten =====================================================================
E.slide("Cyber wächst am schnellsten (19 % pro Jahr), dort ist unser Anteil mit 1,2 % am niedrigsten",
        "ANHANG: Werte nachschlagen. Tabelle ohne Kästen, Fokus mit Marke.", chapter="Anhang")
hdr = [("Segment", ""), ("Markt 2026", "Mrd. €"), ("Wachstum", "% p. a."), ("Zuwachs", "bis 2029, Mrd. €"), ("Unser Anteil", "% 2026"), ("Beratungsbedarf", "% der Kunden"), ("Combined Ratio", "%")]
cwid = [2.53, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6]
xs = [X0 + sum(cwid[:j]) for j in range(len(cwid))]
for j, (h_, u) in enumerate(hdr):
    D.text(xs[j], 1.6, cwid[j] - 0.1, 0.26, h_, 13, M, ZB, "l" if j == 0 else "r")
    D.text(xs[j], 1.88, cwid[j] - 0.1, 0.22, u, 11, L, DB, "l" if j == 0 else "r")
D.rule(X0, 2.18, W, ZB, 0.02)
for r_ in range(8):
    y = 2.28 + r_ * 0.39; foc = r_ in Mo.FOKUS
    if foc: D.shape(S.RECTANGLE, X0 - 0.16, y + 0.07, 0.06, 0.27, fill=ZB, name="Fokus-Marke")
    row = [Mo.SEG[r_], de(Mo.m26[r_]), de(Mo.g[r_] * 100), de(Mo.dz[r_]), de(Mo.sh[r_]), str(Mo.ber[r_]), de(Mo.cr[r_])]
    for j, v in enumerate(row): D.text(xs[j], y, cwid[j] - 0.1, 0.4, v, 14, M if foc else L, DB, "l" if j == 0 else "r", "m")
    D.rule(X0, y + 0.385, W, "E3EAF2")
y = 2.28 + 8 * 0.39 + 0.1; D.rule(X0, y - 0.04, W, ZB, 0.015)
for k, (nm, idx) in enumerate([("Fokus (3)", Mo.FOKUS), ("Übrige (5)", Mo.REST), ("Gesamt", list(range(8)))]):
    yy = y + k * 0.38
    gg = (Mo.m29[idx].sum() / Mo.m26[idx].sum()) ** (1 / 3) - 1
    s_ = (Mo.m26[idx] * Mo.sh[idx]).sum() / Mo.m26[idx].sum()
    row = [nm, de(Mo.m26[idx].sum()), de(gg * 100), de(Mo.dz[idx].sum()), de(s_), "", ""]
    for j, v in enumerate(row): D.text(xs[j], yy, cwid[j] - 0.1, 0.4, v, 14, M, DB, "l" if j == 0 else "r", "m")
E.footer("Anmerkung: Beispieldaten, fiktiv; Gruppenanteile gewichtet nach Marktvolumen. Quelle: Marktstudie 2026; Kundenbefragung 2026 (n = 1.200); Schadenstatistik 2023 bis 2025")

# ================= 11 Anhang: Annahmen ==========================================================================
E.slide("Alle Zahlen folgen aus acht Annahmen, die wir offenlegen", "ANHANG: Methode. Jede Zahl kommt aus modell.py; asserts prüfen die Aussagen vor dem Bauen.", chapter="Anhang")
ass = [("Markt", f"Bruttoprämie Gewerbe 49,5 Mrd. € (2026), {de(Mo.m29.sum())} Mrd. € (2029); Wachstum je Segment konstant."),
       ("Unser Anteil", "2026 je Segment fest; ohne Fokus unverändert; Gruppenwerte gewichtet nach Marktvolumen."),
       ("Anteilsgewinn", "+1,5 Pp in Cyber, Gesundheit, Logistik bis 2029; Hochlauf 20 / 55 / 100 %."),
       ("Marge", f"Mehrergebnis = zusätzlicher Beitrag × (1 − Combined Ratio Fokus, {pct(Mo.cr_f)})."),
       ("Investition", "80 Mio. € in drei Stufen: 10 (2027), 40 (2028), 30 (2029); nur nach Entscheidungspunkt."),
       ("Vorsichtiger Fall", "+1,0 Pp Anteil, Marge 5,0 %; sonst wie Basisfall."),
       ("Befragungen", "Kunden: n = 1.200, ein Hauptgrund je Kunde. Vermittler: n = 412."),
       ("Nicht eingerechnet", "Verwaltungskosten-Effekte, Kannibalisierung, Märkte nach 2032 ohne Wachstum (vorsichtig).")]
for i, (k, v) in enumerate(ass):
    col, row = i % 2, i // 2
    x = X0 + col * (W / 2 + 0.2); y = 1.7 + row * 1.08
    D.rule(x, y - 0.08, W / 2 - 0.2, LB)
    E.big(x, y, 0.6, str(i + 1), 28, ZB)
    D.text(x + 0.6, y + 0.05, W / 2 - 0.9, 0.3, k, 15, M, DB)
    D.text(x + 0.6, y + 0.36, W / 2 - 0.9, 0.6, v, 13, L, DB)
E.footer("Anmerkung: Beispieldaten, fiktiv; Pp = Prozentpunkte. Quelle: modell.py")
D.save(sys.argv[1])
