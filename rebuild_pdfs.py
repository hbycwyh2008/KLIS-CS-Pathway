#!/usr/bin/env python3
"""Rebuild PDFs: all sections use unified TeX Gyre Heros + Microsoft YaHei fonts."""

import pymupdf
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE_DIR = r"c:\Users\ycshi\Desktop\KLIS CS Pathway"

HEROS = "C:/Users/ycshi/AppData/Local/Programs/MiKTeX/fonts/opentype/public/tex-gyre/texgyreheros-regular.otf"
HEROS_B = "C:/Users/ycshi/AppData/Local/Programs/MiKTeX/fonts/opentype/public/tex-gyre/texgyreheros-bold.otf"
HEROS_I = "C:/Users/ycshi/AppData/Local/Programs/MiKTeX/fonts/opentype/public/tex-gyre/texgyreheros-italic.otf"
MSYH = "C:/WINDOWS/Fonts/msyh.ttc"
MSYH_B = "C:/WINDOWS/Fonts/msyhbd.ttc"
FA5 = "C:/Users/ycshi/AppData/Local/Microsoft/Windows/Fonts/fontawesome5-solid-webfont.ttf"

F_REG = pymupdf.Font(fontfile=HEROS)
F_BOLD = pymupdf.Font(fontfile=HEROS_B)
F_ITAL = pymupdf.Font(fontfile=HEROS_I)
F_CN = pymupdf.Font(fontfile=MSYH)
F_CN_B = pymupdf.Font(fontfile=MSYH_B)
F_FA = pymupdf.Font(fontfile=FA5)

DARK_BLUE = (0.1059, 0.2274, 0.3608)
TEAL = (0.1647, 0.6157, 0.5608)
LIGHT_BLUE = (0.9412, 0.9608, 0.9804)
LIGHT_TEAL = (0.9098, 0.9647, 0.9529)
GRAY_SHADOW = (0.9199, 0.9200, 0.9199)
SEP_COLOR = (0.666, 0.846, 0.824)
CN_GRAY = (0.2902, 0.3333, 0.4078)
FOOTER_GRAY = (0.353, 0.416, 0.478)
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
RED_MAIN = (0.9059, 0.4353, 0.3177)
LIGHT_PINK = (0.9922, 0.9412, 0.9255)

ICON_DESKTOP = "\uf108"
ICON_BRAIN = "\uf5dc"
ICON_GRADCAP = "\uf19d"
ICON_CHECK = "\uf058"
ICON_LIST = "\uf0ca"
ICON_LIGHTBULB = "\uf0eb"
ICON_CIRCLE = "\uf111"

