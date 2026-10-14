# Cart2Insights — E-Commerce Business Analytics

## 1. Project Overview
Cart2Insights is an e-commerce data analytics project that explores customer behavior, orders, payments, products, reviews, and delivery performance. The goal is to turn raw e-commerce data into useful business insights.

## 2. Objectives
- Clean and prepare raw datasets.
- Explore e-commerce data using Python and SQL.
- Analyze sales, payment methods, product categories, and customer reviews.
- Evaluate delivery performance.
- Build an interactive dashboard to present key metrics and findings.

## 3. Tools and Technologies
- Python
- Pandas
- Matplotlib
- MySQL
- Streamlit

## 4. Datasets
The project uses nine datasets:
- Customers
- Orders
- Order Items
- Products
- Payments
- Reviews
- Sellers
- Geolocation
- Category Translation

The datasets were cleaned and loaded into MySQL for analysis.

## 5. Data Preparation
The data-cleaning process included checking missing values, duplicate records, column data types, and date columns, and preparing cleaned CSV files for analysis.

## 6. Business Analysis
The project explores:
- Order status distribution
- Monthly order trends
- Payment methods and payment values
- Top product categories by revenue
- Customer distribution by state
- Customer review scores
- Average Order Value (AOV)
- Delivery time and late-delivery rates
- Relationship between delivery performance and review scores
- Frequently ordered products and seller performance

## 7. Key Findings
- The dataset contains 99,441 customer records and 99,441 order records.
- Credit cards are the most frequently used payment method.
- Health & beauty and watches & gifts are among the leading categories by item revenue.
- Average Order Value is approximately R$160.99.
- Approximately 77.1% of reviews received 4 or 5 stars.
- Average delivery time for delivered orders was approximately 12.5 days.
- Approximately 8.11% of delivered orders were late.
- On-time or early deliveries had a higher average review score than late deliveries.

## 8. Dashboard
An interactive Streamlit dashboard presents key metrics, charts, and business insights derived from the datasets.

To run the dashboard from the project folder:

```bash
python -m streamlit run cart2insights_dashboard.py
```

## 9. Conclusion
Cart2Insights demonstrates how data cleaning, SQL analysis, and Python visualization can help identify e-commerce trends and areas for improvement in customer satisfaction and delivery performance.