#Task 4 — Visualizations
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1  Setup
df = pd.read_csv("/content/trends_20260414_analysed.csv")
os.makedirs("outputs", exist_ok=True)

#2 Chart 1: Top 10 Stories by Score

top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten titles
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)
plt.figure()
sns.barplot(x="score", y="short_title", data=top10, palette="coolwarm")
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# 3 Chart 2: Stories per Category

plt.figure()
sns.countplot(x="category", data=df,palette="dark")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.show()

# 4 Chart 3: Score vs Comments

plt.figure()

sns.scatterplot(
    x="score",
    y="num_comments",
    hue="is_popular",
    data=df,
    palette="icefire"
)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.show()

# Bonus 

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1
sns.barplot(x="score", y="short_title", data=top10, palette="coolwarm", ax=axes[0])
axes[0].set_title("Top Stories")

# Chart 2
sns.countplot(x="category", data=df, palette="dark", ax=axes[1])
axes[1].set_title("Categories")
axes[1].tick_params(axis='x', rotation=45)

# Chart 3
sns.scatterplot(
    x="score",
    y="num_comments",
    hue="is_popular",
    data=df,
    palette="icefire",
    ax=axes[2]
)
axes[2].set_title("Score vs Comments")
fig.suptitle("TrendPulse Dashboard")
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()