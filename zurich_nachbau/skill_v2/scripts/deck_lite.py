# -*- coding: utf-8 -*-
"""deck_lite: Zurich-Folien OHNE Master Playbook (Fallback-Modus, bis Master, Schriften und Piktogramme vorliegen).

Setzt das Gestaltungssystem aus references/visual-system.md um: Raster, Typo-Rollen, Farben, Icons, Diagramm-Grammatik.
Schriftnamen bleiben "Zurich Sans Light/Medium" und "Ogg": Mit installierten Originalschriften erscheint die echte Typo.
Icons: Phosphor (MIT, assets/icons/LICENSE_phosphor.txt), eingefärbt in Zurich Blue bzw. Weiß.

    import deck_lite as D
    D.new_deck()
    D.slide("Action-Titel als ganzer Satz", notes="...", tracker=(1, "Warum dort"))
    D.header(D.X0, 1.5, 6, "MARKTZUWACHS, MRD. €", icon="chart-line-up")
    ...
    D.footer("Quelle ..."); D.save("deck.pptx")
"""
from __future__ import annotations
from pathlib import Path
from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE as S, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.dml import MSO_LINE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_TICK_MARK, XL_TICK_LABEL_POSITION, XL_MARKER_STYLE
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml

SKILL = Path(__file__).resolve().parent.parent
ICONS = SKILL / "assets" / "icons"
C_NS = "http://schemas.openxmlformats.org/drawingml/2006/chart"

# ------------------------------------------------------------------ Farben (nur offizielle Zurich-Primärfarben)
DB, ZB, MB, LB, WHITE = "23366F", "2167AE", "5495CF", "91BFE3", "FFFFFF"
DOVE, ZW = "DDE4E3", "ECEEEF"
FOCUS, CONTEXT = ZB, LB                  # Diagramme: Hervorhebung = Zurich Blue, Kontext = Light Blue
# ------------------------------------------------------------------ Typo-Rollen
L, M, O = "Zurich Sans Light", "Zurich Sans Medium", "Ogg"
T_TITLE, T_CLAIM, T_BODY, T_LABEL, T_SMALL, T_SOURCE = 26, 18, 14, 13, 12, 11
# ------------------------------------------------------------------ Raster (16:9, Zoll)
SW, SH = 13.333, 7.5
X0, W, G = 0.4, 12.53, 0.25               # Rand, Inhaltsbreite, Spaltenabstand
TOP, BOTTOM = 1.5, 6.0                    # Inhaltsbereich
BAND_Y, FOOT_Y = 6.14, 6.93
TITLE_MAX_CHARS = 95                      # 2 Zeilen bei 26 pt auf 10,3 in

_st = {"prs": None, "s": None, "page": 0, "dark": False, "warn": []}
rgb = RGBColor.from_string
def de(v, n=1):
    """Deutsche Zahl: 1.234,5"""
    out = f"{abs(v):,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("\u2212" if v < 0 and float(out.replace(".", "").replace(",", ".")) != 0 else "") + out
def cols(n, gap=G, x0=X0, w=W):
    cw = (w - (n - 1) * gap) / n
    return [(x0 + i * (cw + gap), cw) for i in range(n)]
def split(left, gap=G, x0=X0, w=W):
    """Asymmetrisch: linke Breite in Zoll -> ((x, w), (x, w))"""
    return (x0, left), (x0 + left + gap, w - left - gap)
def s(): return _st["s"]

def new_deck():
    prs = Presentation(); prs.slide_width, prs.slide_height = Inches(SW), Inches(SH)
    _st.update(prs=prs, s=None, page=0, warn=[]); return prs