S1_EN = (
    "This pathway is designed as a clear progression, not as a set of "
    "disconnected courses. First, students move from software to hardware. "
    "In CS1, they build strong foundations in programming, web development, "
    "APIs, and full-stack thinking. In CS2, they extend that knowledge into "
    "robotics, physical computing, and computer vision, so they begin to see "
    "how software connects to real-world systems."
)
S1_CN = (
    "\u672c\u8bfe\u7a0b\u4f53\u7cfb\u662f\u4e00\u4e2a\u6e05\u6670\u7684\u8fdb\u9636\u8def\u5f84\uff0c\u800c\u975e\u4e00\u7cfb\u5217\u5f7c\u6b64\u5272\u88c2\u7684\u8bfe\u7a0b\u3002"
    "\u5b66\u751f\u4ece\u8f6f\u4ef6\u8d70\u5411\u786c\u4ef6\uff1a\u5728 CS1 \u4e2d\uff0c\u4ed6\u4eec\u6253\u4e0b\u7f16\u7a0b\u3001Web \u5f00\u53d1\u3001"
    "API \u548c\u5168\u6808\u601d\u7ef4\u7684\u575a\u5b9e\u57fa\u7840\uff1b\u5728 CS2 \u4e2d\uff0c\u4ed6\u4eec\u5c06\u6240\u5b66\u77e5\u8bc6\u62d3\u5c55\u5230"
    "\u673a\u5668\u4eba\u3001\u7269\u7406\u8ba1\u7b97\u548c\u8ba1\u7b97\u673a\u89c6\u89c9\u9886\u57df\uff0c\u4ece\u800c\u7406\u89e3\u8f6f\u4ef6\u5982\u4f55\u4e0e"
    "\u73b0\u5b9e\u4e16\u754c\u7cfb\u7edf\u76f8\u8fde\u63a5\u3002"
)
S2_EN = (
    "AI is embedded throughout the pathway rather than being treated as a "
    "single isolated subject. AI-related ideas and applications are introduced "
    "across the first four courses, so students gradually develop familiarity "
    "with intelligent systems, computational thinking, and real-world AI contexts."
)
S2_CN = (
    "\u4eba\u5de5\u667a\u80fd\u8d2f\u7a7f\u6574\u4e2a\u8bfe\u7a0b\u4f53\u7cfb\uff0c\u800c\u975e\u88ab\u89c6\u4e3a\u4e00\u95e8\u5b64\u7acb\u7684\u5b66\u79d1\u3002"
    "AI \u76f8\u5173\u7406\u5ff5\u548c\u5e94\u7528\u5728\u524d\u56db\u95e8\u8bfe\u7a0b\u4e2d\u9010\u6b65\u5f15\u5165\uff0c\u4f7f\u5b66\u751f"
    "\u5faa\u5e8f\u6e10\u8fdb\u5730\u719f\u6089\u667a\u80fd\u7cfb\u7edf\u3001\u8ba1\u7b97\u601d\u7ef4\u548c AI \u7684\u5b9e\u9645\u5e94\u7528\u573a\u666f\u3002"
)
S3_EN = (
    "AI Foundations is placed at the end as an advanced elective. By that "
    "stage, students have already built enough background in programming, "
    "systems, and problem solving. The final course focuses more directly on "
    "common algorithms used across different areas of AI, helping students "
    "move beyond using AI tools toward understanding how AI works."
)
S3_CN = (
    "\u300cAI \u57fa\u7840\u300d\u4f5c\u4e3a\u9ad8\u9636\u9009\u4fee\u8bfe\u88ab\u5b89\u6392\u5728\u8bfe\u7a0b\u4f53\u7cfb\u7684\u6700\u540e\u3002"
    "\u6b64\u65f6\u5b66\u751f\u5df2\u5728\u7f16\u7a0b\u3001\u7cfb\u7edf\u548c\u95ee\u9898\u89e3\u51b3\u65b9\u9762\u79ef\u7d2f\u4e86\u5145\u5206\u7684\u80cc"
    "\u666f\u77e5\u8bc6\u3002\u8fd9\u95e8\u8bfe\u7a0b\u66f4\u76f4\u63a5\u5730\u805a\u7126\u4e8e AI \u5404\u9886\u57df\u901a\u7528\u7684\u7b97\u6cd5\uff0c"
    "\u5e2e\u52a9\u5b66\u751f\u4ece\u4f7f\u7528 AI \u5de5\u5177\u8fc8\u5411\u7406\u89e3 AI \u7684\u5de5\u4f5c\u539f\u7406\u3002"
)
AP_EN = (
    "The pathway naturally covers AP CSP Big Ideas through hands-on practice "
    "before students formally take the AP course. For example, Big Idea 1 "
    "(Creative Development) maps directly to the complete software development "
    "cycle in CS1 \u2014 from UI design to full-stack deployment. Students enter "
    "AP CSP having already lived the concepts, not just studied them."
)
AP_CN = (
    "\u672c\u8bfe\u7a0b\u4f53\u7cfb\u5728\u5b66\u751f\u6b63\u5f0f\u53c2\u52a0 AP \u8003\u8bd5\u4e4b\u524d\uff0c\u5df2\u901a\u8fc7\u5b9e\u8df5\u81ea\u7136\u8986\u76d6\u4e86 "
    "AP CSP \u7684\u6838\u5fc3\u7406\u5ff5\uff08Big Ideas\uff09\u3002\u4f8b\u5982\uff0cBig Idea 1\uff08\u521b\u610f\u5f00\u53d1\uff09"
    "\u76f4\u63a5\u5bf9\u5e94 CS1 \u4e2d\u5b66\u751f\u6240\u7ecf\u5386\u7684\u5b8c\u6574\u8f6f\u4ef6\u5f00\u53d1\u6d41\u7a0b\u2014\u2014\u4ece UI \u8bbe\u8ba1"
    "\u5230\u5168\u6808\u90e8\u7f72\u3002\u5b66\u751f\u5728\u8fdb\u5165 AP CSP \u65f6\uff0c\u5df2\u901a\u8fc7\u9879\u76ee\u5b9e\u8df5\u638c\u63e1\u4e86\u6838\u5fc3"
    "\u6982\u5ff5\uff0c\u800c\u975e\u4ec5\u505c\u7559\u5728\u7406\u8bba\u5c42\u9762\u3002"
)
IS_EN = (
    "This pathway moves students from software, to hardware, to AI, with AI "
    "concepts integrated throughout the earlier courses, AP CSP Big Ideas "
    "covered through hands-on practice, and advanced AI algorithms taught in "
    "the final elective."
)
IS_CN = (
    "\u672c\u8bfe\u7a0b\u4f53\u7cfb\u5f15\u5bfc\u5b66\u751f\u4ece\u8f6f\u4ef6\u5230\u786c\u4ef6\uff0c\u518d\u5230\u4eba\u5de5\u667a\u80fd\uff0c"
    "AI \u6982\u5ff5\u878d\u5165\u524d\u671f\u8bfe\u7a0b\uff0cAP CSP \u6838\u5fc3\u7406\u5ff5\u901a\u8fc7\u5b9e\u8df5\u81ea\u7136\u8986\u76d6\uff0c"
    "\u9ad8\u9636 AI \u7b97\u6cd5\u5728\u6700\u7ec8\u9009\u4fee\u8bfe\u4e2d\u6df1\u5165\u8bb2\u6388\u3002"
)

