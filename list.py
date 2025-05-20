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

# ✅ Adding new items using append() (adds at the end)
tea_varieties.append("Iced Tea")
print(tea_varieties)

# 🧠 Things to remember:
# - Use index to access values in a list
# - You can slice lists to get sublists
# - Replace values using index or assign a list when using slices
# - Lists can be empty or have mixed data types
# - Use `in` to check if an element exists
# - Use `+` to concatenate, `*` to repeat
# - Use `append()` to add elements to the end