# ------------------------------------------------------------------ Grundformen
def shape(kind, x, y, w, h, fill=None, line=None, lw=1.0, rad=None, alpha=None, name=None, alt=None):
    sp = s().shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    st = sp._element.find(qn("p:style"))
    if st is not None: sp._element.remove(st)
    if kind == S.ROUNDED_RECTANGLE: sp.adjustments[0] = min(0.5, (rad or 0.12) / min(w, h))
    if fill:
        sp.fill.solid(); sp.fill.fore_color.rgb = rgb(fill)
        if alpha: etree.SubElement(sp._element.spPr.find(qn("a:solidFill"))[0], qn("a:alpha")).set("val", str(alpha * 1000))
    else: sp.fill.background()
    if line: sp.line.color.rgb = rgb(line); sp.line.width = Pt(lw)
    else: sp.line.fill.background()
    if name: sp.name = name
    if alt: sp._element.nvSpPr.cNvPr.set("descr", alt)
    return sp

def _fill_tf(tf, t, size, font, color, align, anchor, bold_runs=None):
    tf.word_wrap = True; tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
    paras = t if isinstance(t, list) else [[(line, False)] for line in t.split("\n")]
    for i, runs in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[align]
        for txt, bold in runs:
            r = p.add_run(); r.text = txt; r.font.size = Pt(size); r.font.name = M if bold else font; r.font.color.rgb = rgb(color)

def text(x, y, w, h, t, size=T_BODY, font=L, color=DB, align="l", anchor="t", spacing=None, name=None):
    """Kein AutoFit. '\\n' = bewusster Umbruch. t kann auch [[(text, fett), ...], ...] sein (Absätze aus Runs)."""
    tb = s().shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    _fill_tf(tb.text_frame, t, size, font, color, align, anchor)
    if spacing:
        for p in tb.text_frame.paragraphs:
            for r in p.runs: r._r.get_or_add_rPr().set("spc", str(spacing))
    if name: tb.name = name
    return tb

def rich(x, y, w, h, parts, size=T_BODY, color=DB, align="l", anchor="t"):
    """Ein Absatz mit fetten Schlüsselwörtern: parts = [("Text ", False), ("6,2 Mrd. €", True), ...]"""
    return text(x, y, w, h, [parts], size, L, color, align, anchor)

def rule(x, y, w, color=LB, weight=0.012): return shape(S.RECTANGLE, x, y, w, weight, fill=color)
def vrule(x, y, h, color=LB, weight=0.012): return shape(S.RECTANGLE, x, y, weight, h, fill=color)

def dash(x1, y1, x2, y2, color=DB, w=1.25):
    c = s().shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    st = c._element.find(qn("p:style"))
    if st is not None: c._element.remove(st)
    c.line.color.rgb = rgb(color); c.line.width = Pt(w); c.line.dash_style = MSO_LINE.DASH; return c

def polyline(pts, color=MB, w=2.25, name=None):
    fb = s().shapes.build_freeform(Inches(pts[0][0]), Inches(pts[0][1]))
    fb.add_line_segments([(Inches(a), Inches(b)) for a, b in pts[1:]], close=False)
    f = fb.convert_to_shape(); f.fill.background()
    st = f._element.find(qn("p:style"))
    if st is not None: f._element.remove(st)
    f.line.color.rgb = rgb(color); f.line.width = Pt(w)
    if name: f.name = name
    return f

def disc(cx, cy, d, fill, name=None): return shape(S.OVAL, cx - d / 2, cy - d / 2, d, d, fill=fill, name=name or "Markierung")

# ------------------------------------------------------------------ Rahmen-Elemente (Zurich-Frame)
def card(x, y, w, h, kind="tint"):
    """tint = Text/Kennzahl-Gruppe; dark = DIE eine Botschaft; line = parallele Gruppen (Optionen). Keine Karte um Diagramme."""
    if kind == "dark": return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=DB)
    if kind == "blue": return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=ZB)
    if kind == "line": return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=WHITE, line=LB)
    return shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=LB, alpha=30)

