import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect("database.db")

# read tables
customers = pd.read_sql("SELECT * FROM customer", conn)
orders = pd.read_sql("SELECT * FROM orders", conn)
sales = pd.read_sql("SELECT * FROM sales", conn)
items = pd.read_sql("SELECT * FROM items", conn)

# merge tables
df = customers.merge(orders, on="customer_id")
df = df.merge(sales, on="order_id")
df = df.merge(items, on="item_id")

# filter age 18-35
df = df[(df["age"] >= 18) & (df["age"] <= 35)]

# remove null quantities
df = df[df["quantity"].notnull()]

# group and sum
result = df.groupby(["customer_id","age","item_name"])["quantity"].sum().reset_index()

# remove zero quantities
result = result[result["quantity"] > 0]

# rename columns
result.columns = ["Customer","Age","Item","Quantity"]

# export csv
result.to_csv("output_pandas.csv", sep=";", index=False)

conn.close()

print("Pandas solution completed")