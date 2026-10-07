import pandas as pd

# Create a Pandas Series
marks = pd.Series([78, 85, 91, 67, 88])
print(marks)

# Create a Pandas Series with custom index
marks2 = pd.Series(
    [78, 85, 91, 67, 88],
    index=["Amit", "Sneha", "Rahul", "Priya", "Karan"]
)
print(marks2)

# Create a DataFrame
data = {
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Karan"],
    "Marks": [78, 85, 91, 67, 88],
    "Attendance": [92, 85, 78, 90, 88]
}

df = pd.DataFrame(data)

# Display complete DataFrame
print(df)

# Display first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

# Display last 2 rows
print("\nLast 2 rows:")
print(df.tail(2))

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Save DataFrame to CSV
df.to_csv("students_output.csv", index=False)
print("\nCSV file saved successfully")

# Read CSV file
df2 = pd.read_csv("students_output.csv")

print("\nData read from CSV:")
print(df2)

