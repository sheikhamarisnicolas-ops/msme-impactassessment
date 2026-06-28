import streamlit as st

st.set_page_config(
    page_title="Impact Assessment – DOST SETUP 4.0 iFund",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
  .block-container { padding: 1.2rem 1rem 3rem 1rem; max-width: 780px; margin: auto; }

  .page-title { font-size: 18px; font-weight: 700; color: #1a1a1a; margin-bottom: 1px; }
  .page-sub   { font-size: 12px; color: #888; margin-bottom: 14px; }

  .period-badge {
    display: inline-block;
    background: #dbeafe; color: #1d4ed8;
    font-size: 11px; font-weight: 600;
    padding: 3px 10px; border-radius: 20px;
    float: right; margin-top: 2px;
  }

  /* Metric cards row */
  .metrics-row { display: flex; gap: 10px; margin: 18px 0 20px 0; }
  .metric-card {
    flex: 1; background: #f9fafb; border-radius: 10px;
    padding: 12px 14px; border: 1px solid #e5e7eb;
  }
  .metric-label { font-size: 11px; color: #9ca3af; font-weight: 500; margin-bottom: 4px; }
  .metric-value { font-size: 26px; font-weight: 700; line-height: 1.1; }
  .metric-sub   { font-size: 11px; color: #9ca3af; margin-top: 2px; }
  .mv-default { color: #1a1a1a; }
  .mv-green   { color: #16a34a; }
  .mv-orange  { color: #d97706; }
  .mv-red     { color: #dc2626; }

  /* Section label */
  .section-label {
    font-size: 11px; font-weight: 700; color: #6b7280;
    letter-spacing: 0.08em; text-transform: uppercase;
    margin: 20px 0 10px 0;
  }

  /* Output cards grid */
  .output-grid { display: flex; gap: 12px; margin-bottom: 12px; }
  .output-card {
    flex: 1; border-radius: 10px; padding: 14px 16px;
    border: 1.5px solid #e5e7eb; background: #fff;
    min-width: 0;
  }
  .output-card.red-border   { border-color: #fca5a5; }
  .output-card.green-border { border-color: #86efac; }
  .output-card.orange-border{ border-color: #fcd34d; }

  .card-type  { font-size: 10px; font-weight: 700; color: #9ca3af; letter-spacing: .06em; text-transform: uppercase; margin-bottom: 5px; }
  .card-title { font-size: 13px; font-weight: 700; color: #111; margin-bottom: 10px; line-height: 1.3; }

  .trow { display: flex; justify-content: space-between; font-size: 12px; color: #374151; margin-bottom: 2px; }
  .trow-val { font-weight: 600; }

  .progress-track { background: #e5e7eb; border-radius: 4px; height: 5px; margin: 8px 0; overflow: hidden; }
  .progress-fill-green  { background: #22c55e; height: 5px; border-radius: 4px; }
  .progress-fill-red    { background: #ef4444; height: 5px; border-radius: 4px; }
  .progress-fill-orange { background: #f59e0b; height: 5px; border-radius: 4px; }

  .verdict-row { display: flex; justify-content: space-between; align-items: center; margin: 8px 0 6px 0; }

  .badge-accomplished    { background: #dcfce7; color: #15803d; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; }
  .badge-partial         { background: #fef9c3; color: #a16207; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; }
  .badge-not-accomplished{ background: #fee2e2; color: #b91c1c; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; }

  .pct-label { font-size: 11px; color: #9ca3af; }

  .card-note { font-size: 11px; color: #6b7280; margin-top: 8px; line-height: 1.4; }

  /* Non-quant card extras */
  .nq-actual-label { font-size: 10px; font-weight: 600; color: #9ca3af; text-transform: uppercase; letter-spacing: .05em; margin: 8px 0 3px 0; }
  .nq-actual-text  { font-size: 12px; color: #374151; line-height: 1.4; margin-bottom: 10px; }
  .verdict-label-inline { font-size: 11px; color: #6b7280; font-weight: 500; }

  /* Overall verdict row */
  .overall-row {
    display: flex; justify-content: space-between; align-items: center;
    border: 1.5px solid #e5e7eb; border-radius: 10px;
    padding: 12px 16px; margin-top: 20px; background: #f9fafb;
  }
  .overall-label { font-size: 13px; font-weight: 600; color: #374151; }
  .overall-badge-green { color: #16a34a; font-size: 13px; font-weight: 600; }
  .overall-badge-orange { color: #d97706; font-size: 13px; font-weight: 600; }
  .overall-badge-red { color: #dc2626; font-size: 13px; font-weight: 600; }

  /* hide streamlit default header decoration */
  div[data-testid="stDecoration"] { display: none; }
  header { visibility: hidden; }
  .stSelectbox > label { display: none !important; }
  div[data-baseweb="select"] { border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)

# ── DATA ──────────────────────────────────────────────────────────────────────

REPORTS = {
    "Honore Cafe": {
        "address": "Capitol Subdivision, Estancia, Kalibo, Aklan",
        "semesters": {
            "S2 2021 (Jul – Dec 2021)": {
                "period_badge": "S2 2021 · July – December 2021",
                "quantifiable": [
                    {
                        "title": "Improve product quality (consistent appearance via 3-deck oven)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Stainless LPG Oven in good working condition as of December 2021.",
                    },
                    {
                        "title": "Reduce baking time by 50% (4 hrs → 2 hrs)",
                        "target_val": "50", "target_unit": "%",
                        "actual_val": "50", "actual_unit": "%",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "",
                    },
                    {
                        "title": "Improve baking capacity by 100% (792 → 1,584 pcs/day)",
                        "target_val": "1,584", "target_unit": "pcs/day",
                        "actual_val": "214", "actual_unit": "pcs/day",
                        "verdict": "not accomplished",
                        "pct": 14,
                        "note": "COVID-19 significantly affected operations during the first year.",
                    },
                    {
                        "title": "Increase production volume by 45% (247,200 → 358,320 pcs)",
                        "target_val": "358,320", "target_unit": "pcs",
                        "actual_val": "77,040", "actual_unit": "pcs",
                        "verdict": "not accomplished",
                        "pct": 0,
                        "note": "Production volume decreased by 69% due to COVID-19.",
                    },
                    {
                        "title": "Increase sales by 78% (₱3.06M → ₱5.46M)",
                        "target_val": "₱5,455,510", "target_unit": "",
                        "actual_val": "₱2,404,800", "actual_unit": "",
                        "verdict": "not accomplished",
                        "pct": 0,
                        "note": "Sales decreased by 21% due to COVID-19 pandemic.",
                    },
                    {
                        "title": "Establish at least 2 additional markets in Aklan",
                        "target_val": "2", "target_unit": "outlets",
                        "actual_val": "1", "actual_unit": "outlet",
                        "verdict": "partially accomplished",
                        "pct": 50,
                        "note": "Only one additional outlet established in Kalibo, Aklan.",
                    },
                    {
                        "title": "Generate at least 1 additional worker",
                        "target_val": "1", "target_unit": "worker",
                        "actual_val": "4", "actual_unit": "workers",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Enhance compliance with food safety standards",
                        "actual": "Enhanced compliance via procured stainless steel equipment and DOST VI Food Safety Consultancy.",
                        "default_verdict": "accomplished",
                    },
                    {
                        "title": "Improve production management using inventory/POS system software",
                        "actual": "No improvement in production management. POS not utilized due to lack of training for new employees.",
                        "default_verdict": "not accomplished",
                    },
                ],
                "overall": "partially accomplished",
            },
            "S1 2024 (Jan – Jun 2024)": {
                "period_badge": "S1 2024 · January – June 2024",
                "quantifiable": [
                    {
                        "title": "Improve product quality (consistent appearance via 3-deck oven)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Stainless LPG Oven in good working condition as of June 2024.",
                    },
                    {
                        "title": "Reduce baking time by 50% (4 hrs → 2 hrs)",
                        "target_val": "50", "target_unit": "%",
                        "actual_val": "50", "actual_unit": "%",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "",
                    },
                    {
                        "title": "Improve baking capacity by 100% (792 → 1,584 pcs/day)",
                        "target_val": "1,584", "target_unit": "pcs/day",
                        "actual_val": "214", "actual_unit": "pcs/day",
                        "verdict": "not accomplished",
                        "pct": 14,
                        "note": "COVID-19 affected operations during the first year.",
                    },
                    {
                        "title": "Increase production volume by 45%",
                        "target_val": "358,320", "target_unit": "pcs",
                        "actual_val": "77,040", "actual_unit": "pcs",
                        "verdict": "not accomplished",
                        "pct": 0,
                        "note": "First-year decline; current period shows recovery.",
                    },
                    {
                        "title": "Increase sales by 78% (₱3.06M → ₱5.46M)",
                        "target_val": "₱5,455,510", "target_unit": "",
                        "actual_val": "₱3,207,600", "actual_unit": "",
                        "verdict": "partially accomplished",
                        "pct": 59,
                        "note": "Sales volume significantly recovered in Jan–Jun 2024.",
                    },
                    {
                        "title": "Establish at least 2 additional markets in Aklan",
                        "target_val": "2", "target_unit": "outlets",
                        "actual_val": "5+", "actual_unit": "outlets",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Multiple new outlets established including Boracay.",
                    },
                    {
                        "title": "Generate at least 1 additional worker",
                        "target_val": "1", "target_unit": "worker",
                        "actual_val": "4", "actual_unit": "workers",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Enhance compliance with food safety standards",
                        "actual": "Compliance enhanced through stainless steel equipment and DOST VI consultancy.",
                        "default_verdict": "accomplished",
                    },
                    {
                        "title": "Improve production management using POS system",
                        "actual": "POS software is now operational and ready for use as of June 2024.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "period_badge": "S2 2024 · July – December 2024",
                "quantifiable": [
                    {
                        "title": "Improve product quality (consistent appearance via 3-deck oven)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Oven in good working condition as of December 2024.",
                    },
                    {
                        "title": "Reduce baking time by 50%",
                        "target_val": "50", "target_unit": "%",
                        "actual_val": "50", "actual_unit": "%",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "",
                    },
                    {
                        "title": "Improve baking capacity by 100% (792 → 1,584 pcs/day)",
                        "target_val": "1,584", "target_unit": "pcs/day",
                        "actual_val": "214", "actual_unit": "pcs/day",
                        "verdict": "not accomplished",
                        "pct": 14,
                        "note": "First-year COVID impact still reflected in capacity metric.",
                    },
                    {
                        "title": "Increase production volume by 45%",
                        "target_val": "45", "target_unit": "%",
                        "actual_val": "-69", "actual_unit": "% (first year)",
                        "verdict": "not accomplished",
                        "pct": 0,
                        "note": "Recovery underway; current production improving each semester.",
                    },
                    {
                        "title": "Increase sales by 78%",
                        "target_val": "₱5,455,510", "target_unit": "",
                        "actual_val": "₱3,384,500", "actual_unit": "",
                        "verdict": "partially accomplished",
                        "pct": 62,
                        "note": "Sales continue to grow; target not yet reached.",
                    },
                    {
                        "title": "Establish at least 2 additional markets in Aklan",
                        "target_val": "2", "target_unit": "outlets",
                        "actual_val": "5+", "actual_unit": "outlets",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "",
                    },
                    {
                        "title": "Generate at least 1 additional worker",
                        "target_val": "1", "target_unit": "worker",
                        "actual_val": "4", "actual_unit": "workers",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Enhance compliance with food safety standards",
                        "actual": "Compliance maintained through procured stainless equipment and DOST VI training.",
                        "default_verdict": "accomplished",
                    },
                    {
                        "title": "Improve production management using POS system",
                        "actual": "POS software in good working condition and utilized by the firm as of December 2024.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "accomplished",
            },
        },
    },
    "Han Jim Marketing Corporation": {
        "address": "Blk 10 Lot 1 Orchidsville Subd. Bonifacio St., Sta. Filomena, City of Iloilo",
        "semesters": {
            "S1 2024 (Jan – Jun 2024)": {
                "period_badge": "S1 2024 · January – June 2024",
                "quantifiable": [
                    {
                        "title": "Upgrade cold storage facility",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Cold storage facility upgraded and in good working condition.",
                    },
                    {
                        "title": "Increase production volume of Kimchi Cabbage by 30%",
                        "target_val": "30", "target_unit": "%",
                        "actual_val": "25", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 83,
                        "note": "Target partially met due to initial calibration period.",
                    },
                    {
                        "title": "Improve purified water system for washing raw vegetables",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Purified water system installed and fully operational.",
                    },
                    {
                        "title": "Expand market to at least 2 additional outlets",
                        "target_val": "2", "target_unit": "outlets",
                        "actual_val": "1", "actual_unit": "outlet",
                        "verdict": "partially accomplished",
                        "pct": 50,
                        "note": "One additional outlet established in Bacolod City.",
                    },
                    {
                        "title": "Increase gross sales by at least 20%",
                        "target_val": "20", "target_unit": "%",
                        "actual_val": "12", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 60,
                        "note": "Increase expected to accelerate in subsequent semester.",
                    },
                ],
                "non_quantifiable": [],
                "overall": "partially accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "period_badge": "S2 2024 · July – December 2024",
                "quantifiable": [
                    {
                        "title": "Upgrade cold storage facility",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Equipment remains in good working condition as of December 2024.",
                    },
                    {
                        "title": "Increase production volume of Kimchi Cabbage by 30%",
                        "target_val": "30", "target_unit": "%",
                        "actual_val": "25", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 83,
                        "note": "Sustained growth maintained in the second half of 2024.",
                    },
                    {
                        "title": "Improve purified water system for washing raw vegetables",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "System used in all washing and rinsing operations.",
                    },
                    {
                        "title": "Expand market to at least 2 additional outlets",
                        "target_val": "2", "target_unit": "outlets",
                        "actual_val": "2", "actual_unit": "outlets",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Outlets established in Bacolod City and Roxas City.",
                    },
                    {
                        "title": "Increase gross sales by at least 20%",
                        "target_val": "20", "target_unit": "%",
                        "actual_val": "21", "actual_unit": "%",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Sales grew from ₱4,050,000 (S2 2023) to ₱4,900,500 (S2 2024).",
                    },
                ],
                "non_quantifiable": [],
                "overall": "accomplished",
            },
        },
    },
    "SJL Corporation": {
        "address": "Lopez Jaena St., Molo Boulevard, City of Iloilo",
        "semesters": {
            "S1 2024 (Jan – Jun 2024)": {
                "period_badge": "S1 2024 · January – June 2024",
                "quantifiable": [
                    {
                        "title": "Acquire large format digital printing equipment",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Equipment acquired and fully operational as of June 2024.",
                    },
                    {
                        "title": "Acquire commercial embroidery machine (12 heads)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Machine installed; staff trained by supplier.",
                    },
                    {
                        "title": "Increase production volume by at least 30%",
                        "target_val": "30", "target_unit": "%",
                        "actual_val": "20", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 67,
                        "note": "On track to meet target by end of 2024.",
                    },
                    {
                        "title": "Expand market to at least 1 additional BPO or corporate client",
                        "target_val": "1", "target_unit": "client",
                        "actual_val": "2", "actual_unit": "clients",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Two new BPO clients acquired in Iloilo City.",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Improve product quality and standardize production processes",
                        "actual": "Product quality improved through use of new equipment and standardized procedures.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "period_badge": "S2 2024 · July – December 2024",
                "quantifiable": [
                    {
                        "title": "Acquire large format digital printing equipment",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Fully operational for all large-format printing orders.",
                    },
                    {
                        "title": "Acquire commercial embroidery machine (12 heads)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Producing embroidered uniforms, caps, and jackets at full capacity.",
                    },
                    {
                        "title": "Increase production volume by at least 30%",
                        "target_val": "30", "target_unit": "%",
                        "actual_val": "32", "actual_unit": "%",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Target achieved as of December 2024.",
                    },
                    {
                        "title": "Expand market to at least 1 additional BPO or corporate client",
                        "target_val": "1", "target_unit": "client",
                        "actual_val": "4", "actual_unit": "clients",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Four new BPO and corporate clients acquired in Iloilo City and nearby municipalities.",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Improve product quality and standardize production processes",
                        "actual": "Standardized QC procedures in place and consistently applied across all product lines.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "accomplished",
            },
        },
    },
    "Filbake Food Corporation": {
        "address": "RA Bldg. XIX Martyrs St., Poblacion, Kalibo, Aklan",
        "semesters": {
            "S1 2023 (Jan – Jun 2023)": {
                "period_badge": "S1 2023 · January – June 2023",
                "quantifiable": [
                    {
                        "title": "Implement beverage line automation (filling & sealing machine)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "partially accomplished",
                        "pct": 50,
                        "note": "Machine delivered and installation commenced. Commissioning in progress.",
                    },
                    {
                        "title": "Increase beverage production volume by at least 40%",
                        "target_val": "40", "target_unit": "%",
                        "actual_val": "5", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 13,
                        "note": "Significant increase expected after full equipment commissioning.",
                    },
                    {
                        "title": "Increase overall gross sales by at least 15%",
                        "target_val": "15", "target_unit": "%",
                        "actual_val": "3", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 20,
                        "note": "Sales grew from ₱29M to ₱29.87M. Growth to accelerate after full automation.",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Adopt Industry 4.0 technologies (ERP/desktop systems)",
                        "actual": "Desktop computers and ERP modules procured; installation ongoing.",
                        "default_verdict": "partially accomplished",
                    },
                    {
                        "title": "Maintain compliance with food safety standards",
                        "actual": "Compliance maintained. Latest internal audit passed with no major findings.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "partially accomplished",
            },
            "S2 2023 (Jul – Dec 2023)": {
                "period_badge": "S2 2023 · July – December 2023",
                "quantifiable": [
                    {
                        "title": "Implement beverage line automation",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Machine now fully commissioned and operational.",
                    },
                    {
                        "title": "Increase beverage production volume by at least 40%",
                        "target_val": "40", "target_unit": "%",
                        "actual_val": "20", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 50,
                        "note": "Volume grew from 25,000 to 30,000 cups/semester.",
                    },
                    {
                        "title": "Increase overall gross sales by at least 15%",
                        "target_val": "15", "target_unit": "%",
                        "actual_val": "8", "actual_unit": "% (cumulative 11%)",
                        "verdict": "partially accomplished",
                        "pct": 73,
                        "note": "On track to reach 15% target.",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Adopt Industry 4.0 technologies (ERP/desktop systems)",
                        "actual": "ERP system with new production monitoring modules fully deployed and in use.",
                        "default_verdict": "accomplished",
                    },
                    {
                        "title": "Maintain compliance with food safety standards",
                        "actual": "Compliance maintained. Latest audit passed with no major findings.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "partially accomplished",
            },
            "S1 2024 (Jan – Jun 2024)": {
                "period_badge": "S1 2024 · January – June 2024",
                "quantifiable": [
                    {
                        "title": "Implement beverage line automation (2nd cycle)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "partially accomplished",
                        "pct": 50,
                        "note": "Partially installed. Full commissioning expected by Q3 2024.",
                    },
                    {
                        "title": "Increase beverage production volume by at least 40%",
                        "target_val": "40", "target_unit": "%",
                        "actual_val": "18", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 45,
                        "note": "Increase expected to accelerate after full automation.",
                    },
                    {
                        "title": "Increase overall gross sales by at least 15%",
                        "target_val": "15", "target_unit": "%",
                        "actual_val": "8", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 53,
                        "note": "Sales grew from ₱30M to ₱32.4M.",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Adopt Industry 4.0 technologies (ERP upgrade)",
                        "actual": "ERP system upgraded with new modules for production monitoring.",
                        "default_verdict": "accomplished",
                    },
                    {
                        "title": "Maintain compliance with food safety standards",
                        "actual": "Compliance maintained. Latest audit passed with no major findings.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "partially accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "period_badge": "S2 2024 · July – December 2024",
                "quantifiable": [
                    {
                        "title": "Implement beverage line automation (2nd cycle)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Machine fully commissioned and operating at capacity.",
                    },
                    {
                        "title": "Increase beverage production volume by at least 40%",
                        "target_val": "40", "target_unit": "%",
                        "actual_val": "40", "actual_unit": "%",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Volume grew from 25,000 (baseline) to 35,000 cups/semester.",
                    },
                    {
                        "title": "Increase overall gross sales by at least 15%",
                        "target_val": "15", "target_unit": "%",
                        "actual_val": "15", "actual_unit": "%",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Sales grew from ₱30M to ₱34.5M.",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Adopt Industry 4.0 technologies (ERP fully operational)",
                        "actual": "ERP system with new modules fully operational. Production monitoring reports generated weekly.",
                        "default_verdict": "accomplished",
                    },
                    {
                        "title": "Maintain compliance with food safety standards",
                        "actual": "All audits passed with no major findings.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "accomplished",
            },
        },
    },
    "Queen's Bakeshop": {
        "address": "Villavert St., District III, Sibalom, Antique",
        "semesters": {
            "S1 2024 (Jan – Jun 2024)": {
                "period_badge": "S1 2024 · January – June 2024",
                "quantifiable": [
                    {
                        "title": "Acquire baking equipment (convection oven & dough mixer)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Equipment acquired, installed, and staff trained.",
                    },
                    {
                        "title": "Increase production volume by at least 30%",
                        "target_val": "30", "target_unit": "%",
                        "actual_val": "20", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 67,
                        "note": "On track to meet target by end of project.",
                    },
                    {
                        "title": "Expand market to at least 1 additional outlet in Sibalom or San Jose",
                        "target_val": "1", "target_unit": "outlet",
                        "actual_val": "1", "actual_unit": "outlet",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "One additional sari-sari store consignment point established in Sibalom.",
                    },
                    {
                        "title": "Increase gross sales by at least 25%",
                        "target_val": "25", "target_unit": "%",
                        "actual_val": "10", "actual_unit": "%",
                        "verdict": "partially accomplished",
                        "pct": 40,
                        "note": "Sales grew from ₱250,000 to ₱275,000/month.",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Improve product quality and consistency of baked goods",
                        "actual": "Product quality improved. Bread texture and consistency are now more standardized.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "partially accomplished",
            },
            "S2 2024 (Jul – Dec 2024)": {
                "period_badge": "S2 2024 · July – December 2024",
                "quantifiable": [
                    {
                        "title": "Acquire baking equipment (convection oven & dough mixer)",
                        "target_val": None, "target_unit": None,
                        "actual_val": None, "actual_unit": None,
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Equipment in good working condition and used in daily production.",
                    },
                    {
                        "title": "Increase production volume by at least 30%",
                        "target_val": "30", "target_unit": "%",
                        "actual_val": "30", "actual_unit": "%",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Target achieved as of December 2024.",
                    },
                    {
                        "title": "Expand market to at least 1 additional outlet",
                        "target_val": "1", "target_unit": "outlet",
                        "actual_val": "2", "actual_unit": "outlets",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Outlets in San Jose, Antique and a local school canteen.",
                    },
                    {
                        "title": "Increase gross sales by at least 25%",
                        "target_val": "25", "target_unit": "%",
                        "actual_val": "25", "actual_unit": "%",
                        "verdict": "accomplished",
                        "pct": 100,
                        "note": "Sales grew from ₱250,000 to ₱312,500/month.",
                    },
                ],
                "non_quantifiable": [
                    {
                        "title": "Improve product quality and consistency of baked goods",
                        "actual": "Product quality and consistency maintained. Customer feedback is positive.",
                        "default_verdict": "accomplished",
                    },
                ],
                "overall": "accomplished",
            },
        },
    },
}

VERDICT_OPTIONS = ["Accomplished", "Partially accomplished", "Not accomplished"]

def verdict_badge(v):
    v_lower = v.lower()
    if v_lower == "accomplished":
        return "accomplished", "✓ Accomplished", "#badge-accomplished"
    elif v_lower == "partially accomplished":
        return "partial", "— Partially accomplished", "#badge-partial"
    else:
        return "not", "✕ Not accomplished", "#badge-not-accomplished"

def badge_html(v):
    _, label, _ = verdict_badge(v)
    v_lower = v.lower()
    if v_lower == "accomplished":
        cls = "badge-accomplished"
    elif v_lower == "partially accomplished":
        cls = "badge-partial"
    else:
        cls = "badge-not-accomplished"
    return f'<span class="{cls}">{label}</span>'

def progress_color(v):
    v_lower = v.lower()
    if v_lower == "accomplished":
        return "progress-fill-green"
    elif v_lower == "partially accomplished":
        return "progress-fill-orange"
    return "progress-fill-red"

def card_border(v):
    v_lower = v.lower()
    if v_lower == "accomplished":
        return "green-border"
    elif v_lower == "partially accomplished":
        return "orange-border"
    return "red-border"

def default_verdict_index(dv):
    dv_lower = dv.lower()
    if dv_lower == "accomplished":
        return 0
    elif dv_lower == "partially accomplished":
        return 1
    return 2

# ── UI ────────────────────────────────────────────────────────────────────────

st.markdown('<div class="page-title">Impact assessment</div>', unsafe_allow_html=True)
st.markdown('<div class="page-sub">DOST SETUP 4.0 iFund Program — Region VI</div>', unsafe_allow_html=True)

msme_names = list(REPORTS.keys())
sel_msme = st.selectbox("MSME", msme_names, label_visibility="collapsed")

msme_data = REPORTS[sel_msme]
sem_names = list(msme_data["semesters"].keys())
sel_sem = st.selectbox("Semester", sem_names, label_visibility="collapsed")

sem_data = msme_data["semesters"][sel_sem]
period_badge = sem_data["period_badge"]
quant_outputs = sem_data["quantifiable"]
nonquant_outputs = sem_data["non_quantifiable"]

st.markdown(f'<div class="period-badge">{period_badge}</div>', unsafe_allow_html=True)
st.markdown("<div style='clear:both; height:4px;'></div>", unsafe_allow_html=True)

# ── Metrics ─────────────────────────────────────────────────────────────────
total_outputs = len(quant_outputs) + len(nonquant_outputs)
accomplished = sum(1 for o in quant_outputs if o["verdict"].lower() == "accomplished")
partial = sum(1 for o in quant_outputs if o["verdict"].lower() == "partially accomplished")
not_acc = sum(1 for o in quant_outputs if o["verdict"].lower() == "not accomplished")
# non-quant defaults
accomplished += sum(1 for o in nonquant_outputs if o["default_verdict"].lower() == "accomplished")
partial += sum(1 for o in nonquant_outputs if o["default_verdict"].lower() == "partially accomplished")
not_acc += sum(1 for o in nonquant_outputs if o["default_verdict"].lower() == "not accomplished")

pct_acc  = f"{round(accomplished/total_outputs*100)}% of outputs" if total_outputs else "—"
pct_part = f"{round(partial/total_outputs*100)}% of outputs" if total_outputs else "—"
pct_not  = f"{round(not_acc/total_outputs*100)}% of outputs" if total_outputs else "—"

st.markdown(f"""
<div class="metrics-row">
  <div class="metric-card">
    <div class="metric-label">Total outputs</div>
    <div class="metric-value mv-default">{total_outputs}</div>
    <div class="metric-sub">this semester</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Accomplished</div>
    <div class="metric-value mv-green">{accomplished}</div>
    <div class="metric-sub">{pct_acc}</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Partially accomplished</div>
    <div class="metric-value mv-orange">{partial}</div>
    <div class="metric-sub">{pct_part}</div>
  </div>
  <div class="metric-card">
    <div class="metric-label">Not accomplished</div>
    <div class="metric-value mv-red">{not_acc}</div>
    <div class="metric-sub">{pct_not}</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Quantifiable Outputs ─────────────────────────────────────────────────────
if quant_outputs:
    st.markdown('<div class="section-label">Quantifiable Outputs</div>', unsafe_allow_html=True)

    pairs = [quant_outputs[i:i+2] for i in range(0, len(quant_outputs), 2)]
    for pair in pairs:
        cols = st.columns(2)
        for col, item in zip(cols, pair):
            with col:
                border_cls = card_border(item["verdict"])
                prog_cls   = progress_color(item["verdict"])
                pct        = item["pct"]
                has_values = item["target_val"] is not None

                target_row = ""
                actual_row = ""
                if has_values:
                    target_row = f'<div class="trow"><span>Target</span><span class="trow-val">{item["target_val"]} {item["target_unit"]}</span></div>'
                    actual_row = f'<div class="trow"><span>Actual</span><span class="trow-val">{item["actual_val"]} {item["actual_unit"]}</span></div>'

                note_html = f'<div class="card-note">{item["note"]}</div>' if item["note"] else ""
                pct_lbl = f'{pct}% of target'

                st.markdown(f"""
<div class="output-card {border_cls}">
  <div class="card-type">Quantifiable</div>
  <div class="card-title">{item['title']}</div>
  {target_row}
  {actual_row}
  <div class="progress-track"><div class="{prog_cls}" style="width:{pct}%;"></div></div>
  <div class="verdict-row">
    {badge_html(item['verdict'])}
    <span class="pct-label">{pct_lbl}</span>
  </div>
  {note_html}
</div>
""", unsafe_allow_html=True)

        # fill empty slot if odd
        if len(pair) == 1:
            pass

# ── Non-Quantifiable Outputs ─────────────────────────────────────────────────
if nonquant_outputs:
    st.markdown('<div class="section-label">Non-Quantifiable Outputs</div>', unsafe_allow_html=True)

    nq_pairs = [nonquant_outputs[i:i+2] for i in range(0, len(nonquant_outputs), 2)]

    # Store verdicts in session state
    if "nq_verdicts" not in st.session_state:
        st.session_state["nq_verdicts"] = {}

    state_key_prefix = f"{sel_msme}_{sel_sem}"

    for pair_idx, pair in enumerate(nq_pairs):
        cols = st.columns(2)
        for col_idx, (col, item) in enumerate(zip(cols, pair)):
            with col:
                state_key = f"{state_key_prefix}_nq_{pair_idx}_{col_idx}"
                default_idx = default_verdict_index(item["default_verdict"])

                border_cls = card_border(VERDICT_OPTIONS[default_idx])

                st.markdown(f"""
<div class="output-card {border_cls}">
  <div class="card-type">Non-Quantifiable</div>
  <div class="card-title">{item['title']}</div>
  <div class="nq-actual-label">Actual accomplishment</div>
  <div class="nq-actual-text">{item['actual']}</div>
  <div class="verdict-label-inline" style="margin-bottom:4px;">Verdict (PSTO):</div>
</div>
""", unsafe_allow_html=True)

                chosen = st.selectbox(
                    f"Verdict for: {item['title'][:30]}",
                    VERDICT_OPTIONS,
                    index=default_idx,
                    key=state_key,
                    label_visibility="collapsed"
                )

                st.markdown(f'<div style="margin: 4px 0 12px 0;">{badge_html(chosen)}</div>', unsafe_allow_html=True)

# ── Overall semester verdict ─────────────────────────────────────────────────
overall = sem_data["overall"]
if overall.lower() == "accomplished":
    overall_html = '<span class="overall-badge-green">✓ Accomplished</span>'
elif overall.lower() == "partially accomplished":
    overall_html = '<span class="overall-badge-orange">— Partially accomplished</span>'
else:
    overall_html = '<span class="overall-badge-red">✕ Not accomplished</span>'

st.markdown(f"""
<div class="overall-row">
  <div style="display:flex;align-items:center;gap:8px;">
    <span style="font-size:16px;">📊</span>
    <span class="overall-label">Overall semester verdict</span>
  </div>
  {overall_html}
</div>
""", unsafe_allow_html=True)

st.markdown("<br><p style='font-size:11px;color:#ccc;text-align:center;'>DOST-VI SETUP 4.0 iFund Program · Region VI</p>", unsafe_allow_html=True)
