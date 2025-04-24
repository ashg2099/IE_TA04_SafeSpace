import pandas as pd

# Load the two CSV files
df1 = pd.read_csv("pedestrian-counting-system-monthly-counts-per-hour (2).csv")
df2 = pd.read_csv("pedestrian-counting-system-monthly-counts-per-hour (3).csv")

# Merge the DataFrames vertically
merged_df = pd.concat([df1, df2], ignore_index=True)

# Remove duplicates (based on all columns or a subset)
merged_df = merged_df.drop_duplicates()

# Save the merged file
merged_df.to_csv("merged_pedestrian_counts.csv", index=False)

# Output some stats
print("✅ Merge complete!")
print(f"Total rows after merge: {len(merged_df)}")
print(f"Columns: {merged_df.columns.tolist()}")