def icon(name, cx, cy, d=0.5, disc_=True, on_dark=False, alt=None):
    """Piktogramm mit Bedeutung. disc_: helle Scheibe dahinter (Zurich-Piktogramm-Sprache)."""
    f = ICONS / f"{name}{'_white' if (on_dark and not disc_) else ''}.png"
    if not f.is_file(): raise FileNotFoundError(f"Icon '{name}' fehlt in {ICONS}")
    if disc_: shape(S.OVAL, cx - d / 2, cy - d / 2, d, d, fill=WHITE if on_dark else LB, alpha=None if on_dark else 35, name=f"Icon-Scheibe {name}")
    k = 0.62 if disc_ else 1.0
    pic = s().shapes.add_picture(str(f), Inches(cx - d * k / 2), Inches(cy - d * k / 2), Inches(d * k), Inches(d * k))
    pic.name = f"Icon {name}"; pic._element.nvPicPr.cNvPr.set("descr", alt or name)
    return pic

def pill(x, y, w, t, fill=DB, color=WHITE, h=0.3, size=11):
    shape(S.ROUNDED_RECTANGLE, x, y, w, h, fill=fill, rad=h / 2)
    return text(x, y, w, h, t, size, M, color, "c", "m")

def badge(cx, cy, n, d=0.36, fill=DB, color=WHITE, size=13):
    disc(cx, cy, d, fill, name=f"Nummer {n}"); return text(cx - d / 2, cy - d / 2, d, d, str(n), size, M, color, "c", "m")

def header(x, y, w, t, icon_name=None, color=ZB):
    """Kopf eines Belegs: Großbuchstaben-Label, optional Icon, darunter feine Linie. Ersetzt die Karte um Diagramme."""
    tx = x
    if icon_name: icon(icon_name, x + 0.17, y + 0.12, 0.34, disc_=False); tx = x + 0.42
    text(tx, y, w - (tx - x), 0.26, t, T_SMALL, M, color, spacing=50)
    rule(x, y + 0.32, w)

def claim(x, y, w, t, icon_name=None, num=None, size=T_CLAIM):
    """Teilaussage über einem Beleg (z. B. '1  Das Wachstum ist klar')."""
    tx = x
    if num is not None: badge(x + 0.18, y + 0.2, num); tx = x + 0.48
    if icon_name: icon(icon_name, tx + 0.22, y + 0.2, 0.44); tx += 0.56
    return text(tx, y, w - (tx - x), 0.42, t, size, M, DB, "l", "m")

def tracker(n, label):
    shape(S.ROUNDED_RECTANGLE, 11.4, 0.93, 1.5, 0.3, fill="E9EBF0", rad=0.15)
    badge(11.57, 1.08, n, 0.24, size=10)
    text(11.78, 0.93, 1.1, 0.3, label, 11, L, DB, "l", "m")

def band(label, sentence, size=16, y=BAND_Y):
    """Dunkles Band: sagt, was der Titel NICHT sagt (Konsequenz, Entscheidung, Bedingung)."""
    shape(S.ROUNDED_RECTANGLE, X0, y, W, 0.66, fill=DB)
    text(X0 + 0.25, y, 1.95, 0.66, label, 12, M, WHITE, "l", "m", spacing=50)
    text(X0 + 2.25, y, W - 2.45, 0.66, sentence, size, L, WHITE, "l", "m")

def takeaway(sentence, y=6.2, size=19):
    """Ruhige Alternative zum Band (wenn die Folie schon ein dunkles Element hat)."""
    rule(X0, y - 0.12, W); return text(X0, y, W, 0.5, sentence, size, M, DB)

def bracket(x0, x1, y, label, size=12, up=False):
    rule(x0, y, x1 - x0, DB, 0.02); dy = -0.1 if up else 0
    shape(S.RECTANGLE, x0, y + dy, 0.02, 0.1, fill=DB); shape(S.RECTANGLE, x1 - 0.02, y + dy, 0.02, 0.1, fill=DB)
    ty = y - 0.32 if up else y + 0.08
    return text(x0 - 0.5, ty, x1 - x0 + 1.0, 0.26, label, size, M, DB, "c")

