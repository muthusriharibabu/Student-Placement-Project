import pandas as pd

# Load dataset
df = pd.read_csv("placement_dataset.csv")

print("Dataset Loaded Successfully\n")

print(df.head())

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum()) 
# Remove duplicate records
df = df.drop_duplicates()


# Fill missing numerical values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nData Cleaning Completed!")




# Convert Yes/No to 1/0
df["Internship"] = df["Internship"].map({
    "Yes": 1,
    "No": 0
})

df["Placement_Status"] = df["Placement_Status"].map({
    "Yes": 1,
    "No": 0
})

print("\nEncoding Completed!")

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")



import matplotlib.pyplot as plt

placement_counts = df["Placement_Status"].value_counts()

plt.bar(["Placed", "Not Placed"],
        [placement_counts[1], placement_counts[0]])

plt.title("Placement Distribution")
plt.xlabel("Placement Status")
plt.ylabel("Number of Students")

plt.show()



# CGPA vs Placement

plt.figure(figsize=(8,5))

plt.scatter(df["CGPA"], df["Placement_Status"])

plt.title("CGPA vs Placement")
plt.xlabel("CGPA")
plt.ylabel("Placement Status")

plt.show()




# Internship vs Placement

internship_placement = df.groupby("Internship")["Placement_Status"].sum()

plt.figure(figsize=(6,4))

internship_placement.plot(kind="bar")

plt.title("Internship vs Placement")
plt.xlabel("Internship")
plt.ylabel("Placed Students")

plt.show()


plt.figure(figsize=(8,5))

plt.scatter(df["Aptitude_Score"], df["Placement_Status"])

plt.title("Aptitude Score vs Placement")
plt.xlabel("Aptitude Score")
plt.ylabel("Placement Status")

plt.show() 