# 📚 Book Sales Analysis

This project focuses on analyzing the best-selling books using Python for data cleaning, SQLite for SQL-based querying, and Power BI for data visualization.

The goal was to explore key patterns such as book popularity, format trends, and pricing insights in a structured and meaningful way. The project walks through the complete flow — from raw data to a polished dashboard.

---

## 🔍 Dataset Overview

The dataset contained details like:
- Book title and author
- Ratings and number of reviews
- Format type and price
- Overall sales ranking

It was initially inconsistent, with:
- Ratings in string form (`"4.9 out of 5 stars"`)
- Commas in numeric fields like reviews
- Price fields containing phrases like `"5 offers from $77.90"`

---

## 🧹 Data Cleaning (Python)

Data preprocessing was done using Python with the help of `pandas`. Key steps included:
- Extracting numeric ratings using regex
- Removing commas and converting review counts to integers
- Parsing and standardizing prices
- Handling missing values
- Renaming columns for clarity

Cleaned data was saved to `clean_books.csv`.

---

## 🗄️ SQL Integration (SQLite)

To simulate working with relational databases:
- The cleaned data was loaded into an SQLite database
- SQL queries were run to explore top-rated books, average prices, and format-based filtering

This step helped bridge Python-based analysis with structured querying.

---

## 📊 Visualization (Power BI)

The final dataset was imported into Power BI to build an interactive dashboard, which includes:
- KPIs (Average Rating, Total Reviews, Average Price)
- Top 10 highest-rated books
- Format distribution
- Price vs Rating scatter plot

> **Note:** Since `.pbix` files cannot be previewed on GitHub directly, a screenshot of the dashboard (`dashboard_screenshot.png`) has been included for reference.

---

## 🧰 Tools Used

- Python (pandas, regex)
- SQLite (via `sqlite3`)
- Power BI
- GitHub

---

## 📁 Files in the Repository

- `Files/clean.py`: Python script for cleaning
- `clean_books.csv`: Cleaned dataset
- `books.pbix`: Power BI dashboard file
- `dashboard_screenshot.png`: Dashboard preview

---
