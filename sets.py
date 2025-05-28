# ---- Set Basics ----

# 1. Creating a set
s = {1, 2, 3}
print(s)  # Output: {1, 2, 3}

# 2. Creating an empty set (must use set())
empty = set()
print(type(empty))  # Output: <class 'set'>

# 3. Duplicates are automatically removed
s = {1, 2, 2, 3}
print(s)  # Output: {1, 2, 3}

# 4. Sets are unordered, mutable, and don't allow indexing
# s[0] => Error

# ---- Set Methods ----

a = {1, 2, 3}
b = {3, 4, 5}

# 1. add(x) – Adds an element
a.add(4)
print(a)  # Output: {1, 2, 3, 4}

# 2. update(iterable) – Adds multiple elements
a.update([5, 6])
print(a)  # Output: {1, 2, 3, 4, 5, 6}

# 3. remove(x) – Removes x; error if not found
a.remove(6)
print(a)  # Output: {1, 2, 3, 4, 5}
# a.remove(10) => KeyError

# 4. discard(x) – Removes x; does nothing if not found
a.discard(10)  # No error

# 5. pop() – Removes and returns an arbitrary element
print(a.pop())  # Removes a random element

# 6. clear() – Removes all elements
c = {1, 2}
c.clear()
print(c)  # Output: set()

# 7. copy() – Returns shallow copy
d = a.copy()
print(d)  # Same content, different object

# ---- Set Operations ----

x = {1, 2, 3}
y = {3, 4, 5}

# 8. union() – Elements from both sets
print(x.union(y))  # Output: {1, 2, 3, 4, 5}

# 9. intersection() – Common elements
print(x.intersection(y))  # Output: {3}

# 10. difference() – Elements in x not in y
print(x.difference(y))  # Output: {1, 2}

# 11. symmetric_difference() – Elements in x or y but not both
print(x.symmetric_difference(y))  # Output: {1, 2, 4, 5}

# ---- In-Place Operation Methods ----

# 12. update() – Like union(), modifies original
x.update(y)
print(x)  # Output: {1, 2, 3, 4, 5}

# Reset x for further examples
x = {1, 2, 3}

# 13. intersection_update()
x.intersection_update({2, 3, 4})
print(x)  # Output: {2, 3}

x = {1, 2, 3}
# 14. difference_update()
x.difference_update({2, 3})
print(x)  # Output: {1}

x = {1, 2, 3}
# 15. symmetric_difference_update()
x.symmetric_difference_update({2, 4})
print(x)  # Output: {1, 3, 4}

# ---- Set Comparison ----

a = {1, 2}
b = {1, 2, 3}

# 16. issubset()
print(a.issubset(b))  # Output: True

# 17. issuperset()
print(b.issuperset(a))  # Output: True

# 18. isdisjoint() – True if no common elements
print(a.isdisjoint({4, 5}))  # Output: True

# ---- Set Operators ----

s1 = {1, 2, 3}
s2 = {3, 4}

print(s1 | s2)   # Union: {1, 2, 3, 4}
print(s1 & s2)   # Intersection: {3}
print(s1 - s2)   # Difference: {1, 2}
print(s1 ^ s2)   # Symmetric Difference: {1, 2, 4}

# ---- Frozenset ----

# 19. frozenset() – Immutable version of set
fset = frozenset([1, 2, 3])
print(fset)  # Output: frozenset({1, 2, 3})

# fset.add(4) => Error: 'frozenset' object has no attribute 'add'

# ---- Built-in Functions with Sets ----

s = {10, 20, 30}

# len()
print(len(s))  # Output: 3

# max(), min(), sum()
print(max(s))  # Output: 30
print(min(s))  # Output: 10
print(sum(s))  # Output: 60

# any(), all()
print(any({0, False, 5}))  # Output: True
print(all({1, True, 3}))   # Output: True

# ---- Set Comprehensions ----

squares = {x * x for x in range(5)}
print(squares)  # Output: {0, 1, 4, 9, 16}

# ---- Set from Strings or Lists ----

print(set("banana"))  # Output: {'b', 'n', 'a'}
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}
