"""Step Count Analyzer — Code with me EP 6 (Friday build challenge).

A tiny real app: feed it one week of daily step counts and it prints
a full fitness report. Uses Week 1 skills (variables, lists, functions,
loops, conditions) plus NumPy (arrays, vectorized math — no loops needed
for the math). Run it with:  python3 code.py
"""

import numpy as np

# --- sample data: one week of real-looking step counts, Mon -> Sun ---
WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]
STEPS = [8234, 10211, 5490, 12003, 9788, 3142, 8865]
DAILY_GOAL = 10000


def build_report(steps, week, goal):
    """Take a week's step counts, return a dict with every stat."""
    arr = np.array(steps)              # list -> NumPy array: math-ready
    total = arr.sum()                  # one line does the whole week
    average = arr.mean()
    best_idx = arr.argmax()            # position of the biggest day
    worst_idx = arr.argmin()
    above_goal = (arr >= goal).sum()   # boolean mask, then count True values
    report = {
        "total": int(total),
        "average": round(float(average)),
        "best_day": week[int(best_idx)],
        "best_steps": int(arr[int(best_idx)]),
        "worst_day": week[int(worst_idx)],
        "worst_steps": int(arr[int(worst_idx)]),
        "days_above_goal": int(above_goal),
    }
    return report


def verdict(report, goal):
    """A friendly one-line verdict based on the week's numbers."""
    if report["days_above_goal"] >= 5:
        return "Outstanding week — you crushed your goal five or more days!"
    if report["days_above_goal"] >= 3:
        return "Solid week! Three or more goal days. Keep it rolling."
    if report["average"] >= goal:
        return "Decent week — your average is at goal, push the low days up."
    return "Tough week. Your body is begging for one extra walk."


def print_report(report, goal):
    """Print the fitness report in a tidy, readable layout."""
    print("=" * 44)
    print("      STEP COUNT ANALYZER — WEEKLY REPORT")
    print("=" * 44)
    print(f"Total steps this week : {report['total']:,}")
    print(f"Daily average         : {report['average']:,}")
    print(f"Best day              : {report['best_day']} ({report['best_steps']:,} steps)")
    print(f"Worst day             : {report['worst_day']} ({report['worst_steps']:,} steps)")
    print(f"Days above {goal:,} goal : {report['days_above_goal']} of 7")
    print("-" * 44)
    print("Verdict:", verdict(report, goal))
    print("=" * 44)


if __name__ == "__main__":
    report = build_report(STEPS, WEEK, DAILY_GOAL)
    print_report(report, DAILY_GOAL)
