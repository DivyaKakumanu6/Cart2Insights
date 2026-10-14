# Cart2Insights Project
print("Welcome to Cart2Insights")
import os
import pandas as pd
customers = pd.read_csv("olist_customers_dataset.csv")
print(customers.head())
print("Dataset shape:", customers.shape)
print(customers.info())
print("Missing values:")
print(customers.isnull().sum())
print("Duplicate rows:", customers.duplicated().sum())
print(customers.dtypes)
customers.to_csv("cleaned_customers.csv", index=False)

#2 orders dataset checking
orders = pd.read_csv("olist_orders_dataset.csv")
print(orders.head())
print("Shape:", orders.shape)
print(orders.info())
print(orders.isnull().sum())
print("Duplicate rows:", orders.duplicated().sum())
print(orders.dtypes)

# Cleaning the data
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column], errors="coerce")
print(orders.dtypes)
print(orders.isnull().sum())
print(orders["order_status"].value_counts())
delivered_orders = orders[orders["order_status"] == "delivered"]

print("Delivered orders:", delivered_orders.shape[0])
print(delivered_orders.isnull().sum())
print("Duplicate rows:", orders.duplicated().sum())
print(orders.groupby("order_status")[
    [
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date"
    ]
      ].agg(lambda column: column.isnull().sum()))

print(
    orders[
        (orders["order_status"] == "delivered") &
        (orders["order_delivered_customer_date"].isnull())
    ]
)

missing_delivery = orders[
    (orders["order_status"] == "delivered") &
    (orders["order_delivered_customer_date"].isnull())
]

print(missing_delivery[[
    "order_id",
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]].to_string(index=False))

print(
    orders[
        (orders["order_status"] == "delivered") &
        (orders["order_approved_at"].isnull())
    ][[
        "order_id",
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date"
    ]].to_string(index=False)
)

print("Shape:", orders.shape)

print("Missing values:")
print(orders.isnull().sum())

print("Duplicate rows:", orders.duplicated().sum())
orders.to_csv("cleaned_orders.csv", index=False, date_format="%Y-%m-%d %H:%M:%S")
print("Orders CSV saved successfully!")

print("Orders dataset saved successfully!")
#order_items cleaning
order_items = pd.read_csv("olist_order_items_dataset.csv")
print(order_items.head())
print("Shape:", order_items.shape)
print(order_items.info())
print(order_items.isnull().sum())
print("Duplicate rows:", order_items.duplicated().sum())
print(order_items.dtypes)
order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)
print(order_items.dtypes)
print(order_items.isnull().sum())
order_items.to_csv("cleaned_order_items.csv", index=False)
print("Order Items dataset saved successfully!")
# products database cleaning
products = pd.read_csv("olist_products_dataset.csv")
print(products.head())
print("Products dataset shape:", products.shape)
print(products.columns)
print(products.dtypes)
print(products.isnull().sum())
print("Duplicate rows:", products.duplicated().sum())
print(products[products["product_category_name"].isnull()].head(10))
print(products[products["product_weight_g"].isnull()])
print(products.isnull().sum())
print("Products shape before cleaning:", products.shape)
products["product_category_name"] = products["product_category_name"].fillna("Unknown")
print(products.isnull().sum())
print(products[products["product_name_lenght"].isnull()].head())
products["product_name_lenght"] = products["product_name_lenght"].fillna(products["product_name_lenght"].mean())
products["product_description_lenght"] = products["product_description_lenght"].fillna(products["product_description_lenght"].mean())
products["product_photos_qty"] = products["product_photos_qty"].fillna(products["product_photos_qty"].mean())

