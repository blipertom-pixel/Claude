# -*- coding: utf-8 -*-
"""EIN Modell für das ganze Deck (fiktive Beispieldaten). Jede Zahl auf einer Folie kommt von hier; asserts sichern die Aussagen."""
import json
import numpy as np
from pathlib import Path

SEG = ["Gesundheit", "Cyber", "Logistik", "Handwerk", "Handel", "Industrie", "Gastro", "Freie Berufe"]
FOKUS = [0, 1, 2]
REST = [3, 4, 5, 6, 7]
m26 = np.array([6.0, 3.0, 5.0, 8.0, 9.0, 9.5, 2.5, 2.0])        # Marktvolumen Gewerbe 2026, Mrd. € Bruttoprämie
dz = np.array([2.4, 2.2, 1.6, 0.9, 0.9, 0.6, 0.2, 0.2])          # Zuwachs bis 2029, Mrd. €
m29 = m26 + dz
sh = np.array([2.3, 2.0, 2.0, 3.6, 3.4, 3.8, 3.0, 3.5])          # unser Anteil 2026, %
g = (m29 / m26) ** (1 / 3) - 1                                    # Wachstum p. a.
def gsum(idx, a): return a[idx].sum()
def wshare(idx, mk): return (mk[idx] * sh[idx]).sum() / mk[idx].sum()
F_dz, R_dz = gsum(FOKUS, dz), gsum(REST, dz)
F_g = (gsum(FOKUS, m29) / gsum(FOKUS, m26)) ** (1 / 3) - 1
R_g = (gsum(REST, m29) / gsum(REST, m26)) ** (1 / 3) - 1
F_sh, R_sh = wshare(FOKUS, m26), wshare(REST, m26)
tot26 = (m26 * sh / 100).sum(); tot29_base = (m29 * sh / 100).sum()
share26 = tot26 / m26.sum() * 100; share29_base = tot29_base / m29.sum() * 100

# ---- Business Case: Anteilsgewinn auf das Marktvolumen, Hochlauf, Marge, Tranchen
YEARS = list(range(2027, 2036))
RAMP = {2027: 0.30, 2028: 0.65}                                   # danach 100 %
def mkt(idx, year):                                               # geometrischer Verlauf 2026 -> 2029, danach konstant (vorsichtig)
    t = min(year, 2029) - 2026
    return (m26[idx].sum() * ((m29[idx].sum() / m26[idx].sum()) ** (1 / 3)) ** t) * 1000   # Mio. €
OPT = {
    "A": dict(name="Breit wachsen", idx=list(range(8)), pp=0.3, margin=0.07, inv={2027: 30, 2028: 60, 2029: 50}),
    "B": dict(name="Fokus auf drei Segmente", idx=FOKUS, pp=0.9, margin=0.12, inv={2027: 10, 2028: 40, 2029: 30}),
}
def case(o, pp=None, margin=None):
    pp = o["pp"] if pp is None else pp; margin = o["margin"] if margin is None else margin
    rows, cum = [], 0.0
    for y in YEARS:
        gwp = mkt(o["idx"], y) * pp / 100 * RAMP.get(y, 1.0)
        contrib = gwp * margin; inv = o["inv"].get(y, 0)
        cum += contrib - inv
        rows.append(dict(year=y, gwp=gwp, contrib=contrib, inv=inv, cum=cum))
    return rows
def payback(rows, horizon=2045, o=None, pp=None, margin=None):
    for r in rows:
        if r["cum"] >= 0: return r["year"]
    last = rows[-1]; cum = last["cum"]; y = last["year"]
    while cum < 0 and y < horizon:
        y += 1; cum += last["contrib"]
    return y if cum >= 0 else None
CA, CB = case(OPT["A"]), case(OPT["B"])
PB_A, PB_B = payback(CA), payback(CB)
TROUGH_B = min(r["cum"] for r in CB)
RUN_A, RUN_B = CA[2]["contrib"], CB[2]["contrib"]                  # Ergebnisbeitrag ab 2029 p. a.
GWP_B29, GWP_A29 = CB[2]["gwp"], CA[2]["gwp"]
INV_A, INV_B = sum(OPT["A"]["inv"].values()), sum(OPT["B"]["inv"].values())
# Sensitivität Option B: Amortisationsjahr je Anteilsgewinn x Marge
SENS_PP = [0.5, 0.7, 0.9, 1.1, 1.3]; SENS_M = [0.08, 0.10, 0.12, 0.14]
SENS = [[payback(case(OPT["B"], pp=p, margin=mg)) for p in SENS_PP] for mg in SENS_M]

