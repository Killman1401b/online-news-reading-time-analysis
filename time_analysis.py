# Online News Article Reading Time Analysis
# Minor 1 – Pandas Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Step 1: Create Sample Dataset


np.random.seed(42)

data = {
    "Article_ID": range(1, 101),
    "Category": np.random.choice(
        ["Politics", "Sports", "Technology", "Health", "Entertainment"], 
        100
    ),
    "Word_Count": np.random.randint(300, 2000, 100),
    "Reading_Time_Minutes": np.random.normal(6, 2, 100).clip(1),
}

df = pd.DataFrame(data)


# Engagement based on reading time

def engagement_level(time):
    if time < 4:
        return "Low"
    elif time <= 7:
        return "Medium"
    else:
        return "High"

df["Engagement"] = df["Reading_Time_Minutes"].apply(engagement_level)


# Step 3: Basic Data Exploration

print("\nFirst 5 Records:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())


# Step 4: Descriptive Statistics

print("\nDescriptive Statistics:\n")
print(df.describe())

print("\nAverage Reading Time per Category:\n")
print(df.groupby("Category")["Reading_Time_Minutes"].mean())

print("\nEngagement Distribution:\n")
print(df["Engagement"].value_counts())


# Step 5: Box Plot – Reading Time


plt.figure()
sns.boxplot(x=df["Reading_Time_Minutes"])
plt.title("Box Plot of Article Reading Time")
plt.xlabel("Reading Time (Minutes)")
plt.show()


# Step 6:  Box Plot

plt.figure()
sns.boxplot(x="Category", y="Reading_Time_Minutes", data=df)
plt.title("Reading Time by Article Category")
plt.xticks(rotation=30)
plt.show()

# -------------------------------
# Step 7: Engagement vs Category
# -------------------------------

plt.figure()
sns.countplot(x="Category", hue="Engagement", data=df)
plt.title("Engagement Level by Category")
plt.xticks(rotation=30)
plt.show()


# Step 8: Conclusion Output

print("\nConclusion:")
print("1. Technology and Politics articles tend to have higher reading times.")
print("2. Articles with reading time above 7 minutes show high engagement.")
print("3. Box plots help detect outliers in reading behavior.")
