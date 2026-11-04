"""Evaluation Metrics in Python - Portfolio project #19."""

import random
from operator import gt, ge, lt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (confusion_matrix, accuracy_score,
                             precision_score, recall_score, f1_score,
                             classification_report)

# Build 300 customers. Risk rises with calls, late payments and
# charges, and falls with tenure. Noise flips a few labels, because
# real customers are never perfectly predictable.
rng = random.Random(42)
rows = []
for _ in range(300):
    tenure = rng.randint(1, 60)
    charges = rng.randint(35, 110)
    calls = rng.choice([0, 0, 0, 1, 1, 2, 2, 3, 4, 5])
    late = rng.choice([0, 0, 0, 1, 1, 2, 3])
    risk = calls * 1.0 + late * 0.9 + (charges - 40) / 30 - tenure / 25
    churn = 1 if gt(risk, 3.9) else 0
    flip = rng.random()
    if churn == 0 and lt(flip, 0.03):
        churn = 1
    elif churn == 1 and lt(flip, 0.12):
        churn = 0
    rows.append({"tenure_months": tenure, "monthly_charges": charges,
                 "support_calls": calls, "late_payments": late,
                 "churned": churn})
customers = pd.DataFrame(rows)
X = customers[["tenure_months", "monthly_charges",
               "support_calls", "late_payments"]]
y = customers["churned"]
print(f"Examples: {len(customers)} customers, {int(y.sum())} churned")

# Stratified split: the exam keeps the same churn mix (Ep 12/17).
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
print(f"Train: {len(X_train)}, Test: {len(X_test)} "
      f"({int((y_test == 0).sum())} stay, {int(y_test.sum())} churn)")


def judge(name, pred):
    tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
    print(f"\n{name}: TN={tn} FP={fp} FN={fn} TP={tp}")
    print(f"  accuracy {accuracy_score(y_test, pred):.3f}  "
          f"precision {precision_score(y_test, pred, zero_division=0):.3f}  "
          f"recall {recall_score(y_test, pred, zero_division=0):.3f}  "
          f"F1 {f1_score(y_test, pred, zero_division=0):.3f}")


# The lazy model: always predict the majority class (stay).
dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)
judge("Dummy (always stay)", dummy.predict(X_test))

# The real model: scaled logistic regression (Ep 17).
model = make_pipeline(StandardScaler(),
                      LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
pred = model.predict(X_test)
judge("Logistic regression", pred)
print("\nFull report:")
print(classification_report(y_test, pred,
                            target_names=["stay", "churn"],
                            zero_division=0))

# Lower the bar: flag anyone at 30 percent churn risk or more.
proba = model.predict_proba(X_test)[:, 1]
pred30 = [1 if ge(p, 0.3) else 0 for p in proba]
judge("Logistic regression, threshold 0.3", pred30)
print("\nDone - accuracy flatters; precision and recall tell the truth.")
