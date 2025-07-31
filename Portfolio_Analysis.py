import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading CSV
df = pd.read_csv("Small_Portfolio_data.csv")

# Create a date range for the index
dates = pd.date_range('2015-02-01', periods=3)

# Setting the new index for the first 3 rows
df_subset = df.head(3)
df_subset.index = dates

# Printing the updated DataFrame
print(df_subset)

# Convert the stock price columns to numeric, coercing errors (non-numeric) to NaN
df[['GE', 'JPM', 'MSFT', 'PG']] = df[['GE', 'JPM', 'MSFT', 'PG']].apply(pd.to_numeric, errors='coerce')

# Calculate the percentage change (daily returns) for the stock price columns
returns = df[['GE', 'JPM', 'MSFT', 'PG']].pct_change()

# Print the daily returns
print("\nDaily Returns:\n", returns)

