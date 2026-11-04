"""Decision Trees & Random Forests - Portfolio project #18."""

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 72 customers: tenure, bill, calls, late payments, left? (1/0)
customers = pd.DataFrame({
    "tenure_months": [2,3,4,5,6,8,9,11,13,15,18,20,24,28,32,36,40,44,48,54,1,7,12,22,30,42,3,16,26,50,2,5,10,14,19,25,31,38,45,52,4,8,17,21,27,33,39,46,6,10,15,23,29,35,41,47,53,3,9,20,7,18,35,5,44,12,28,3,50,16,9,26],
    "monthly_charges": [95,89,99,85,92,78,88,72,80,65,70,60,68,55,62,50,58,45,52,40,105,82,75,66,59,48,98,71,63,44,92,90,84,77,69,61,57,49,47,42,97,86,74,67,60,54,51,46,93,81,73,64,58,53,50,44,41,96,87,68,70,95,88,55,90,60,92,60,85,98,66,78],
    "support_calls": [5,4,6,3,4,2,3,1,2,1,1,0,1,0,1,0,0,0,1,0,6,3,2,1,0,0,5,2,1,0,5,4,2,2,1,1,0,0,0,0,6,3,2,1,1,0,0,0,4,3,2,1,0,1,0,0,0,5,3,1,1,4,5,0,3,0,4,1,2,5,0,2],
    "late_payments": [3,2,4,2,3,1,2,1,1,0,1,0,0,0,1,0,0,0,0,0,4,2,1,1,0,0,3,1,0,0,3,2,1,1,0,0,0,0,0,0,4,2,1,1,0,0,0,0,2,2,1,0,0,0,0,0,0,3,2,1,0,3,2,0,2,0,3,0,1,4,0,1],
    "churned": [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,0,0],
})
X = customers[["tenure_months", "monthly_charges", "support_calls", "late_payments"]]
y = customers["churned"]
print(f"Examples: {len(customers)} customers, {int(y.sum())} churned")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
print(f"Train: {len(X_train)}, Test: {len(X_test)} ({int(y_test.sum())} churners in test)")

# One readable tree: depth capped at 3 so a human can draw it.
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)
print("\nThe tree, as plain rules:")
print(export_text(tree, feature_names=list(X.columns)))
acc = accuracy_score(y_test, tree.predict(X_test))
print(f"Tree accuracy: {acc:.3f} ({int(acc * len(y_test))}/{len(y_test)})")

# Overfitting trap: no depth limit = the tree memorizes.
deep = DecisionTreeClassifier(random_state=42)
deep.fit(X_train, y_train)
print(f"\nUnlimited tree - train: {accuracy_score(y_train, deep.predict(X_train)):.3f}, "
      f"test: {accuracy_score(y_test, deep.predict(X_test)):.3f}")

# Forest: 100 trees, shuffled copies, majority vote wins.
forest = RandomForestClassifier(n_estimators=100, random_state=42)
forest.fit(X_train, y_train)
acc = accuracy_score(y_test, forest.predict(X_test))
print(f"\nForest accuracy: {acc:.3f} ({int(acc * len(y_test))}/{len(y_test)})")
print("Feature importances (what the forest leaned on):")
for name, imp in sorted(zip(X.columns, forest.feature_importances_),
                        key=lambda p: -p[1]):
    print(f"  {name}: {imp:.2f}")

# One small test misleads - judge all three over 5 folds.
cv = StratifiedKFold(5, shuffle=True, random_state=42)
models = [("Tree (depth 3)", DecisionTreeClassifier(max_depth=3, random_state=42)), ("Tree (unlimited)", DecisionTreeClassifier(random_state=42)), ("Forest (100 trees)", RandomForestClassifier(n_estimators=100, random_state=42))]
for label, m in models:
    print(f"5-fold CV {label}: {cross_val_score(m, X, y, cv=cv).mean():.3f}")

def check(name, tenure, bill, calls, late):
    row = pd.DataFrame({"tenure_months": [tenure],"monthly_charges": [bill],
                        "support_calls": [calls],"late_payments": [late]})
    t = "CHURN" if tree.predict(row)[0] == 1 else "STAY"
    f = "CHURN" if forest.predict(row)[0] == 1 else "STAY"
    print(f"{name}: tree says {t}, forest says {f}")

check("At-risk (2mo, $95, 5 calls, 3 late)", 2, 95, 5, 3)
check("Loyal (48mo, $52, 0 calls, 0 late)", 48, 52, 0, 0)
print("\nDone - one tree you can draw, one forest that votes.")
