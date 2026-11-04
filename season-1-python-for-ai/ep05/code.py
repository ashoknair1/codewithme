# episode 5 — functions: writing reusable, interview-ready code
# Beginner-clean: only uses ideas from episodes 1-5
# (setup, variables, lists/tuples/dicts, loops/conditions, and now functions).
# Run it:  python3 functions.py

# --- 1. your first function: a recipe card ---
def greet():
    print("Hello! Ready to cook some Python?")

greet()   # calling the function runs the recipe

# --- 2. parameters: blanks you fill in every time you call it ---
def tip_calculator(bill, percent):
    tip = bill * percent / 100
    total = bill + tip
    return total          # return HANDS the answer back to the caller

dinner = tip_calculator(50, 20)
print(f"Dinner total: ${dinner:.2f}")

coffee = tip_calculator(4.50, 15)
print(f"Coffee total: ${coffee:.2f}")

# one function, every bill, forever — that is the whole superpower.

# --- 3. the classic beginner bug: printing instead of returning ---
def bad_total(bill, percent):
    total = bill + percent / 100 * bill
    print(total)          # looks fine... but NOTHING comes back!

x = bad_total(50, 20)
print(f"x is: {x}")       # -> None. None means "nothing came back."

# --- 4. the fix: return instead of print ---
def good_total(bill, percent):
    total = bill + percent / 100 * bill
    return total          # one word changes everything

y = good_total(50, 20)
print(f"y is: {y}")       # -> 60.0. now we can USE the answer.

# --- 5. power move: reuse everything from episode 4 ---
# same cart, same loop, same decision — now wrapped in a function
def is_over_budget(cart, limit):
    total = 0
    for item in cart:
        total = total + item["price"]
    if total > limit:
        return True
    else:
        return False

cart = [
    {"name": "milk",   "price": 3.49},
    {"name": "bread",  "price": 2.99},
    {"name": "coffee", "price": 8.99},
]

if is_over_budget(cart, 20):
    print("Over budget! Put something back.")
else:
    print("Under budget — nice shopping!")

# reuse it with a different limit — zero extra code:
if is_over_budget(cart, 15):
    print("(and it is also over 15)")