BIL_SECTIONS = [
    (ICON_DESKTOP, "Software to Hardware", "\u4ece\u8f6f\u4ef6\u5230\u786c\u4ef6", " / ",
     S1_EN, S1_CN, 68, 46, False),
    (ICON_BRAIN, "AI Embedded Throughout / AI", "\u8d2f\u7a7f\u59cb\u7ec8", " ",
     S2_EN, S2_CN, 52, 32, False),
    (ICON_GRADCAP, "AI Foundations as Capstone / AI", "\u57fa\u7840\u4f5c\u4e3a\u9876\u5c42\u8bfe\u7a0b", " ",
     S3_EN, S3_CN, 68, 46, False),
    (ICON_CHECK, "AP-Aligned by Design", "\u4e0e AP \u8003\u7eb2\u81ea\u7136\u5bf9\u9f50", " / ",
     AP_EN, AP_CN, 68, 46, False),
    (ICON_LIST, "In Short", "\u603b\u7ed3", " / ",
     IS_EN, IS_CN, 54, 32, True),
]

SENSOR_TOTAL = 5 * 95.49
NEW_BUDGET_TOTAL = 7345.14 + SENSOR_TOTAL


def draw_section(page, top, h, hdr_h, left, right, off=2.83, summary=False):
    mc = TEAL if summary else DARK_BLUE
    bc = LIGHT_TEAL if summary else LIGHT_BLUE
    page.draw_rect(pymupdf.Rect(left + off, top + off, right + off, top + h + off),
                   fill=GRAY_SHADOW, color=None, width=0)
    page.draw_rect(pymupdf.Rect(left, top, right, top + h),
                   fill=mc, color=None, width=0)
    page.draw_rect(pymupdf.Rect(left, top + hdr_h, right, top + h),
                   fill=bc, color=None, width=0)
    page.draw_line(pymupdf.Point(left + 1.5, top),
                   pymupdf.Point(left + 1.5, top + h),
                   color=mc, width=3.0)


def icon_header_bi(pg, x, y, icon, en, cn, sep=" / ", fs=10.9):
    tw = pymupdf.TextWriter(pg.rect)
    tw.append(pymupdf.Point(x, y), icon, font=F_FA, fontsize=fs)
    tw.write_text(pg, color=WHITE)
    tw2 = pymupdf.TextWriter(pg.rect)
    tw2.append(pymupdf.Point(tw.last_point.x + 5, y), en + sep, font=F_BOLD, fontsize=fs)
    tw2.write_text(pg, color=WHITE)
    tw3 = pymupdf.TextWriter(pg.rect)
    tw3.append(pymupdf.Point(tw2.last_point.x, y), cn, font=F_CN_B, fontsize=fs)
    tw3.write_text(pg, color=WHITE)