def footer(src=None):
    c = WHITE if _st["dark"] else DB
    if src: text(X0, FOOT_Y, 11.0, 0.45, src, T_SOURCE, L, c, name="Quelle")
    text(11.9, FOOT_Y + 0.02, 0.3, 0.25, str(_st["page"]), 10, L, c, "r")
    text(12.3, FOOT_Y + 0.02, 0.65, 0.25, "© Zurich", 10, L, c)

def _logo(dark):
    shape(S.OVAL, 11.45, 0.42, 0.4, 0.4, fill=WHITE if dark else ZB, name="Logo (Nachbildung)", alt="Zurich Logo")
    text(11.45, 0.42, 0.4, 0.4, "Z", 16, M, ZB if dark else WHITE, "c", "m")
    text(11.95, 0.42, 1.1, 0.4, "ZURICH", 15, M, WHITE if dark else ZB, "l", "m", spacing=100)

def _set_title(t, x, y, w, h, size, color):
    tt = s().shapes.title
    tt.left, tt.top, tt.width, tt.height = Inches(x), Inches(y), Inches(w), Inches(h)
    _fill_tf(tt.text_frame, t, size, L, color, "l", "t")
    for p in tt.text_frame.paragraphs:
        for r in p.runs: r.font.bold = False

def slide(title, notes="", dark=False, tracker_=None, hero=False, title_w=10.3):
    """Neue Folie mit echtem Titel-Platzhalter (Gliederung, Barrierefreiheit), Logo, optional Kapitel-Pille."""
    prs = _st["prs"]; _st["page"] += 1; _st["dark"] = dark
    sl = prs.slides.add_slide(prs.slide_layouts[5]); _st["s"] = sl
    if dark: sl.background.fill.solid(); sl.background.fill.fore_color.rgb = rgb(DB)
    flat = title.replace("\n", " ")
    if not hero:
        _set_title(title, 0.44, 0.34, title_w, 0.9, T_TITLE, WHITE if dark else ZB)
        if len(flat) > TITLE_MAX_CHARS: _st["warn"].append(f"Folie {_st['page']}: Titel {len(flat)} Zeichen (> {TITLE_MAX_CHARS})")
    _logo(dark)
    if tracker_: tracker(*tracker_)
    sl.notes_slide.notes_text_frame.text = notes
    if not notes: _st["warn"].append(f"Folie {_st['page']}: keine Notizen")
    return sl

def hero_title(t, sub, x=0.7, y=2.2, w=10.6, size=40):
    _set_title(t, x, y, w, 2.4, size, WHITE)
    text(x, 4.85, 9.3, 0.7, sub, 17, L, WHITE)

# ------------------------------------------------------------------ Diagramme (nativ, editierbar; Beschriftung mit Dezimalkomma)
def _layout(ch, inner):
    pa = ch._chartSpace.chart.plotArea
    for old in pa.findall(qn("c:layout")): pa.remove(old)
    x, y, w, h = inner
    pa.insert(0, parse_xml(f'<c:layout xmlns:c="{C_NS}"><c:manualLayout><c:layoutTarget val="inner"/><c:xMode val="edge"/><c:yMode val="edge"/>'
                           f'<c:x val="{x}"/><c:y val="{y}"/><c:w val="{w}"/><c:h val="{h}"/></c:manualLayout></c:layout>'))
def _transparent(ch):
    cs = ch._chartSpace
    sp = parse_xml(f'<c:spPr xmlns:c="{C_NS}" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr>')
    for old in cs.findall(qn("c:spPr")): cs.remove(old)
    cs.insert(list(cs).index(cs.find(qn("c:chart"))) + 1, sp)