products["product_weight_g"] = products["product_weight_g"].fillna(products["product_weight_g"].mean())
products["product_length_cm"] = products["product_length_cm"].fillna(products["product_length_cm"].mean())
products["product_height_cm"] = products["product_height_cm"].fillna(products["product_height_cm"].mean())
products["product_width_cm"] = products["product_width_cm"].fillna(products["product_width_cm"].mean())
print(products.isnull().sum())
products.to_csv("cleaned_products.csv", index=False)
print("Products dataset saved successfully!")
# products dataset cleaning
payments = pd.read_csv("olist_order_payments_dataset.csv")
print(payments.head())
print("Payments dataset shape:", payments.shape)
print(payments.columns)
print(payments.dtypes)
print(payments.isnull().sum())
print("Duplicate rows:", payments.duplicated().sum())
payments.to_csv("cleaned_payments.csv", index=False)
print("Payments dataset saved successfully!")
# reviews dataset cleaning
reviews = pd.read_csv("olist_order_reviews_dataset.csv")
print(reviews.head())
print("Reviews dataset shape:", reviews.shape)
print(reviews.columns)
print(reviews.dtypes)
print(reviews.isnull().sum())
print("Duplicate rows:", reviews.duplicated().sum())
reviews["review_comment_title"] = reviews["review_comment_title"].fillna("No comment")
reviews["review_comment_message"] = reviews["review_comment_message"].fillna("No comment")
print(reviews.isnull().sum())
reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"])
reviews["review_answer_timestamp"] = pd.to_datetime(reviews["review_answer_timestamp"])
print(reviews.dtypes)
reviews.to_csv("cleaned_reviews.csv", index=False)
print("Reviews dataset saved successfully!")
# sellers data cleaning
sellers = pd.read_csv("olist_sellers_dataset.csv")
print(sellers.head())
print("Sellers dataset shape:", sellers.shape)
print(sellers.columns)
print(sellers.dtypes)
print(sellers.isnull().sum())
print("Duplicate rows:", sellers.duplicated().sum())
sellers.to_csv("cleaned_sellers.csv", index=False)
print("Sellers dataset saved successfully!")
# geolocation dataset cleaning
geolocation = pd.read_csv("olist_geolocation_dataset.csv")
print(geolocation.head())
print("Geolocation dataset shape:", geolocation.shape)
print(geolocation.columns)
print(geolocation.dtypes)
print(geolocation.isnull().sum())
print("Duplicate rows:", geolocation.duplicated().sum())
geolocation = geolocation.drop_duplicates()
print("Duplicate rows after cleaning:", geolocation.duplicated().sum())
print("Geolocation shape after cleaning:", geolocation.shape)
geolocation.to_csv("cleaned_geolocation.csv", index=False)
print("Geolocation dataset saved successfully!")

#product category name translation cleaning
category_translation = pd.read_csv("product_category_name_translation.csv")
print(category_translation.head())
print(category_translation.shape)
print(category_translation.dtypes)
print(category_translation.isnull().sum())
print(category_translation.duplicated().sum())
category_translation.to_csv("cleaned_category_translation.csv", index=False)
print("Category Translation dataset saved successfully")

