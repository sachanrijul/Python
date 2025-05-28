# String Formatting in Python using format() and f-strings

# 1. Basic substitution using format()
print("Hello, {}".format("Alice"))  # Output: 'Hello, Alice'

# 2. Positional arguments
print("{1} is older than {0}".format("Bob", "Alice"))  # Output: 'Alice is older than Bob'

# 3. Keyword arguments
print("{name} is {age} years old.".format(name="Charlie", age=25))  # Output: 'Charlie is 25 years old.'

# 4. f-string (Python 3.6+)
name = "David"
age = 30
print(f"{name} is {age} years old.")  # Output: 'David is 30 years old.'

# ---- Format Specifiers for Numbers ----

num = 123.456789

# 5. Floating-point number with 2 decimal places
print("{:.2f}".format(num))  # Output: '123.46'

# 6. Floating-point in exponential notation
print("{:.2e}".format(num))  # Output: '1.23e+02'

# 7. Floating-point with fixed width and precision
print("{:10.2f}".format(num))  # Output: '    123.46' (right-aligned, width 10)

# 8. Floating-point left aligned
print("{:<10.2f}".format(num))  # Output: '123.46    '

# 9. Floating-point centered
print("{:^10.2f}".format(num))  # Output: '  123.46  '

# 10. Integer in decimal
print("{:d}".format(42))  # Output: '42'

# 11. Integer in binary
print("{:b}".format(10))  # Output: '1010'

# 12. Integer in octal
print("{:o}".format(10))  # Output: '12'

# 13. Integer in hexadecimal (lowercase)
print("{:x}".format(255))  # Output: 'ff'

# 14. Integer in hexadecimal (uppercase)
print("{:X}".format(255))  # Output: 'FF'

# 15. Integer with sign
print("{:+d}".format(42))  # Output: '+42'
print("{:+d}".format(-42))  # Output: '-42'

# 16. Zero padding
print("{:05d}".format(42))  # Output: '00042'

# 17. Thousands separator using comma
print("{:,}".format(1234567))  # Output: '1,234,567'

# 18. Percentage formatting
print("{:.2%}".format(0.1234))  # Output: '12.34%'

# 19. General format (uses fixed or scientific automatically)
print("{:g}".format(123456.0))  # Output: '123456'
print("{:g}".format(0.0000123456))  # Output: '1.23456e-05'

# ---- Alignment & Padding ----

# 20. Right-align text
print("{:>10}".format("Hello"))  # Output: '     Hello'

# 21. Left-align text
print("{:<10}".format("Hello"))  # Output: 'Hello     '

# 22. Center-align text
print("{:^10}".format("Hello"))  # Output: '  Hello   '

# 23. Custom fill character
print("{:*^10}".format("Hi"))  # Output: '****Hi****'

# ---- Formatting with dictionaries and objects ----

# 24. Accessing dict keys
person = {"name": "Eve", "age": 22}
print("{0[name]} is {0[age]}".format(person))  # Output: 'Eve is 22'

# 25. Accessing object attributes
class User:
    def __init__(self, name):
        self.name = name
u = User("Frank")
print("{0.name}".format(u))  # Output: 'Frank'

# 26. Nested formatting
value = 12.3456
width = 10
precision = 3
print(f"{value:{width}.{precision}f}")  # Output: '     12.346'

# ---- f-string with expressions ----

# 27. Arithmetic inside f-string
print(f"{5 * 2}")  # Output: '10'

# 28. Calling functions inside f-string
def greet(name): return f"Hi {name}"
print(f"{greet('Grace')}")  # Output: 'Hi Grace'

# ---- Number Base Prefixes ----

# 29. Binary with prefix
print("{:#b}".format(10))  # Output: '0b1010'

# 30. Octal with prefix
print("{:#o}".format(10))  # Output: '0o12'

# 31. Hexadecimal with prefix
print("{:#x}".format(255))  # Output: '0xff'

# ---- Misc ----

# 32. Truncating strings
print("{:.5}".format("Hello, World"))  # Output: 'Hello'

# 33. Mixing multiple format specifiers
print("{:+08.2f}".format(123.4))  # Output: '+0123.40' (sign + width + zero-padding + 2 decimal)
