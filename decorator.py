# -----------------------
# 1. What is a Decorator?
# -----------------------
# A decorator is a function that takes another function as input,
# wraps it with extra functionality, and returns the modified function.

def simple_decorator(func):  # A decorator function
    def wrapper():  # The wrapper adds functionality
        print("Before the function is called.")
        func()  # Call the original function
        print("After the function is called.")
    return wrapper  # Return the wrapped version

@simple_decorator  # Using the decorator on the greet function
def greet():
    print("Hello, world!")

greet()
# Output:
# Before the function is called.
# Hello, world!
# After the function is called.


# -----------------------------------------
# 2. Decorators Without Using @ Syntax
# -----------------------------------------
# Instead of using @ syntax, you can manually assign the decorated function.

def greet2():
    print("Hi there!")

decorated_greet = simple_decorator(greet2)  # Manually applying the decorator
decorated_greet()
# Output:
# Before the function is called.
# Hi there!
# After the function is called.


# --------------------------
# 3. Decorator with Arguments
# --------------------------
# This decorator can accept any number of arguments for the wrapped function.

def decorator_with_args(func):
    def wrapper(*args, **kwargs):  # Accept any arguments
        print(f"Arguments were: {args}, {kwargs}")
        return func(*args, **kwargs)  # Pass arguments to the original function
    return wrapper

@decorator_with_args
def add(a, b):  # Function that takes two arguments
    return a + b

print(add(5, 3))
# Output:
# Arguments were: (5, 3), {}
# 8


# -----------------------------
# 4. Multiple Decorators (Stacking)
# -----------------------------
# You can stack multiple decorators; the bottom one is applied first.

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1  # Applied last
@decorator2  # Applied first
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Decorator 1
# Decorator 2
# Hello!


# ----------------------------------
# 5. Returning Values from Decorators
# ----------------------------------
# You can also return values from decorated functions.

def square_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2  # Square the result before returning
    return wrapper

@square_result
def get_number():
    return 5

print(get_number())  # Output: 25


# -----------------------------------
# 6. Preserving Metadata with functools.wraps
# -----------------------------------
# Decorators usually hide the original function's name and docstring.
# Use functools.wraps to preserve them.

import functools

def logging_decorator(func):
    @functools.wraps(func)  # Preserve metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logging_decorator
def example():
    """This is an example function."""
    print("Running example.")

example()
print(example.__name__)  # Output: example
print(example.__doc__)   # Output: This is an example function.


# -------------------------------------
# 7. Class-based Decorators
# -------------------------------------
# Decorators can also be implemented using classes with __call__ method.

class ClassDecorator:
    def __init__(self, func):
        self.func = func  # Store the original function

    def __call__(self, *args, **kwargs):
        print("Class-based decorator before function call.")
        result = self.func(*args, **kwargs)  # Call the function
        print("Class-based decorator after function call.")
        return result

@ClassDecorator
def say_hi():
    print("Hi!")

say_hi()
# Output:
# Class-based decorator before function call.
# Hi!
# Class-based decorator after function call.


# --------------------------------------
# 8. Parameterized Decorator (Decorator Factory)
# --------------------------------------
# A decorator that accepts arguments (like repeat count).

def repeat(n):  # This is a decorator factory
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):  # Repeat n times
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  # Repeat the function 3 times
def welcome():
    print("Welcome!")

welcome()
# Output: Welcome! (3 times)


# ---------------------------
# 9. Using Decorators in Real Use Cases
# ---------------------------
# Example: Timer decorator to measure execution time.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Start timer
        val = func(*args, **kwargs)
        end = time.time()  # End timer
        print(f"Time taken: {end - start:.5f} seconds")
        return val
    return wrapper

@timer
def long_task():
    time.sleep(1)  # Simulate delay
    print("Task done!")

long_task()
# Output: Time taken: ~1 second


# ---------------------------
# 10. Chaining Decorators with Arguments
# ---------------------------
# You can also chain decorators for HTML formatting, for example.

def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"  # Wrap output in <b> tags
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"  # Wrap output in <i> tags
    return wrapper

@bold
@italic
def formatted_text():
    return "Hello"

print(formatted_text())  # Output: <b><i>Hello</i></b>
