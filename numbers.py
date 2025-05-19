# 1. Introduction to Python
# Python is a high-level, interpreted programming language.
# It is dynamically typed and garbage collected.
# Python supports multiple programming paradigms: procedural, object-oriented, functional.
# It is popular for ease of use, readability, and a large standard library.

# ------------------------
# 2. How Python Works Internally
# Python code is first compiled into bytecode.
# This bytecode runs on the Python Virtual Machine (PVM).
# The source code (.py) -> bytecode (.pyc) -> PVM executes the bytecode.
# This makes Python portable across platforms.

print("Hello, World!")  # Simple example of Python print statement

# ------------------------
# 3. Using Python in Shell (Interactive Mode)
# Python can be used interactively in the shell (REPL).
# You can execute statements line by line and see immediate output.
# Useful for testing and experimenting with code snippets.

a = 10
b = 20
print(a + b)

# ------------------------
# 4. Mutable vs Immutable Data Types
# Immutable types: values cannot be changed after creation.
# Examples: int, float, string, tuple
# Mutable types: values can be changed after creation.
# Examples: list, dict, set

x = 5
# x = 6  # Rebinding to new object, not modifying the existing one.

my_list = [1, 2, 3]
my_list[0] = 100  # Mutable change inside the list

# ------------------------
# 5. Python Data Types Overview
# Basic data types:
# int - integer numbers
# float - decimal numbers
# str - string of characters
# bool - True or False
# NoneType - special type representing 'no value'

num_int = 42
num_float = 3.1415
my_str = "Python is fun"
flag = True
nothing = None

# ------------------------
# 6. Variables and Assignment
# Variables are references to objects.
# No declaration needed.
# Assignment binds a name to an object.

x = 10
y = x  # y points to same object as x

# ------------------------
# 7. Basic Operations
# Arithmetic operators: +, -, *, /, %, ** (power), // (floor division)
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not

a = 7
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division (float)
print(a % b)   # Modulus (remainder)
print(a ** b)  # Power
print(a // b)  # Floor division

print(a == b)  # Equality check (False)
print(a != b)  # Not equal (True)
print(a > b)   # Greater than (True)

print((a > b) and (b > 0))  # Logical AND (True)
print(not(a < b))            # Logical NOT (True)

# ------------------------
# 8. Comments in Python
# Use # for single line comments.
# Use triple quotes ''' or """ for multi-line docstrings or comments.

# This is a comment
'''
This is a
multi-line comment
'''

# ------------------------
# 9. Printing Output
# Use print() to display output.
# Multiple items can be printed separated by commas or formatted with f-strings.

name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# Using f-string (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# ------------------------
# 10. Input from User
# Use input() to take input from user as string.
# Convert to needed type with int(), float(), etc.

user_input = input("Enter a number: ")
num = int(user_input)
print("You entered", num)

# ------------------------
# 11. Conditional Statements
# Use if, elif, else for decision making.

x = 10

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# ------------------------
# 12. Loops
# for loop: iterate over sequences or ranges
# while loop: repeats while condition is true

for i in range(5):
    print("Iteration", i)

count = 0
while count < 5:
    print("Count is", count)
    count += 1

# ------------------------
# 13. Functions
# Defined using def keyword.
# Can take arguments and return values.

def add(a, b):
    return a + b

result = add(3, 4)
print("Addition result:", result)

# Function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Bob")

# ------------------------
# 14. Lists
# Ordered, mutable collection of items.

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Access first element

fruits.append("date")  # Add element
print(fruits)

fruits.remove("banana")  # Remove element
print(fruits)

# ------------------------
# 15. Tuples
# Ordered, immutable collection.

point = (10, 20)
print(point[0])

# Single element tuple needs a comma
single_tuple = (5,)
print(single_tuple)

# ------------------------
# 16. Dictionaries
# Key-value pairs, unordered (Python 3.7+ maintains insertion order)

person = {"name": "Alice", "age": 25}
print(person["name"])

person["age"] = 26  # Update value
print(person)

person["city"] = "New York"  # Add new key-value
print(person)

# Loop through dictionary keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# ------------------------
# 17. Sets
# Unordered collection of unique items.

my_set = {1, 2, 3, 3, 2}
print(my_set)  # Output: {1, 2, 3}

my_set.add(4)
print(my_set)

my_set.remove(2)
print(my_set)

# ------------------------
# 18. Importing Modules
# Use import statement to include modules.

import math

print(math.sqrt(16))
print(math.pi)

# ------------------------
# 19. String Operations (added)
# Strings are immutable sequences of characters.
# Common operations: concatenation, repetition, slicing, methods.

s = "Hello"
t = "World"

print(s + " " + t)   # Concatenation
print(s * 3)         # Repetition

print(s[1:4])        # Slicing 'ell'
print(s.lower())     # lowercase 'hello'
print(t.upper())     # uppercase 'WORLD'
print(s.replace('l', 'L'))  # Replace 'l' with 'L'

# ------------------------
# 20. Error Handling (added)
# Use try-except blocks to handle exceptions.

try:
    x = int(input("Enter a number: "))
    print(f"You entered {x}")
except ValueError:
    print("That's not a valid number!")

# ------------------------
# 21. Python Indentation (added)
# Indentation is crucial in Python. It defines code blocks.
# Usually 4 spaces per indentation level.

if True:
    print("Indented block")
    if True:
        print("Nested block")

# ------------------------
# 22. Boolean Context (added)
# In conditions, Python evaluates objects' truthiness.
# None, 0, empty sequences ('' , [], ()) and empty dict/set are False.
# Others are True.

if []:
    print("This won't print")
else:
    print("Empty list is False")

if "non-empty":
    print("Non-empty string is True")

# ------------------------
# End of enhanced Python Basics Notes
