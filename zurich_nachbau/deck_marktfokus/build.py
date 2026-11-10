# -*- coding: utf-8 -*-
"""Lern-Deck Marktfokus (fiktiv): Folie für Folie nach Ghost Deck (Methode_Deck_bauen.md, Abschnitt 7)."""
import sys
sys.path.insert(0, "..")
import zhelp as Z
from zhelp import *

def band(label, sentence, size=16, y=6.14):
    shape(S.ROUNDED_RECTANGLE, 0.4, y, 12.53, 0.66, fill=DB)
    text(0.65, y, 1.9, 0.66, label, 12, M, WHITE, "l", "m")
    text(2.55, y, 10.2, 0.66, sentence, size, L, WHITE, "l", "m")

# ======================= Folie 2: Antwort zuerst =======================================================
Z.PAGE = 1      # diese Folie trägt die Nummer 2 (Folie 1 folgt im nächsten Schritt)
new_slide("Wir setzen 80 Mio. € auf drei Segmente, weil Markt, Rechnung und Datenbasis dafür sprechen",
          "Situation: Der Markt wächst bis 2029 um 9,0 Mrd. €. Komplikation: 69 % davon liegen in drei Segmenten, in denen wir nur 2,1 % Anteil haben. "
          "Frage: Wo setzen wir Geld ein, und können wir den Daten trauen? Antwort: 80 Mio. € auf Gesundheit, Cyber und Logistik. "
          "Gründe: (1) Markt (Folie 3), (2) Rechnung (Folie 4 und 5), (3) Datenbasis und Umsetzung (Folie 6 und 7). Fiktive Daten.")
args = [("Der Markt wächst dort am stärksten", "Drei Segmente liefern 6,2 von 9,0 Mrd. € Zuwachs,\nunser Anteil liegt dort nur bei 2,1 %.", "69 %", "des Marktzuwachses", "Folie 3"),
        ("Die Rechnung geht auf", "Der Fokus bringt 1,16 € Mehr-Anteil je investiertem Euro,\ndie breite Streuung nur 0,32 €.", "1,16 €", "Beitrag je investiertem Euro", "Folie 4 und 5"),
        ("Die Daten tragen, wir prüfen sie vor jeder Ausgabe", "Der Anteil wächst um 11,5 % pro Jahr,\nein Nachlassen des Tempos ist nicht belegt.", "11,5 %", "Wachstum pro Jahr", "Folie 6 und 7")]
RH, GAP, Y0 = 1.38, 0.13, 1.5
for i, (claim, proof, num, cap, ref) in enumerate(args):
    y = Y0 + i * (RH + GAP)
    shape(S.ROUNDED_RECTANGLE, 0.4, y, 12.53, RH, fill=WHITE, line=LB)
    shape(S.OVAL, 0.7, y + RH / 2 - 0.22, 0.44, 0.44, fill=DB)
    text(0.7, y + RH / 2 - 0.22, 0.44, 0.44, str(i + 1), 16, M, WHITE, "c", "m")
    text(1.5, y + 0.28, 7.6, 0.4, claim, 20, M, DB)
    text(1.5, y + 0.78, 7.5, 0.5, proof, 14, L, DB)
    shape(S.RECTANGLE, 9.45, y + 0.25, 0.015, RH - 0.5, fill="D5E3F2")
    text(9.75, y + 0.16, 3.0, 0.7, num, 40, O, ZB, "l", "m")
    text(9.75, y + 0.86, 3.0, 0.25, cap, 12, M, DB)
    text(9.75, y + 1.08, 3.0, 0.22, ref, 11, L, DB)
band("WIR BITTEN UM", "Freigabe von 80 Mio. € für 2027 bis 2029 und den Start des Piloten im ersten Quartal.")
footer("Beispieldaten, fiktiv. 80 Mio. € = Investition der Option „Fokus auf drei Segmente“; 1,16 € = 93 Mio. € Mehr-Anteil geteilt durch 80 Mio. €.")
prs.save(sys.argv[1])
