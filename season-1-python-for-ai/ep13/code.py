"""Feature Scaling & Encoding — Episode 13: Preparing data for algorithms.

Portfolio project #13: save this file, run it, put it on GitHub.

Yesterday we split honestly: 16 videos to study, 4 locked away as the
exam. Today we prepare the study set for its first real algorithm:
scale the numbers so no column can shout over the others, and encode
the words so the model can read them.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Our dataset: the same 20 videos, now with two new columns.
# prev_views = views of the creator's previous video (momentum),
# category   = the kind of video, as a WORD (models cannot read words).
videos = pd.DataFrame({
    "duration_min": [4, 7, 10, 5, 12, 8, 6, 15, 9, 3,
                     11, 7, 14, 6, 10, 8, 5, 13, 9, 7],
    "prev_views":   [9800, 15200, 22100, 12400, 31500, 19800, 14700,
                     40200, 18900, 8600, 27600, 16900, 35800, 17300,
                     25400, 20100, 13200, 33900, 21700, 15800],
    "category":     ["tutorial", "tutorial", "vlog", "tutorial", "review",
                     "vlog", "tutorial", "review", "vlog", "tutorial",
                     "review", "tutorial", "vlog", "tutorial", "review",
                     "vlog", "tutorial", "review", "vlog", "tutorial"],
    "views":        [15200, 28400, 41700, 19800, 52300, 33900,
                     24100, 61800, 30200, 12400, 47600, 27900,
                     58400, 26500, 44100, 32600, 21300, 54900,
                     36800, 25700],
})

# X = the questions (duration, momentum, category).
# y = the answer we want to predict later (views).
X = videos[["duration_min", "prev_views", "category"]]
y = videos["views"]

# STEP 1 — SPLIT FIRST (yesterday's lesson). We split BEFORE scaling,
# because everything we learn about the data must come from the
# study set only. The exam stays locked away and untouched.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Train: {X_train.shape[0]} videos to study")
print(f"Test:  {X_test.shape[0]} videos locked away for the exam")

# STEP 2 — SCALE the numbers. Look at the problem first:
# duration lives between 3 and 15, prev_views between 8,600 and
# 40,200. In any distance or gradient calculation, prev_views is
# thousands of times louder — duration becomes a whisper.
# StandardScaler rewrites each column as: (value - mean) / spread,
# so every column ends up centered on 0 with the same spread.
scaler = StandardScaler()
numeric = ["duration_min", "prev_views"]

# fit_transform on TRAIN: the scaler learns the mean and spread
# from the study set ONLY.
X_train_scaled = X_train.copy()
X_train_scaled[numeric] = scaler.fit_transform(X_train[numeric])

# transform on TEST: we APPLY the study set's mean and spread to
# the exam. We never fit on the exam — that would be peeking.
X_test_scaled = X_test.copy()
X_test_scaled[numeric] = scaler.transform(X_test[numeric])

print("\nBefore scaling, train ranges:")
print(f"  duration_min: {X_train['duration_min'].min()} to {X_train['duration_min'].max()}")
print(f"  prev_views:   {X_train['prev_views'].min()} to {X_train['prev_views'].max()}")
print("After scaling, both columns live roughly between -2 and +2:")
print(X_train_scaled[numeric].round(2).head())

# STEP 3 — ENCODE the words. A model cannot read "tutorial", so
# one-hot encoding gives each category its own 0/1 column:
# category_tutorial = 1 means yes, this one is a tutorial.
X_train_ready = pd.get_dummies(X_train_scaled, columns=["category"], dtype=int)
X_test_ready = pd.get_dummies(X_test_scaled, columns=["category"], dtype=int)

print("\nModel-ready train set — numbers only, fair scales:")
print(X_train_ready.round(2).head())
print(f"\nFinal shapes — train: {X_train_ready.shape}, test: {X_test_ready.shape}")
print("Done — scaled, encoded, and the exam was never peeked at.")
