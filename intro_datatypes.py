# 🧠 How does Python actually work behind the scenes?

# 1. Python is an interpreted language.
#    - Python code is not directly converted into machine code.
#    - Instead, it is interpreted and executed by the Python interpreter.

# 2. CPython is the most widely used implementation of Python.
#    - CPython is written in C.
#    - It converts Python code into bytecode (.pyc files).
#    - This bytecode is then run by the Python Virtual Machine (PVM).

# 3. Python Execution Flow:
#    Step 1: .py (source code)
#    Step 2: Compilation to bytecode (.pyc)
#    Step 3: Execution by Python Virtual Machine (PVM)

# 4. Role of the Interpreter:
#    - Reads code line by line
#    - Converts to intermediate bytecode
#    - Executes using the PVM

# 5. Memory Management in Python:
#    - Python automatically handles memory using a Garbage Collector.
#    - It uses reference counting + cyclic garbage collection.
#    - Every object has a reference count.
#    - When the reference count drops to 0, memory is deallocated.

# 6. Dynamic Typing:
#    - You don’t need to declare a variable’s type.
#    - Type is decided at runtime.

# Example: Understanding dynamic typing
x = 10        # int
x = "hello"   # now x is a str
x = [1, 2, 3] # now x is a list

# 7. Namespace and Scope:
#    - Every variable resides in a namespace.
#    - Python maintains a hierarchy: Local → Enclosing → Global → Built-in (LEGB Rule)

# Example: LEGB Rule in function scopes
def outer():
    x = "outer"
    
    def inner():
        x = "inner"
        print(x)  # 'inner' from local scope

    inner()
    print(x)      # 'outer' from enclosing scope

outer()

# 8. Objects Everywhere:
#    - Everything in Python is an object (even functions and classes).

# Example: Functions are objects
def greet():
    print("Hello!")

greet.lang = "English"  # assigning attribute to function
print(greet.lang)

# 9. Compilation vs Interpretation in Python:
#    - Compilation to bytecode makes execution faster.
#    - But final execution is still interpreted by the PVM.

# Final Note:
# - Python is beginner-friendly due to its simple syntax and internal architecture.
# - Understanding inner workings helps in writing optimized and bug-free code.
#-----------------------------------------------------------------------------

# 🐚 What is the Python Shell?

# 1. Python Shell (REPL):
#    - REPL stands for: Read – Evaluate – Print – Loop
#    - It’s an interactive environment to test small Python snippets.

# 2. Ways to open the Python shell:
#    - Open terminal/command prompt → type `python` or `python3`
#    - For Windows users: Python must be added to PATH during installation
#    - Once inside, you see >>> prompt for typing code

# Example: Simple operations in Python Shell
print("Hello from shell!")
5 + 3
"Python".upper()

# 3. Features of the Python Shell:
#    - Immediate feedback (good for learning/testing)
#    - No need to create a separate file
#    - Supports variables, functions, loops, etc.

# Example: Using a variable in shell
name = "Alice"
print(name)

# 4. Using Shell for quick math
2 ** 10         # Exponentiation
round(3.14159, 2)

# 5. Limitations of Python Shell:
#    - Temporary workspace (no code is saved unless copied)
#    - Not suitable for long scripts or structured programs

# 6. Alternatives to basic shell:
#    - IPython: Advanced shell with more features
#    - Jupyter Notebook: GUI-based, ideal for data science
#    - Python IDEs: Offer script-based coding (VS Code, PyCharm, etc.)

# 7. Exiting the Python Shell:
#    - Type `exit()` or press Ctrl+Z (Windows) / Ctrl+D (Linux/Mac)

# Summary:
# - Python shell is great for quick experimentation.
# - It's an excellent tool for beginners to get comfortable with the language.
#-----------------------------------------------------------------------------

# 🔁 What is "mutable" and "immutable" in Python?

# 1. Definition:
#    - Mutable: Objects that can be changed after creation.
#    - Immutable: Objects that cannot be changed after creation.