def icon_header_en(pg, x, y, icon, en, fs=10.9):
    tw = pymupdf.TextWriter(pg.rect)
    tw.append(pymupdf.Point(x, y), icon, font=F_FA, fontsize=fs)
    tw.write_text(pg, color=WHITE)
    tw2 = pymupdf.TextWriter(pg.rect)
    tw2.append(pymupdf.Point(tw.last_point.x + 5, y), en, font=F_BOLD, fontsize=fs)
    tw2.write_text(pg, color=WHITE)


def body_en(pg, tl, tr, top, h, text, bold=False):
    fpath = HEROS_B if bold else HEROS
    fname = "eb" if bold else "er"
    return pg.insert_textbox(pymupdf.Rect(tl, top, tr, top + h),
                             text, fontsize=10.9, fontname=fname, fontfile=fpath, color=BLACK)


def body_cn(pg, tl, tr, top, h, text):
    return pg.insert_textbox(pymupdf.Rect(tl, top, tr, top + h),
                             text, fontsize=10.0, fontname="cn", fontfile=MSYH, color=CN_GRAY)


def bil_section(pg, y, icon, en_title, cn_title, sep, en_body, cn_body,
                en_h, cn_h, L, R, TL, TR, hdr_h=16.6, summary=False):
    gap_e, gap_sep, pad = 5, 3, 3
    total_h = int(hdr_h + gap_e + en_h + gap_sep + cn_h + pad)
    draw_section(pg, y, total_h, hdr_h, L, R, summary=summary)
    icon_header_bi(pg, TL, y + 13, icon, en_title, cn_title, sep=sep)
    et = y + hdr_h + gap_e
    body_en(pg, TL, TR, et, en_h, en_body, bold=summary)
    sep_y = et + en_h
    pg.draw_line(pymupdf.Point(TL, sep_y), pymupdf.Point(TR, sep_y),
                 color=SEP_COLOR, width=0.4)
    body_cn(pg, TL, TR, sep_y + gap_sep, cn_h, cn_body)
    return y + total_h


def nds_section(pg, y, icon, en_title, en_body, en_h,
                L, R, TL, TR, hdr_h=17.3, off=2.9, summary=False):
    gap_e, pad = 8, 5
    total_h = int(hdr_h + gap_e + en_h + pad)
    draw_section(pg, y, total_h, hdr_h, L, R, off=off, summary=summary)
    icon_header_en(pg, TL, y + 13.5, icon, en_title)
    et = y + hdr_h + gap_e
    body_en(pg, TL, TR, et, en_h, en_body, bold=summary)
    return y + total_h