# EDA
import pandas as pd
customers = pd.read_csv("cleaned_customers.csv")
print("Customers dataset shape:", customers.shape)
print(customers.head())
print(customers.dtypes)
print(customers.isnull().sum())
print(customers["customer_state"].value_counts())
# visualizing the top 10 customer state
import matplotlib.pyplot as plt
top_10_states = customers["customer_state"].value_counts().head(10)
top_10_states.plot(kind="bar")
plt.title("Top 10 States by Customer Records")
plt.xlabel("State")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print(customers["customer_unique_id"].nunique())
# top 10 cities
print(customers["customer_city"].value_counts().head(10))
top_10_cities = customers["customer_city"].value_counts().head(10)
top_10_cities.plot(kind="bar")
plt.title("Top 10 Cities by Customer Records")
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
state_percentage = customers["customer_state"].value_counts(normalize=True) * 100
print(state_percentage.round(2))
#EDA for orders dataset
orders = pd.read_csv("cleaned_orders.csv")
print("Orders dataset shape:", orders.shape)
print(orders.head())
print(orders.dtypes)
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
orders["order_approved_at"] = pd.to_datetime(orders["order_approved_at"])
orders["order_delivered_carrier_date"] = pd.to_datetime(orders["order_delivered_carrier_date"])
orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"])
orders["order_estimated_delivery_date"] = pd.to_datetime(orders["order_estimated_delivery_date"])
print(orders.dtypes)
print(orders["order_status"].value_counts())
orders["order_status"].value_counts().plot(kind="bar")
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# calculating delivery time
orders["delivery_time_days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_purchase_timestamp"]
).dt.days
print(orders["delivery_time_days"].describe())
#comparing actual time delivery and estimated time delivery
orders["delivery_difference_days"] = (
    orders["order_delivered_customer_date"] -
    orders["order_estimated_delivery_date"]
).dt.days
print(orders["delivery_difference_days"].describe())
# early and late deliveries
early_deliveries = (orders["delivery_difference_days"] < 0).sum()
on_time_deliveries = (orders["delivery_difference_days"] == 0).sum()
late_deliveries = (orders["delivery_difference_days"] > 0).sum()
print("Early deliveries:", early_deliveries)
print("On-time deliveries:", on_time_deliveries)
print("Late deliveries:", late_deliveries)
# delivery performance chart
delivery_summary = pd.Series({
    "Early": early_deliveries,
    "On-time": on_time_deliveries,
    "Late": late_deliveries
})
delivery_summary.plot(kind="bar")
plt.title("Delivery Performance")
plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# EDA for cleaned payments dataset
payments = pd.read_csv("cleaned_payments.csv")
print("Payments dataset shape:", payments.shape)
print(payments.head())
print(payments.dtypes)
print(payments.isnull().sum())
print(payments["payment_type"].value_counts())
# Payment Method Chart
payments["payment_type"].value_counts().plot(kind="bar")
plt.title("Payment Methods Used by Customers")
plt.xlabel("Payment Method")
plt.ylabel("Number of Payment Records")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
payment_totals = payments.groupby("payment_type")["payment_value"].sum()
print(payment_totals.round(2).sort_values(ascending=False))
# Payment Value by Method Chart
payment_totals.sort_values(ascending=False).plot(kind="bar")
plt.title("Total Payment Value by Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Payment Value (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print(payments["payment_installments"].describe())
print(payments["payment_installments"].value_counts().sort_index())
# Installment chart
installment_counts = payments.loc[
    payments["payment_installments"] > 0, "payment_installments"
].value_counts().sort_index()
installment_counts.plot(kind="bar")
plt.title("Payment Installment Preferences")
plt.xlabel("Number of Installments")
plt.ylabel("Number of Payment Records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print(payments[payments["payment_installments"] == 0])
zero_orders = payments.loc[
    payments["payment_installments"] == 0, "order_id"
]
print(payments[payments["order_id"].isin(zero_orders)])
print(payments["payment_value"].describe())
print(payments[payments["payment_value"] == 0])
zero_payment_summary = payments[payments["payment_value"] == 0]["payment_type"].value_counts()
print(zero_payment_summary)
# EDA for cleaned order items dataset
order_items = pd.read_csv("cleaned_order_items.csv")
print("Order Items dataset shape:", order_items.shape)
print(order_items.head())
print(order_items.dtypes)
order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"]
)
print(order_items.dtypes)
print(order_items.isnull().sum())
print(order_items["price"].describe())
print(order_items["freight_value"].describe())
order_items["total_item_value"] = (
    order_items["price"] + order_items["freight_value"]
)
print(order_items["total_item_value"].describe())
# Average and freight price chart
average_costs = pd.Series({
    "Product Price": order_items["price"].mean(),
    "Freight Cost": order_items["freight_value"].mean()
})
average_costs.plot(kind="bar")
plt.title("Average Product Price vs Freight Cost")
plt.xlabel("Cost Type")
plt.ylabel("Average Value (R$)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
top_expensive_items = order_items.nlargest(10, "price")
print(top_expensive_items[["product_id", "price", "freight_value"]])
# Chart of top 10 expensive items
top_expensive_items.plot(
    x="product_id",
    y="price",
    kind="bar",
    legend=False
)
plt.title("Top 10 Highest-Priced Order Items")
plt.xlabel("Product ID")
plt.ylabel("Price (R$)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
 # Most frequently ordered products
top_products = order_items["product_id"].value_counts().head(10)
print(top_products)
# Top 10 Products Chart
top_products.plot(kind="bar")
plt.title("Top 10 Most Frequently Ordered Products")
plt.xlabel("Product ID")
plt.ylabel("Number of Order Items")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
#Total sales value by product
product_sales = order_items.groupby("product_id")["price"].sum()
print(product_sales.sort_values(ascending=False).head(10))
# Top 10 Products by Sales Value
top_product_sales = product_sales.sort_values(
    ascending=False
).head(10)
top_product_sales.plot(kind="bar")
plt.title("Top 10 Products by Total Sales Value")
plt.xlabel("Product ID")
plt.ylabel("Total Sales Value (R$)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
# EDA for cleaned products
products = pd.read_csv("cleaned_products.csv")
print(products.shape)
print(products.head())
print(products.dtypes)
print(products.isnull().sum())
print(products.duplicated().sum())
print(products["product_category_name"].value_counts().head(10))
top_categories = products["product_category_name"].value_counts().head(10)
top_categories.plot(kind="bar")
plt.title("Top 10 Product Categories by Number of Products")
plt.xlabel("Product Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
print(products["product_weight_g"].describe())
print((products["product_weight_g"] == 0).sum())
print(products[products["product_weight_g"] == 0])
print(products.loc[products["product_category_name"] == "cama_mesa_banho", "product_weight_g"].median())
# REplacing 4 zero weight products
products.loc[products["product_weight_g"] == 0, "product_weight_g"] = 1250.0
print((products["product_weight_g"] == 0).sum())
products.to_csv("cleaned_products.csv", index=False)
#EDA for cleaned reviews
reviews = pd.read_csv("cleaned_reviews.csv")
print(reviews.shape)
print(reviews.head())
print(reviews["review_score"].value_counts().sort_index())
# Review score chart
reviews["review_score"].value_counts().sort_index().plot(kind="bar")
plt.title("Distribution of Customer Review Scores")
plt.xlabel("Review Score")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
print(reviews.isnull().sum())
print(reviews.duplicated().sum())
#EDA for cleaned sellers
sellers = pd.read_csv("cleaned_sellers.csv")
print(sellers.shape)
print(sellers.head())
print(sellers.isnull().sum())
print(sellers.duplicated().sum())
print(sellers["seller_state"].value_counts().head(10))
# Top 10 Seller state chart
sellers["seller_state"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Seller States")
plt.xlabel("State")
plt.ylabel("Number of Sellers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# EDA for cleaned category translation
category_translation = pd.read_csv("cleaned_category_translation.csv")
print(category_translation.shape)
print(category_translation.head())
print(category_translation.isnull().sum())
print(category_translation.duplicated().sum())
# EDA for cleaned geolocation
geolocation = pd.read_csv("cleaned_geolocation.csv")
print(geolocation.shape)
print(geolocation.isnull().sum())
print(geolocation.duplicated().sum())
# SQL connection
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="cart2insights_new"
)
if connection.is_connected():
    print("Connected to MySQL successfully!")
cursor = connection.cursor()
print("MySQL cursor created successfully!")

payments = pd.read_csv("cleaned_payments.csv")
payments = payments.astype(object).where(pd.notna(payments), None)

cursor.execute("SELECT COUNT(*) FROM payments")
existing_payments = cursor.fetchone()[0]

if existing_payments == 0:
    payments_data = [
        tuple(row)
        for row in payments.itertuples(index=False, name=None)
    ]

    cursor.executemany(
        """
        INSERT INTO payments (
            order_id,
            payment_sequential,
            payment_type,
            payment_installments,
            payment_value
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        payments_data
    )

    connection.commit()
    print("Payments data loaded successfully!")
else:
    print(
        f"Payments table already contains {existing_payments} rows. "
        "Skipping insert to avoid duplicates."
    )

cursor.execute("SELECT COUNT(*) FROM payments")
print("Payments rows in MySQL:", cursor.fetchone()[0])

reviews = pd.read_csv("cleaned_reviews.csv")
reviews = reviews.astype(object).where(pd.notna(reviews), None)

cursor.execute("SELECT COUNT(*) FROM reviews")
existing_reviews = cursor.fetchone()[0]

if existing_reviews == 0:
    reviews_data = [
        tuple(row)
        for row in reviews.itertuples(index=False, name=None)
    ]

    cursor.executemany(
        """
        INSERT INTO reviews (
            review_id,
            order_id,
            review_score,
            review_comment_title,
            review_comment_message,
            review_creation_date,
            review_answer_timestamp
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        reviews_data
    )

    connection.commit()
    print("Reviews data loaded successfully!")
else:
    print(f"Reviews table already contains {existing_reviews} rows. Skipping insert.")

cursor.execute("SELECT COUNT(*) FROM reviews")
print("Reviews rows in MySQL:", cursor.fetchone()[0])

sellers = pd.read_csv("cleaned_sellers.csv")
sellers = sellers.astype(object).where(pd.notna(sellers), None)

cursor.execute("SELECT COUNT(*) FROM sellers")
existing_sellers = cursor.fetchone()[0]

if existing_sellers == 0:
    sellers_data = [
        tuple(row)
        for row in sellers.itertuples(index=False, name=None)
    ]

    cursor.executemany(
        """
        INSERT INTO sellers (
            seller_id,
            seller_zip_code_prefix,
            seller_city,
            seller_state
        )
        VALUES (%s, %s, %s, %s)
        """,
        sellers_data
    )

    connection.commit()
    print("Sellers data loaded successfully!")
else:
    print(f"Sellers table already contains {existing_sellers} rows. Skipping insert.")

cursor.execute("SELECT COUNT(*) FROM sellers")
print("Sellers rows in MySQL:", cursor.fetchone()[0])

cursor.close()
connection.close()

geolocation = pd.read_csv("cleaned_geolocation.csv")
geolocation = geolocation.astype(object).where(pd.notna(geolocation), None)

cursor.execute("SELECT COUNT(*) FROM geolocation")
existing_geolocation = cursor.fetchone()[0]

if existing_geolocation == 0:
    geolocation_data = [
        tuple(row)
        for row in geolocation.itertuples(index=False, name=None)
    ]

    cursor.executemany(
        """
        INSERT INTO geolocation (
            geolocation_zip_code_prefix,
            geolocation_lat,
            geolocation_lng,
            geolocation_city,
            geolocation_state
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        geolocation_data
    )

    connection.commit()
    print("Geolocation data loaded successfully!")
else:
    print(
        f"Geolocation table already contains {existing_geolocation} rows. "
        "Skipping insert."
    )

cursor.execute("SELECT COUNT(*) FROM geolocation")
print("Geolocation rows in MySQL:", cursor.fetchone()[0])

cursor.close()
connection.close()
import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="cart2insights_new"
)
cursor = connection.cursor()

translation = pd.read_csv("cleaned_category_translation.csv")
translation = translation.astype(object).where(pd.notna(translation), None)

translation_data = [
    tuple(row)
    for row in translation.itertuples(index=False, name=None)
]

cursor.execute("SELECT COUNT(*) FROM translation")
existing_translation = cursor.fetchone()[0]

if existing_translation == 0:
    cursor.executemany(
        """
        INSERT INTO translation (
            product_category_name,
            product_category_name_english
        )
        VALUES (%s, %s)
        """,
        translation_data
    )
    connection.commit()
    print("Translation data loaded successfully!")
else:
    print("Translation table already contains data. Skipping insert.")

cursor.execute("SELECT COUNT(*) FROM translation")
print("Translation rows in MySQL:", cursor.fetchone()[0])

cursor.close()
connection.close()