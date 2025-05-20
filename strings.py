# 📌 Strings and Slicing in Python

# Python strings can be defined using:
# - Single quotes ('...')
# - Double quotes ("...")
# - Triple quotes ('''...''' or """...""") → Useful for multiline strings

# Example:
str1 = 'Single quoted'
str2 = "Double quoted"
str3 = '''Triple
quoted
string'''

# 🔹 Triple quotes retain formatting (newlines, tabs, etc.)

# Let's assign a string to a variable
tea = "Masala Tea"

# Strings are treated like arrays → indexing and slicing works

# ✅ Indexing example (to get first character)
first_char = tea[0]
print(f"First character: {first_char}")  # Output: M

# ✅ Slicing example (to extract substring)
# Let's extract 'Masala' from 'Masala Tea'
# Indexes: 0 1 2 3 4 5 6 7 8
# Characters: M a s a l a   T e a

slice_tea = tea[0:6]
print(f"Sliced string: {slice_tea}")  # Output: Masala

# 🔹 Indexing is zero-based
# 🔹 The end index in slicing is exclusive

# ✅ More slicing examples using numbers
num_list = "0123456789"

# Slice full string
print(num_list[:])  # Output: 0123456789

# Slice from index 3 to end
print(num_list[3:])  # Output: 3456789

# Slice from start to index 7 (exclusive)
print(num_list[:7])  # Output: 0123456

# Slice from index 0 to 7 with a step of 2
print(num_list[0:7:2])  # Output: 0246

# Slice from index 0 to 7 with a step of 3
print(num_list[0:7:3])  # Output: 036

# ✅ Negative indexing example
# Last character: num_list[-1]
print(f"Last character: {num_list[-1]}")  # Output: 9

# ✅ Reverse slicing using negative step
print(num_list[::-1])  # Output: 9876543210

# ✅ Partial reverse slice (reverse first 5 digits)
print(num_list[4::-1])  # Output: 43210

# ✅ Using len() function
print(len(num_list))  # Output: 10

# 🔹 Slicing does NOT raise IndexError if indices are out of range
print(num_list[0:100])  # Output: 0123456789 (just returns up to available length)

# 🔹 Strings are immutable → cannot change characters in-place
# Example (this will raise an error):
# num_list[0] = "X"  ❌

# ✅ Unicode Strings
# Most Python strings are Unicode by default
# Useful when dealing with international characters (e.g., Japanese, Arabic)

# ✅ Use ord() to get Unicode code point of a character
print(ord("A"))  # Output: 65

# ✅ Use chr() to convert Unicode code point to character
print(chr(65))  # Output: A

# ✅ Common string methods
sample = "Hello World"

# Convert to lowercase
print(sample.lower())  # Output: hello world

# Convert to uppercase
print(sample.upper())  # Output: HELLO WORLD

# (More string methods like .replace(), .find(), etc. will be covered in upcoming videos)

# 💡 Tip:
# Many tutorials overcomplicate string slicing—understand the basics and practice.
# Try using slicing in mini projects or exercises.

# End of notes for this section ✅