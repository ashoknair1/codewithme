"""Video Charts — Episode 11: Data visualization with Matplotlib.

Portfolio project #11: save this file, run it, put it on GitHub.

Yesterday SQL told us which video category averages the most views.
Today we make that answer VISIBLE: a bar chart anyone can read in
three seconds, plus a line chart for change over time.
Matplotlib is the classic Python chart library — nothing new to learn
about data, we are just drawing it.
"""

import matplotlib.pyplot as plt

# Our category averages from Episode 10's GROUP BY query (views).
categories = ["music", "cooking", "education", "travel", "unknown", "fitness"]
avg_views = [688000, 634000, 603500, 485000, 458000, 231500]

# CHART 1 — A bar chart COMPARES categories.
# Rule of thumb: comparing things = bars.
plt.figure(figsize=(9, 5))
plt.bar(categories, avg_views, color="#38bdf8")

# Labels are not decoration — without them the chart says nothing.
plt.title("Average views by video category")
plt.xlabel("Category")
plt.ylabel("Average views")
plt.ylim(0, 750000)  # honest axis: always start bars at zero

# Save it as a picture you can share anywhere (report, GitHub, slides).
plt.savefig("category_chart.png", dpi=150)
plt.close()
print("Saved category_chart.png — music wins, and now everyone can SEE it")

# CHART 2 — A line chart shows CHANGE OVER TIME.
# One week of views on a single video (a made-up but realistic week).
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
daily_views = [12400, 15800, 14900, 18200, 24500, 31200, 28700]

plt.figure(figsize=(9, 5))
plt.plot(days, daily_views, marker="o", color="#fb923c", linewidth=3)
plt.title("Views per day — one video, one week")
plt.xlabel("Day")
plt.ylabel("Views")
plt.grid(axis="y", alpha=0.3)  # light gridlines help the eye compare

plt.savefig("weekly_chart.png", dpi=150)
plt.close()
print("Saved weekly_chart.png — the weekend spike tells the story")

print("\nDone — numbers became a story.")
