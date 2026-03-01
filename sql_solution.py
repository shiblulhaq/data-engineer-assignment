import sqlite3
import csv

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

query = """
SELECT
c.customer_id AS Customer,
c.age AS Age,
i.item_name AS Item,
SUM(s.quantity) AS Quantity
FROM customer c
JOIN orders o ON c.customer_id = o.customer_id
JOIN sales s ON o.order_id = s.order_id
JOIN items i ON s.item_id = i.item_id
WHERE c.age BETWEEN 18 AND 35
AND s.quantity IS NOT NULL
GROUP BY c.customer_id, c.age, i.item_name
HAVING SUM(s.quantity) > 0
"""

cursor.execute(query)

rows = cursor.fetchall()

with open("output_sql.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Customer","Age","Item","Quantity"])
    writer.writerows(rows)

conn.close()

print("CSV file created successfully")