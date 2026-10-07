import pandas as pd
import numpy as np
from io import StringIO

# Create CSV data
csv_data = """Name,Marks,Department,Attendance
Amit,78,CS,92
Sneha,85,IT,85
Rahul,91,CS,78
Priya,67,IT,90
Karan,88,CS,88
"""

# Read CSV data
df = pd.read_csv(StringIO(csv_data))

print("Original DataFrame:")
print(df)

# Check for missing values
print("\nMissing Values:")
print(df.isnull())

print("\nMissing Values Count:")
print(df.isnull().sum())

# Fill missing values with 0
df_filled = df.fillna(0)

print("\nAfter Filling Missing Values:")
print(df_filled)

# Drop rows containing missing values
df_dropped = df.dropna()

print("\nAfter Dropping Missing Values:")
print(df_dropped)

# Filter CS students
cs_students = df[df["Department"] == "CS"]

print("\nCS Students:")
print(cs_students)

# Select Name and Marks
name_marks = df[["Name", "Marks"]]

print("\nName and Marks:")
print(name_marks)

# Sort by Marks in descending order
sorted_df = df.sort_values(by="Marks", ascending=False)

print("\nStudents Sorted by Marks:")
print(sorted_df)

# Group by Department and calculate average marks
grouped = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(grouped)

