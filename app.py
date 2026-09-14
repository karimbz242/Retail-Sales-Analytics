import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Retail Sales Analytics",
    page_icon="📊",
    layout="wide"
)
st.markdown("""
<style>
[data-baseweb="tag"] {
    background-color: #2196F3 !important;
}

[data-baseweb="tag"] * {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stMetricValue"] {
    font-size: 24px !important;
}
</style>
""", unsafe_allow_html=True)

# Load dataset
df = pd.read_csv("data/Superstore.csv")

# Clean data
df = df.dropna(subset=["Order Date"])

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Dashboard filters
st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

selected_segment = st.sidebar.multiselect(
    "Select Segment",
    options=sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique())
)
selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(df["Order Date"].min(), df["Order Date"].max()),
    min_value=df["Order Date"].min(),
    max_value=df["Order Date"].max()
)
# Apply filters
if len(selected_dates) == 2:
    filtered_df = df[
        (df["Region"].isin(selected_region)) &
        (df["Category"].isin(selected_category)) &
        (df["Segment"].isin(selected_segment)) &
        (df["Order Date"].dt.date >= selected_dates[0]) &
        (df["Order Date"].dt.date <= selected_dates[1])
    ]
else:
    filtered_df = df[
        (df["Region"].isin(selected_region)) &
        (df["Category"].isin(selected_category)) &
        (df["Segment"].isin(selected_segment))
    
]

# Dashboard title
st.title("📊 Retail Sales Analytics Dashboard")
st.write(
    "Interactive analysis of sales, profitability, customers, "
    "products, and regional performance."
)

# Calculate KPIs
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
average_order_value = total_sales / total_orders
total_quantity = filtered_df["Quantity"].sum()
profit_margin = (total_profit / total_sales) * 100


# Display KPI cards
col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Profit Margin", f"{profit_margin:.2f}%")
col4.metric("Total Orders", f"{total_orders:,}")
col5.metric("Average Order Value", f"${average_order_value:,.2f}")
col6.metric("Total Quantity", f"{total_quantity:,.0f}")

# Download filtered data
st.subheader("Download Filtered Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv,
    file_name="filtered_retail_sales.csv",
    mime="text/csv"
)

# Sales by Category
st.subheader("Sales by Category")
category_sales = filtered_df.groupby("Category")["Sales"].sum()
st.bar_chart(category_sales)

# Profit by Region
st.subheader("Profit by Region")
region_profit = filtered_df.groupby("Region")["Profit"].sum()
st.bar_chart(region_profit)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")
monthly_sales = filtered_df.groupby(
        filtered_df["Order Date"].dt.month
)["Sales"].sum()

monthly_sales.index = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]
st.line_chart(monthly_sales)

# Sales vs Profit Trend
st.subheader("Sales vs Profit Trend")

monthly_performance = filtered_df.groupby(
    filtered_df["Order Date"].dt.to_period("M")
)[["Sales", "Profit"]].sum()

monthly_performance.index = monthly_performance.index.astype(str)

st.line_chart(monthly_performance)

# Top Sub-Categories by Profit
st.subheader("Top Sub-Categories by Profit")

subcategory_profit = (
    filtered_df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)

)

st.bar_chart(subcategory_profit)