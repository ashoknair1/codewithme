"""Gradebook Analyzer — Episode 7: Pandas basics, DataFrames.

Portfolio project #7: save as gradebook.py, run it, put it on GitHub.

A DataFrame is a programmable spreadsheet: rows of students, columns of data.
Five questions, about five lines of pandas.
"""

import pandas as pd

# Our class data: two plain Python lists. Pandas calls a table like this a DataFrame.
NAMES = ["Ava", "Ravi", "Mia", "Jon", "Zoe"]
SCORES = [92, 76, 88, 59, 95]
PASS_MARK = 60


def build_gradebook(names, scores):
    """Turn two lists into a pandas DataFrame (one dict, one call)."""
    gradebook = pd.DataFrame({"name": names, "score": scores})
    return gradebook


def analyze(gradebook):
    """Answer five questions about the class — about five lines of pandas."""
    # A Series is ONE column of the DataFrame. .mean() averages it.
    average = gradebook["score"].mean()

    # idxmax() gives the INDEX (row number) of the biggest score...
    topper_row = gradebook["score"].idxmax()
    topper = gradebook.loc[topper_row, "name"]
    topper_score = int(gradebook.loc[topper_row, "score"])

    # Boolean mask: ask every row "did you score 90 or more?" (episode 6 trick!)
    high_scorers = gradebook[gradebook["score"] >= 90]["name"].tolist()

    # Add a brand-new column: True for every score at or above 60.
    gradebook["passed"] = gradebook["score"] >= PASS_MARK
    pass_rate = gradebook["passed"].mean() * 100   # mean of True/False = share of True

    return {
        "average": round(average, 1),
        "topper": topper,
        "topper_score": topper_score,
        "high_scorers": high_scorers,
        "passed": gradebook[gradebook["passed"]]["name"].tolist(),
        "failed": gradebook[~gradebook["passed"]]["name"].tolist(),
        "pass_rate": round(pass_rate, 1),
    }


def print_report(report):
    """Print the five answers in a clean little report."""
    print(f"Class average : {report['average']}")
    print(f"Topper        : {report['topper']} ({report['topper_score']})")
    print(f"90+ club      : {', '.join(report['high_scorers'])}")
    print(f"Passed        : {', '.join(report['passed'])}")
    print(f"Failed        : {', '.join(report['failed'])}")
    print(f"Pass rate     : {report['pass_rate']}%")


if __name__ == "__main__":
    gradebook = build_gradebook(NAMES, SCORES)

    # The three hello commands for ANY dataset:
    print(gradebook.head())       # first 5 rows — a quick peek at the table
    gradebook.info()              # rows, columns, and column types (prints itself)
    print(gradebook.describe())  # instant stats: count, mean, min, max...

    print_report(analyze(gradebook))
