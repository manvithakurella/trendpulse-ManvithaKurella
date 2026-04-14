#Task_2: TrendPulse: What's Actually Trending Right Now

import pandas as pd

#1 Load the JSON file

df = pd.read_json("/trends_20260414.json")

print(f"Loaded {len(df)} stories from {"/trends_20260414.json"}")

# 2 — Clean the Data
# Remove duplicates based on post_id
df = df.drop_duplicates(subset="post_id")
print("After removing duplicates:", len(df))

# Removing Null
df = df.dropna(subset=["post_id", "title", "score"])
print("After removing nulls:", len(df))

# Convert data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low-Scores
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))

# Remove extra whitespace from title
df["title"] = df["title"].str.strip()

# 3 — Save as CSV
output_path = "/trends_20260414.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")

# stories per category
if "category" in df.columns:
    print("\nStories per category:")
    print(df["category"].value_counts())
else:
    print("\nNo 'category' column found.")