# A dictionary is a collection of key-value pairs.
# It's unordered (in Python < 3.7), mutable, and indexed by keys (not positions).
# Syntax: {key1: value1, key2: value2, ...}

# ✅ Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# ✅ Using dict() constructor
dict_2 = dict(name="Bob", age=30)
dict_3 = dict([("x", 1), ("y", 2)])  # list of tuples
print(dict_2)
print(dict_3)

# 🔑 Keys must be immutable (str, int, tuple, etc.), and unique
# ❌ The following will overwrite the previous key
bad_dict = {"a": 1, "a": 2}
print(bad_dict)  # {'a': 2}

# ✅ Accessing values using keys
print(my_dict["name"])   # Output: Alice

# ❗ Accessing a non-existing key directly will raise KeyError
# print(my_dict["gender"])  # ❌ Error

# ✅ Using get() method to safely access keys
print(my_dict.get("gender"))        # Output: None
print(my_dict.get("gender", "N/A")) # Output: N/A

# ✅ Changing a value
my_dict["age"] = 30

# ✅ Adding a new key-value pair
my_dict["gender"] = "Female"

# ✅ Deleting a key-value pair
del my_dict["city"]

# ✅ Using pop() method
removed_value = my_dict.pop("age")
print(removed_value)  # Output: 30

# ✅ Using popitem() – removes last inserted item (Python 3.7+)
last_item = my_dict.popitem()
print(last_item)  # ('gender', 'Female')

# ✅ Using setdefault() – get value or insert default if key not found
print(my_dict.setdefault("city", "Mumbai"))  # Adds city with value if missing

# ✅ Checking if a key exists
if "name" in my_dict:
    print("Key exists")

# ✅ Looping through dictionary
for key in my_dict:
    print(key, "->", my_dict[key])

# ✅ Looping through items (key-value pairs)
for key, value in my_dict.items():
    print(f"{key}: {value}")

# ✅ Getting all keys
print(list(my_dict.keys()))

# ✅ Getting all values
print(list(my_dict.values()))

# ✅ Getting all key-value pairs
print(list(my_dict.items()))

# ✅ Dictionary Length
print(len(my_dict))

# ✅ Dictionary with mixed data types
mixed_dict = {
    "name": "Sara",
    "marks": [90, 95, 100],
    "details": {"age": 21, "city": "Delhi"}
}
print(mixed_dict["details"]["city"])

# ✅ Nested dictionaries
students = {
    "101": {"name": "Bob", "marks": 90},
    "102": {"name": "Tom", "marks": 85}
}
print(students["101"]["marks"])  # Output: 90

# ✅ Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ✅ Using zip() to create dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
zipped_dict = dict(zip(keys, values))
print(zipped_dict)

# ✅ Clearing dictionary
my_dict.clear()
print(my_dict)  # {}

# ✅ Copying dictionaries (shallow copy)
d1 = {"x": 10, "y": 20}
d2 = d1.copy()
print(d2)

# ✅ Copying (deep copy - when dictionary has nested dicts)
import copy
nested = {"a": {"b": 1}}
shallow = nested.copy()
deep = copy.deepcopy(nested)
nested["a"]["b"] = 99
print(shallow)  # {'a': {'b': 99}} → changed
print(deep)     # {'a': {'b': 1}} → safe

# ✅ Merging dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# ✅ Merging using pipe (Python 3.9+)
d3 = {"x": 100}
merged = d1 | d2 | d3
print(merged)

# ✅ Unpacking multiple dictionaries (Python 3.5+)
d4 = {**d1, **d2, **d3}
print(d4)

# ⚠️ Avoiding common mistakes
# - Mutable keys like lists are not allowed
# my_dict = {[1, 2]: "invalid"}  # ❌ TypeError

# - Duplicate keys are overwritten
conflict = {"a": 10, "a": 99}
print(conflict)  # {'a': 99}

# ----------- All Dictionary Methods in Python -----------

# Sample dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 1. get(key[, default]) – Returns value if key exists, else default
print(person.get("name"))       # Output: Alice
print(person.get("gender", "N/A"))  # Output: N/A

# 2. keys() – Returns a view object of all keys
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])

# 3. values() – Returns a view object of all values
print(person.values())  # Output: dict_values(['Alice', 25, 'New York'])

# 4. items() – Returns a view object of key-value tuples
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# 5. update([other]) – Adds or updates multiple key-value pairs
person.update({"age": 26, "gender": "Female"})
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'gender': 'Female'}

# 6. pop(key[, default]) – Removes and returns value for key; error if not found and no default
print(person.pop("city"))  # Output: New York
# print(person.pop("salary"))  # KeyError
print(person.pop("salary", "Not Found"))  # Output: Not Found

# 7. popitem() – Removes and returns last inserted key-value pair
print(person.popitem())  # Output: ('gender', 'Female')

# 8. setdefault(key[, default]) – Returns value if key exists, else inserts with default
print(person.setdefault("name", "Unknown"))  # Output: Alice (already exists)
print(person.setdefault("country", "USA"))   # Adds country: 'USA'
print(person)  # Output includes new key: {'name': 'Alice', 'age': 26, 'country': 'USA'}

# 9. clear() – Removes all items from dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print(temp)  # Output: {}

# 10. copy() – Returns a shallow copy of the dictionary
original = {"x": 10, "y": 20}
copy_dict = original.copy()
print(copy_dict)  # Output: {'x': 10, 'y': 20}
print(copy_dict is original)  # Output: False (different object)

# ----------- Bonus: Dictionary Comprehensions -----------

# Dictionary comprehension example
squares = {x: x * x for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ----------- Iterating through a dictionary -----------

info = {"a": 1, "b": 2}
for key in info:
    print(key, info[key])  # Output: a 1 \n b 2

for key, value in info.items():
    print(f"{key} -> {value}")  # Output: a -> 1 \n b -> 2

# ----------- Built-in Functions with Dictionary -----------

# len() – Number of key-value pairs
print(len(info))  # Output: 2

# str(), type()
print(str(info))  # Output: string representation
print(type(info))  # Output: <class 'dict'>
