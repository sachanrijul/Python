# 📌 Tuples are immutable sequences in Python.
# That means once a tuple is created, you can't change, add, or remove elements.

# ✅ Tuple creation using ()
empty_tuple = ()
single_element_wrong = ("Tea")     # This is a string, not a tuple
single_element_correct = ("Tea",)  # This is a tuple with one element
multi_element_tuple = ("Black", "Green", "Oolong")

print(type(empty_tuple))            # Output: <class 'tuple'>
print(type(single_element_wrong))   # Output: <class 'str'>
print(type(single_element_correct)) # Output: <class 'tuple'>

# ✅ Creating a tuple without using parentheses (tuple packing)
t = "A", "B", "C"
print(t)              # Output: ('A', 'B', 'C')
print(type(t))        # Output: <class 'tuple'>

# ✅ Tuple unpacking (number of variables must match)
a, b, c = t
print(a, b, c)        # Output: A B C

# ✅ Nested Tuple
nested = ("Chai", ("Adrak", "Elaichi"))
print(nested[1][0])   # Output: Adrak

# ✅ Accessing elements (indexing & slicing)
print(multi_element_tuple[1])   # Output: Green
print(multi_element_tuple[-1])  # Output: Oolong
print(multi_element_tuple[0:2]) # Output: ('Black', 'Green')

# ✅ Length of a tuple
print(len(multi_element_tuple))  # Output: 3

# ✅ Concatenation of tuples
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4)

# ✅ Repetition
t4 = ("Hi",) * 3
print(t4)  # Output: ('Hi', 'Hi', 'Hi')

# ✅ Membership test
print("Green" in multi_element_tuple)  # Output: True

# ✅ Iterating through a tuple
for tea in multi_element_tuple:
    print(tea)

# ✅ Using tuples as dictionary keys (because they are immutable)
my_dict = {("Math", 101): "Algebra", ("Sci", 102): "Physics"}
print(my_dict[("Math", 101)])  # Output: Algebra

# ✅ Built-in functions
num_tuple = (5, 2, 9, 1)
print(max(num_tuple))     # Output: 9
print(min(num_tuple))     # Output: 1
print(sum(num_tuple))     # Output: 17
print(sorted(num_tuple))  # Output: [1, 2, 5, 9] => Returns a list, not a tuple

# ✅ Tuple methods (only 2 methods)
colors = ("Red", "Blue", "Red", "Green")
print(colors.count("Red"))     # Output: 2
print(colors.index("Green"))   # Output: 3

# ❌ Modifying tuple is not allowed
# t = (1, 2, 3)
# t[0] = 100  # ❌ TypeError

# ✅ But if tuple contains mutable elements like a list, that list can be modified
t = (1, 2, [3, 4])
t[2][0] = 100
print(t)  # Output: (1, 2, [100, 4])

# ✅ Use case of tuple: returning multiple values from a function
def calc(a, b):
    return a + b, a * b

result = calc(2, 3)
print(result)        # Output: (5, 6)
add, mul = calc(4, 5)
print(add, mul)      # Output: 9 20
