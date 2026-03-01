import sqlite3
import logging
from contextlib import closing

DB_NAME = "database.db"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    logging.info("Connected to SQLite database.")
    return conn

def create_tables(conn):

    queries = [

    """
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        age INTEGER
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS items (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        item_id INTEGER,
        quantity INTEGER
    );
    """
    ]

    cursor = conn.cursor()

    for q in queries:
        cursor.execute(q)

    conn.commit()

def insert_data(conn):

    cursor = conn.cursor()

    customers = [
        (1,21),
        (2,23),
        (3,35),
        (4,45)
    ]

    items = [
        (1,'x'),
        (2,'y'),
        (3,'z')
    ]

    orders = [
        (1,1),
        (2,2),
        (3,3)
    ]

    sales = [
        (1,1,1,10),
        (2,2,1,1),
        (3,2,2,1),
        (4,2,3,1),
        (5,3,3,2)
    ]

    cursor.executemany("INSERT INTO customer VALUES (?,?)", customers)
    cursor.executemany("INSERT INTO items VALUES (?,?)", items)
    cursor.executemany("INSERT INTO orders VALUES (?,?)", orders)
    cursor.executemany("INSERT INTO sales VALUES (?,?,?,?)", sales)

    conn.commit()

def main():

    conn = create_connection(DB_NAME)

    create_tables(conn)
    insert_data(conn)

    conn.close()

    print("Database created successfully")

if __name__ == "__main__":
    main()