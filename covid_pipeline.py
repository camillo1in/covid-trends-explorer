import pandas as pd

df = pd.read_csv("owid-covid-data.csv")
print(df.shape)
print(df.columns)
print(df.head())

import sqlite3

# Create (or connect to) SQLite database
conn = sqlite3.connect("covid_data.db")

# Store DataFrame as a table named 'covid'
df.to_sql("covid", conn, if_exists="replace", index=False)

# Confirm write success
print("Data written to SQLite database.")