# ==========================================================
# BILINGUAL PDF
# ==========================================================
def rebuild_bilingual():
    bak = os.path.join(BASE_DIR, "KLIS CS Pathway & Prerequisites Bilingual.pdf.bak")
    out = os.path.join(BASE_DIR, "KLIS CS Pathway & Prerequisites Bilingual.pdf")
    src = pymupdf.open(bak)
    dst = pymupdf.open()
    pw, ph = src[0].rect.width, src[0].rect.height

    dst.insert_pdf(src, from_page=0, to_page=0)

    pg = dst.new_page(width=pw, height=ph)
    L, R, TL, TR = 39.7, 555.6, 52.5, 542.8

    pg.draw_rect(pymupdf.Rect(0, 0, pw, 79), fill=DARK_BLUE, color=None, width=0)
    pg.draw_rect(pymupdf.Rect(0, 79, pw, 84), fill=TEAL, color=None, width=0)

    tw = pymupdf.TextWriter(pg.rect)
    tw.append(pymupdf.Point(235.2, 51.5), "CS PATHWAY", font=F_REG, fontsize=9.9)
    tw.write_text(pg, color=WHITE)
    tw2 = pymupdf.TextWriter(pg.rect)
    tw2.append(pymupdf.Point(tw.last_point.x + 3, 51.5), "/", font=F_REG, fontsize=9.9)
    tw2.write_text(pg, color=WHITE)
    tw3 = pymupdf.TextWriter(pg.rect)
    tw3.append(pymupdf.Point(tw2.last_point.x + 5, 51.5), "\u8bfe\u7a0b\u4f53\u7cfb",
               font=F_CN, fontsize=10.0)
    tw3.write_text(pg, color=WHITE)

    tw4 = pymupdf.TextWriter(pg.rect)
    tw4.append(pymupdf.Point(154.0, 78.7), "Design Rationale", font=F_BOLD, fontsize=21.8)
    tw4.write_text(pg, color=WHITE)
    tw5 = pymupdf.TextWriter(pg.rect)
    tw5.append(pymupdf.Point(tw4.last_point.x + 10, 78.7), "\u8bbe\u8ba1\u7406\u5ff5",
               font=F_CN_B, fontsize=21.9)
    tw5.write_text(pg, color=WHITE)

    GAP = 7
    y = 100

    for icon, en_title, cn_title, sep, en_body, cn_body, en_h, cn_h, is_summary in BIL_SECTIONS:
        hdr = 16.3 if is_summary else 16.6
        y = bil_section(pg, y, icon, en_title, cn_title, sep, en_body, cn_body,
                        en_h, cn_h, L, R, TL, TR, hdr_h=hdr, summary=is_summary)
        y += GAP

    tw_fi = pymupdf.TextWriter(pg.rect)
    tw_fi.append(pymupdf.Point(163.1, 799.9), ICON_CIRCLE, font=F_FA, fontsize=10.0)
    tw_fi.write_text(pg, color=FOOTER_GRAY)
    tw_fe = pymupdf.TextWriter(pg.rect)
    tw_fe.append(pymupdf.Point(183.0, 799.9), "See reverse for prerequisites",
                 font=F_ITAL, fontsize=9.9)
    tw_fe.write_text(pg, color=FOOTER_GRAY)
    tw_fs = pymupdf.TextWriter(pg.rect)
    tw_fs.append(pymupdf.Point(tw_fe.last_point.x + 5, 799.9), "/", font=F_ITAL, fontsize=9.9)
    tw_fs.write_text(pg, color=FOOTER_GRAY)
    tw_fc = pymupdf.TextWriter(pg.rect)
    tw_fc.append(pymupdf.Point(tw_fs.last_point.x + 5, 799.9),
                 "\u7ffb\u9762\u67e5\u770b\u8bfe\u7a0b\u5148\u4fee\u8981\u6c42",
                 font=F_CN, fontsize=10.0)
    tw_fc.write_text(pg, color=FOOTER_GRAY)

    dst.insert_pdf(src, from_page=2, to_page=2)

    dst.save(out, garbage=4, deflate=True)
    dst.close()
    src.close()
    print("\u2713 Bilingual PDF rebuilt with YaHei")


