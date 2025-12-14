import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Beverages Sales Dashboard",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
df = pd.read_excel("coca_cola_sales.xlsx")

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.title("🔎 Filters")

region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

# ---------------- APPLY FILTER ----------------
if region == "All":
    filtered_df = df.copy()
else:
    filtered_df = df[df["Region"] == region]

# ---------------- TITLE ----------------
st.title("🥤 Beverages Analytics Dashboard")
st.caption("Interactive Business Intelligence Website (Streamlit)")
st.markdown("---")

# ---------------- KPI METRICS ----------------
total_sales = int(filtered_df["Total Sales"].sum())
operating_profit = int(filtered_df["Operating Profit"].sum())
units_sold = int(filtered_df["Units Sold"].sum())

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"{total_sales:,}")
col2.metric("📈 Operating Profit", f"{operating_profit:,}")
col3.metric("📦 Units Sold", f"{units_sold:,}")

st.markdown("---")

# ---------------- SALES BY BRAND ----------------
st.subheader("📊 Sales by Beverage Brand")

brand_sales = (
    filtered_df.groupby("Beverage Brand")["Total Sales"]
    .sum()
    .reset_index()
)

fig_sales = px.bar(
    brand_sales,
    x="Beverage Brand",
    y="Total Sales",
    color="Beverage Brand",
    text_auto=".2s",
    title="Total Sales by Beverage Brand"
)

fig_sales.update_layout(showlegend=False)

st.plotly_chart(fig_sales, use_container_width=True)

# ---------------- OPERATING PROFIT BY BRAND ----------------
st.subheader("📉 Operating Profit by Beverage Brand")

brand_profit = (
    filtered_df.groupby("Beverage Brand")["Operating Profit"]
    .sum()
    .reset_index()
)

fig_profit = px.bar(
    brand_profit,
    x="Beverage Brand",
    y="Operating Profit",
    color="Beverage Brand",
    text_auto=".2s",
    title="Operating Profit by Beverage Brand"
)

fig_profit.update_layout(showlegend=False)

st.plotly_chart(fig_profit, use_container_width=True)

# ---------------- UNITS SOLD BY BRAND ----------------
st.subheader("📦 Units Sold by Beverage Brand")

brand_units = (
    filtered_df.groupby("Beverage Brand")["Units Sold"]
    .sum()
    .reset_index()
)

fig_units = px.bar(
    brand_units,
    x="Beverage Brand",
    y="Units Sold",
    color="Beverage Brand",
    text_auto=".2s",
    title="Units Sold by Beverage Brand"
)

fig_units.update_layout(showlegend=False)

st.plotly_chart(fig_units, use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown("---")

