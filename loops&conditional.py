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
