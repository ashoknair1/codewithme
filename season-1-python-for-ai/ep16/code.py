"""Pass or Fail? Build Your First Classifier - Portfolio project #16."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# 24 students: study hours, attendance percent, and did they pass (1/0)?
students = pd.DataFrame({
    "study_hours": [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7,
                    7, 8, 8, 9, 9, 10, 11, 12, 1.5, 3.5, 6.5, 9.5],
    "attendance": [55, 60, 70, 58, 75, 65, 80, 70, 85, 75, 90, 68,
                   88, 82, 95, 78, 92, 85, 90, 98, 50, 62, 72, 88],
    "passed": [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
})

# FEATURES (X) = the questions. LABEL (y) = the category to predict.
X = students[["study_hours", "attendance"]]
y = students["passed"]
print(f"Examples: {len(students)} students")
print(f"Features (X): study_hours, attendance")
print(f"Label (y): passed (1 = pass, 0 = fail)")

# Honest split first (Episode 12): train on 18, test on 6 unseen.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)
print(f"Train: {len(X_train)} students, Test: {len(X_test)} students")

# Scale first (Episode 13): hours run 1-12, attendance 50-98.
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
print("Trained: scaler + logistic regression pipeline")

# Predict the categories for the 6 students the model never saw.
predictions = model.predict(X_test)
print("\nTest predictions vs reality:")
for (hours, att), real, guess in zip(X_test.values, y_test, predictions):
    print(f"  {hours}h, {att}%: predicted {'pass' if guess == 1 else 'fail'},"
          f" real {'pass' if real == 1 else 'fail'}")

# Honest score: how many categories did it get right?
acc = accuracy_score(y_test, predictions)
print(f"\nAccuracy: {acc:.3f} ({int(acc * len(y_test))}/{len(y_test)} correct)")
print("Confusion matrix (real rows x predicted cols):")
print(confusion_matrix(y_test, predictions))

# New student: 6 hours, 80 percent. predict needs a one-row table.
new_student = pd.DataFrame({"study_hours": [6], "attendance": [80]})
label = model.predict(new_student)[0]
proba = model.predict_proba(new_student)[0]
print(f"\nNew student (6h, 80%): {'PASS' if label == 1 else 'FAIL'}")
print(f"Confidence: fail {proba[0] * 100:.1f}%, pass {proba[1] * 100:.1f}%")

# A struggling student and a borderline student.
for name, row in [("Struggling (2h, 55%)", {"study_hours": [2], "attendance": [55]}),
                  ("Borderline (4h, 70%)", {"study_hours": [4], "attendance": [70]})]:
    s = pd.DataFrame(row)
    p = model.predict_proba(s)[0]
    print(f"{name}: {'PASS' if model.predict(s)[0] == 1 else 'FAIL'} "
          f"(pass probability {p[1] * 100:.1f}%)")
print("\nDone - your first classifier, trained and honestly tested.")
print("Limit: 100% on 6 tests is promising, not proof - never use a")
print("toy model for real decisions about real students.")
