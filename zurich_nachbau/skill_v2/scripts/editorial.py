# -*- coding: utf-8 -*-
"""editorial: Bildsprache 2.1 für Zurich-Decks (auf deck_lite aufgesetzt).

Regeln des Nutzers (10.11.2026): keine dunklen Folien, kein Balken unten auf jeder Folie, keine Kennzahl-Blöcke rechts,
keine getönten Kästen. Erlaubt und erwünscht: ein Zurich-Blue-Band quer durch die Mitte mit weißen, leicht schwebenden Karten.
Stattdessen: Weißraum, große Typografie (Ogg-Zahlen als Gestaltungselement), ein großes Bild je Folie, Anmerkungen direkt im Bild,
feine Linien, jede Folie mit eigenem Layout.
"""
from lxml import etree
import deck_lite as D
from deck_lite import S, Inches, Pt, qn, rgb, de, ZB, DB, MB, LB, WHITE, L, M, O

X0, W = 0.6, 12.13                      # großzügiger Rand
TITLE_Y, TITLE_SIZE = 0.48, 26

def slide(title, notes="", chapter=None, title_w=10.0):
    """Weiße Folie: Titel (echter Platzhalter), Logo, Kapitelmarke als Text (keine Pille)."""
    sl = D.slide(title, notes, dark=False, hero=True)
    D._set_title(title, X0, TITLE_Y, title_w, 1.0, TITLE_SIZE, ZB)
    if len(title.replace("\n", " ")) > 95: D._st["warn"].append(f"Folie {D._st['page']}: Titel zu lang")
    if chapter: D.text(10.6, 0.98, 2.13, 0.25, chapter.upper(), 10, M, ZB, "r", spacing=120)
    return sl

def to_front(sp):
    tree = sp._element.getparent(); tree.remove(sp._element); tree.append(sp._element); return sp

def shadow(sp, blur=0.25, dist=0.04, alpha=16):
    spPr = sp._element.spPr
    eff = etree.SubElement(spPr, qn("a:effectLst"))
    sh = etree.SubElement(eff, qn("a:outerShdw"), blurRad=str(int(blur * 914400)), dist=str(int(dist * 914400)), dir="5400000", algn="t", rotWithShape="0")
    c = etree.SubElement(sh, qn("a:srgbClr"), val=DB); etree.SubElement(c, qn("a:alpha"), val=str(alpha * 1000))
    return sp

def white_card(x, y, w, h, name="Karte"):
    sp = D.shape(S.RECTANGLE, x, y, w, h, fill=WHITE, name=name)
    return shadow(sp)

def blue_band(y, h, name="Band"):
    return D.shape(S.RECTANGLE, 0, y, D.SW, h, fill=ZB, name=name)

def kicker(x, y, w, t, color=ZB):
    """Kleine Großbuchstaben-Zeile über einem Element (nicht über dem Folientitel)."""
    return D.text(x, y, w, 0.24, t.upper(), 10, M, color, spacing=120)

def big(x, y, w, t, size=54, color=ZB, align="l", h=None):
    return D.text(x, y, w, h or size / 72 * 1.25, t, size, O, color, align, "t")

def accent_line(x, y, w=0.6, color=ZB): return D.shape(S.RECTANGLE, x, y, w, 0.035, fill=color, name="Akzent")

def statement(t, y=6.15, size=17, x=X0, w=W):
    """Schlusssatz der Folie: kurzer Akzentstrich + Satz. Ersetzt das Band."""
    accent_line(x, y - 0.12); return D.text(x, y, w, 0.5, t, size, M, DB)

def leader(x1, y1, x2, y2, color=DB, w=0.75):
    c = D.s().shapes.add_connector(1, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    st = c._element.find(qn("p:style"))
    if st is not None: c._element.remove(st)
    c.line.color.rgb = rgb(color); c.line.width = Pt(w); return c

def footer(src):
    D.text(X0, 6.98, 10.6, 0.4, src, 10, L, DB, name="Quelle")
    D.text(11.73, 7.0, 0.4, 0.22, str(D._st["page"]), 10, L, DB, "r")
    D.text(12.18, 7.0, 0.6, 0.22, "© Zurich", 10, L, DB)
