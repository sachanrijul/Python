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

# 1. capitalize() – Capitalizes the first character
print("hello".capitalize())  # Output: 'Hello'

# 2. casefold() – Converts string to lowercase (more aggressive than lower)
print("HELLOß".casefold())  # Output: 'helloss'

# 3. center(width, fillchar=' ') – Centers the string with padding
print("hi".center(10, '-'))  # Output: '----hi----'

# 4. count(sub[, start[, end]]) – Counts occurrences of a substring
print("banana".count("a"))  # Output: 3

# 5. encode(encoding='utf-8') – Encodes the string into bytes
print("café".encode())  # Output: b'caf\xc3\xa9'

# 6. endswith(suffix[, start[, end]]) – Checks if string ends with suffix
print("main.py".endswith(".py"))  # Output: True

# 7. expandtabs(tabsize=8) – Expands tabs to spaces
print("hello\tworld".expandtabs(4))  # Output: 'hello   world'

# 8. find(sub[, start[, end]]) – Finds first occurrence, returns -1 if not found
print("hello".find("e"))  # Output: 1

# 9. format() – Formats strings using placeholders
print("Hello, {}".format("Alice"))  # Output: 'Hello, Alice'

# 10. format_map(mapping) – Like format, but uses a dictionary
print("Hello, {name}".format_map({'name': 'Bob'}))  # Output: 'Hello, Bob'

# 11. index(sub[, start[, end]]) – Like find(), but raises error if not found
print("hello".index("l"))  # Output: 2

# 12. isalnum() – Checks if all characters are alphanumeric
print("abc123".isalnum())  # Output: True

# 13. isalpha() – Checks if all characters are alphabetic
print("abc".isalpha())  # Output: True

# 14. isascii() – Checks if all characters are ASCII
print("hello".isascii())  # Output: True

# 15. isdecimal() – Checks if all characters are decimal digits
print("123".isdecimal())  # Output: True

# 16. isdigit() – Checks if all characters are digits (includes superscripts)
print("123".isdigit())  # Output: True

# 17. isidentifier() – Checks if valid identifier
print("var_1".isidentifier())  # Output: True

# 18. islower() – Checks if all cased characters are lowercase
print("hello".islower())  # Output: True

# 19. isnumeric() – Checks if all characters are numeric (fractions, etc.)
print("⅔".isnumeric())  # Output: True

# 20. isprintable() – Checks if all characters are printable
print("hello\n".isprintable())  # Output: False

# 21. isspace() – Checks if all characters are whitespace
print("   ".isspace())  # Output: True

# 22. istitle() – Checks if string is titlecased
print("Hello World".istitle())  # Output: True

# 23. isupper() – Checks if all cased characters are uppercase
print("HELLO".isupper())  # Output: True

# 24. join(iterable) – Joins iterable items into a single string
print("-".join(["a", "b", "c"]))  # Output: 'a-b-c'

# 25. ljust(width[, fillchar]) – Left-justifies string
print("hi".ljust(5, '*'))  # Output: 'hi***'

# 26. lower() – Converts to lowercase
print("HELLO".lower())  # Output: 'hello'

# 27. lstrip([chars]) – Strips characters from left side
print("   hello ".lstrip())  # Output: 'hello '

# 28. maketrans() – Creates translation table
trans = str.maketrans("ae", "12")
# 29. translate() – Applies translation table
print("apple".translate(trans))  # Output: '1ppl2'

# 30. partition(sep) – Splits into 3 parts (before, sep, after)
print("abc:def".partition(":"))  # Output: ('abc', ':', 'def')

# 31. replace(old, new[, count]) – Replaces substrings
print("hello world".replace("l", "x"))  # Output: 'hexxo worxd'

# 32. rfind(sub[, start[, end]]) – Finds last occurrence or -1
print("hello world".rfind("o"))  # Output: 7

# 33. rindex(sub[, start[, end]]) – Like rfind, but error if not found
print("hello".rindex("l"))  # Output: 3

# 34. rjust(width[, fillchar]) – Right-justifies string
print("hi".rjust(5, '-'))  # Output: '---hi'

# 35. rpartition(sep) – Splits into 3 parts from right
print("a:b:c".rpartition(":"))  # Output: ('a:b', ':', 'c')

# 36. rsplit([sep[, maxsplit]]) – Splits from the right
print("one two three".rsplit(" ", 1))  # Output: ['one two', 'three']

# 37. rstrip([chars]) – Strips characters from right
print("hello   ".rstrip())  # Output: 'hello'

# 38. split([sep[, maxsplit]]) – Splits string by separator
print("a,b,c".split(","))  # Output: ['a', 'b', 'c']

# 39. splitlines([keepends]) – Splits at line boundaries
print("line1\nline2".splitlines())  # Output: ['line1', 'line2']

# 40. startswith(prefix[, start[, end]]) – Checks if string starts with prefix
print("hello".startswith("he"))  # Output: True

# 41. strip([chars]) – Removes leading/trailing characters
print("  hello  ".strip())  # Output: 'hello'

# 42. swapcase() – Swaps case
print("HeLLo".swapcase())  # Output: 'hEllO'

# 43. title() – Title-cases the string
print("hello world".title())  # Output: 'Hello World'

# 44. upper() – Converts to uppercase
print("hello".upper())  # Output: 'HELLO'

# 45. zfill(width) – Pads with zeros on the left
print("42".zfill(5))  # Output: '00042'


# End of notes for this section ✅