def _chart(kind, x, y, w, h, cats, series, alt, fmt="0.0"):
    cd = CategoryChartData(number_format=fmt); cd.categories = cats
    for nm, vals in series: cd.add_series(nm, [float(v) for v in vals])
    gf = s().shapes.add_chart(kind, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    gf.name = alt[:60]; gf._element.nvGraphicFramePr.cNvPr.set("descr", alt)
    ch = gf.chart; ch.has_legend = False; ch.has_title = False
    ch.font.size = Pt(T_LABEL); ch.font.name = L; ch.font.color.rgb = rgb(DB)
    return ch
def _axes_off(ch, vmin, vmax, cat_labels):
    va = ch.value_axis; va.minimum_scale, va.maximum_scale = vmin, vmax
    va.has_major_gridlines = False; va.format.line.fill.background()
    va.tick_label_position = XL_TICK_LABEL_POSITION.NONE; va.major_tick_mark = XL_TICK_MARK.NONE
    ca = ch.category_axis; ca.major_tick_mark = XL_TICK_MARK.NONE; ca.format.line.color.rgb = rgb(LB)
    if cat_labels: ca.tick_labels.font.size = Pt(T_LABEL)
    else: ca.tick_label_position = XL_TICK_LABEL_POSITION.NONE

def bars_h(x, y, w, h, cats, vals, focus, vmax, label, show_cats=True, cat_w=1.25, alt=""):
    """Horizontale Balken, sortiert vorgeben. focus = Indizes der hervorgehobenen Zeilen. label(v) -> Text am Balkenende."""
    ch = _chart(XL_CHART_TYPE.BAR_CLUSTERED, x, y, w, h, cats, [("Wert", vals)], alt or "Balkendiagramm")
    pl = ch.plots[0]; pl.gap_width = 40; pl.vary_by_categories = False
    for i in range(len(vals)):
        pt = pl.series[0].points[i]; pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(FOCUS if i in focus else CONTEXT)
    _axes_off(ch, 0, vmax, show_cats); ch.category_axis.reverse_order = True
    ix = (cat_w / w) if show_cats else 0.01; iw = 1 - ix - 0.12
    _layout(ch, (ix, 0.0, iw, 1.0)); _transparent(ch)
    pl_, pw_, n = x + w * ix, w * iw, len(vals); rh = h / n
    for i, v in enumerate(vals):
        text(pl_ + pw_ * v / vmax + 0.07, y + rh * (i + 0.5) - 0.13, 0.9, 0.26, label(v), T_LABEL, M if i in focus else L, DB)
    return [y + rh * (i + 0.5) for i in range(n)], rh

def columns(x, y, w, h, cats, vals, colors, vmin, vmax, label, inner=(0.03, 0.12, 0.94, 0.7), alt="", gap=70, cat_labels=True):
    ch = _chart(XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, w, h, cats, [("Wert", vals)], alt or "Säulendiagramm")
    pl = ch.plots[0]; pl.gap_width = gap; pl.vary_by_categories = False
    for i, c in enumerate(colors):
        pt = pl.series[0].points[i]; pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(c)
    _axes_off(ch, vmin, vmax, cat_labels); _layout(ch, inner); _transparent(ch)
    n = len(vals); pl_, pw_ = x + w * inner[0], w * inner[2]; pt_, ph_ = y + h * inner[1], h * inner[3]
    X = lambda i: pl_ + pw_ * (i + 0.5) / n
    Y = lambda v: pt_ + ph_ * (1 - (v - vmin) / (vmax - vmin))
    if label:
        for i, v in enumerate(vals):
            yy = Y(v) - 0.32 if v >= 0 else Y(v) + 0.04
            text(X(i) - 0.6, yy, 1.2, 0.28, label(v), T_LABEL, M, DB, "c")
    return X, Y

def lines(x, y, w, h, cats, series, vmin, vmax, inner=(0.03, 0.06, 0.94, 0.78), alt="", markers=True):
    """series = [(name, vals, color, width_pt)]. Rückgabe: X(i), Y(v) in Zoll für Beschriftungen."""
    ch = _chart(XL_CHART_TYPE.LINE_MARKERS if markers else XL_CHART_TYPE.LINE, x, y, w, h, cats, [(n_, v_) for n_, v_, _, _ in series], alt or "Liniendiagramm", "0.00")
    for k, (_, _, col, wd) in enumerate(series):
        ser = ch.plots[0].series[k]; ser.smooth = False
        ser.format.line.color.rgb = rgb(col); ser.format.line.width = Pt(wd)
        if markers:
            ser.marker.style = XL_MARKER_STYLE.CIRCLE; ser.marker.size = 4
            ser.marker.format.fill.solid(); ser.marker.format.fill.fore_color.rgb = rgb(col); ser.marker.format.line.fill.background()
        else: ser.marker.style = XL_MARKER_STYLE.NONE
    _axes_off(ch, vmin, vmax, False); _layout(ch, inner); _transparent(ch)
    n = len(cats); pl_, pw_ = x + w * inner[0], w * inner[2]; pt_, ph_ = y + h * inner[1], h * inner[3]
    return (lambda i: pl_ + pw_ * (i + 0.5) / n), (lambda v: pt_ + ph_ * (1 - (v - vmin) / (vmax - vmin))), (pl_, pw_, pt_ + ph_)

def xlabels(X, idxs, texts, ybase, xmin=None, xmax=None, size=T_SMALL):
    for i, tx in zip(idxs, texts):
        bx = X(i) - 0.5
        if xmax is not None: bx = min(bx, xmax - 1.0)
        if xmin is not None: bx = max(bx, xmin)
        text(bx, ybase, 1.0, 0.26, tx, size, L, DB, "c")

def compare_bars(x, y, title, items, vmax, lab_w=0.95, bar_w=1.2, fmt=lambda v: de(v), row=0.36):
    """Vergleichspaar für Zusammenfassungen: [("Fokus", 13.0, FOCUS), ("übrige", 2.9, CONTEXT)]. Belegt eine Behauptung auf einen Blick."""
    text(x, y, lab_w + bar_w + 0.6, 0.22, title, T_SOURCE, M, ZB, spacing=30)
    for k, (lb, v, col) in enumerate(items):
        yy = y + 0.3 + k * row
        text(x, yy, lab_w, 0.28, lb, T_SMALL, L, DB, "l", "m")
        shape(S.RECTANGLE, x + lab_w, yy + 0.04, max(bar_w * v / vmax, 0.03), 0.2, fill=col)
        text(x + lab_w + bar_w * v / vmax + 0.07, yy, 0.7, 0.28, fmt(v), T_SMALL, M, DB, "l", "m")

def table(x, y, w, h, header_, rows, widths, align, focus_rows=(), size=14, name="Tabelle"):
    from pptx.enum.text import PP_ALIGN as A
    gt = s().shapes.add_table(len(rows) + 1, len(header_), Inches(x), Inches(y), Inches(w), Inches(h)); gt.name = name
    tb = gt.table; tb.first_row = True
    for j, wd in enumerate(widths): tb.columns[j].width = Inches(wd)
    def setc(c, t, sz, font, color, fill, al):
        c.fill.solid(); c.fill.fore_color.rgb = rgb(fill)
        c.margin_left = c.margin_right = Inches(0.12); c.margin_top = c.margin_bottom = Inches(0.03); c.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = c.text_frame.paragraphs[0]; p.alignment = {"l": A.LEFT, "r": A.RIGHT, "c": A.CENTER}[al]
        r = p.add_run(); r.text = t; r.font.size = Pt(sz); r.font.name = font; r.font.color.rgb = rgb(color)
    for j, hd in enumerate(header_): setc(tb.cell(0, j), hd, size - 1, M, WHITE, DB, align[j])
    for i, row in enumerate(rows, start=1):
        fill = "DCEAF6" if (i - 1) in focus_rows else WHITE
        for j, v in enumerate(row): setc(tb.cell(i, j), v, size, M if (j == 0 and (i - 1) in focus_rows) else L, DB, fill, align[j])
    return tb

def save(path):
    _st["prs"].save(path)
    for wmsg in _st["warn"]: print("WARN", wmsg)
