# 🎯 Topic: Lists in Python (a.k.a. Arrays in other languages)

# ✅ In Python, a list is an ordered collection that allows storing multiple values in a single variable.

# ▶️ To create a list, use square brackets []

# Creating a list of tea varieties:
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]

# ✅ Variable names can be anything, but should be meaningful.

# ▶️ Print the entire list
print(tea_varieties)

# ▶️ Accessing individual items using index (0-based indexing)
print(tea_varieties[0])  # Black Tea
print(tea_varieties[1])  # Green Tea
print(tea_varieties[-1]) # White Tea (Negative indexing for the last element)

# ▶️ List slicing: [start : end]
# End index is not included
print(tea_varieties[0:2])  # ['Black Tea', 'Green Tea']
print(tea_varieties[2:])   # ['Oolong Tea', 'White Tea']
print(tea_varieties[:3])   # ['Black Tea', 'Green Tea', 'Oolong Tea']

# ▶️ Slicing with step (hopping)
print(tea_varieties[0:4:2])  # ['Black Tea', 'Oolong Tea']

# ▶️ Changing an item by index
tea_varieties[3] = "Herbal Tea"  # Replacing White Tea with Herbal Tea
print(tea_varieties)

# ❌ Incorrect way to modify using slicing with a string (will treat the string as an iterable)
# tea_varieties[1:2] = "Lemon Tea"  # Incorrect

# ✅ Correct way: assign a list to the slice
tea_varieties[1:2] = ["Lemon Tea"]
print(tea_varieties)

# 🔍 Why does this happen?
# "Lemon Tea" is a string, and assigning it via slicing splits it into characters unless passed as a list.

# Resetting list to original for clarity
tea_varieties = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]
print(tea_varieties)

# ✅ Proper slicing replacement using a single-element list
tea_varieties[1:2] = ["Lemon Tea"]
print(tea_varieties)

# ✅ If you want to change just one value, it's better to use a direct index:
tea_varieties[1] = "Masala Chai"
print(tea_varieties)

# ✅ Creating an empty list
empty_list = []
print(empty_list)  # []

# ✅ Creating a heterogeneous list (different data types)
mixed_list = ["Chai", 42, 3.14, True]
print(mixed_list)

# ✅ Length of a list
print(len(tea_varieties))  # 4

# ✅ List inside a list (Nested list)
nested_list = ["Green Tea", ["Ginger", "Tulsi"], "Honey"]
print(nested_list)
print(nested_list[1])       # ['Ginger', 'Tulsi']
print(nested_list[1][0])    # Ginger

# ✅ Check if item exists in list (membership test)
print("Masala Chai" in tea_varieties)   # True
print("Milk Tea" in tea_varieties)      # False

# ✅ List concatenation (combine two lists)
more_tea = ["Milk Tea", "Lemon Tea"]
all_tea = tea_varieties + more_tea
print(all_tea)

# ✅ List repetition
repeat_tea = ["Kadak Chai"] * 3
print(repeat_tea)  # ['Kadak Chai', 'Kadak Chai', 'Kadak Chai']

# All Python List Methods with Examples

# Sample list
numbers = [1, 2, 3, 4, 2]

# 1. append(x) – Adds item to end of list
numbers.append(5)
print(numbers)  # Output: [1, 2, 3, 4, 2, 5]

# 2. extend(iterable) – Adds all elements from an iterable (e.g. another list)
numbers.extend([6, 7])
print(numbers)  # Output: [1, 2, 3, 4, 2, 5, 6, 7]

# 3. insert(index, element) – Inserts item at given position
numbers.insert(2, 99)
print(numbers)  # Output: [1, 2, 99, 3, 4, 2, 5, 6, 7]

# 4. remove(x) – Removes first occurrence of value x
numbers.remove(2)
print(numbers)  # Output: [1, 99, 3, 4, 2, 5, 6, 7]

# 5. pop([index]) – Removes and returns item at index (default last)
print(numbers.pop())     # Output: 7 (removed last element)
print(numbers.pop(1))    # Output: 99 (removed at index 1)
print(numbers)           # Output: [1, 3, 4, 2, 5, 6]

# 6. clear() – Removes all elements from the list
temp = [1, 2, 3]
temp.clear()
print(temp)  # Output: []

# 7. index(x[, start[, end]]) – Returns first index of value
print(numbers.index(4))  # Output: 2

# 8. count(x) – Returns number of occurrences of value
print(numbers.count(2))  # Output: 1

# 9. sort(key=None, reverse=False) – Sorts list in place
unsorted_list = [5, 2, 9, 1]
unsorted_list.sort()
print(unsorted_list)  # Output: [1, 2, 5, 9]

# Sort in reverse order
unsorted_list.sort(reverse=True)
print(unsorted_list)  # Output: [9, 5, 2, 1]

# Sort using a key (e.g., absolute value)
mixed = [-3, 1, -2, 4]
mixed.sort(key=abs)
print(mixed)  # Output: [1, -2, -3, 4]

# 10. reverse() – Reverses the list in place
a = [1, 2, 3]
a.reverse()
print(a)  # Output: [3, 2, 1]

# 11. copy() – Returns a shallow copy of the list
original = [1, 2, 3]
copy_list = original.copy()
print(copy_list)  # Output: [1, 2, 3]

# Confirm they are different objects
print(original is copy_list)  # Output: False

# ----- Other Useful Built-in Functions for Lists (not methods) -----

# len() – Get length of list
print(len(original))  # Output: 3

# sum() – Sum of elements (only numeric types)
print(sum([1, 2, 3]))  # Output: 6

# max(), min() – Max and min elements
print(max([1, 5, 3]))  # Output: 5
print(min([1, 5, 3]))  # Output: 1

# sorted() – Returns a new sorted list (doesn't modify original)
nums = [3, 1, 4]
print(sorted(nums))   # Output: [1, 3, 4]
print(nums)           # Output: [3, 1, 4]

# any() – True if any element is True
print(any([0, False, 5]))  # Output: True

# all() – True if all elements are True
print(all([1, True, 5]))   # Output: True

# enumerate() – Returns index-value pairs
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)
# Output:
# 0 a
# 1 b
# 2 c

# zip() – Combines multiple iterables
a = [1, 2]
b = ['x', 'y']
print(list(zip(a, b)))  # Output: [(1, 'x'), (2, 'y')]

# List comprehensions – Short form to create lists
squares = [x * x for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]


# 🧠 Things to remember:
# - Use index to access values in a list
# - You can slice lists to get sublists
# - Replace values using index or assign a list when using slices
# - Lists can be empty or have mixed data types
# - Use `in` to check if an element exists
# - Use `+` to concatenate, `*` to repeat
# - Use `append()` to add elements to the end
