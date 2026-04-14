#Task 3 — Analysis with Pandas & NumPy

import pandas as pd
import numpy as np
# 1 — Load and Explore

df = pd. read_csv("/trends_20260414.csv")
print("First 5 rows:\n")
print(df.head())

#Shape of Dataframe
print("\nShape of DataFrame:", df.shape)

# Average values
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", avg_score)
print("Average comments:", avg_comments)

# 2 — Basic Analysis with NumPy

scores = df["score"].values
comments = df["num_comments"].values
print("\n--- NumPy Analysis ---")
print("Mean score:", np.mean(scores))
print("Median score:", np.median(scores))
print("Standard deviation:", np.std(scores))
print("Max score:", np.max(scores))
print("Min score:", np.min(scores))

# Category with most stories
count = df["category"].value_counts()[top_category]
print(f"Most stories in: {top_category} ({count} stories)")

# Story with most comments
max_comments_index = np.argmax(comments)
top_story = df.iloc[max_comments_index]
print(f'Most commented story: "{top_story["title"]}" — {top_story["num_comments"]:,} comments')

# 3 — Add New Columns

# Engagement column
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular column
df["is_popular"] = df["score"] > avg_score

# 4 — Save Result

output_path = "/trends_20260414_analysed.csv"
df.to_csv(output_path, index=False)
print(f"\nSaved analysed data to {output_path}")