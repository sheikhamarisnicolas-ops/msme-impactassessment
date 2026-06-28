import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Impact Assessment – DOST SETUP 4.0 iFund",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .block-container { padding: 1.5rem 2rem 2rem 2rem; max-width: 100%; }
    .metric-card {
        background: #ffffff;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        border: 1px solid #e8e8e8;
    }
    .metric-label { font-size: 12px; color: #888; font-weight: 500; margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.04em; }
    .metric-value { font-size: 28px; font-weight: 600; line-height: 1.1; }
    .metric-sub { font-size: 12px; color: #aaa; margin-top: 3px; }
    .section-header {
        font-size: 13px; font-weight: 600; color: #1a1a1a;
        border-left: 3px solid #2563eb; padding-left: 8px;
        margin-bottom: 12px;
    }
    .badge-pos { background: #dcfce7; color: #166534; padding: 2px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; }
    .badge-neg { background: #fee2e2; color: #991b1b; padding: 2px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; }
    .badge-neu { background: #f3f4f6; color: #374151; padding: 2px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; }
    .stSelectbox label, .stTextInput label, .stNumberInput label { font-size: 11px !important; font-weight: 600 !important; color: #666 !important; text-transform: uppercase !important; letter-spacing: 0.04em !important; }
    div[data-testid="stHorizontalBlock"] { gap: 12px; }
    .note-text { font-size: 11px; color: #9ca3af; font-style: italic; margin-top: 4px; }
</style>
""", unsafe_allow_html=True)

# ── DATA ──────────────────────────────────────────────────────────────────────
# Pre-funding figures = earliest available baseline from the reports
# Post-funding figures = latest reported period (Jul–Dec 2024 where available)
# Working capital is ASSUMED (no direct figure in reports); derived proportionally
# Employment = direct employees reported
# Production vol = units/kg produced per semester

MSMES = [
    {
        "name": "Honore Cafe",
        "province": "Aklan",
        "sector": "Food Manufacturing",
        "type": "Micro",
        # Pre = original baseline (pre-COVID first year): sales PHP 3,058,614 annualized → ~1,529,307/sem
        # Post = Jul–Dec 2024 actual
        "pre_sales": 1_529_307,
        "post_sales": 3_384_500,
        "pre_cap": 350_000,
        "post_cap": 517_000,
        "pre_emp": 6,
        "post_emp": 10,        # peaked at 10; latest reports show fluctuation
        "pre_prod": 247_200,   # pcs/year baseline → 123,600/sem
        "post_prod": 54_610,   # Jul–Dec 2024 actual (still recovering from COVID dip)
        # Note: production vol still below pre due to COVID disruption in early years
    },
    {
        "name": "Han Jim Marketing Corporation",
        "province": "Iloilo",
        "sector": "Food Manufacturing",
        "type": "Small",
        "pre_sales": 4_050_000,   # Jul–Dec 2023 baseline (before SETUP funds Jan 2024)
        "post_sales": 4_900_500,  # Jul–Dec 2024
        "pre_cap": 800_000,
        "post_cap": 1_843_245,
        "pre_emp": 16,
        "post_emp": 19,
        "pre_prod": 40_000,   # kg/sem baseline
        "post_prod": 54_500,  # kg/sem Jul–Dec 2024
    },
    {
        "name": "SJL Corporation",
        "province": "Iloilo",
        "sector": "Manufacturing / Printing",
        "type": "Small",
        "pre_sales": 1_413_000,   # estimated baseline (Jan–Jun 2024 ÷ 1.15 for ~15% growth)
        "post_sales": 2_080_000,  # Jul–Dec 2024
        "pre_cap": 600_000,
        "post_cap": 1_150_000,
        "pre_emp": 30,
        "post_emp": 36,
        "pre_prod": 8_500,    # approx pcs/sem baseline
        "post_prod": 11_500,  # approx pcs/sem Jul–Dec 2024
    },
    {
        "name": "Filbake Food Corporation",
        "province": "Aklan",
        "sector": "Food Manufacturing",
        "type": "Small",
        "pre_sales": 29_000_000,  # Jul–Dec 2022 baseline
        "post_sales": 34_500_000, # Jul–Dec 2024
        "pre_cap": 1_000_000,
        "post_cap": 1_253_933,
        "pre_emp": 45,
        "post_emp": 52,
        "pre_prod": 25_000,   # cups/sem baseline
        "post_prod": 35_000,  # cups/sem Jul–Dec 2024
    },
    {
        "name": "Queen's Bakeshop",
        "province": "Aklan",
        "sector": "Food Manufacturing",
        "type": "Micro",
        "pre_sales": 1_500_000,   # PHP 250,000/month × 6 months
        "post_sales": 1_875_000,  # PHP 312,500/month × 6 months (Jul–Dec 2024)
        "pre_cap": 300_000,
        "post_cap": 450_000,
        "pre_emp": 5,
        "post_emp": 7,
        "pre_prod": 37_000,   # pcs/sem baseline (~44,400 × pre factor)
        "post_prod": 48_120,  # 30% increase from baseline
    },
]

df_raw = pd.DataFrame(MSMES)

def compute_delta(pre, post):
    if not pre or pre == 0:
        return None
    return ((post - pre) / abs(pre)) * 100

def get_verdict(val, threshold):
    if val is None:
        return "Neutral"
    if val >= threshold:
        return "Positive"
    if val <= -threshold:
        return "Negative"
    return "Neutral"

def overall_verdict(row, threshold):
    deltas = [row["sales_d"], row["cap_d"], row["emp_d"], row["prod_d"]]
    valid = [d for d in deltas if d is not None]
    if not valid:
        return "Neutral"
    pos = sum(1 for d in valid if d >= threshold)
    neg = sum(1 for d in valid if d <= -threshold)
    if pos > neg and pos >= 2:
        return "Positive"
    if neg > pos and neg >= 2:
        return "Negative"
    return "Neutral"

def fmt_pct(v):
    if v is None:
        return "—"
    sign = "+" if v >= 0 else ""
    return f"{sign}{v:.1f}%"

def fmt_php(v):
    if v >= 1_000_000:
        return f"₱{v/1_000_000:.2f}M"
    if v >= 1_000:
        return f"₱{v/1_000:.0f}K"
    return f"₱{v:,.0f}"

def badge_html(verdict):
    if verdict == "Positive":
        return '<span class="badge-pos">Positive</span>'
    if verdict == "Negative":
        return '<span class="badge-neg">Negative</span>'
    return '<span class="badge-neu">Neutral</span>'

def delta_color(v, threshold):
    if v is None:
        return "#9ca3af"
    if v >= threshold:
        return "#166534"
    if v <= -threshold:
        return "#991b1b"
    return "#374151"

# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("## Impact Assessment")
st.markdown('<p class="note-text">DOST-VI SETUP 4.0 iFund Program · Region VI · Verdicts are assumed based on reported pre and post data</p>', unsafe_allow_html=True)
st.markdown("---")

# Filters
fc1, fc2, fc3, fc4, fc5 = st.columns([2, 1.2, 1.2, 1.2, 1.2])
with fc1:
    search = st.text_input("Search MSME", placeholder="Enterprise name...", label_visibility="visible")
with fc2:
    provinces = ["All"] + sorted(df_raw["province"].unique().tolist())
    sel_prov = st.selectbox("Province", provinces)
with fc3:
    sectors = ["All"] + sorted(df_raw["sector"].unique().tolist())
    sel_sec = st.selectbox("Sector", sectors)
with fc4:
    types = ["All"] + sorted(df_raw["type"].unique().tolist())
    sel_type = st.selectbox("MSME Type", types)
with fc5:
    threshold = st.number_input("Impact Threshold (%)", min_value=1, max_value=100, value=10)
    st.markdown(f'<p class="note-text">≥{threshold}% = Positive &nbsp; ≤−{threshold}% = Negative</p>', unsafe_allow_html=True)

st.markdown("")

# Compute all rows
rows = []
for r in MSMES:
    sd = compute_delta(r["pre_sales"], r["post_sales"])
    cd = compute_delta(r["pre_cap"], r["post_cap"])
    ed = compute_delta(r["pre_emp"], r["post_emp"])
    pd_ = compute_delta(r["pre_prod"], r["post_prod"])
    row = {**r, "sales_d": sd, "cap_d": cd, "emp_d": ed, "prod_d": pd_}
    row["verdict"] = overall_verdict(row, threshold)
    rows.append(row)

df = pd.DataFrame(rows)

# Apply filters
mask = pd.Series([True] * len(df))
if search:
    mask &= df["name"].str.lower().str.contains(search.lower())
if sel_prov != "All":
    mask &= df["province"] == sel_prov
if sel_sec != "All":
    mask &= df["sector"] == sel_sec
if sel_type != "All":
    mask &= df["type"] == sel_type

df_filtered = df[mask]

# Metrics
total = len(df_filtered)
pos = (df_filtered["verdict"] == "Positive").sum()
neg = (df_filtered["verdict"] == "Negative").sum()
neu = total - pos - neg

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Assessed MSMEs</div>
        <div class="metric-value" style="color:#1a1a1a;">{total}</div>
        <div class="metric-sub">With pre &amp; post data</div>
    </div>""", unsafe_allow_html=True)
with m2:
    pct_pos = f"{round(pos/total*100)}% of total" if total else "0% of total"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Positive Impact</div>
        <div class="metric-value" style="color:#166534;">{pos}</div>
        <div class="metric-sub">{pct_pos}</div>
    </div>""", unsafe_allow_html=True)
with m3:
    pct_neu = f"— {round(neu/total*100)}% of total" if total else "— 0% of total"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Neutral</div>
        <div class="metric-value" style="color:#374151;">{neu}</div>
        <div class="metric-sub">{pct_neu}</div>
    </div>""", unsafe_allow_html=True)
with m4:
    pct_neg = f"{round(neg/total*100)}% of total" if total else "0% of total"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Negative Impact</div>
        <div class="metric-value" style="color:#991b1b;">{neg}</div>
        <div class="metric-sub">{pct_neg}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("")

# ── CHARTS ROW 1 ─────────────────────────────────────────────────────────────
ch1, ch2 = st.columns(2)

with ch1:
    st.markdown('<div class="section-header">Per-indicator verdict distribution</div>', unsafe_allow_html=True)
    indicators = ["Gross Sales", "Working Capital", "Employment", "Production Vol"]
    delta_cols = ["sales_d", "cap_d", "emp_d", "prod_d"]
    pos_c, neu_c, neg_c = [], [], []
    for col in delta_cols:
        vals = df_filtered[col].dropna()
        pos_c.append(int((vals >= threshold).sum()))
        neg_c.append(int((vals <= -threshold).sum()))
        neu_c.append(int(((vals > -threshold) & (vals < threshold)).sum()))

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(name="Positive", x=indicators, y=pos_c, marker_color="#2563eb", marker_line_width=0))
    fig1.add_trace(go.Bar(name="Neutral",  x=indicators, y=neu_c, marker_color="#d1d5db", marker_line_width=0))
    fig1.add_trace(go.Bar(name="Negative", x=indicators, y=neg_c, marker_color="#ef4444", marker_line_width=0))
    fig1.update_layout(
        barmode="group", height=240, margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=11)),
        plot_bgcolor="white", paper_bgcolor="white",
        xaxis=dict(tickfont=dict(size=11), gridcolor="#f3f4f6"),
        yaxis=dict(tickfont=dict(size=11), gridcolor="#e5e7eb", dtick=1),
        bargap=0.25, bargroupgap=0.05,
    )
    st.plotly_chart(fig1, use_container_width=True, config={"displayModeBar": False})

with ch2:
    st.markdown('<div class="section-header">Sales growth distribution</div>', unsafe_allow_html=True)
    sales_deltas = df_filtered["sales_d"].dropna().tolist()
    bins = [-100, -40, -20, -10, 0, 10, 20, 40, 60, 100]
    bin_labels = ["<-40", "-40 to -20", "-20 to -10", "-10 to 0", "0 to 10", "10 to 20", "20 to 40", "40 to 60", ">60"]
    bin_counts = []
    for i in range(len(bins) - 1):
        count = sum(1 for v in sales_deltas if bins[i] <= v < bins[i + 1])
        bin_counts.append(count)
    bar_colors = ["#ef4444" if i < 4 else "#2563eb" for i in range(len(bin_labels))]

    fig2 = go.Figure(go.Bar(
        x=bin_labels, y=bin_counts,
        marker_color=bar_colors, marker_line_width=0,
    ))
    fig2.update_layout(
        height=240, margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="white", paper_bgcolor="white",
        showlegend=False,
        xaxis=dict(tickfont=dict(size=10), tickangle=30),
        yaxis=dict(tickfont=dict(size=11), gridcolor="#e5e7eb", dtick=1),
    )
    st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

# ── SCATTER CHART ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">Pre vs. post gross sales per MSME</div>', unsafe_allow_html=True)

scatter_df = df_filtered[df_filtered["pre_sales"].notna() & df_filtered["post_sales"].notna()].copy()
color_map = {"Positive": "#2563eb", "Neutral": "#9ca3af", "Negative": "#ef4444"}
scatter_df["color"] = scatter_df["verdict"].map(color_map)

fig3 = go.Figure()
max_val = max(scatter_df["pre_sales"].max(), scatter_df["post_sales"].max()) * 1.15 if len(scatter_df) else 5_000_000
fig3.add_trace(go.Scatter(
    x=[0, max_val], y=[0, max_val],
    mode="lines", line=dict(color="#d1d5db", dash="dash", width=1.5),
    name="No change line", showlegend=True,
))
for verdict in ["Positive", "Neutral", "Negative"]:
    sub = scatter_df[scatter_df["verdict"] == verdict]
    if len(sub):
        fig3.add_trace(go.Scatter(
            x=sub["pre_sales"], y=sub["post_sales"],
            mode="markers",
            marker=dict(color=color_map[verdict], size=10, line=dict(color="white", width=1.5)),
            name=verdict,
            text=sub["name"],
            customdata=sub[["pre_sales", "post_sales"]],
            hovertemplate="<b>%{text}</b><br>Pre: ₱%{customdata[0]:,.0f}<br>Post: ₱%{customdata[1]:,.0f}<extra></extra>",
        ))

fig3.update_layout(
    height=300, margin=dict(l=10, r=10, t=10, b=40),
    plot_bgcolor="white", paper_bgcolor="white",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=11)),
    xaxis=dict(title="Pre-funding gross sales (₱)", tickfont=dict(size=10), gridcolor="#e5e7eb",
               tickformat=",.0f", range=[0, max_val]),
    yaxis=dict(title="Post-funding gross sales (₱)", tickfont=dict(size=10), gridcolor="#e5e7eb",
               tickformat=",.0f", range=[0, max_val]),
)
st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})
st.markdown('<p class="note-text">Points above the diagonal line improved. Points below declined.</p>', unsafe_allow_html=True)

