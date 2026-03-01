# Data Engineer Assignment

This project analyzes purchase quantities for customers aged 18–35 using a SQLite database.

## Solutions
Two solutions were implemented:

1. SQL-based solution using SQLite queries
2. Pandas-based solution using Python data processing

Both solutions produce identical results.

## Project Structure

create_database.py – Creates SQLite database and inserts sample data  
sql_solution.py – Extracts results using SQL  
pandas_solution.py – Extracts results using Pandas  
database.db – SQLite database  
output_sql.csv – SQL output  
output_pandas.csv – Pandas output  

## Requirements

Python 3.x  
pandas  

Install dependencies:

pip install -r requirements.txt

## Run Scripts

Create database:

python create_database.py

Run SQL solution:

python sql_solution.py

Run Pandas solution:

python pandas_solution.py

Output CSV files will be generated using semicolon delimiter.