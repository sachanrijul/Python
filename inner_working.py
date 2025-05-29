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