# ==========================================================
# NEEDS PDF
# ==========================================================
def rebuild_needs():
    bak = os.path.join(BASE_DIR, "KLIS CS Pathway and Needs.pdf.bak")
    out = os.path.join(BASE_DIR, "KLIS CS Pathway and Needs.pdf")
    src = pymupdf.open(bak)
    dst = pymupdf.open()
    pw, ph = src[0].rect.width, src[0].rect.height

    dst.insert_pdf(src, from_page=0, to_page=0)

    L, R, TL, TR = 68.0, 527.2, 82.8, 515.0
    GAP = 10

    # Page 2: overview (copied) + Design Rationale header + Section 1
    pg2 = dst.new_page(width=pw, height=ph)
    pg2.show_pdf_page(pymupdf.Rect(0, 0, pw, 640), src, 1,
                      clip=pymupdf.Rect(0, 0, pw, 640))

    tw_dr_icon = pymupdf.TextWriter(pg2.rect)
    tw_dr_icon.append(pymupdf.Point(68.0, 648.7), ICON_LIGHTBULB, font=F_FA, fontsize=14)
    tw_dr_icon.write_text(pg2, color=DARK_BLUE)
    tw_dr = pymupdf.TextWriter(pg2.rect)
    tw_dr.append(pymupdf.Point(95.0, 648.7), "Design Rationale", font=F_BOLD, fontsize=14)
    tw_dr.write_text(pg2, color=DARK_BLUE)

    nds_section(pg2, 668, ICON_DESKTOP,
                "Software to Hardware Progression", S1_EN, 84,
                L, R, TL, TR)

    tw_f2 = pymupdf.TextWriter(pg2.rect)
    tw_f2.append(pymupdf.Point(246, 809.4), "Learn. Build. Innovate. Protect.",
                 font=F_REG, fontsize=9.9)
    tw_f2.write_text(pg2, color=FOOTER_GRAY)

    # Page 3: Sections 2-5
    pg3 = dst.new_page(width=pw, height=ph)
    pg3.show_pdf_page(pymupdf.Rect(0, 0, pw, 48), src, 2,
                      clip=pymupdf.Rect(0, 0, pw, 48))

    y3 = 58
    y3 = nds_section(pg3, y3, ICON_BRAIN,
                     "AI Embedded Throughout", S2_EN, 68,
                     L, R, TL, TR)
    y3 += GAP
    y3 = nds_section(pg3, y3, ICON_GRADCAP,
                     "AI Foundations as Capstone", S3_EN, 68,
                     L, R, TL, TR)
    y3 += GAP
    y3 = nds_section(pg3, y3, ICON_CHECK,
                     "AP-Aligned by Design", AP_EN, 84,
                     L, R, TL, TR)
    y3 += GAP
    y3 = nds_section(pg3, y3, ICON_LIST,
                     "In Short", IS_EN, 54,
                     L, R, TL, TR, summary=True)

    tw_f3 = pymupdf.TextWriter(pg3.rect)
    tw_f3.append(pymupdf.Point(246, 809.4), "Learn. Build. Innovate. Protect.",
                 font=F_REG, fontsize=9.9)
    tw_f3.write_text(pg3, color=FOOTER_GRAY)

    # Page 4: Budget (with VEX sensor line)
    pg4 = dst.new_page(width=pw, height=ph)
    CUT4 = 655
    pg4.show_pdf_page(pymupdf.Rect(0, 0, pw, CUT4), src, 3,
                      clip=pymupdf.Rect(0, 0, pw, CUT4))

    NEW_BOTTOM = 698.8 + 16.5
    NEW_SHADOW = 701.7 + 16.5
    pg4.draw_rect(pymupdf.Rect(70.9, CUT4, 530.1, NEW_SHADOW),
                  fill=GRAY_SHADOW, color=None, width=0)
    pg4.draw_rect(pymupdf.Rect(68.0, CUT4, 527.2, NEW_BOTTOM),
                  fill=RED_MAIN, color=None, width=0)
    pg4.draw_rect(pymupdf.Rect(68.0, CUT4, 527.2, NEW_BOTTOM),
                  fill=LIGHT_PINK, color=None, width=0)
    pg4.draw_line(pymupdf.Point(69.5, CUT4), pymupdf.Point(69.5, NEW_BOTTOM),
                  color=RED_MAIN, width=3.0)

    ny = 647.7 + 16.5
    tw_b = pymupdf.TextWriter(pg4.rect)
    tw_b.append(pymupdf.Point(89.4, ny), "\u2022 ", font=F_REG, fontsize=10.9)
    tw_b.write_text(pg4, color=BLACK)
    tw_d = pymupdf.TextWriter(pg4.rect)
    tw_d.append(pymupdf.Point(100.3, ny), "5 VEX V5 AI Vision Sensors: ",
                font=F_REG, fontsize=10.9)
    tw_d.write_text(pg4, color=BLACK)
    tw_p = pymupdf.TextWriter(pg4.rect)
    tw_p.append(pymupdf.Point(tw_d.last_point.x, ny),
                f"USD {SENSOR_TOTAL:,.2f}", font=F_BOLD, fontsize=10.9)
    tw_p.write_text(pg4, color=BLACK)

    tbt = 657.4 + 16.5
    tbb = 688.0 + 16.5
    pg4.draw_rect(pymupdf.Rect(182.5, tbt, 425.0, tbb),
                  fill=RED_MAIN, color=None, width=0)
    ty = 676.1 + 16.5
    tw_tl = pymupdf.TextWriter(pg4.rect)
    tw_tl.append(pymupdf.Point(192.5, ty), "Total First-Year Cost:",
                 font=F_BOLD, fontsize=11.9)
    tw_tl.write_text(pg4, color=WHITE)
    tw_ta = pymupdf.TextWriter(pg4.rect)
    tw_ta.append(pymupdf.Point(327.5, ty), f"USD {NEW_BUDGET_TOTAL:,.2f}",
                 font=F_BOLD, fontsize=11.9)
    tw_ta.write_text(pg4, color=WHITE)

    pg4.show_pdf_page(pymupdf.Rect(0, 795, pw, ph), src, 3,
                      clip=pymupdf.Rect(0, 795, pw, ph))

    dst.save(out, garbage=4, deflate=True)
    dst.close()
    src.close()
    print("\u2713 Needs PDF rebuilt with unified fonts")


if __name__ == "__main__":
    rebuild_bilingual()
    rebuild_needs()
    print("\nDone.")
