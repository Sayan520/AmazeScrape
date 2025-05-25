import os
import pandas as pd
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT, OUTPUT_DIR

# Function to save data to a CSV or Excel file
def save_data(data, filename, fmt):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, f"{filename}.{fmt}")

    try:
        if fmt == "csv":
            data.to_csv(path, index=False)
        elif fmt == "xlsx":
            data.to_excel(path, index=False, engine="openpyxl")
        return path
    except Exception as e:
        print("Save error:", e)
        return None

# Function to save data to MySQL database (optional)
def save_to_mysql(df):
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        port=DB_PORT

    )
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO products (name, price, rating) VALUES (%s, %s, %s)
        """, (row["Product Name"], row["Price"], row["Rating"]))

    conn.commit()
    conn.close()
