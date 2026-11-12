# -*- coding: utf-8 -*-
"""EIN Modell für das Deck Marktfokus v5 (fiktive Beispieldaten). Jede Zahl auf den Folien kommt von hier."""
import numpy as np

SEG = ["Cyber", "Gesundheit", "Logistik", "Handwerk", "Freie Berufe", "Industrie", "Handel", "Gastro"]
FOKUS, REST = [0, 1, 2], [3, 4, 5, 6, 7]
m26 = np.array([3.0, 6.0, 5.0, 8.0, 5.0, 9.5, 9.0, 4.0])            # Marktvolumen 2026, Mrd. € Bruttoprämie
g   = np.array([0.19, 0.13, 0.11, 0.078, 0.074, 0.020, 0.026, 0.012]) # Wachstum p. a. 2026-2029
sh  = np.array([1.2, 2.2, 2.6, 2.9, 3.3, 3.6, 3.9, 4.2])              # unser Anteil 2026, %
ber = np.array([78, 71, 66, 63, 58, 62, 49, 35])                      # Beratungsbedarf, % der Kunden
cr  = np.array([92.5, 93.8, 93.0, 97.2, 95.5, 94.5, 96.8, 99.0])      # Combined Ratio, %

m29 = m26 * (1 + g) ** 3
dz = m29 - m26
mkt_g = (m29.sum() / m26.sum()) ** (1 / 3) - 1
F_dz_share = dz[FOKUS].sum() / dz.sum()
def wsh(idx): return (m26[idx] * sh[idx]).sum() / m26[idx].sum()
F_sh, R_sh = wsh(FOKUS), wsh(REST)
share26 = (m26 * sh).sum() / m26.sum()

# ---- Auswahl-Filter
STEP1 = [i for i in range(8) if g[i] > mkt_g]
STEP2 = [i for i in STEP1 if ber[i] >= 60]
STEP3 = [i for i in STEP2 if cr[i] < 95]

# ---- Beitrag (Mio. €)
B26 = (m26 * sh).sum() * 10
B29_ohne = (m29 * sh).sum() * 10
B29_markt = B26 * (1 + mkt_g) ** 3
PP = 1.5                                                             # Anteilsgewinn Fokus bis 2029, Pp
B_plus = m29[FOKUS].sum() * PP * 10
B29_mit = B29_ohne + B_plus
g_ohne = (B29_ohne / B26) ** (1 / 3) - 1
g_mit = (B29_mit / B26) ** (1 / 3) - 1
share29_ohne = (m29 * sh).sum() / m29.sum()
share29_mit = B29_mit / 10 / m29.sum()

# ---- Kunde (Hauptgrund für den Abschluss, % der Kunden; Kundenbefragung n = 1.200)
REASONS = ["Beratung", "Schadenservice", "Preis", "Marke und Vertrauen"]
R_FOK = [41, 27, 18, 14]; R_REST = [24, 22, 35, 19]

# ---- Business Case: Mehrergebnis = zusätzlicher Beitrag × (1 − Combined Ratio Fokus)
YEARS = list(range(2027, 2036))
RAMP = {2027: 0.2, 2028: 0.55}                                      # Anteil des Ziel-Pp-Gewinns
INV = {2027: 10, 2028: 40, 2029: 30}
cr_f = (m26[FOKUS] * cr[FOKUS]).sum() / m26[FOKUS].sum()
def fokus_mkt(y): return (m26[FOKUS] * (1 + g[FOKUS]) ** (y - 2026)).sum()
def case(pp=PP, margin=None, delay=0, factor=1.0):
    margin = (100 - cr_f) / 100 if margin is None else margin
    rows, cum = [], 0.0
    for y in YEARS:
        ramp = 0.0 if y - delay < 2027 else RAMP.get(y - delay, 1.0)
        beitrag = fokus_mkt(min(y, 2032)) * pp * ramp * 10 * factor
        res = beitrag * margin; cum += res - INV.get(y, 0)
        rows.append(dict(year=y, beitrag=beitrag, res=res, cum=cum))
    return rows
def payback(rows): return next((r["year"] for r in rows if r["cum"] >= 0), None)
BASE = case(); CAUT = case(pp=1.0, margin=0.05)
PB_BASE, PB_CAUT = payback(BASE), payback(CAUT)
RES29 = BASE[2]["res"]; TROUGH = min(r["cum"] for r in BASE)
MARGIN = (100 - cr_f) / 100

# ---- Größe der Chance: Lücke unseres Fokus-Anteils zum Durchschnitt, bewertet am Fokusmarkt 2029
GAP_PP = share26 - F_sh
PRIZE = GAP_PP * m29[FOKUS].sum() * 10                               # Mio. € Beitrag pro Jahr

# ---- Risiken: Wirkung auf das Amortisationsjahr (Basisfall 2031)
RISKS = [("Anteilsgewinn nur +1,0 statt +1,5 Pp", case(pp=1.0)),
         ("Combined Ratio im Neugeschäft 2 Pp schlechter", case(margin=MARGIN - 0.02)),
         ("Vertrieb startet ein Jahr später", case(delay=1)),
         ("Ein Fünftel des Mehrbeitrags kommt aus dem eigenen Bestand", case(factor=0.8))]
RISK_PB = [payback(r) for _, r in RISKS]

# ---- Stufen und Entscheidungspunkte
STAGES = [("Pilot Cyber", "Feb bis Okt 2027", 10), ("Gesundheit und Logistik", "2028", 40), ("Skalieren", "2029", 30)]
AT_RISK = [10, 50, 80]

def de(v, n=1):
    s = f"{abs(v):,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−" if v < 0 and round(abs(v), n) != 0 else "") + s

assert STEP1 == [0, 1, 2, 3, 4] and STEP2 == [0, 1, 2, 3] and STEP3 == FOKUS
assert sum(R_FOK) == 100 and sum(R_REST) == 100 and sum(INV.values()) == 80
assert g_ohne < mkt_g < g_mit and share29_ohne < share26 < share29_mit

if __name__ == "__main__":
    print("GAP_PP", round(GAP_PP, 2), "PRIZE", round(PRIZE), "RISK_PB", RISK_PB, "margin", round(MARGIN, 4))
    print("Markt 26/29", round(m26.sum(), 1), round(m29.sum(), 2), "Zuwachs", round(dz.sum(), 2), "mkt_g", round(mkt_g * 100, 2))
    print("dz", np.round(dz, 2), "Fokusanteil Zuwachs", round(F_dz_share * 100, 1))
    print("Anteil F/R/ges", round(F_sh, 2), round(R_sh, 2), round(share26, 2), "-> 2029 ohne/mit", round(share29_ohne, 2), round(share29_mit, 2))
    print("Beitrag 26", round(B26), "29 ohne", round(B29_ohne), "markt", round(B29_markt), "plus", round(B_plus), "mit", round(B29_mit))
    print("g ohne/mit", round(g_ohne * 100, 2), round(g_mit * 100, 2), "cr_f", round(cr_f, 2))
    print("BASE", [(r["year"], round(r["res"], 1), round(r["cum"], 1)) for r in BASE])
    print("CAUT", [(r["year"], round(r["res"], 1), round(r["cum"], 1)) for r in CAUT])
    print("PB", PB_BASE, PB_CAUT, "RES29", round(RES29, 1), "Trough", round(TROUGH, 1))
