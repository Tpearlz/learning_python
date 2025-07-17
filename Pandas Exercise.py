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

# 2. Reading and Writing Files
# Reading CSV
# df = pd.read_csv('your_file.csv')  # Uncomment when file is available

# Writing CSV
# df.to_csv('output.csv', index=False)  # Uncomment to save file