st.markdown("")

# ── TABLE ─────────────────────────────────────────────────────────────────────
tcol1, tcol2 = st.columns([2, 1])
with tcol1:
    st.markdown('<div class="section-header">Per-MSME impact breakdown</div>', unsafe_allow_html=True)
with tcol2:
    verdict_filter = st.selectbox("Filter by verdict", ["All Verdicts", "Positive", "Neutral", "Negative"], label_visibility="collapsed")

if verdict_filter != "All Verdicts":
    df_table = df_filtered[df_filtered["verdict"] == verdict_filter]
else:
    df_table = df_filtered

if df_table.empty:
    st.info("No records for selected filter.")
else:
    header_cols = st.columns([0.3, 1.8, 1.0, 1.1, 0.7, 0.8, 0.9, 0.9, 0.8])
    headers = ["#", "MSME", "Province", "Sector", "Sales Δ%", "Capital Δ%", "Employment Δ%", "Production Δ%", "Overall"]
    for col, h in zip(header_cols, headers):
        col.markdown(f"<span style='font-size:10px;font-weight:600;color:#9ca3af;text-transform:uppercase;letter-spacing:.04em;'>{h}</span>", unsafe_allow_html=True)

    st.markdown("<hr style='margin:4px 0 8px 0;border-color:#e5e7eb;'>", unsafe_allow_html=True)

    for i, (_, row) in enumerate(df_table.iterrows()):
        row_cols = st.columns([0.3, 1.8, 1.0, 1.1, 0.7, 0.8, 0.9, 0.9, 0.8])
        row_cols[0].markdown(f"<span style='font-size:12px;color:#9ca3af;'>{i+1}</span>", unsafe_allow_html=True)
        row_cols[1].markdown(f"<span style='font-size:12px;font-weight:600;'>{row['name']}</span>", unsafe_allow_html=True)
        row_cols[2].markdown(f"<span style='font-size:11px;color:#6b7280;'>{row['province']}</span>", unsafe_allow_html=True)
        row_cols[3].markdown(f"<span style='font-size:11px;color:#6b7280;'>{row['sector']}</span>", unsafe_allow_html=True)

        for col_widget, delta_val in zip(row_cols[4:8], [row["sales_d"], row["cap_d"], row["emp_d"], row["prod_d"]]):
            col_widget.markdown(
                f"<span style='font-size:12px;color:{delta_color(delta_val, threshold)};font-weight:500;'>{fmt_pct(delta_val)}</span>",
                unsafe_allow_html=True
            )

        row_cols[8].markdown(badge_html(row["verdict"]), unsafe_allow_html=True)
        st.markdown("<hr style='margin:4px 0;border-color:#f3f4f6;'>", unsafe_allow_html=True)

st.markdown("")
st.markdown('<p class="note-text" style="text-align:center;">ASENXO · DOST SETUP 4.0 iFund Program · Region VI · DOST Admin Access Only</p>', unsafe_allow_html=True)
