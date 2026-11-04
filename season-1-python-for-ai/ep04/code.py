# episode 4 — loops & conditions: thinking like a program
# Beginner-clean: only uses ideas from episodes 1–4.
# Run it:  python3 loops.py

# --- our data from episode 3: a shopping cart (a list of dictionaries) ---
cart = [
    {"name": "milk",   "price": 3.49},
    {"name": "bread",  "price": 2.99},
    {"name": "eggs",   "price": 4.25},
    {"name": "coffee", "price": 8.99},
]

# --- 1. for loop: do the same thing for EVERY item ---
total = 0
for item in cart:
    total = total + item["price"]
print(f"Cart total: ${total:.2f}")

# --- 2. if / elif / else: make a decision ---
if total > 20:
    print("Over budget! Put something back.")
elif total == 20:
    print("Exactly $20 — perfect shopping!")
else:
    print("Under budget — well done!")

# --- 3. loop + condition together: decide about each item ---
for item in cart:
    if item["price"] > 4:
        print(item["name"], "is pricey")
    else:
        print(item["name"], "is a good deal")

# --- 4. while loop: repeat UNTIL the tank is empty ---
slices = 8
while slices > 0:
    print(f"Eating a slice... {slices - 1} left")
    slices = slices - 1
print("All gone!")
