#!/usr/bin/env python3
"""Episode 3: Lists, Tuples & Dictionaries — the grocery list app.
Run it: python3 code.py
Every line below is explained in the episode."""
# A LIST: an ordered collection you can change.
# Think: a numbered shopping list on a piece of paper.
groceries = ["milk", "bread", "eggs", "spinach"]

print(groceries)

# Indexing starts at 0 — Python counts like a programmer, not a person.
print(groceries[0])    # milk  (first item)
print(groceries[-1])   # spinach (count backwards from the end!)

# Slicing: grab a chunk [start:stop] (stop is NOT included)
print(groceries[1:3])  # ['bread', 'eggs']

# Lists are editable: add and remove items
groceries.append("apples")   # add to the end
groceries.remove("bread")    # remove by value
print(len(groceries), "items on the list")  # len() = how many
print(groceries)

# A TUPLE: like a list, but LOCKED.
# Think: your home's GPS coordinates on a plaque — you don't edit them.
home = (17.45, 78.38)  # (latitude, longitude)
print(home[0])  # 17.45
# home[0] = 18.0  # <- TypeError! Tuples refuse to change.

# A DICTIONARY: pairs of label -> value, like a contact card.
# Think: labeled jars from Episode 2, all bundled in one box.
product = {
    "name": "milk",
    "price": 3.49,
    "in_stock": True,
}

print(product["name"])        # milk
product["price"] = 3.99       # update a value by its label
print(product)

# THE REAL WORLD: a LIST of DICTIONARIES.
# This is exactly what a shopping-cart API hands you (it's called JSON).
cart = [
    {"name": "milk", "price": 3.49},
    {"name": "bread", "price": 2.99},
    {"name": "eggs", "price": 4.25},
]

total = cart[0]["price"] + cart[1]["price"] + cart[2]["price"]
print(f"Cart total: ${total:.2f}")

# --- YOUR CHALLENGE (portfolio piece #3) ---
# grocery_list.py:
#   1. Make a list of 5 groceries
#   2. Append one more item
#   3. Remove one item
#   4. Print how many items are on the list, then the list itself
#   Bonus: make a dictionary for ONE product with name, price, in_stock
