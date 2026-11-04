"""Video Database — Episode 10: SQL basics in Python with sqlite3.

Portfolio project #10: save this file, run it, put it on GitHub.

Yesterday we cleaned a messy dataset. Today we put that clean data into a
real database and ask it questions with SQL — SELECT, WHERE, ORDER BY,
GROUP BY — the language in 22.7% of ML job postings (Huntr 2026).
sqlite3 is built into Python: nothing to install.
"""

import sqlite3

# Our clean video data from Episode 9 (title, category, views, likes).
videos = [
    ("Python Tutorial for Beginners", "education", 512000, 18400),
    ("LoFi Beats to Study To", "music", 891000, 45200),
    ("10-Minute Pasta Recipe", "cooking", 634000, 18000),
    ("Travel Vlog: Tokyo on a Budget", "travel", 485000, 9200),
    ("Home Workout No Equipment", "fitness", 287000, 11900),
    ("Data Analyst Salary Breakdown", "education", 695000, 23800),
    ("Street Food Tour: Bangkok", "unknown", 458000, 17600),
    ("Guitar Lesson: 4 Easy Chords", "music", 485000, 21400),
    ("Morning Yoga for Beginners", "fitness", 176000, 18000),
]

# STEP 1 — Connect. This creates the database file if it does not exist.
conn = sqlite3.connect("videos.db")
cursor = conn.cursor()  # the cursor runs our SQL commands

# STEP 2 — Create the table (start fresh each run so the demo is repeatable).
cursor.execute("DROP TABLE IF EXISTS videos")
cursor.execute("""
    CREATE TABLE videos (
        title TEXT,
        category TEXT,
        views INTEGER,
        likes INTEGER
    )
""")

# STEP 3 — Insert all rows at once, then COMMIT.
# Forget commit and your data quietly vanishes when the program ends.
cursor.executemany("INSERT INTO videos VALUES (?, ?, ?, ?)", videos)
conn.commit()
print("Saved", len(videos), "videos to the database")

# QUESTION 1 — What are our top 3 videos by views?
print("\nTop 3 videos by views:")
for title, views in cursor.execute("""
        SELECT title, views FROM videos
        ORDER BY views DESC
        LIMIT 3
        """):
    print(f"  {title}: {views:,} views")

# QUESTION 2 — Which videos passed 500,000 views?
print("\nVideos over 500,000 views:")
for (title,) in cursor.execute("""
        SELECT title FROM videos
        WHERE views > 500000
        """):
    print(" ", title)

# QUESTION 3 — Which category averages the most views?
print("\nAverage views by category:")
for category, count, avg_views in cursor.execute("""
        SELECT category, COUNT(*), AVG(views) FROM videos
        GROUP BY category
        ORDER BY AVG(views) DESC
        """):
    print(f"  {category}: {count} videos, {avg_views:,.0f} average views")

conn.close()
print("\nDone — ask your data anything.")