# ---- Tranchen und Entscheidungspunkte
PH = [("Datenbasis klären", "Q1 2027", 2), ("Pilot in Cyber", "Q2 bis Q4 2027", 8),
      ("Auf drei Segmente ausweiten", "2028", 40), ("Skalieren und steuern", "2029", 30)]
STOP = [sum(p[2] for p in PH[:k + 1]) for k in range(3)]          # Einsatz, wenn Entscheidungspunkt k+1 scheitert

# ---- Befragung (Nachfrage) in den Fokus-Segmenten: Anteil der Gewerbekunden, die Schutz anfragen, %
d = np.array(json.load(open(Path(__file__).parent / "befragung.json"))["d"])
dem = 28.0 + np.concatenate([[0], np.cumsum(d)])                  # 24 Monate, Nov 2024 bis Okt 2026
pace = np.array([d[i:i + 3].mean() for i in range(21)])
dem_growth = (dem[-1] / dem[0]) ** (12 / 23) - 1
dem_trend = np.exp(12 * np.polyfit(np.arange(24), np.log(dem), 1)[0]) - 1
dem_last12 = dem[23] / dem[11] - 1
N_RESP = 1200                                                      # Befragte je Monat (Annahme)
p_mid = dem.mean() / 100
se_pp = np.sqrt(p_mid * (1 - p_mid) / N_RESP) * 100                # Stichprobenfehler eines Monatswerts, Pp
noise_diff = np.sqrt(2) * se_pp                                    # erwartete Streuung einer Monatsänderung aus Zufall allein
obs_sd = d.std(ddof=1)
SMOOTH = noise_diff / obs_sd

def de(v, n=1): return f"{v:,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ---- Aussagen, die auf Folien stehen, werden hier geprüft
assert abs(dz.sum() - 9.0) < 1e-9 and abs(m26.sum() - 45.0) < 1e-9 and abs(m29.sum() - 54.0) < 1e-9
assert round(F_dz / dz.sum() * 100) == 69 and round(F_sh, 1) == 2.1 and round(R_sh, 1) == 3.5
assert round(F_g * 100, 1) == 13.0 and round(R_g * 100, 1) == 2.9
assert round(share26, 1) == 3.1 and round(share29_base, 1) == 3.0
assert INV_A == 140 and INV_B == 80 and sum(p[2] for p in PH) == INV_B and STOP == [2, 10, 50]
assert (d > 0).all() and abs(dem[-1] - 34.5) < 1e-9 and round(dem_growth * 100, 1) == 11.5
assert (np.round(pace, 2) <= 0.17).sum() == 2 and round(pace.max(), 2) == 0.41

if __name__ == "__main__":
    print("Wachstum p.a.", np.round(g * 100, 1), "Fokus", round(F_g * 100, 1), "Rest", round(R_g * 100, 1))
    print("Anteil gesamt 2026/2029 base", round(share26, 2), round(share29_base, 2))
    for k, rows in (("A", CA), ("B", CB)):
        print(k, [(r["year"], round(r["gwp"], 1), round(r["contrib"], 1), r["inv"], round(r["cum"], 1)) for r in rows])
    print("Payback A/B", PB_A, PB_B, "Tief B", round(TROUGH_B, 1), "Run A/B", round(RUN_A, 1), round(RUN_B, 1), "GWP29 A/B", round(GWP_A29), round(GWP_B29))
    print("Sens (Zeilen Marge 8..14 %, Spalten pp .5..1.3):"); [print(m, r) for m, r in zip(SENS_M, SENS)]
    print("Nachfrage: growth", round(dem_growth * 100, 2), "trend", round(dem_trend * 100, 2), "last12", round(dem_last12 * 100, 2))
    print("se_pp", round(se_pp, 2), "noise_diff", round(noise_diff, 2), "obs_sd", round(obs_sd, 3), "SMOOTH", round(SMOOTH, 1))
