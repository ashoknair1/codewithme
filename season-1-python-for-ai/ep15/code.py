"""Predict Salaries with Linear Regression - Portfolio project #15."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 20 people: years of experience and their salary in dollars.
people = pd.DataFrame({
    "years_experience": [0, 1, 1, 2, 2, 3, 3, 4, 5, 5,
                         6, 7, 7, 8, 9, 10, 11, 12, 13, 15],
    "salary": [34000, 39000, 36000, 48000, 44000, 53000, 50000,
               61000, 58000, 69000, 66000, 79000, 73000, 86000,
               82000, 98000, 94000, 112000, 106000, 128000],
})

# FEATURES (X) = the question. LABEL (y) = the answer.
X = people[["years_experience"]]
y = people["salary"]
print(f"Examples: {len(people)} people")
print(f"Feature (X): years_experience")
print(f"Label (y): salary")

# Honest split first (Episode 12): train on 15, test on 5 unseen.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)
print(f"Train: {len(X_train)} people, Test: {len(X_test)} people")

# Train: fit finds the best-fit line through the training points.
model = LinearRegression()
model.fit(X_train, y_train)
print(f"Slope: ${model.coef_[0]:,.2f} per extra year")
print(f"Intercept: ${model.intercept_:,.2f} at zero years")

# Predict on the 5 people the model never saw.
predictions = model.predict(X_test)
print("\nTest predictions vs reality:")
for years, real, guess in zip(X_test["years_experience"], y_test, predictions):
    print(f"  {years} years: predicted ${guess:,.0f}, real ${real:,}")

# Honest scores: average miss in dollars, and R-squared.
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"\nMean absolute error: ${mae:,.2f}")
print(f"R-squared: {r2:.3f}")

# Predict a brand-new person: 6 years of experience.
# Note: predict needs a table shape, not a bare number.
new_person = pd.DataFrame({"years_experience": [6]})
print(f"\nPrediction for 6 years: ${model.predict(new_person)[0]:,.0f}")
print("Done - your first real model, trained and honestly tested.")
