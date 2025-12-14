import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="Coca-Cola Sales Dashboard",
    page_icon="🥤",
    layout="wide"
)

# ---------------------------------
# LOAD DATA
# ---------------------------------
@st.cache_data
def load_data():
    df = pd.read_excel("coca_cola_sales.xlsx")
    return df

df = load_data()

# ---------------------------------
# SIDEBAR FILTERS
# ---------------------------------
st.sidebar.header("🔎 Filters")

region_filter = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["Region"].dropna().unique().tolist())
)

if region_filter != "All":
    df = df[df["Region"] == region_filter]

# ---------------------------------
# KPI CALCULATIONS
# ---------------------------------
total_sales = int(df["Total Sales"].sum())
operating_profit = int(df["Operating Profit"].sum())
units_sold = int(df["Units Sold"].sum())

# ---------------------------------
# TITLE
# ---------------------------------
st.markdown("## 🥤 Coca-Cola Sales Analytics Dashboard")
st.caption("Interactive Business Intelligence Website (Streamlit)")
st.markdown("---")

# ---------------------------------
# KPI SECTION
# ---------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"{total_sales:,}")
col2.metric("📈 Operating Profit", f"{operating_profit:,}")
col3.metric("📦 Units Sold", f"{units_sold:,}")

st.markdown("---")

# ---------------------------------
# SALES BY BRAND
# ---------------------------------
st.subheader("📊 Sales by Beverage Brand")

brand_sales = (
    df.groupby("Beverage Brand", as_index=False)["Total Sales"]
    .sum()
    .sort_values(by="Total Sales", ascending=False)
)

fig_brand = px.bar(
    brand_sales,
    x="Beverage Brand",
    y="Total Sales",
    color="Beverage Brand",
    text_auto=True,
    template="plotly_white"
)

st.plotly_chart(fig_brand, use_container_width=True)

# ---------------------------------
# SALES BY REGION
# ---------------------------------
st.subheader("🌍 Sales by Region")

region_sales = (
    df.groupby("Region", as_index=False)["Total Sales"]
    .sum()
)

fig_region = px.pie(
    region_sales,
    values="Total Sales",
    names="Region",
    hole=0.4,
    template="plotly_white"
)

st.plotly_chart(fig_region, use_container_width=True)

# ---------------------------------
# PROFIT VS UNITS SOLD
# ---------------------------------
st.subheader("📦 Units Sold vs 📈 Operating Profit")

fig_scatter = px.scatter(
    df,
    x="Units Sold",
    y="Operating Profit",
    color="Beverage Brand",
    size="Total Sales",
    template="plotly_white"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# ---------------------------------
# DATA TABLE
# ---------------------------------
st.subheader("📄 Raw Sales Data")
st.dataframe(df, use_container_width=True)

# ---------------------------------
# FOOTER
# ---------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Python, Streamlit & Plotly")
