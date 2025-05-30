# ------------------- Python File Handling (Complete Notes) -------------------

"""
📁 Python provides built-in functions to work with files:
- Open a file
- Read from it
- Write to it
- Close it
- Handle binary and text data

Files can be of two types:
1. Text files (.txt, .py, .csv, etc.)
2. Binary files (.exe, .jpg, .mp4, etc.)
"""

# ------------------- 1. Opening a File -------------------

"""
Syntax: open(filename, mode)

Modes:
- 'r'  → Read (default), file must exist
- 'w'  → Write, creates file or overwrites if exists
- 'a'  → Append, creates if doesn't exist
- 'x'  → Exclusive creation, fails if file exists
- 'b'  → Binary mode
- 't'  → Text mode (default)
- '+'  → Read and write
"""

f = open("example.txt", "w")  # Write mode
f.write("Hello, world!")
f.close()

# Behind the scenes:
# open() returns a file object which manages a buffer in memory.
# File is locked until explicitly closed or released by garbage collector.

# ------------------- 2. Reading From a File -------------------

f = open("example.txt", "r")
content = f.read()
print(content)
f.close()

# read()         → reads full content
# read(n)        → reads first n characters
# readline()     → reads a single line
# readlines()    → returns list of lines

# ------------------- 3. Writing to a File -------------------

f = open("example.txt", "w")
f.write("New content!")   # Overwrites existing content
f.close()

# ------------------- 4. Appending to a File -------------------

f = open("example.txt", "a")
f.write("\nAppended line")
f.close()

# ------------------- 5. Using with open(...) as (Context Manager) -------------------

with open("example.txt", "r") as f:
    print(f.read())

# Automatically closes the file, even if an error occurs
# Recommended way to handle files

# ------------------- 6. File Object Methods -------------------

with open("example.txt", "r") as f:
    print(f.readable())   # True if file is readable
    print(f.writable())   # False
    print(f.closed)       # False
print(f.closed)           # True after 'with' block

# ------------------- 7. Using tell() and seek() -------------------

with open("example.txt", "r") as f:
    print("Current position:", f.tell())  # 0
    print("Reading:", f.read(5))
    print("New position:", f.tell())      # 5
    f.seek(0)                             # Go back to start
    print("After seek:", f.read(5))

# ------------------- 8. Reading and Writing Binary Files -------------------

# Writing a binary file
with open("data.bin", "wb") as f:
    f.write(b"This is binary data")

# Reading binary
with open("data.bin", "rb") as f:
    data = f.read()
    print(data)

# ------------------- 9. Handling File Not Found / Errors -------------------

try:
    with open("not_exist.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("Error:", e)

# ------------------- 10. Creating a New File Using 'x' Mode -------------------

try:
    with open("newfile.txt", "x") as f:
        f.write("This file is created only if it doesn't exist.")
except FileExistsError:
    print("File already exists!")

# ------------------- 11. Using writelines() -------------------

lines = ["Line1\n", "Line2\n", "Line3\n"]
with open("lines.txt", "w") as f:
    f.writelines(lines)

# ------------------- 12. Looping Over File Lines -------------------

with open("lines.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())

# ------------------- 13. Truncate a File -------------------

with open("truncate.txt", "w") as f:
    f.write("This is a long text")
    f.truncate(10)  # Keeps only the first 10 characters

# ------------------- 14. Check If File Exists Before Accessing -------------------

import os

if os.path.exists("lines.txt"):
    print("File exists!")
else:
    print("File does not exist!")

# ------------------- 15. Deleting a File -------------------

import os

if os.path.exists("delete_me.txt"):
    os.remove("delete_me.txt")
    print("File deleted")

# ------------------- Summary -------------------

"""
✔ open() → Opens a file and returns a file object
✔ Modes → 'r', 'w', 'a', 'x', with binary/text modifiers
✔ read(), write(), readline(), readlines(), writelines()
✔ seek(), tell() for pointer control
✔ Use 'with open(...)' to manage file safely
✔ Handle exceptions for safety and debugging
✔ Use os module to work with file paths and existence
✔ Work with both text and binary data easily
"""

# ------------------- End of File Handling Notes -------------------
