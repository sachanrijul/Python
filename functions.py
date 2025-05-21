# =============================================
# Comprehensive Python Functions Notes
# =============================================

# 1. Built-in Functions
# ---------------------
# Python comes with many built-in functions accessible without import.
# Examples:
print(len("Python"))       # Returns length: 6
print(type(123))           # Returns type: <class 'int'>
print(sum([1, 2, 3, 4]))   # Sums elements: 10

# These are implemented in C inside Python interpreter for speed.

# --------------------------------------------

# 2. User-Defined Functions
# -------------------------
# Functions you define using the `def` keyword.
# They consist of a name, parameters, and a body.
def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# When you call a function:
# - Python creates a new frame on the call stack
# - Assigns arguments to parameters
# - Executes the body
# - Returns the result or None if no return statement

# --------------------------------------------

# 3. Lambda (Anonymous) Functions
# -------------------------------
# Small anonymous functions using the `lambda` keyword.
# Syntax: lambda arguments: expression

square = lambda x: x * x
print(square(6))  # 36

# Useful for short throwaway functions.
# Common with higher-order functions like map, filter, reduce.

# Example with map:
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]

# --------------------------------------------

# 4. Recursive Functions
# ----------------------
# A function that calls itself to solve a problem by breaking it down.

def factorial(n):
    """Return factorial of n (n!)."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120

# Important to have a base case to avoid infinite recursion.
# Each recursive call adds a new frame to the call stack.

# --------------------------------------------

# 5. Higher-Order Functions
# -------------------------
# Functions that take other functions as arguments or return them.

def apply_func(func, value):
    """Apply function 'func' to 'value'."""
    return func(value)

def increment(x):
    return x + 1

print(apply_func(increment, 7))  # 8

# Higher-order functions enable functional programming paradigms.

# --------------------------------------------

# 6. Nested Functions and Closures
# --------------------------------
# Nested functions are defined inside other functions.

def outer_func(msg):
    def inner_func():
        print(msg)  # Accesses 'msg' from outer scope
    return inner_func

closure_func = outer_func("Hello from closure!")
closure_func()  # Prints: Hello from closure!

# The returned function 'closure_func' remembers 'msg' even after outer_func returns.
# This is called a closure — a function with preserved enclosing state.

# --------------------------------------------

# 7. Generator Functions
# ----------------------
# Functions that use `yield` to return an iterator which produces values lazily.

def countdown(n):
    """Count down from n to 1."""
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)
# Outputs: 5 4 3 2 1 (each on a new line)

# Generators save memory by producing items on demand.

# --------------------------------------------

# 8. Coroutine Functions
# ----------------------
# Similar to generators, but can also receive values with `.send()`.

def echo():
    while True:
        received = yield
        print("Received:", received)

co = echo()
next(co)            # Prime the coroutine to first yield
co.send("Hello!")   # Prints: Received: Hello!

# Coroutines are useful for asynchronous programming and cooperative multitasking.

# --------------------------------------------

# 9. Async Functions (Python 3.5+)
# --------------------------------
# Defined with `async def` and use `await` for asynchronous I/O.

import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    print("Start")
    await say_after(1, "Hello after 1 second")
    await say_after(2, "Hello after 2 seconds")
    print("End")

# To run async functions:
# asyncio.run(main())

# Async functions run in a single-threaded event loop, improving efficiency for IO-bound tasks.

# --------------------------------------------

# 10. Partial Functions
# ---------------------
# From functools, allow fixing some arguments of a function to create a new function.

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, y=2)
print(double(5))  # 10

# Partials are useful to simplify function calls or customize behavior.

# --------------------------------------------

# 11. Decorators (Function Wrappers)
# ----------------------------------
# Decorators modify or enhance functions without changing their source code.

def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Before the function call
# Hello!
# After the function call

# Decorators are often used for logging, access control, caching, etc.

# --------------------------------------------

# 12. Internal Memory Concepts
# ----------------------------
# - Each function call creates a frame on the call stack.
# - Variables inside a function live in that frame’s local namespace.
# - Python follows LEGB rule to resolve variables:
#    L - Local: Inside current function
#    E - Enclosing: Outer function scopes
#    G - Global: Module-level
#    B - Built-in: Python’s built-in names
# - Closures keep references to variables in enclosing scopes.
# - Function objects store code objects and metadata.
# - You can inspect bytecode with the dis module:

import dis

def add(x, y):
    return x + y

dis.dis(add)

# Bytecode is what Python interpreter executes.

# --------------------------------------------

# 13. Class Methods, Static Methods, Property Decorators
# ------------------------------------------------------

class ExampleClass:
    class_var = 42  # Class variable shared by all instances

    def __init__(self, value):
        self.instance_var = value  # Instance variable unique to each object

    # Class Method
    @classmethod
    def update_class_var(cls, new_value):
        """Modify class variable."""
        cls.class_var = new_value

    # Alternative Constructor using class method
    @classmethod
    def from_double(cls, value):
        """Create instance with double the value."""
        return cls(value * 2)

    # Static Method
    @staticmethod
    def multiply(x, y):
        """Utility function not dependent on class or instance."""
        return x * y

    # Property with getter, setter, deleter
    @property
    def value(self):
        print("Getting value")
        return self._value

    @value.setter
    def value(self, val):
        if val < 0:
            raise ValueError("Value cannot be negative")
        print("Setting value")
        self._value = val

    @value.deleter
    def value(self):
        print("Deleting value")
        del self._value

# Usage examples:

# Access and modify class variable
print(ExampleClass.class_var)   # 42
ExampleClass.update_class_var(100)
print(ExampleClass.class_var)   # 100

# Create instance normally
obj1 = ExampleClass(10)
print(obj1.instance_var)        # 10

# Create instance via alternative constructor
obj2 = ExampleClass.from_double(10)
print(obj2.instance_var)        # 20

# Call static method
print(ExampleClass.multiply(4, 5))  # 20

# Using property
obj1.value = 50          # Setting value
print(obj1.value)        # Getting value -> 50
del obj1.value           # Deleting value

# --------------------------------------------

# Summary of Class-related decorators:
# -----------------------------------
# @classmethod:
# - Takes class (cls) as first argument.
# - Can access and modify class state.
# - Often used for alternate constructors.

# @staticmethod:
# - Does not take instance or class reference.
# - Behaves like regular function but logically grouped inside class.
# - Useful for utility/helper functions.

# @property:
# - Turns method into attribute-like access.
# - Enables getter, setter, deleter control.
# - Provides encapsulation and validation.

# --------------------------------------------

# End of Comprehensive Python Functions Notes
# ===========================================
