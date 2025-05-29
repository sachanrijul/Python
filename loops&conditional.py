# ----------------------------------------
# CONDITIONALS IN PYTHON
# ----------------------------------------

# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# if-elif-else ladder
x = 0
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Nested if
x = 10
if x > 0:
    if x < 20:
        print("x is between 0 and 20")

# Ternary operator (Conditional Expression)
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)

# Logical operators in conditionals
x = 7
if x > 0 and x < 10:
    print("x is between 1 and 9")

if x < 0 or x > 5:
    print("x is either less than 0 or greater than 5")

if not (x == 5):
    print("x is not 5")

# ----------------------------------------
# LOOPS IN PYTHON
# ----------------------------------------

# WHILE LOOP
i = 1
while i <= 5:
    print(i)
    i += 1

# Infinite while loop example (Be cautious!)
# while True:
#     print("This will run forever")

# FOR LOOP
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for letter in "Python":
    print(letter)

# Using range() in for loop
for i in range(5):
    print(i)

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # prints 1, 3, 5, 7, 9

# ----------------------------------------
# NESTED LOOPS
# ----------------------------------------

# Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# Nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# ----------------------------------------
# LOOP CONTROL STATEMENTS
# ----------------------------------------

# break – terminates the loop
for i in range(1, 6):
    if i == 3:
        break
    print(i)  # prints 1, 2

# continue – skips the current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # prints 1, 2, 4, 5

# pass – does nothing, used as a placeholder
for i in range(1, 4):
    if i == 2:
        pass  # Do nothing for now
    print(i)

# ----------------------------------------
# ELSE WITH LOOPS
# ----------------------------------------

# else with while
i = 1
while i < 3:
    print(i)
    i += 1
else:
    print("Loop ended normally")

# else with for
for i in range(3):
    print(i)
else:
    print("For loop completed")

# else doesn't execute if loop is broken using break
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("Won't be printed due to break")

# ----------------------------------------
# COMPREHENSIONS USING LOOPS (Extra)
# ----------------------------------------

# List comprehension
squares = [x * x for x in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]

# With condition
even_squares = [x * x for x in range(6) if x % 2 == 0]
print(even_squares)  # [0, 4, 16]

# Dictionary comprehension
squares_dict = {x: x * x for x in range(4)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9}

# Set comprehension
unique_letters = {char for char in "hello"}
print(unique_letters)

# ----------------------------------------
# MATCH CASE STATEMENT (Python 3.10+)
# ----------------------------------------

# Similar to switch-case in other languages
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")

# ----------------------------------------
# Behind the Scenes of Loops in Python
# ----------------------------------------

# 🔁 Iteration and Loop mean the same thing
# Iteration = The act of repeating
# Loop = The structure used to perform iteration

# Python provides various Iteration Tools:
# 1. for loop
# 2. comprehensions (list, set, dict comprehension)
# 3. map, filter, etc.

# All these iteration tools work only on Iterables

# 📦 What are Iterables?
# These are objects you can loop over.
# Examples:
iterable_list = [1, 2, 3, 4]   # list
iterable_string = "hello"     # string
# File objects are also iterable (they return lines one by one)

# Python must check:
# Before using a loop, it checks if the object is iterable

# 🧠 Behind the Scenes (Internals of Loop Execution)

# Step 1:
# When you use a loop on an iterable object, Python internally calls the __iter__() method
it = iter(iterable_list)  # Same as iterable_list.__iter__()

# Step 2:
# This returns an iterator object, which supports the __next__() method

# Step 3:
# Python repeatedly calls the __next__() method to get values from the iterator

print(next(it))  # Output: 1
print(next(it))  # Output: 2
print(next(it))  # Output: 3
print(next(it))  # Output: 4

# Step 4:
# Once there are no more values, __next__() raises a StopIteration exception

# Uncomment below to see the exception:
# print(next(it))  # Raises StopIteration

# 🛑 This exception signals Python to stop the loop

# ----------------------------------------
# This is why Python’s for loop works automatically:
# It handles __iter__ and __next__ behind the scenes

# Example:
for val in iterable_list:
    print(val)

# Internally this performs:
# 1. Creating an iterator using __iter__()
# 2. Fetching next item using __next__()
# 3. Ending the loop when StopIteration is raised

# ✅ Practical Understanding:
# Every time you use a for loop,
# Python internally creates an iterator using __iter__()
# and fetches items using __next__()

# ✅ Files are also iterable:
# When you open a file and use a loop, it reads line-by-line

# Example:
# with open("example.txt") as file:
#     for line in file:
#         print(line)

