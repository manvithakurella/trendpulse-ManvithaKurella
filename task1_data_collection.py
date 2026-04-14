
#Task1_Fetch Data from API

import requests
import time
import json
import os
from datetime import datetime

headers = {"User-Agent": "TrendPulse/1.0"}

#Category Keywords

CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def get_category(title):
  tilte = title.lower()
  for category, keywords in CATEGORIES.items():
    for word in keywords:
      if word in title:
        return category
  return None

# Step 1 — Get the list of top story IDs:
def fetch_data():
  url = "https://hacker-news.firebaseio.com/v0/topstories.json"
  ids = requests.get(url, headers=headers).json()[:500]

  collected = []
  category_count = {cat: 0 for cat in CATEGORIES}

#Step 2 — Get each story's details:

  for story_ids in ids:
    try:
      res = requests.get(
          f"https://hacker-news.firebaseio.com/v0/item/{story_ids}.json",
          headers=headers
      )
      data = res.json()

      if not data or "title" not in data:
          continue
      category = get_category(data["title"])
      if category and category_count[category] < 25:
         story = {
             "post_id": data.get("id"),
             "title": data.get("title"),
             "category": category,
             "score": data.get("score", 0),
             "num_comments": data.get("descendants", 0),
             "author": data.get("by"),
             "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

         }

         collected.append(story)
         category_count[category]+=1

      #Stop if all catergories filled

      if all(v>=25 for v in category_count.values()):
          break
    except Exception as e:
        print(f"Error Fetching {story_id}: {e}")

  return collected

# Save File in JSON

def save_json(data):
  os.makedirs("data", exist_ok=True)
  filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

  with open(filename, "w") as f:
    json.dump(data, f,indent=4)


  print(f"collected {len(data)} stories.saved to {filename}")

if __name__ == "__main__":
  data = fetch_data()
  save_json(data)