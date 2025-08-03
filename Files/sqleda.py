
import sqlite3

import pandas as pd

df = pd.read_csv("clean_books.csv")

conn = sqlite3.connect("books.db")
df.to_sql("books", conn, if_exists="replace", index=False)
print("Data loaded into SQLite database successfully.")

cursor = conn.cursor()
query = "SELECT Title, Author, Rating FROM books ORDER BY Rating DESC LIMIT 5;"
cursor.execute(query)
for row in cursor.fetchall():
    print(row)