# ----------------------------------------
# The 3 main components behind loops:
# 1. Iterable Object (like list, file, string)
# 2. Iterator (which provides __next__())
# 3. Iteration Tool (like for loop, map, comprehensions)

# These three work together to perform looping in Python

# ✅ Bonus Concept:
# You can call next() in two ways:
# Either using next() or using __next__()
it = iter([10, 20, 30])
print(it.__next__())  # Output: 10
print(next(it))       # Output: 20

# ------------------- Membership Operators in Python (Full Notes) -------------------

"""
Membership operators are used to test whether a value is a member of a sequence or collection.

There are only two:
1. `in`     → Returns True if the element is found
2. `not in` → Returns True if the element is NOT found

These operators work with:
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
- Ranges
- Any iterable that implements __contains__() or __iter__() with comparison
"""

# ---------- Behind the Scenes ----------

# The expression: `x in collection` actually calls:
# - collection.__contains__(x)
# If __contains__ is not defined, Python falls back to:
# - iterating over the object using __iter__() and comparing items using ==

# ---------- 1. Strings ----------

text = "hello world"

# Check if substring exists
print("hello" in text)       # True → 'hello' is a substring
print("world" in text)       # True
print("hi" in text)          # False
print("h" in text)           # True → 'h' is a character in the string
print(" " in text)           # True → space exists

# Case sensitivity
print("Hello" in text)       # False → 'H' ≠ 'h'

# Membership with `not in`
print("z" not in text)       # True

# Behind the scenes: text.__contains__('hello')

# ---------- 2. Lists ----------

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)    # True
print("grape" in fruits)     # False
print("banana" not in fruits)  # False

# Works with numbers too
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)          # True
print(10 not in numbers)     # True

# Membership is checked using == comparison:
print(3.0 in numbers)        # True → 3 == 3.0 is True
print("3" in numbers)        # False → string "3" is not equal to integer 3

# ---------- 3. Tuples ----------

colors = ("red", "green", "blue")
print("green" in colors)     # True
print("yellow" in colors)    # False

# Tuple is immutable, but membership check is allowed

# ---------- 4. Sets ----------

my_set = {10, 20, 30}
print(20 in my_set)          # True
print(25 not in my_set)      # True

# Very fast! Set lookup is O(1) due to hashing
# Uses __contains__() with hash lookup instead of linear search

# Example of fast set lookup:
large_list = list(range(1000000))
large_set = set(large_list)

import time

start = time.time()
print(999999 in large_list)   # Slower
print("Time (list):", time.time() - start)

start = time.time()
print(999999 in large_set)    # Faster
print("Time (set):", time.time() - start)

# ---------- 5. Dictionaries ----------

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Membership works only with keys
print("name" in person)       # True
print("Alice" in person)      # False (Alice is a value, not a key)
print("Alice" in person.values())  # True

# You can check keys, values, or key-value pairs:
print("age" in person.keys())      # True
print(25 in person.values())       # True
print(("age", 25) in person.items())  # True

# ---------- 6. Ranges ----------

print(5 in range(10))         # True (range(0,10) includes 5)
print(10 in range(10))        # False

# Range is memory-efficient and checks using arithmetic, not iteration

# ---------- 7. Nested Structures ----------

matrix = [[1, 2], [3, 4], [5, 6]]

print([1, 2] in matrix)       # True → entire list [1, 2] is an element
print(2 in matrix)            # False → 2 is inside a sublist, not top-level

# For deeper checks, you may use nested loops or flatten the structure

# ---------- 8. Membership with Custom Objects ----------

class Person:
    def __init__(self, name):
        self.name = name

people = [Person("Alice"), Person("Bob")]

# Direct membership check won’t work without custom __eq__
print(Person("Alice") in people)  # False → different memory, not equal

# To make this work, we override __eq__
class Person2:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name

group = [Person2("Alice"), Person2("Bob")]
print(Person2("Alice") in group)  # True → __eq__ returns True

# ---------- Use in Control Structures ----------

word = "python"
if "t" in word:
    print("The letter 't' is present.")  # Output

if "z" not in word:
    print("The letter 'z' is not present.")  # Output

# ---------- Notes ----------

"""
✔ Works with all iterable types
✔ Case-sensitive for strings
✔ For dictionaries, checks keys by default
✔ Set membership is the fastest due to hashing
✔ Behind the scenes: __contains__ or iteration
✔ Can be used in conditions, loops, filters, comprehensions, etc.
✔ Custom object behavior depends on __eq__ method
"""

# ---------- End of Membership Operator Notes ----------
