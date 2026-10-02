import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
#       STUDENT PERFORMANCE - EDA
# ==========================================

# Create dataset
data = {
    "Name": [
        "Anu", "Ravi", "Priya", "Kiran", "Sita",
        "Rahul", "Divya", "Arjun", "Meena", "Vijay"
    ],

    "Age": [
        20, 21, 20, 22, 21,
        20, 22, 21, 20, 22
    ],

    "Gender": [
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male"
    ],

    "Python": [
        85, 72, 90, 65, 88,
        76, 95, 70, 82, 68
    ],

    "SQL": [
        80, 75, 92, 60, 85,
        78, 94, 72, 84, 65
    ],

    "Java": [
        78, 70, 88, 62, 90,
        74, 96, 68, 80, 64
    ],

    "Attendance": [
        92, 85, 96, 75, 90,
        82, 98, 78, 88, 72
    ]
}


# Convert data into DataFrame
df = pd.DataFrame(data)


# ==========================================
# 1. DISPLAY DATASET
# ==========================================

print("\n========== STUDENT DATASET ==========")
print(df)


# ==========================================
# 2. DATASET INFORMATION
# ==========================================

print("\n========== DATASET INFORMATION ==========")
print(df.info())


# ==========================================
# 3. CHECK MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# ==========================================
# 4. STATISTICAL SUMMARY
# ==========================================

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# ==========================================
# 5. AVERAGE MARKS
# ==========================================

df["Average"] = df[["Python", "SQL", "Java"]].mean(axis=1)

print("\n========== STUDENT AVERAGES ==========")

print(
    df[
        ["Name", "Python", "SQL", "Java", "Average"]
    ]
)


# ==========================================
# 6. HIGHEST PERFORMING STUDENT
# ==========================================

highest_student = df.loc[df["Average"].idxmax()]

print("\n========== HIGHEST PERFORMING STUDENT ==========")

print("Name:", highest_student["Name"])
print("Average Marks:", round(highest_student["Average"], 2))


# ==========================================
# 7. LOWEST PERFORMING STUDENT
# ==========================================

lowest_student = df.loc[df["Average"].idxmin()]

print("\n========== LOWEST PERFORMING STUDENT ==========")

print("Name:", lowest_student["Name"])
print("Average Marks:", round(lowest_student["Average"], 2))


# ==========================================
# 8. SUBJECT AVERAGES
# ==========================================

python_average = df["Python"].mean()
sql_average = df["SQL"].mean()
java_average = df["Java"].mean()

print("\n========== SUBJECT AVERAGES ==========")

print("Python Average:", round(python_average, 2))
print("SQL Average:", round(sql_average, 2))
print("Java Average:", round(java_average, 2))


# ==========================================
# 9. GENDER COUNT
# ==========================================

print("\n========== GENDER COUNT ==========")

print(df["Gender"].value_counts())


# ==========================================
# 10. ATTENDANCE ANALYSIS
# ==========================================

print("\n========== ATTENDANCE ANALYSIS ==========")

print("Average Attendance:",
      round(df["Attendance"].mean(), 2))

print("Highest Attendance:",
      df["Attendance"].max())

print("Lowest Attendance:",
      df["Attendance"].min())


# ==========================================
# 11. BAR CHART - SUBJECT AVERAGES
# ==========================================

subjects = ["Python", "SQL", "Java"]

averages = [
    python_average,
    sql_average,
    java_average
]

plt.figure(figsize=(8, 5))

plt.bar(subjects, averages)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()


# ==========================================
# 12. BAR CHART - STUDENT AVERAGES
# ==========================================

plt.figure(figsize=(10, 5))

plt.bar(df["Name"], df["Average"])

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.show()


# ==========================================
# 13. SCATTER PLOT
# ==========================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Attendance"],
    df["Average"]
)

plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")

plt.show()


# ==========================================
# 14. FINAL OBSERVATIONS
# ==========================================

print("\n========== FINAL OBSERVATIONS ==========")

print(
    "1. The dataset contains student performance information."
)

print(
    "2. Average marks were calculated for Python, SQL and Java."
)

print(
    "3. The highest and lowest performing students were identified."
)

print(
    "4. Subject-wise average marks were calculated."
)

print(
    "5. Attendance was compared with student performance."
)

print(
    "6. Charts were created to visualize the data."
)

print("\n========== EDA PROJECT COMPLETED ==========")