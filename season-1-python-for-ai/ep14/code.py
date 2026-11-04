"""What Is Machine Learning? — Episode 14: Types of ML, where the jobs are.

Portfolio project #14: save this file, run it, put it on GitHub.

For two weeks we prepared data honestly: cleaned it, charted it,
split it, scaled it, encoded it. Today we name what all of that was
for. Machine learning means the computer finds the pattern in
examples instead of following rules a person wrote by hand.
"""

import pandas as pd

# Our running dataset: the same 20 videos, now model-ready (Ep13).
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

# FEATURES = the questions the model may look at (columns in X).
# LABEL    = the answer we want it to learn to predict (y).
features = ["duration_min", "prev_views", "category"]
label = "views"
X = videos[features]
y = videos[label]
print(f"Features (X): {features}")
print(f"Label (y):    {label}")
print(f"Examples:     {len(videos)} videos")

# A pattern nobody wrote a rule for: average views per category.
# No if-statement told us this — the data itself shows it.
print("\nAverage views by category (a pattern in the data):")
print(videos.groupby("category")["views"].mean().round(0))

# THE THREE TYPES OF ML — tell them apart by the training signal.
# labels + a number to predict    — supervised regression
# labels + a category to predict  — supervised classification
# no labels, just structure       — unsupervised (clustering)
# rewards for actions taken       — reinforcement learning
def ml_type(signal):
    if signal == "labels_number":
        return "Supervised — regression (predict a number)"
    if signal == "labels_category":
        return "Supervised — classification (predict a category)"
    if signal == "no_labels":
        return "Unsupervised — clustering (find groups)"
    if signal == "rewards":
        return "Reinforcement — learn by trial and reward"
    return "Unknown signal"

tasks = [
    ("Predict views for a new video", "labels_number"),
    ("Predict tutorial, vlog or review", "labels_category"),
    ("Group viewers into segments, no answers given", "no_labels"),
    ("Teach a game agent with points for good moves", "rewards"),
]

print("\nSorting real tasks into ML types:")
for name, signal in tasks:
    print(f"  {name} — {ml_type(signal)}")

print("\nDone — every ML job posting is one of these three stories.")
