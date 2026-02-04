a = "Student Performance Analysis"
print(a.upper())
print("\n")
# Import libraries
import pandas as pd

# Load Data
print("Load Data")
df = pd.read_csv("student.csv")
print(df)
print("\n")

# Explore Data
print("Explore Data")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns}")
print("\n")
# Find Missing Values
print("Find Missing Values")
print(df.isnull())
print("\n")

# Total count of missing values for each column.
print("Total count of missing values for each column.")
print(df.isnull().sum())
print("\n")

# Handle Missing Values
print("Handle Missing Values")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)
print("\n")

# Convert Age value and marks to the Integer
print("Convert Age value and marks to the Integer")
df["Age"] = df["Age"].round().astype(int)
df["Marks"] = df["Marks"].round().astype(int)
print(df)
print("\n")

# Insights
print("Insight")
# Average Marks
average_marks = df["Marks"].mean()
# Top Students
top_students = df[df["Marks"] >= 80]

print("Average Marks:",round(average_marks, 2))
print("Top Performing Students:")
# Descending order for "Marks" column
top_students = top_students.sort_values(by="Marks", ascending=False)
print(top_students)
print("\n")

# # City-wise average marks
print("# City-wise average marks")
city_avg = df.groupby("City")["Marks"].mean()
print(city_avg)
print("\n")

# Save clean Data
df.to_csv("Clean_student.csv", index=False)
print("Cleaned data saved as cleaned_student.csv")

