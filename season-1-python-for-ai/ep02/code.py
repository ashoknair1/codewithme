# Code with me - Episode 2: Variables & Data Types
# Run it by typing:  python variables.py

# A variable is a labeled jar. You put a value inside, you give the jar
# a name, and later you grab the value back by name. That's it.

# --- NUMBERS ---
# An int (integer) is a whole number — no decimal point.
age = 25
years_coding = 0

# A float is a number WITH a decimal point. Python needs the dot
# to know it's not a whole number.
price = 19.99
pi = 3.14159

# --- TEXT ---
# A str (string) is text. Always wrap it in quotes — " or ' both work.
name = "Maya"
city = "Austin"

# --- TRUE / FALSE ---
# A bool (boolean) is either True or False.
# Capital T, capital F — Python is picky about this.
is_student = True
has_drivers_license = False

# type() tells you what's inside the jar. Your detective magnifying glass.
print(type(age))            # <class 'int'>
print(type(price))          # <class 'float'>
print(type(name))           # <class 'str'>
print(type(is_student))     # <class 'bool'>

# --- USING VARIABLES ---
# f-strings: put an f before the quotes, drop variables inside {curly braces}.
print(f"Hi! I'm {name}. I'm {age} years old and I live in {city}.")

# Change a variable once at the top, and every calculation below updates.
total = price * 3
print(f"Three notebooks cost ${total:.2f}")  # :.2f just formats to 2 decimals

# --- THE MISTAKE EVERY BEGINNER MAKES ---
# Uncomment the next line to see the famous crash:
# print("I'm " + age + " years old")
# TypeError: can only concatenate str (not "int") to str
# The + sign glues TEXT to TEXT only. Use an f-string instead:
print(f"I'm {age} years old")  # works perfectly

# --- YOUR CHALLENGE: coffee shop calculator (portfolio project #2) ---
# Save this part as coffee_shop.py and run it!
shop = input("What's your shop's name? ")
cups = input("How many cups did you sell today? ")
# TRAP: input() ALWAYS gives you text — even "40" is a string in disguise.
# int() converts it into a real number:
cups = int(cups)
total_sales = cups * 2.50
print(f"{shop} sold {cups} cups today for a total of ${total_sales:.2f}!")
print("That's portfolio project #2. Two finished programs in two days!")
