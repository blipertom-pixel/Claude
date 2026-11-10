# -*- coding: utf-8 -*-
"""Vier neue Zurich-Folien (ohne Master), nach Gestaltungsleitfaden: Beleg, Optionen, Fahrplan, Entscheidung.
Alle Zahlen sind fiktive Beispieldaten und aus einem Modell abgeleitet (siehe Fußnoten)."""
import zhelp as Z
from zhelp import *
from pptx.oxml import parse_xml

C_NS = "http://schemas.openxmlformats.org/drawingml/2006/chart"


def plot_layout(chart, x, y, w, h):
    pa = chart._chartSpace.chart.plotArea
    for old in pa.findall(qn("c:layout")): pa.remove(old)
    lay = parse_xml(f'<c:layout xmlns:c="{C_NS}"><c:manualLayout><c:layoutTarget val="inner"/><c:xMode val="edge"/>'
                    f'<c:yMode val="edge"/><c:x val="{x}"/><c:y val="{y}"/><c:w val="{w}"/><c:h val="{h}"/></c:manualLayout></c:layout>')
    pa.insert(0, lay)


def transparent(chart):
    cs = chart._chartSpace
    sp = parse_xml('<c:spPr xmlns:c="%s" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr>' % C_NS)
    for old in cs.findall(qn("c:spPr")): cs.remove(old)
    cs.insert(list(cs).index(cs.find(qn("c:chart"))) + 1, sp)


def hbar(x, y, w, h, cats, vals, nfocus, vmax, fmt, show_cats, inner, alt, labels=True):
    cd = CategoryChartData(number_format=fmt); cd.categories = cats; cd.add_series("Wert", vals)
    gf = Z.s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, Inches(x), Inches(y), Inches(w), Inches(h), cd)
    gf._element.nvGraphicFramePr.cNvPr.set("descr", alt); gf.name = alt[:40]
    ch = gf.chart; ch.has_legend = False; ch.has_title = False
    ch.font.size = Pt(13); ch.font.name = L; ch.font.color.rgb = rgb(DB)
    pl = ch.plots[0]; pl.gap_width = 38; pl.vary_by_categories = False
    for i in range(len(vals)):
        pt = pl.series[0].points[i]; pt.format.fill.solid()
        pt.format.fill.fore_color.rgb = rgb(ZB if i < nfocus else FOCUS_LIGHT)
    if labels:
        pl.has_data_labels = True
        dl = pl.data_labels; dl.number_format = fmt; dl.number_format_is_linked = False
        dl.position = XL_LABEL_POSITION.OUTSIDE_END; dl.font.size = Pt(13); dl.font.name = L; dl.font.color.rgb = rgb(DB)
    va = ch.value_axis; va.minimum_scale, va.maximum_scale = 0, vmax
    va.has_major_gridlines = False; va.visible = False
    ca = ch.category_axis; ca.reverse_order = True; ca.major_tick_mark = XL_TICK_MARK.NONE
    ca.format.line.color.rgb = rgb(LB)
    if show_cats:
        ca.tick_labels.font.size = Pt(13)
    else:
        from pptx.enum.chart import XL_TICK_LABEL_POSITION
        ca.tick_label_position = XL_TICK_LABEL_POSITION.NONE
    plot_layout(ch, *inner); transparent(ch)
    return gf


