import streamlit as st

st.set_page_config(
    page_title="Impact Assessment – DOST SETUP 4.0 iFund",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #f5f5f0;
}

.block-container {
    padding: 2rem 1rem 4rem 1rem;
    max-width: 800px;
    margin: auto;
}

/* Hide streamlit chrome */
header, footer, [data-testid="stDecoration"] { visibility: hidden; }
#MainMenu { visibility: hidden; }

/* ── Page header ── */
.page-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 16px;
}
.page-title   { font-size: 20px; font-weight: 700; color: #111; margin: 0; }
.page-sub     { font-size: 12px; color: #999; margin: 2px 0 0 0; }
.period-badge {
    background: #dbeafe;
    color: #1d4ed8;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 20px;
    white-space: nowrap;
}

/* ── Dropdowns ── */
.stSelectbox > div > div {
    background: #fff;
    border-radius: 8px;
    border: 1.5px solid #e0e0e0;
    font-size: 13px;
}
.stSelectbox label { display: none !important; }

/* ── Metric cards ── */
.metrics-row {
    display: flex;
    gap: 10px;
    margin: 20px 0;
}
.metric-card {
    flex: 1;
    background: #fff;
    border-radius: 12px;
    padding: 14px 16px;
    border: 1.5px solid #ececec;
}
.metric-label { font-size: 11px; color: #aaa; font-weight: 500; margin-bottom: 6px; }
.metric-value { font-size: 30px; font-weight: 700; line-height: 1; margin-bottom: 4px; }
.metric-sub   { font-size: 11px; color: #bbb; }
.c-default { color: #111; }
.c-green   { color: #16a34a; }
.c-orange  { color: #d97706; }
.c-red     { color: #dc2626; }

/* ── Section label ── */
.section-label {
    font-size: 11px;
    font-weight: 700;
    color: #888;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin: 24px 0 12px 0;
}

/* ── Output cards ── */
.out-card {
    background: #fff;
    border-radius: 12px;
    border: 1.5px solid #e5e7eb;
    padding: 16px;
    height: 100%;
    box-sizing: border-box;
}
.out-card.border-green  { border-color: #86efac; }
.out-card.border-orange { border-color: #fcd34d; }
.out-card.border-red    { border-color: #fca5a5; }

.card-type  {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #bbb;
    margin-bottom: 6px;
}
.card-title {
    font-size: 13px;
    font-weight: 700;
    color: #111;
    line-height: 1.4;
    margin-bottom: 12px;
}
.tr {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: #555;
    margin-bottom: 3px;
}
.tr-val { font-weight: 600; color: #111; }

/* Progress bar */
.prog-track {
    background: #f0f0f0;
    border-radius: 99px;
    height: 5px;
    margin: 10px 0 8px 0;
    overflow: hidden;
}
.prog-fill { height: 5px; border-radius: 99px; }
.fill-green  { background: #22c55e; }
.fill-orange { background: #f59e0b; }
.fill-red    { background: #ef4444; }
.fill-gray   { background: #d1d5db; }

/* Verdict row */
.vrow {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 6px 0;
}
.pct-text { font-size: 11px; color: #aaa; }

/* Badges */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 20px;
}
.badge-green  { background: #dcfce7; color: #15803d; }
.badge-orange { background: #fef9c3; color: #a16207; }
.badge-red    { background: #fee2e2; color: #b91c1c; }

.card-note {
    font-size: 11px;
    color: #888;
    line-height: 1.5;
    margin-top: 10px;
    padding-top: 10px;
    border-top: 1px solid #f3f4f6;
}

/* Non-quant */
.nq-actual-lbl {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #bbb;
    margin: 10px 0 4px 0;
}
.nq-actual-txt {
    font-size: 12px;
    color: #444;
    line-height: 1.5;
    margin-bottom: 12px;
}
.verdict-psto-lbl {
    font-size: 11px;
    color: #888;
    font-weight: 500;
    margin-bottom: 4px;
}

/* Make selectbox inside NQ card tight */
div[data-testid="stSelectbox"] > div > div {
    min-height: 36px !important;
    font-size: 12px !important;
}

/* ── Overall verdict ── */
.overall-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #fff;
    border: 1.5px solid #e5e7eb;
    border-radius: 12px;
    padding: 14px 18px;
    margin-top: 24px;
}
.overall-lbl {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    font-weight: 600;
    color: #333;
}
.overall-icon { font-size: 16px; }

/* ── Footer ── */
.footer {
    text-align: center;
    font-size: 11px;
    color: #ccc;
    margin-top: 32px;
}

/* Gap between card rows */
.card-gap { margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════════════════════════════════════

VERDICT_OPTIONS = ["Accomplished", "Partially accomplished", "Not accomplished"]

def badge(v):
    v = v.lower()
    if v == "accomplished":
        return '<span class="badge badge-green">✓ Accomplished</span>'
    elif v == "partially accomplished":
        return '<span class="badge badge-orange">— Partially accomplished</span>'
    return '<span class="badge badge-red">✕ Not accomplished</span>'

def overall_badge(v):
    v = v.lower()
    if v == "accomplished":
        return '<span style="color:#16a34a;font-size:13px;font-weight:700;">✓ Accomplished</span>'
    elif v == "partially accomplished":
        return '<span style="color:#d97706;font-size:13px;font-weight:700;">— Partially accomplished</span>'
    return '<span style="color:#dc2626;font-size:13px;font-weight:700;">✕ Not accomplished</span>'

def border_cls(v):
    v = v.lower()
    if v == "accomplished": return "border-green"
    if v == "partially accomplished": return "border-orange"
    return "border-red"

def fill_cls(v):
    v = v.lower()
    if v == "accomplished": return "fill-green"
    if v == "partially accomplished": return "fill-orange"
    return "fill-red"

def verdict_idx(v):
    v = v.lower()
    if v == "accomplished": return 0
    if v == "partially accomplished": return 1
    return 2

REPORTS = {
    "Honore Cafe": {
        "semesters": {
            "S2 2021 (Jul – Dec 2021)": {
                "badge": "S2 2021 · July – December 2021",
                "outputs": [
                    {
                        "type": "quantifiable",
                        "title": "Improve product quality via 3-deck oven",
                        "target": None, "actual": None, "unit": "",
                        "verdict": "accomplished", "pct": 100,
                        "note": "LPG Oven in good working condition as of December 2021.",
                    },
                    {
                        "type": "quantifiable",
                        "title": "Reduce baking time by 50% (4 hrs → 2 hrs)",
                        "target": "50%", "actual": "50%", "unit": "",
                        "verdict": "accomplished", "pct": 100,
                        "note": "",
                    },
                    {
                        "type": "quantifiable",
                        "title": "Improve baking capacity by 100% (792 → 1,584 pcs/day)",
                        "target": "1,584 pcs/day", "actual": "214 pcs/day", "unit": "",
                        "verdict": "not accomplished", "pct": 14,
                        "note": "COVID-19 significantly affected operations during the first year.",
                    },
                    {
                        "type": "quantifiable",
                        "title": "Increase production volume by 45%",
                        "target": "358,320 pcs", "actual": "77,040 pcs", "unit": "",
                        "verdict": "not accomplished", "pct": 0,
                        "note": "Production decreased 69% due to COVID-19.",
                    },
                    {
                        "type": "quantifiable",
                        "title": "Increase sales by 78% (₱3.06M → ₱5.46M)",
                        "target": "₱5,455,510", "actual": "₱2,404,800", "unit": "",
                        "verdict": "not accomplished", "pct": 0,
                        "note": "Sales decreased 21% due to COVID-19.",
                    },
                    {
                        "type": "quantifiable",
                        "title": "Establish at least 2 additional markets in Aklan",
                        "target": "2 outlets", "actual": "1 outlet", "unit": "",
                        "verdict": "partially accomplished", "pct": 50,
                        "note": "Only one additional outlet established in Kalibo, Aklan.",
                    },
                    {
                        "type": "quantifiable",
                        "title": "Generate at least 1 additional worker",
                        "target": "1 worker", "actual": "4 workers", "unit": "",
                        "verdict": "accomplished", "pct": 100,
                        "note": "",
                    },
                    {
                        "type": "non-quantifiable",
                        "title": "Enhance compliance with food safety standards",
                        "actual_text": "Enhanced via procured stainless steel equipment and DOST VI Food Safety Consultancy.",
                        "default_verdict": "accomplished",
                    },
                    {
                        "type": "non-quantifiable",
                        "title": "Improve production management using inventory/POS system",
                        "actual_text": "No improvement. POS not utilized due to lack of training for new employees as of December 2021.",
                        "default_verdict": "not accomplished",
                    },
                ],
                "overall": "partially accomplished",
            },
            "S1 2024 (Jan – Jun 2024)": {
                "badge": "S1 2024 · January – June 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Improve product quality via 3-deck oven", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "LPG Oven in good working condition as of June 2024."},
                    {"type": "quantifiable", "title": "Reduce baking time by 50% (4 hrs → 2 hrs)", "target": "50%", "actual": "50%", "unit": "", "verdict": "accomplished", "pct": 100, "note": ""},
                    {"type": "quantifiable", "title": "Improve baking capacity by 100% (792 → 1,584 pcs/day)", "target": "1,584 pcs/day", "actual": "214 pcs/day", "unit": "", "verdict": "not accomplished", "pct": 14, "note": "First-year COVID impact."},
                    {"type": "quantifiable", "title": "Increase production volume by 45%", "target": "358,320 pcs", "actual": "52,380 pcs", "unit": "", "verdict": "partially accomplished", "pct": 59, "note": "Recovery underway; significant growth in Jan–Jun 2024."},
                    {"type": "quantifiable", "title": "Increase sales by 78% (₱3.06M → ₱5.46M)", "target": "₱5,455,510", "actual": "₱3,207,600", "unit": "", "verdict": "partially accomplished", "pct": 59, "note": "Sales significantly recovered."},
                    {"type": "quantifiable", "title": "Establish at least 2 additional markets in Aklan", "target": "2 outlets", "actual": "5+ outlets", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Multiple new outlets including Boracay."},
                    {"type": "quantifiable", "title": "Generate at least 1 additional worker", "target": "1 worker", "actual": "4 workers", "unit": "", "verdict": "accomplished", "pct": 100, "note": ""},
                    {"type": "non-quantifiable", "title": "Enhance compliance with food safety standards", "actual_text": "Compliance enhanced through stainless steel equipment and DOST VI consultancy.", "default_verdict": "accomplished"},
                    {"type": "non-quantifiable", "title": "Improve production management using POS system", "actual_text": "POS software is now operational and ready for use as of June 2024.", "default_verdict": "accomplished"},
                ],
                "overall": "accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "badge": "S2 2024 · July – December 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Improve product quality via 3-deck oven", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Oven in good working condition as of December 2024."},
                    {"type": "quantifiable", "title": "Reduce baking time by 50%", "target": "50%", "actual": "50%", "unit": "", "verdict": "accomplished", "pct": 100, "note": ""},
                    {"type": "quantifiable", "title": "Improve baking capacity by 100%", "target": "1,584 pcs/day", "actual": "214 pcs/day", "unit": "", "verdict": "not accomplished", "pct": 14, "note": "COVID first-year impact still reflected."},
                    {"type": "quantifiable", "title": "Increase production volume by 45%", "target": "45%", "actual": "Recovery ongoing", "unit": "", "verdict": "partially accomplished", "pct": 50, "note": "Improving each semester."},
                    {"type": "quantifiable", "title": "Increase sales by 78%", "target": "₱5,455,510", "actual": "₱3,384,500", "unit": "", "verdict": "partially accomplished", "pct": 62, "note": "Sales continue to grow; target not yet reached."},
                    {"type": "quantifiable", "title": "Establish at least 2 additional markets", "target": "2 outlets", "actual": "5+ outlets", "unit": "", "verdict": "accomplished", "pct": 100, "note": ""},
                    {"type": "quantifiable", "title": "Generate at least 1 additional worker", "target": "1 worker", "actual": "4 workers", "unit": "", "verdict": "accomplished", "pct": 100, "note": ""},
                    {"type": "non-quantifiable", "title": "Enhance compliance with food safety standards", "actual_text": "Compliance maintained through equipment and DOST VI training.", "default_verdict": "accomplished"},
                    {"type": "non-quantifiable", "title": "Improve production management using POS system", "actual_text": "POS software in good working condition and utilized by the firm as of December 2024.", "default_verdict": "accomplished"},
                ],
                "overall": "accomplished",
            },
        },
    },
    "Han Jim Marketing Corporation": {
        "semesters": {
            "S1 2024 (Jan – Jun 2024)": {
                "badge": "S1 2024 · January – June 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Upgrade cold storage facility", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Cold storage upgraded and in good working condition."},
                    {"type": "quantifiable", "title": "Increase Kimchi Cabbage production volume by 30%", "target": "30%", "actual": "25%", "unit": "", "verdict": "partially accomplished", "pct": 83, "note": "Target partially met due to initial calibration period."},
                    {"type": "quantifiable", "title": "Improve purified water system for washing raw vegetables", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "System installed and fully operational."},
                    {"type": "quantifiable", "title": "Expand market to at least 2 additional outlets", "target": "2 outlets", "actual": "1 outlet", "unit": "", "verdict": "partially accomplished", "pct": 50, "note": "One outlet in Bacolod City. Expansion ongoing."},
                    {"type": "quantifiable", "title": "Increase gross sales by at least 20%", "target": "20%", "actual": "12%", "unit": "", "verdict": "partially accomplished", "pct": 60, "note": "Expected to accelerate in next semester."},
                ],
                "overall": "partially accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "badge": "S2 2024 · July – December 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Upgrade cold storage facility", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Equipment in good condition as of December 2024."},
                    {"type": "quantifiable", "title": "Increase Kimchi Cabbage production volume by 30%", "target": "30%", "actual": "25%", "unit": "", "verdict": "partially accomplished", "pct": 83, "note": "Sustained growth maintained in S2 2024."},
                    {"type": "quantifiable", "title": "Improve purified water system", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Used in all washing and rinsing operations."},
                    {"type": "quantifiable", "title": "Expand market to at least 2 additional outlets", "target": "2 outlets", "actual": "2 outlets", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Outlets in Bacolod City and Roxas City."},
                    {"type": "quantifiable", "title": "Increase gross sales by at least 20%", "target": "20%", "actual": "21%", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Sales grew from ₱4,050,000 to ₱4,900,500."},
                ],
                "overall": "accomplished",
            },
        },
    },
    "SJL Corporation": {
        "semesters": {
            "S1 2024 (Jan – Jun 2024)": {
                "badge": "S1 2024 · January – June 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Acquire large format digital printing machine", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Equipment acquired and fully operational."},
                    {"type": "quantifiable", "title": "Acquire commercial embroidery machine (12 heads)", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Machine installed; staff trained by supplier."},
                    {"type": "quantifiable", "title": "Increase production volume by at least 30%", "target": "30%", "actual": "20%", "unit": "", "verdict": "partially accomplished", "pct": 67, "note": "On track to meet target by end of 2024."},
                    {"type": "quantifiable", "title": "Expand market to at least 1 additional BPO/corporate client", "target": "1 client", "actual": "2 clients", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Two new BPO clients in Iloilo City."},
                    {"type": "non-quantifiable", "title": "Improve product quality and standardize production processes", "actual_text": "Product quality improved through new equipment and standardized procedures.", "default_verdict": "accomplished"},
                ],
                "overall": "accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "badge": "S2 2024 · July – December 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Acquire large format digital printing machine", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Fully operational for all large-format printing orders."},
                    {"type": "quantifiable", "title": "Acquire commercial embroidery machine (12 heads)", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Producing uniforms, caps, and jackets at full capacity."},
                    {"type": "quantifiable", "title": "Increase production volume by at least 30%", "target": "30%", "actual": "32%", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Target achieved as of December 2024."},
                    {"type": "quantifiable", "title": "Expand market to at least 1 additional BPO/corporate client", "target": "1 client", "actual": "4 clients", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Four new clients in Iloilo City and nearby municipalities."},
                    {"type": "non-quantifiable", "title": "Improve product quality and standardize production processes", "actual_text": "Standardized QC procedures consistently applied across all product lines.", "default_verdict": "accomplished"},
                ],
                "overall": "accomplished",
            },
        },
    },
    "Filbake Food Corporation": {
        "semesters": {
            "S1 2023 (Jan – Jun 2023)": {
                "badge": "S1 2023 · January – June 2023",
                "outputs": [
                    {"type": "quantifiable", "title": "Implement beverage line automation (filling & sealing machine)", "target": None, "actual": None, "unit": "", "verdict": "partially accomplished", "pct": 50, "note": "Machine delivered; installation and commissioning in progress."},
                    {"type": "quantifiable", "title": "Increase beverage production volume by 40%", "target": "40%", "actual": "5%", "unit": "", "verdict": "partially accomplished", "pct": 13, "note": "Significant increase expected after full commissioning."},
                    {"type": "quantifiable", "title": "Increase overall gross sales by 15%", "target": "15%", "actual": "3%", "unit": "", "verdict": "partially accomplished", "pct": 20, "note": "Sales grew from ₱29M to ₱29.87M."},
                    {"type": "non-quantifiable", "title": "Adopt Industry 4.0 technologies (ERP/desktop systems)", "actual_text": "Desktop computers and ERP modules procured; installation ongoing.", "default_verdict": "partially accomplished"},
                    {"type": "non-quantifiable", "title": "Maintain compliance with food safety standards", "actual_text": "Compliance maintained. Latest internal audit passed with no major findings.", "default_verdict": "accomplished"},
                ],
                "overall": "partially accomplished",
            },
            "S2 2023 (Jul – Dec 2023)": {
                "badge": "S2 2023 · July – December 2023",
                "outputs": [
                    {"type": "quantifiable", "title": "Implement beverage line automation", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Machine now fully commissioned and operational."},
                    {"type": "quantifiable", "title": "Increase beverage production volume by 40%", "target": "40%", "actual": "20%", "unit": "", "verdict": "partially accomplished", "pct": 50, "note": "Volume grew from 25,000 to 30,000 cups/semester."},
                    {"type": "quantifiable", "title": "Increase overall gross sales by 15%", "target": "15%", "actual": "8% (cumulative 11%)", "unit": "", "verdict": "partially accomplished", "pct": 73, "note": "On track to reach 15% target."},
                    {"type": "non-quantifiable", "title": "Adopt Industry 4.0 technologies (ERP deployment)", "actual_text": "ERP system with production monitoring modules fully deployed and in use.", "default_verdict": "accomplished"},
                    {"type": "non-quantifiable", "title": "Maintain compliance with food safety standards", "actual_text": "Compliance maintained. Latest audit passed with no major findings.", "default_verdict": "accomplished"},
                ],
                "overall": "partially accomplished",
            },
            "S1 2024 (Jan – Jun 2024)": {
                "badge": "S1 2024 · January – June 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Implement beverage line automation (2nd cycle)", "target": None, "actual": None, "unit": "", "verdict": "partially accomplished", "pct": 50, "note": "Partially installed. Full commissioning expected Q3 2024."},
                    {"type": "quantifiable", "title": "Increase beverage production volume by 40%", "target": "40%", "actual": "18%", "unit": "", "verdict": "partially accomplished", "pct": 45, "note": "Will accelerate after full automation."},
                    {"type": "quantifiable", "title": "Increase overall gross sales by 15%", "target": "15%", "actual": "8%", "unit": "", "verdict": "partially accomplished", "pct": 53, "note": "Sales grew from ₱30M to ₱32.4M."},
                    {"type": "non-quantifiable", "title": "Adopt Industry 4.0 technologies (ERP upgrade)", "actual_text": "ERP system upgraded with new modules for production monitoring.", "default_verdict": "accomplished"},
                    {"type": "non-quantifiable", "title": "Maintain compliance with food safety standards", "actual_text": "Compliance maintained. Latest audit passed with no major findings.", "default_verdict": "accomplished"},
                ],
                "overall": "partially accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "badge": "S2 2024 · July – December 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Implement beverage line automation (2nd cycle)", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Machine fully commissioned and at capacity."},
                    {"type": "quantifiable", "title": "Increase beverage production volume by 40%", "target": "40%", "actual": "40%", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Volume grew from 25,000 to 35,000 cups/semester."},
                    {"type": "quantifiable", "title": "Increase overall gross sales by 15%", "target": "15%", "actual": "15%", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Sales grew from ₱30M to ₱34.5M."},
                    {"type": "non-quantifiable", "title": "Adopt Industry 4.0 technologies (ERP fully operational)", "actual_text": "ERP fully operational. Weekly production monitoring reports generated.", "default_verdict": "accomplished"},
                    {"type": "non-quantifiable", "title": "Maintain compliance with food safety standards", "actual_text": "All audits passed with no major findings.", "default_verdict": "accomplished"},
                ],
                "overall": "accomplished",
            },
        },
    },
    "Queen's Bakeshop": {
        "semesters": {
            "S1 2024 (Jan – Jun 2024)": {
                "badge": "S1 2024 · January – June 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Acquire baking equipment (convection oven & dough mixer)", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Equipment acquired, installed, and staff trained."},
                    {"type": "quantifiable", "title": "Increase production volume by at least 30%", "target": "30%", "actual": "20%", "unit": "", "verdict": "partially accomplished", "pct": 67, "note": "On track to meet target by end of project."},
                    {"type": "quantifiable", "title": "Expand market to at least 1 additional outlet", "target": "1 outlet", "actual": "1 outlet", "unit": "", "verdict": "accomplished", "pct": 100, "note": "One sari-sari store consignment point in Sibalom."},
                    {"type": "quantifiable", "title": "Increase gross sales by at least 25%", "target": "25%", "actual": "10%", "unit": "", "verdict": "partially accomplished", "pct": 40, "note": "Sales grew from ₱250,000 to ₱275,000/month."},
                    {"type": "non-quantifiable", "title": "Improve product quality and consistency of baked goods", "actual_text": "Product quality improved. Bread texture and consistency are now more standardized.", "default_verdict": "accomplished"},
                ],
                "overall": "partially accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "badge": "S2 2024 · July – December 2024",
                "outputs": [
                    {"type": "quantifiable", "title": "Acquire baking equipment (convection oven & dough mixer)", "target": None, "actual": None, "unit": "", "verdict": "accomplished", "pct": 100, "note": "Equipment in good condition and used in daily production."},
                    {"type": "quantifiable", "title": "Increase production volume by at least 30%", "target": "30%", "actual": "30%", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Target achieved as of December 2024."},
                    {"type": "quantifiable", "title": "Expand market to at least 1 additional outlet", "target": "1 outlet", "actual": "2 outlets", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Outlets in San Jose, Antique and a local school canteen."},
                    {"type": "quantifiable", "title": "Increase gross sales by at least 25%", "target": "25%", "actual": "25%", "unit": "", "verdict": "accomplished", "pct": 100, "note": "Sales grew from ₱250,000 to ₱312,500/month."},
                    {"type": "non-quantifiable", "title": "Improve product quality and consistency of baked goods", "actual_text": "Quality and consistency maintained. Customer feedback is positive.", "default_verdict": "accomplished"},
                ],
                "overall": "accomplished",
            },
        },
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# UI
# ══════════════════════════════════════════════════════════════════════════════

# Header
st.markdown("""
<div class="page-header">
  <div>
    <div class="page-title">Impact assessment</div>
    <div class="page-sub">DOST SETUP 4.0 iFund Program — Region VI</div>
  </div>
</div>
""", unsafe_allow_html=True)

# Selectors
col_msme, col_sem = st.columns(2)
with col_msme:
    sel_msme = st.selectbox("MSME", list(REPORTS.keys()), label_visibility="collapsed")
with col_sem:
    sem_options = list(REPORTS[sel_msme]["semesters"].keys())
    sel_sem = st.selectbox("Semester", sem_options, label_visibility="collapsed")

sem = REPORTS[sel_msme]["semesters"][sel_sem]
all_outputs = sem["outputs"]

# Period badge
st.markdown(f'<div style="text-align:right;margin-top:-8px;margin-bottom:8px;"><span class="period-badge">{sem["badge"]}</span></div>', unsafe_allow_html=True)

# Split outputs
quant = [o for o in all_outputs if o["type"] == "quantifiable"]
nonquant = [o for o in all_outputs if o["type"] == "non-quantifiable"]

# ── Metric cards ──────────────────────────────────────────────────────────────
total = len(all_outputs)

# Count NQ using default verdicts for metric display
nq_default_counts = {"accomplished": 0, "partially accomplished": 0, "not accomplished": 0}
for o in nonquant:
    nq_default_counts[o["default_verdict"].lower()] += 1

acc  = sum(1 for o in quant if o["verdict"].lower() == "accomplished") + nq_default_counts["accomplished"]
part = sum(1 for o in quant if o["verdict"].lower() == "partially accomplished") + nq_default_counts["partially accomplished"]
nacc = sum(1 for o in quant if o["verdict"].lower() == "not accomplished") + nq_default_counts["not accomplished"]

def pct_label(n, t):
    return f"{round(n/t*100)}% of outputs" if t else "—"

st.markdown(f"""
<div class="metrics-row">
  <div class="metric-card">
    <div class="metric-label">Total outputs</div>
    <div class="metric-value c-default">{total}</div>
    <div class="metric-sub">this semester</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Accomplished</div>
    <div class="metric-value c-green">{acc}</div>
    <div class="metric-sub">{pct_label(acc, total)}</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Partially accomplished</div>
    <div class="metric-value c-orange">{part}</div>
    <div class="metric-sub">{pct_label(part, total)}</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Not accomplished</div>
    <div class="metric-value c-red">{nacc}</div>
    <div class="metric-sub">{pct_label(nacc, total)}</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Quantifiable Outputs ──────────────────────────────────────────────────────
if quant:
    st.markdown('<div class="section-label">Quantifiable Outputs</div>', unsafe_allow_html=True)
    pairs = [quant[i:i+2] for i in range(0, len(quant), 2)]
    for pair in pairs:
        cols = st.columns(2)
        for col, item in zip(cols, pair):
            with col:
                bc  = border_cls(item["verdict"])
                fc  = fill_cls(item["verdict"])
                pct = item["pct"]

                t_row = f'<div class="tr"><span>Target</span><span class="tr-val">{item["target"]}</span></div>' if item["target"] else ""
                a_row = f'<div class="tr"><span>Actual</span><span class="tr-val">{item["actual"]}</span></div>' if item["actual"] else ""
                note  = f'<div class="card-note">{item["note"]}</div>' if item["note"] else ""

                st.markdown(f"""
<div class="out-card {bc} card-gap">
  <div class="card-type">Quantifiable</div>
  <div class="card-title">{item['title']}</div>
  {t_row}
  {a_row}
  <div class="prog-track"><div class="prog-fill {fc}" style="width:{pct}%"></div></div>
  <div class="vrow">
    {badge(item['verdict'])}
    <span class="pct-text">{pct}% of target</span>
  </div>
  {note}
</div>
""", unsafe_allow_html=True)

# ── Non-Quantifiable Outputs ──────────────────────────────────────────────────
if nonquant:
    st.markdown('<div class="section-label">Non-Quantifiable Outputs</div>', unsafe_allow_html=True)
    nq_pairs = [nonquant[i:i+2] for i in range(0, len(nonquant), 2)]
    state_prefix = f"{sel_msme}|{sel_sem}"

    for pi, pair in enumerate(nq_pairs):
        cols = st.columns(2)
        for ci, (col, item) in enumerate(zip(cols, pair)):
            with col:
                key = f"nq|{state_prefix}|{pi}|{ci}"
                def_idx = verdict_idx(item["default_verdict"])

                # Card top
                st.markdown(f"""
<div class="out-card card-gap" style="padding-bottom:8px;">
  <div class="card-type">Non-Quantifiable</div>
  <div class="card-title">{item['title']}</div>
  <div class="nq-actual-lbl">Actual accomplishment</div>
  <div class="nq-actual-txt">{item['actual_text']}</div>
  <div class="verdict-psto-lbl">Verdict (PSTO):</div>
</div>
""", unsafe_allow_html=True)

                # Selectbox sits right below the card, visually grouped
                chosen = st.selectbox(
                    label=item["title"],
                    options=VERDICT_OPTIONS,
                    index=def_idx,
                    key=key,
                    label_visibility="collapsed"
                )

                # Badge below selectbox
                st.markdown(f'<div style="margin:4px 0 16px 0;">{badge(chosen)}</div>', unsafe_allow_html=True)

# ── Overall Verdict ───────────────────────────────────────────────────────────
st.markdown(f"""
<div class="overall-card">
  <div class="overall-lbl">
    <span class="overall-icon">📊</span>
    Overall semester verdict
  </div>
  {overall_badge(sem['overall'])}
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">DOST-VI SETUP 4.0 iFund Program · Region VI · ASENXO</div>', unsafe_allow_html=True)
