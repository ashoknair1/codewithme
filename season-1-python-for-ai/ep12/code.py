"""Train-Test Split — Episode 12: How models are honestly evaluated.

Portfolio project #12: save this file, run it, put it on GitHub.

Yesterday we charted data. Today we cross into machine learning —
but before any model, one honest habit: NEVER judge a model on the
same data it learned from. That is like letting a student write
their own exam answers. The train-test split is the fix.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

# Our dataset: 20 videos. Two things we KNOW before publishing
# (duration in minutes, words in the title) and the one thing we
# want to PREDICT later (views). Realistic, made-up teaching data.
videos = pd.DataFrame({
    "duration_min": [4, 7, 10, 5, 12, 8, 6, 15, 9, 3,
                     11, 7, 14, 6, 10, 8, 5, 13, 9, 7],
    "title_words":  [6, 8, 7, 9, 6, 10, 7, 8, 5, 6,
                     9, 7, 8, 11, 6, 8, 7, 9, 10, 6],
    "views":        [15200, 28400, 41700, 19800, 52300, 33900,
                     24100, 61800, 30200, 12400, 47600, 27900,
                     58400, 26500, 44100, 32600, 21300, 54900,
                     36800, 25700],
})
print(f"Dataset: {videos.shape[0]} videos, {videos.shape[1]} columns")

# X = the QUESTIONS (what the model may look at while learning).
# y = the ANSWERS (what we want it to predict).
X = videos[["duration_min", "title_words"]]
y = videos["views"]

# THE SPLIT — one call, four piles back:
#   X_train / y_train = the STUDY SET (80% — the model learns here)
#   X_test  / y_test  = the EXAM SET  (20% — locked away, unseen)
# test_size=0.2 means 20% becomes the exam.
# random_state=42 is a fixed shuffle "seed": run this file a hundred
# times and you get the SAME split every time. Without it, the split
# changes on every run and nobody can reproduce your results.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Train set: {X_train.shape[0]} videos — the model studies these")
print(f"Test set:  {X_test.shape[0]} videos — locked away for the exam")
print("\nThe exam questions (the model has NEVER seen these rows):")
print(X_test)
print("\nThe exam answers (we check the model's guesses against these):")
print(y_test)

print("\nDone — 16 to study, 4 for the exam. That is an honest test.")
