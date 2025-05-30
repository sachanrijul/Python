# ------------------- Python Exceptions & Exception Handling -------------------

"""
✅ An exception is an error that occurs during the execution of a program.
✅ When Python encounters an error, it stops the program and raises an exception.
✅ We use **exception handling** to catch and deal with such errors gracefully.
"""

# ------------------- 1. Basic try-except -------------------

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Output: You can't divide by zero!
# Behind the scenes:
# Python sees division by zero and raises a ZeroDivisionError
# The except block catches and handles it

# ------------------- 2. Catching Multiple Exceptions -------------------

try:
    a = int("abc")
except (ValueError, TypeError) as e:
    print("Caught an error:", e)

# Output: Caught an error: invalid literal for int() with base 10: 'abc'

# ------------------- 3. Generic Exception Catch (Not Recommended) -------------------

undefined_variable = None

try:
    result = undefined_variable + 5
except Exception as e:
    print("Something went wrong:", e)

# Note: Always catch specific exceptions when possible

# ------------------- 4. try-except-else -------------------

try:
    num = int("100")
except ValueError:
    print("Invalid input")
else:
    print("Conversion successful:", num)

# Output:
# Conversion successful: 100
# else block runs only when no exception is raised

# ------------------- 5. try-except-finally -------------------

try:
    f = open("file.txt", "w")
    f.write("Hello!")
except IOError:
    print("Error writing to file")
finally:
    f.close()
    print("File closed (finally block always runs)")

# ------------------- 6. Raising Exceptions Manually -------------------

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age set to", age)

try:
    set_age(-1)
except ValueError as ve:
    print("Error:", ve)

# ------------------- 7. Custom Exception Class -------------------

class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative number not allowed: {value}")

def square_root(n):
    if n < 0:
        raise NegativeNumberError(n)
    return n ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print(e)

# ------------------- 8. Built-in Exception Hierarchy -------------------

"""
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    ├── OverflowError
      │    └── FloatingPointError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── FileNotFoundError
      ├── ImportError
      └── ... many others
"""

# ------------------- 9. Common Built-in Exceptions -------------------

try:
    print([1, 2, 3][5])  # IndexError
except IndexError as e:
    print("IndexError:", e)

try:
    d = {"a": 1}
    print(d["b"])  # KeyError
except KeyError as e:
    print("KeyError:", e)

try:
    int("xyz")  # ValueError
except ValueError as e:
    print("ValueError:", e)

try:
    open("nofile.txt")  # FileNotFoundError
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# ------------------- 10. Nested try-except -------------------

try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Inner handler")
        raise  # re-raises the exception
except ZeroDivisionError:
    print("Outer handler")

# Output:
# Inner handler
# Outer handler

# ------------------- 11. Catching Multiple Exception Types Separately -------------------

try:
    value = int("abc")
except TypeError:
    print("Caught a TypeError")
except ValueError:
    print("Caught a ValueError")

# ------------------- 12. Best Practices -------------------

"""
✔ Catch specific exceptions rather than using a generic except
✔ Use finally to release resources (like files or DB connections)
✔ Avoid bare `except:` unless absolutely necessary
✔ Document custom exception classes properly
✔ Raise meaningful error messages
"""

# ------------------- Summary -------------------

"""
✅ try               → Code that may raise an exception
✅ except            → Catch and handle the exception
✅ else              → Executes if no exception is raised
✅ finally           → Executes no matter what (good for cleanup)
✅ raise             → Manually throw an exception
✅ Custom Exceptions → Define using class MyException(Exception)
"""

# ------------------- End of Exception Handling Notes -------------------