# 2. Why does it matter?
#    - It affects how variables behave when passed to functions.
#    - Helps avoid unintended bugs in your code.

# 3. Immutable Data Types in Python:
#    - int, float, bool, str, tuple, frozenset

# Example: Immutable behavior with strings
name = "Alice"
print(id(name))   # memory location before

name = "Bob"
print(id(name))   # new memory location → changed

# Example: Immutable behavior with integers
x = 5
print(id(x))      # e.g., 140703460204112
x = x + 1
print(id(x))      # new memory address

# 4. Mutable Data Types in Python:
#    - list, dict, set, bytearray

# Example: Mutable behavior with lists
numbers = [1, 2, 3]
print(id(numbers))  # memory location before

numbers.append(4)
print(numbers)
print(id(numbers))  # same memory location → object changed in-place

# 5. Mutability inside Immutable types:
#    - Tuples are immutable, but can contain mutable objects

# Example: Mutable inside immutable
t = (1, 2, [3, 4])
print(t)
t[2].append(5)   # allowed because list inside tuple is mutable
print(t)

# 6. Function Behavior:
#    - Mutable objects can be changed inside functions
#    - Immutable objects cannot (new copy is created)

# Example: Function with immutable type
def modify_immutable(x):
    x += 1
    print("Inside function:", x)

a = 10
modify_immutable(a)
print("Outside function:", a)  # unchanged

# Example: Function with mutable type
def modify_mutable(lst):
    lst.append(99)
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_mutable(my_list)
print("Outside function:", my_list)  # changed

# Summary:
# - Use mutable types when you want to modify objects in place.
# - Use immutable types for safety and simplicity (e.g., keys in dicts).
#-----------------------------------------------------------------------

# 📦 What is a Data Type?
# - Data types define what kind of value a variable can hold.
# - Python is dynamically typed → No need to declare data type explicitly.

# ----------------------------------------
# 🔢 1. Numeric Types
# ----------------------------------------
# int: Integer values (positive or negative, no decimal)
x = 10
y = -5

# float: Decimal or floating-point values
pi = 3.14

# complex: Complex numbers with real and imaginary parts
z = 2 + 3j
print(z.real)  # 2.0
print(z.imag)  # 3.0

# ----------------------------------------
# 🔤 2. Text Type
# ----------------------------------------
# str: Sequence of Unicode characters
name = "Python"
print(name.upper())

# ----------------------------------------
# 📋 3. Sequence Types
# ----------------------------------------
# list: Mutable sequence of items
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")

# tuple: Immutable sequence of items
colors = ("red", "green", "blue")

# range: Immutable sequence of numbers
r = range(1, 5)
print(list(r))  # [1, 2, 3, 4]

# ----------------------------------------
# 🔑 4. Mapping Type
# ----------------------------------------
# dict: Key-value pairs (unordered, mutable)
student = {"name": "Alice", "age": 20}
student["grade"] = "A"

# ----------------------------------------
# 📦 5. Set Types
# ----------------------------------------
# set: Unordered, unique values (mutable)
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}

# frozenset: Immutable version of set
fs = frozenset([1, 2, 2, 3])
print(fs)

# ----------------------------------------
# ✅ 6. Boolean Type
# ----------------------------------------
# bool: True or False values
is_active = True
print(5 > 3)  # True

# ----------------------------------------
# 💾 7. Binary Types
# ----------------------------------------
# bytes, bytearray, memoryview (used for binary data)
b = bytes(3)
ba = bytearray([1, 2, 3])
mv = memoryview(b)

# ----------------------------------------
# 🧪 Type Checking and Conversion
# ----------------------------------------
# Check type of variable
print(type(name))   # <class 'str'>

# Convert one type to another
num = "123"
num_int = int(num)

# ----------------------------------------
# 🧠 Summary
# ----------------------------------------
# - Python has various built-in types categorized into numeric, sequence, mapping, set, boolean, and binary.

# Understanding data types helps in writing efficient and bug-free code.
# Use type() to inspect and int(), str(), etc. to convert.