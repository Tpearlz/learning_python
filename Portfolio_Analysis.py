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