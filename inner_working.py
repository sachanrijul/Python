# Python Interpreter Behavior
# - Python performs several internal optimizations.
# - Sometimes results can look unexpected due to behind-the-scenes behavior.
# - Important to understand how Python memory and references work.

# Python memory management is automatic:
# - Python uses reference counting for memory management.
# - When an object has no references, it's cleaned up by garbage collection.

# Example: Reference Behavior
a = 10
b = 10

# Both 'a' and 'b' point to the same object in memory (due to interning for small integers).
# Python doesn't create two separate objects for 10.

# Interning Optimization:
# - For small integers and strings, Python reuses memory via interning.
# - That's why multiple variables with the same value may point to the same object.

# Check memory address (id is the memory location)
print(id(a), id(b))  # Likely the same

# Works for strings too (interned)
s1 = "hello"
s2 = "hello"
print(id(s1), id(s2))  # Likely same due to interning

# But not always for longer or dynamic strings
s3 = "hello world!"
s4 = "hello world!"
print(id(s3), id(s4))  # Might be different

# Reference Counting
# Python keeps a count of how many references exist to an object.

import sys
print(sys.getrefcount(10))  # Might show higher due to internal temporary references

# ⚠️ sys.getrefcount() is not always reliable
# - It includes the temporary reference made by the function call itself.
# - Some blogs show fixed numbers like 3 or more due to internal caching.

# Garbage Collection:
# - If no reference remains, object is deallocated.
# - Python doesn't keep any empty references.
# - This is handled via the garbage collector.

# Example:
x = 5
print(id(x))
x = None  # Original 5 may be deallocated if no other references exist

# But due to interning of small integers, 5 may still persist in memory

# Internals: Memory & Data Types
# - In Python, data types are bound to the object in memory, not the variable.
# - Variable names just point to objects.
# - Type is stored with the object, not with the variable.

a = 3
print(type(a))  # Output: <class 'int'>

# Interview Tip:
# Q: Does Python store type information with variables?
# A: No. Type is with the object in memory, not the variable name.

# Mutable vs Immutable Reference Behavior:
# - Immutable objects (e.g., int, str, tuple) cannot be modified in-place.
# - Mutable objects (e.g., list, dict, set) can be modified without changing memory location.

lst1 = [1, 2, 3]
print("Before:", id(lst1))
lst1.append(4)
print("After:", id(lst1))  # Same ID → modified in-place (mutable)

num = 100
print("Before:", id(num))
num += 1
print("After:", id(num))  # Different ID → new object created (immutable)

# Key Takeaways:
# - Python reuses memory for immutable objects (e.g., numbers, strings).
# - Reference counting helps manage memory.
# - sys.getrefcount() can be misleading.
# - Memory is allocated only when referenced.
# - Type is a property of the object, not the variable.
# - Immutable types result in new memory allocation when modified.
# - Mutable types can be modified without changing ID.

# Advanced Note:
# - Python’s behavior depends on the implementation (e.g., CPython).
# - CPython uses interning, reference counting, and garbage collection.
# - These details may differ in PyPy or Jython.

# Example: Temporary Object Reference
def show_refcount(x):
    print(sys.getrefcount(x))

show_refcount(100)

# Conclusion:
# - Understanding Python internals helps avoid confusion during debugging and interviews.
# - Don't rely too heavily on visual count of references—many are abstracted away.
# - Always check behavior for mutable vs immutable to avoid side-effects.

# something extra ::--
# You have seen the use of this.
'''
if __name__ = "__main__":
    main()
'''
# It is used to stop unexpected exicution like when we import any module or any local file it exicutes automatically but if we use it, it will not exicute autmatically.

# ------------------- Dunder (Double Underscore) Methods in Python -------------------

"""
Dunder methods (short for "double underscore") are also called **magic methods** or **special methods**.
They are methods with double underscores at the beginning and end of their names, like __init__, __str__, __len__, etc.

Python automatically calls these methods behind the scenes during certain operations.
You can override them in your class to customize behavior of your objects.
"""

