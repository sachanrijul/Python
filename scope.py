# ==========================
# Scope and Namespace in Python
# ==========================

# Namespace: A container that holds a mapping of names to objects.
# Types of namespaces:
# 1. Built-in Namespace – contains built-in functions like print(), len(), etc.
# 2. Global Namespace – created when the script is executed and contains global variables and functions.
# 3. Local Namespace – created inside a function and contains local variables.

# When are namespaces created?
# - Built-in: Created when Python interpreter starts.
# - Global: Created when a script/module is run.
# - Local: Created when a function is called.

# Viewing built-in namespace
print(dir(__builtins__))  # Displays all built-in functions and variables

# Scope: Refers to the visibility of variables.
# LEGB Rule for scope resolution:
# L – Local
# E – Enclosing
# G – Global
# B – Built-in

# LEGB Rule in action:
# If a variable is not found in the local scope,
# Python will look in the enclosing scope,
# then the global scope, and finally the built-in scope.

# Example to demonstrate scope and namespace

x = 10  # Global variable

def outer_function():
    x = 20  # Enclosing variable
    def inner_function():
        x = 30  # Local variable
        print("Inner x:", x)
    inner_function()
    print("Outer x:", x)

outer_function()
print("Global x:", x)

# Output:
# Inner x: 30
# Outer x: 20
# Global x: 10

# Using 'global' keyword
# It allows modification of a global variable from within a local scope

y = 5

def change_global():
    global y
    y = 100

change_global()
print("Modified global y:", y)  # Output: 100

# Using 'nonlocal' keyword
# It allows modification of an enclosing (non-global) variable

def outer():
    z = 10
    def inner():
        nonlocal z
        z = 20
    inner()
    print("z after inner():", z)

outer()  # Output: z after inner(): 20

# Example of misuse of 'nonlocal' keyword
# Trying to use nonlocal without an enclosing variable raises an error

def wrong_nonlocal():
    def inner():
        # nonlocal a  # This would raise a SyntaxError because 'a' is not in any enclosing scope
        a = 10
    inner()

# wrong_nonlocal()  # Uncommenting nonlocal a will raise SyntaxError

# Classes also create their own namespace

class Test:
    val = 10  # val belongs to the namespace of Test

print(Test.__dict__)  # Shows the class namespace

# Summary:
# - 'global' affects global variables.
# - 'nonlocal' affects variables in the nearest enclosing scope.
# - Python resolves variable names using the LEGB rule.
# - Namespaces are created at different times based on their scope.
# - Classes and built-ins also have their own namespaces.
