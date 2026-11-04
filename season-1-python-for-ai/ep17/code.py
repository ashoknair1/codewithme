"""Predict Customer Churn with Logistic Regression - Portfolio project #17."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# 30 customers: months stayed, monthly bill, support calls, left? (1/0)
customers = pd.DataFrame({
    "tenure_months": [2, 3, 4, 5, 6, 8, 9, 11, 13, 15, 18, 20, 24, 28, 32,
                      36, 40, 44, 48, 54, 1, 7, 12, 22, 30, 42, 3, 16, 26, 50],
    "monthly_charges": [95, 89, 99, 85, 92, 78, 88, 72, 80, 65, 70, 60, 68, 55,
                        62, 50, 58, 45, 52, 40, 105, 82, 75, 66, 59, 48, 98, 71, 63, 44],
    "support_calls": [5, 4, 6, 3, 4, 2, 3, 1, 2, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
                      6, 3, 2, 1, 0, 0, 5, 2, 1, 0],
    "churned": [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
})

# X = the evidence. y = churned (1 = left, 0 = stayed).
X = customers[["tenure_months", "monthly_charges", "support_calls"]]
y = customers["churned"]
print(f"Examples: {len(customers)} customers, {int(y.sum())} churned")

# Stratify: without it, random_state=42 puts ZERO churners in the test set.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
print(f"Train: {len(X_train)}, Test: {len(X_test)} ({int(y_test.sum())} churners in test)")

# Scale first (Ep 13), then logistic regression learns the weights.
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
print("Trained: scaler + logistic regression pipeline")

# Coefficients on the SCALED features:
lr = model.named_steps["logisticregression"]
for name, coef in zip(X.columns, lr.coef_[0]):
    print(f"  weight {name}: {coef:+.2f}")
print(f"  intercept: {lr.intercept_[0]:+.2f}")

# Predict the 8 customers the model never saw.
predictions = model.predict(X_test)
print("\nTest predictions vs reality:")
for (ten, bill, calls), real, guess in zip(X_test.values, y_test, predictions):
    print(f"  {ten}mo, ${bill}, {calls} calls: predicted {'churn' if guess == 1 else 'stay'}, real {'churn' if real == 1 else 'stay'}")

acc = accuracy_score(y_test, predictions)
print(f"\nAccuracy: {acc:.3f} ({int(acc * len(y_test))}/{len(y_test)} correct)")
print("Confusion matrix (real rows x predicted cols):")
print(confusion_matrix(y_test, predictions))

# New customers: label + probability.
def check(name, tenure, bill, calls):
    row = pd.DataFrame({"tenure_months": [tenure],
                        "monthly_charges": [bill],
                        "support_calls": [calls]})
    proba = model.predict_proba(row)[0]
    print(f"{name}: {'CHURN' if model.predict(row)[0] == 1 else 'STAY'} "
          f"(churn probability {proba[1] * 100:.1f}%)")

check("At-risk (2mo, $95, 5 calls)", 2, 95, 5)
check("Borderline (9mo, $88, 3 calls)", 9, 88, 3)
check("Loyal (48mo, $52, 0 calls)", 48, 52, 0)
print("\nDone - a churn predictor that explains itself.")
print("Limit: 8/8 on 8 tests is promising, not proof - a toy")
print("model never decides a real customer's offer alone.")