# ------------------- 1. Object Initialization -------------------

class Person:
    def __init__(self, name, age):
        # __init__ is the constructor; called when an object is created
        self.name = name
        self.age = age

    def __str__(self):
        # __str__ is used by str() and print() to return a human-readable string
        return f"{self.name} is {self.age} years old"

p = Person("Alice", 25)
print(p)  # Calls __str__

# Behind the scenes: print(p) → str(p) → p.__str__()

# ------------------- 2. Object Representation -------------------

class DebugPerson:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # __repr__ is for unambiguous representation, used in debugging
        return f"DebugPerson(name='{self.name}')"

dp = DebugPerson("Bob")
print(repr(dp))  # Output: DebugPerson(name='Bob')
print([dp])      # Uses __repr__ when inside collections

# ------------------- 3. Object Comparison -------------------

class Number:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

a = Number(5)
b = Number(10)

print(a == b)  # False → __eq__
print(a < b)   # True  → __lt__

# Similar dunder methods:
# __ne__, __le__, __gt__, __ge__ for other comparisons

# ------------------- 4. Operator Overloading -------------------

class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other.x)

    def __mul__(self, other):
        return Vector(self.x * other.x)

    def __str__(self):
        return f"Vector({self.x})"

v1 = Vector(2)
v2 = Vector(3)
print(v1 + v2)  # Vector(5) → __add__
print(v1 * v2)  # Vector(6) → __mul__

# Other arithmetic methods:
# __sub__, __truediv__, __floordiv__, __mod__, __pow__

# ------------------- 5. Length, Boolean, and Indexing -------------------

class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __contains__(self, item):
        return item in self.data

    def __bool__(self):
        return bool(self.data)

lst = MyList([10, 20, 30])
print(len(lst))      # 3 → __len__
print(lst[1])        # 20 → __getitem__
print(10 in lst)     # True → __contains__
print(bool(lst))     # True → __bool__

# ------------------- 6. Context Managers (with statement) -------------------

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file...")
        self.file.close()

# Usage of context manager
with FileManager("sample.txt") as f:
    f.write("Hello!")

# __enter__ is called at the start, __exit__ at the end (even if error occurs)

# ------------------- 7. Callable Objects -------------------

class Adder:
    def __init__(self, base):
        self.base = base

    def __call__(self, x):
        return self.base + x

add5 = Adder(5)
print(add5(10))  # 15 → __call__

# Behind the scenes: add5(10) → add5.__call__(10)

# ------------------- 8. Attribute Access & Management -------------------

class Demo:
    def __init__(self):
        self.value = 42

    def __getattr__(self, name):
        # Called only when attribute is not found normally
        return f"{name} not found!"

    def __setattr__(self, name, value):
        # Called for every attribute assignment
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f"Deleting attribute {name}")
        super().__delattr__(name)

d = Demo()
print(d.unknown)       # "unknown not found!" → __getattr__
d.value = 100          # __setattr__
del d.value            # __delattr__

# ------------------- 9. Object Lifecycle -------------------

class Life:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

obj = Life()
del obj  # __del__ is called (but timing is up to garbage collector)

# ------------------- Summary of Popular Dunder Methods -------------------

"""
✅ __init__      → Constructor
✅ __str__       → User-readable string
✅ __repr__      → Debug/official string
✅ __len__       → Length (used by len())
✅ __getitem__   → Indexing (obj[index])
✅ __setitem__   → Index assignment (obj[index] = val)
✅ __contains__  → Membership (in)
✅ __eq__, __lt__, __gt__, etc. → Comparisons
✅ __add__, __sub__, etc. → Arithmetic ops
✅ __enter__, __exit__    → Context managers (with statement)
✅ __call__      → Makes object callable like a function
✅ __getattr__, __setattr__, __delattr__ → Custom attribute behavior
✅ __bool__      → Boolean conversion
✅ __del__       → Destructor
"""

# ------------------- End of Dunder Methods Notes -------------------
