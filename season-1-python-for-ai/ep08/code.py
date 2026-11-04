"""Dataset Explorer — Episode 8: Loading datasets with pandas.

Portfolio project #8: save this file and videos.csv in the SAME folder,
run it, put both on GitHub.

Real data lives in files: a CSV is a table where each row is one line
and each column is separated by a comma. pd.read_csv turns that file
into a DataFrame you can question with code.
"""

import pandas as pd

# Load a REAL dataset: 12 YouTube videos with their category, views, likes.
# videos.csv must be in the same folder as this script.
df = pd.read_csv("videos.csv")

# The four "hello" commands for ANY dataset:
print(df.head())          # first 5 rows — a quick peek at the table
print(df.shape)           # (rows, columns): 12 videos, 4 columns
df.info()                 # column names, types, and any missing values
print(df.describe())      # instant stats: count, mean, min, max, ...

# A real question: which category averages the most views?
avg_views = df.groupby("category")["views"].mean()
print(avg_views.sort_values(ascending=False))

# The three most-watched videos — sorted, and saved to a brand-new CSV:
top3 = df.sort_values("views", ascending=False).head(3)
top3.to_csv("top3.csv", index=False)
print("Saved top3.csv —", top3["title"].tolist())


if __name__ == "__main__":
    pass  # everything above already runs when you press play
