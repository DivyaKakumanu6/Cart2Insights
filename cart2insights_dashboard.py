import streamlit as st
import pandas as pd
import mysql.connector
# Dashboard settings
st.set_page_config(page_title="Cart2Insights", page_icon="🛒", layout="wide")

# Dashboard title
st.title("🛒 Cart2Insights")
st.subheader("E-Commerce Analytics Dashboard")

# Load cleaned data
orders = pd.read_csv("cleaned_orders.csv")
customers = pd.read_csv("cleaned_customers.csv")
products = pd.read_csv("cleaned_products.csv")
payments = pd.read_csv("cleaned_payments.csv")

# Display key metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", f"{len(orders):,}")
col2.metric("Total Customers", f"{len(customers):,}")
col3.metric("Total Products", f"{len(products):,}")
col4.metric("Payment Records", f"{len(payments):,}")

# Payment method chart
st.subheader("Payment Methods")
payment_counts = payments["payment_type"].value_counts()
st.bar_chart(payment_counts)

# Customer review chart
st.subheader("Customer Review Scores")
reviews = pd.read_csv("cleaned_reviews.csv")
review_counts = reviews["review_score"].value_counts().sort_index()
st.bar_chart(review_counts)

# Product category chart
st.subheader("Top 10 Product Categories")
category_counts = products["product_category_name"].value_counts().head(10)
st.bar_chart(category_counts)
st.subheader("Order Status Distribution")
status_counts = orders["order_status"].value_counts()
st.bar_chart(status_counts)

st.subheader("Monthly Order Trend")

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["order_month"] = (
    orders["order_purchase_timestamp"].dt.to_period("M").astype(str)
)
monthly_orders = orders["order_month"].value_counts().sort_index()

st.line_chart(monthly_orders)
st.subheader("Top 10 Customer States")
state_counts = customers["customer_state"].value_counts().head(10)
st.bar_chart(state_counts)

st.subheader("Top 10 Categories by Revenue")

category_revenue = (
    products.merge(
        pd.read_csv("cleaned_order_items.csv"),
        on="product_id"
    )
    .groupby("product_category_name")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
st.bar_chart(category_revenue)

st.subheader("Total Payment Value by Payment Method")

payment_value = payments.groupby("payment_type")["payment_value"].sum()

st.bar_chart(payment_value)

st.subheader("Top 10 Most Frequently Ordered Products")

order_items = pd.read_csv("cleaned_order_items.csv")

product_order_counts = order_items["product_id"].value_counts().head(10)
st.bar_chart(product_order_counts)

st.header("📊 Key Business Insights")

st.markdown("""
- **Customer Satisfaction:** 77.1% of customer reviews received 4 or 5 stars.
- **Payment Preference:** Credit cards account for the largest share of payment records.
- **Top Product Categories:** Health & beauty and watches & gifts lead in item revenue.
- **Average Order Value:** Customers spend approximately R$160.99 per order on average.
- **Delivery Performance:** Approximately 8.11% of delivered orders were late.
- **Delivery and Reviews:** On-time or early deliveries averaged 4.29 stars, compared with 2.57 stars for late deliveries.
""")