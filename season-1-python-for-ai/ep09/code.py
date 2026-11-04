"""Data Cleaner — Episode 9: Cleaning data with pandas.

Portfolio project #9: save this file and videos_messy.csv in the SAME
folder, run it, put both on GitHub.

Real data is messy: rows go missing, rows get pasted twice. Cleaning is
the real 80% of a data job — find the mess, then fix it on purpose:
fill what you can reasonably fill, drop what you truly cannot use.
"""

import pandas as pd

# Load the MESSY dataset: 12 videos with gaps and double-pasted rows.
# videos_messy.csv must be in the same folder as this script.
df = pd.read_csv("videos_messy.csv")
print("Before cleaning:", df.shape)

# STEP 1 — FIND the mess. Never clean blind.
print(df.isna().sum())        # missing values, column by column
print("Duplicate rows:", df.duplicated().sum())

# STEP 2 — Remove exact duplicate rows (keep the first copy).
df = df.drop_duplicates()

# STEP 3 — Fill gaps you can reasonably fill.
# A missing category becomes "unknown" — honest, not invented.
df["category"] = df["category"].fillna("unknown")
# Missing numbers get the MEDIAN (the typical value), not the mean —
# one viral video would drag the mean up and lie to you.
df["views"] = df["views"].fillna(df["views"].median())
df["likes"] = df["likes"].fillna(df["likes"].median())

# STEP 4 — Drop what you cannot use: a row with no title tells us nothing.
df = df.dropna(subset=["title"])

# STEP 5 — Prove it is clean before you trust it.
print("After cleaning:", df.shape)
print(df.isna().sum())
print("Duplicate rows now:", df.duplicated().sum())

# Save the clean dataset — this is the file you hand to your team.
df.to_csv("videos_clean.csv", index=False)
print("Saved videos_clean.csv")
print(df.head(10))
