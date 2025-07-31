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

# Let's say our portfolio has:
# - 0% in GE
# - 50% in JPM
# - 25% in MSFT
# -75% in PG
weights = np.array([0, 0.5, 0.25, 0.75])

# Calculate mean daily return of each stock
mean_daily_returns = returns.mean()

# Portfolio return is weighted average of individual returns
port_return = np.sum(mean_daily_returns * weights)
print("\nPortfolio Return (daily average):", port_return)

# Add a 'Portfolio' column by multiplying weights
# Deep copy for independent manipulation
portfolio_returns = returns.copy(deep=True)
portfolio_returns['Portfolio'] = portfolio_returns.dot(weights)
