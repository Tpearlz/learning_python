# Importing pandas
import pandas as pd

#1. Creating Data Structures
# Series
s = pd.Series([10, 20, 30, 40])
print("Series:\n", s)


# DataFrame
data = {
   'Name': ['Alice', 'Bob', 'Charlie'],
   'Age': [25, 30, 35],
   'Salary': [70000, 80000, 90000]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
