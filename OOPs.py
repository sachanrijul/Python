# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects"
# Objects are instances of classes and can hold data (attributes) and functions (methods)

# 🌟 Key Concepts of OOP:
# 1. Class – Blueprint for creating objects
# 2. Object – An instance of a class
# 3. Encapsulation – Hiding internal details of an object
# 4. Inheritance – One class can inherit properties/methods of another
# 5. Polymorphism – Different classes can be treated as the same type through a common interface
# 6. Abstraction – Hiding complex implementation details and showing only the necessary parts

# 🔁 Difference between Procedural and OOP:

# Procedural style:
def greet(name):
    return f"Hello {name}!"

print(greet("Alice"))

# Object-Oriented style:
class Greeter:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello {self.name}!"

greeter = Greeter("Alice")
print(greeter.greet())

# ✅ Output for both: Hello Alice!
# But in OOP, we organize code better and it scales easily for large programs.

# 🔹 A class is a blueprint for creating objects.
# 🔹 An object is an instance of a class.
# 🔹 The __init__() method is a special method (constructor) used to initialize the object.
# 🔹 'self' refers to the current instance of the class.

# 📘 Defining a class and creating objects:

class Person:
    # Constructor method
    def __init__(self, name, age):
        self.name = name     # instance variable
        self.age = age       # instance variable

    # Method to display information
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# 🎯 Creating objects (instances) of the class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# 🎯 Calling the method using objects
person1.introduce()
person2.introduce()

# ✅ Output:
# My name is Alice and I am 25 years old.
# My name is Bob and I am 30 years old.

# 🔍 Key Points:
# - `class Person:` defines a class named `Person`.
# - `__init__` is automatically called when an object is created.
# - `self.name = name` assigns the value to the instance.
# - `person1` and `person2` are two separate objects with their own data.

# 🔹 Attributes are variables that belong to an object or class.
# 🔹 Methods are functions defined inside a class.

# 🔹 There are two types of attributes:
# 1. Instance attributes: Unique to each object.
# 2. Class attributes: Shared across all instances of the class.

class Student:
    # Class attribute (shared by all instances)
    school = "Greenwood High"

    def __init__(self, name, grade):
        # Instance attributes (unique to each instance)
        self.name = name
        self.grade = grade

    # Instance method (uses 'self')
    def show_details(self):
        print(f"Name: {self.name}, Grade: {self.grade}, School: {Student.school}")

    # Class method (uses 'cls' instead of 'self')
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # Static method (doesn’t access instance or class)
    @staticmethod
    def is_passed(marks):
        return marks >= 40

# 🎯 Creating instances
s1 = Student("John", "10th")
s2 = Student("Lara", "9th")

# 🎯 Accessing instance method
s1.show_details()
s2.show_details()

# 🎯 Changing class attribute via class method
Student.change_school("Blue Ridge School")
s1.show_details()  # Now school is updated for all

# 🎯 Using static method
print(Student.is_passed(45))  # True
print(Student.is_passed(30))  # False

# 🔍 Key Points:
# - Instance Attribute: Defined inside __init__ using self. Each object has its own copy.
# - Class Attribute: Shared across all objects. Defined directly inside the class.
# - Instance Method: Uses self to access instance attributes.
# - Class Method: Uses @classmethod and cls to modify class-level attributes.
# - Static Method: Uses @staticmethod, cannot access instance or class attributes.

# 🔹 Encapsulation means hiding the internal details of an object and restricting direct access.
# 🔹 It helps protect the integrity of the data.

# In Python, we use:
# - Public members (no underscore): accessible from anywhere
# - Protected members (one underscore _): should not be accessed outside the class (convention)
# - Private members (two underscores __): name mangled to prevent direct access

class Account:
    def __init__(self, owner, balance):
        self.owner = owner           # Public attribute
        self._bank_name = "SBI"      # Protected attribute
        self.__balance = balance     # Private attribute

    # Public method to view balance (uses encapsulation)
    def get_balance(self):
        return self.__balance

    # Public method to modify balance safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

# 🎯 Creating an object
acc = Account("Alice", 1000)

# Accessing public attribute
print(acc.owner)

# Accessing protected attribute (allowed but discouraged)
print(acc._bank_name)

# Accessing private attribute directly (Not recommended — gives error)
# print(acc.__balance)  # ❌ AttributeError

# Accessing private attribute using getter method
print(acc.get_balance())  # ✅ Safe access: 1000

# Using methods to deposit and withdraw
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())  # ✅ Output: 1200

# 🔍 Key Points:
# - Public: Can be accessed anywhere.
# - Protected (_): Should be treated as non-public. Can still be accessed.
# - Private (__): Name mangled, not directly accessible.
# - Encapsulation uses getters/setters to control data access/modification.

# 🔹 Inheritance allows one class (child) to acquire properties and behaviors (methods) of another class (parent).
# 🔹 It promotes code reuse and models "is-a" relationships.

# 🔹 Types of Inheritance in Python:
# - Single Inheritance
# - Multiple Inheritance (covered in next topic)
# - Multilevel and Hierarchical Inheritance (less common)

# 🔹 Using 'super()' to call parent class methods or constructor

# 📘 Example of Single Inheritance:

# Parent class
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print(f"{self.species} makes a sound.")

# Child class
class Dog(Animal):
    def __init__(self, breed):
        # Calling parent class constructor using super()
        super().__init__("Dog")
        self.breed = breed

    def bark(self):
        print(f"{self.breed} barks loudly.")

    # Overriding parent method
    def speak(self):
        print(f"{self.breed} says Woof!")

# 🎯 Creating an object of the child class
dog1 = Dog("Labrador")

# Accessing parent and child class methods
dog1.bark()
dog1.speak()

# ✅ Output:
# Labrador barks loudly.
# Labrador says Woof!

# 🔍 Key Points:
# - Child class inherits from the parent using class Child(Parent).
# - super() is used to access methods or constructor of the parent.
# - Method Overriding allows child class to redefine a parent method.
# - Python supports other types of inheritance too: multilevel, multiple, etc.

# 🔹 Multiple Inheritance allows a class to inherit from more than one parent class.
# 🔹 Python supports this directly.
# 🔹 Method Resolution Order (MRO) defines the order in which methods are inherited and resolved.
# 🔹 The Diamond Problem occurs when two parent classes inherit from a common grandparent class.

# 📘 Example of Multiple Inheritance:

class Father:
    def skills(self):
        print("Father: Gardening, Cooking")

class Mother:
    def skills(self):
        print("Mother: Art, Craft")

# Child inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        print("Child: Gaming, Dancing")
        # Accessing both parent methods using super() and direct call
        super().skills()         # Uses MRO: Father first
        Mother.skills(self)      # Explicitly call Mother’s method

# 🎯 Creating object
c = Child()
c.skills()

# ✅ Output:
# Child: Gaming, Dancing
# Father: Gardening, Cooking
# Mother: Art, Craft

# 🔹 MRO (Method Resolution Order) for Child class:
# You can view it using: print(Child.__mro__)
# Output: (<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)

# 🔍 Key Points:
# - Multiple inheritance: class Child(Parent1, Parent2)
# - MRO determines method resolution order.
# - super() follows MRO from left to right.
# - To avoid conflicts in Diamond Problem, always design carefully.

# 🔹 Polymorphism means "many forms".
# 🔹 In OOP, it refers to the ability to use the same method name for different types (classes).
# 🔹 Achieved through:
#    1. Method Overriding (in inheritance)
#    2. Duck Typing (Python's dynamic nature)
#    3. Built-in function polymorphism (e.g., len())

# 📘 Example 1: Polymorphism with Method Overriding

class Bird:
    def sound(self):
        print("Birds make different sounds.")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps.")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks.")

# 🎯 Polymorphic behavior
def make_sound(bird):
    bird.sound()

# 🎯 Test with different bird types
b1 = Sparrow()
b2 = Parrot()

make_sound(b1)
make_sound(b2)

# ✅ Output:
# Sparrow chirps.
# Parrot talks.

# 📘 Example 2: Duck Typing in Python

class Laptop:
    def code(self):
        print("Coding using a laptop.")

class Mobile:
    def code(self):
        print("Coding using a mobile.")

def start_coding(device):
    device.code()  # Doesn't care about type, just expects .code() method

# 🎯 Calling with different objects
start_coding(Laptop())
start_coding(Mobile())

# ✅ Output:
# Coding using a laptop.
# Coding using a mobile.

# 📘 Example 3: Built-in function polymorphism

print(len("Python"))     # 6 (string)
print(len([1, 2, 3]))     # 3 (list)
print(len({'a': 1}))      # 1 (dict)

# 🔍 Key Points:
# - Polymorphism allows different classes to define the same method name in their own way.
# - Inheritance + method overriding = runtime polymorphism.
# - Duck Typing: "If it quacks like a duck, it’s a duck".
# - Python's dynamic typing supports flexible and powerful polymorphism.

# 🔹 Abstraction hides internal implementation details and shows only the necessary features.
# 🔹 Achieved in Python using:
#   - Abstract Base Classes (ABCs)
#   - The `abc` module
# 🔹 Abstract methods must be defined in subclasses.
# 🔹 A class containing one or more abstract methods becomes an abstract class and cannot be instantiated.

from abc import ABC, abstractmethod

# 📘 Abstract Base Class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# 📘 Concrete Class implementing abstract methods
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

    def stop_engine(self):
        print("Bike engine stopped.")

# 🎯 You cannot create an object of an abstract class
# v = Vehicle()  ❌ TypeError

# 🎯 Creating objects of subclasses
c = Car()
b = Bike()

c.start_engine()
c.stop_engine()
b.start_engine()
b.stop_engine()

# ✅ Output:
# Car engine started.
# Car engine stopped.
# Bike engine started.
# Bike engine stopped.

# 🔍 Key Points:
# - Abstraction = Hiding complex implementation and showing only necessary parts.
# - Use `abc` module and inherit from ABC.
# - Abstract methods are declared using `@abstractmethod`.
# - You cannot instantiate an abstract class.
# - Subclasses must implement all abstract methods.

# 🔹 Constructor (__init__) is a special method that runs when an object is created.
# 🔹 Destructor (__del__) is a special method that runs when an object is about to be destroyed (garbage collected).
# 🔹 Constructors are used to initialize attributes.
# 🔹 Destructors can be used to perform cleanup actions.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} created.")

    def __del__(self):
        print(f"Person {self.name} destroyed.")

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# 🎯 Creating an object
p1 = Person("Alice", 25)
p1.introduce()

# 🎯 Deleting the object explicitly
del p1

# Output example:
# Person Alice created.
# My name is Alice and I am 25 years old.
# Person Alice destroyed.

# Note: Destructor may not run immediately when `del` is called, depends on Python's garbage collection.

# 🔍 Key Points:
# - __init__() is called automatically during object creation.
# - __del__() is called when the object is about to be destroyed.
# - Use constructor for initializing attributes.
# - Destructor is rarely needed but useful for cleanup (like closing files).

# 🔹 Python does not support method overloading by default (multiple methods with same name but different parameters).
# 🔹 Method overloading can be simulated using default arguments or *args, **kwargs.
# 🔹 Operator overloading allows customizing behavior of operators (+, -, *, etc.) for user-defined classes using special methods (dunder methods).

# 📘 Simulating Method Overloading using default parameters:

class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

m = MathOperations()
print(m.add(5, 10))      # Output: 15
print(m.add(5, 10, 15))  # Output: 30

# 📘 Operator Overloading example:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2     # Calls __add__

print(p3)        # Output: Point(6, 8)

# 🔍 Key Points:
# - Python does not have built-in method overloading but uses default args to simulate.
# - Operator overloading uses special methods like __add__, __sub__, __mul__, etc.
# - These allow classes to define behavior for operators when used with objects.
# - __str__ is used to return a readable string representation of the object.

# 🔹 Instance variables belong to individual objects.
# 🔹 Class variables are shared by all instances of the class.
# 🔹 Changes to a class variable affect all instances unless overridden in an instance.

class Employee:
    # Class variable
    company = "ABC Corp"

    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary

# 🎯 Creating instances
e1 = Employee("John", 50000)
e2 = Employee("Jane", 60000)

# Accessing class variable
print(e1.company)  # ABC Corp
print(e2.company)  # ABC Corp

# Changing class variable
Employee.company = "XYZ Inc"
print(e1.company)  # XYZ Inc
print(e2.company)  # XYZ Inc

# Overriding class variable for one instance
e1.company = "Individual Corp"
print(e1.company)  # Individual Corp (instance variable now)
print(e2.company)  # XYZ Inc (still class variable)

# 🔍 Key Points:
# - Instance variables are unique to each object.
# - Class variables are shared among all objects.
# - Access class variables using ClassName.var or instance.var.
# - Assigning a value to instance.var creates/overrides instance variable.

# 🔹 Both are methods inside a class but differ in what they can access.
# 🔹 Static methods don’t access instance or class data.
# 🔹 Class methods access class variables and use the 'cls' parameter.
# 🔹 Instance methods access instance variables and use the 'self' parameter.

class Example:

    class_var = "Class Variable"

    def instance_method(self):
        # Access instance and class data
        print(f"Instance method called. {self.class_var}")

    @classmethod
    def class_method(cls):
        # Access class variable via cls
        print(f"Class method called. {cls.class_var}")

    @staticmethod
    def static_method():
        # No access to instance or class variables
        print("Static method called.")

# 🎯 Testing methods
obj = Example()

obj.instance_method()   # Instance method
Example.class_method()  # Class method
Example.static_method() # Static method

# 🔍 Key Points:
# - Instance method: first parameter is 'self', access instance & class data.
# - Class method: first parameter is 'cls', access class data, decorated with @classmethod.
# - Static method: no implicit first argument, no access to class or instance data, decorated with @staticmethod.

# 🔹 Properties allow controlled access to instance variables.
# 🔹 Use @property decorator to define a getter method.
# 🔹 Use @<property_name>.setter decorator to define a setter method.
# 🔹 Helps enforce encapsulation without changing the external interface.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Protected attribute

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot go below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

# 🎯 Usage
temp = Temperature(25)
print(temp.celsius)        # 25
print(temp.fahrenheit)     # 77.0

temp.celsius = 30          # Setting new value
print(temp.celsius)        # 30

# temp.celsius = -300      # Raises ValueError

# 🔍 Key Points:
# - Use @property to create read-only attributes or control access.
# - Setter allows validation before setting a value.
# - Properties let you use methods like attributes, maintaining interface.

# 🔹 MRO defines the order in which Python looks for methods in a hierarchy of classes.
# 🔹 Important in multiple inheritance to determine which method to call.
# 🔹 Python uses the C3 linearization algorithm for MRO.
# 🔹 You can view MRO using the __mro__ attribute or mro() method.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()   # Which show() is called?

# Output:
# B

# Explanation:
# MRO for D: D -> B -> C -> A -> object

print(D.__mro__)

# Output:
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# 🔍 Key Points:
# - MRO helps Python decide method calls in multiple inheritance.
# - Order is left-to-right depth-first with C3 linearization.
# - Use ClassName.__mro__ or ClassName.mro() to inspect MRO.

# 🔹 Exception handling manages runtime errors gracefully.
# 🔹 Use try-except blocks inside class methods to catch and handle exceptions.
# 🔹 You can define custom exceptions by inheriting from Exception.
# 🔹 Useful to make classes robust and user-friendly.

# 📘 Example: Exception handling in methods

class Calculator:
    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
            return None
        else:
            return result

calc = Calculator()
print(calc.divide(10, 2))  # 5.0
print(calc.divide(5, 0))   # Error message, returns None

# 📘 Example: Custom Exception

class NegativeValueError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeValueError("Withdrawal amount cannot be negative!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

account = BankAccount(1000)

try:
    account.withdraw(-500)
except NegativeValueError as e:
    print(f"Custom Exception: {e}")

# 🔍 Key Points:
# - Use try-except blocks inside class methods.
# - Define custom exceptions by subclassing Exception.
# - Raise exceptions using `raise` keyword.
# - Exception handling improves code reliability.

# 🔹 Both are ways to build complex objects from simpler ones.
# 🔹 Composition: Strong "has-a" relationship where the part cannot exist without the whole.
# 🔹 Aggregation: Weak "has-a" relationship where the part can exist independently.

# 📘 Composition Example:

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine (composition)

    def start(self):
        self.engine.start()
        print("Car started.")

car = Car()
car.start()

# Output:
# Engine started.
# Car started.

# 📘 Aggregation Example:

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_employees(self):
        for emp in self.employees:
            print(emp.name)

e1 = Employee("John")
e2 = Employee("Jane")

dept = Department()
dept.add_employee(e1)
dept.add_employee(e2)

dept.show_employees()

# Output:
# John
# Jane

# 🔍 Key Points:
# - Composition implies ownership; parts are created/destroyed with whole.
# - Aggregation implies a relationship without ownership; parts exist independently.
# - Composition: Car has Engine that it owns.
# - Aggregation: Department has Employees which can exist separately.

# 🔹 Python does not have explicit interfaces like some languages.
# 🔹 Abstract Base Classes (ABCs) can be used to define interfaces.
# 🔹 Classes implementing the interface must implement all abstract methods.
# 🔹 Enforces a contract for subclasses.

from abc import ABC, abstractmethod

# 📘 Interface-like Abstract Base Class
class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

# Concrete class implementing interface
class Paypal(PaymentGateway):
    def pay(self, amount):
        print(f"Paying {amount} via Paypal")

    def refund(self, amount):
        print(f"Refunding {amount} via Paypal")

class Stripe(PaymentGateway):
    def pay(self, amount):
        print(f"Paying {amount} via Stripe")

    def refund(self, amount):
        print(f"Refunding {amount} via Stripe")

# 🎯 Testing
paypal = Paypal()
paypal.pay(100)
paypal.refund(50)

stripe = Stripe()
stripe.pay(200)
stripe.refund(100)

# 🔍 Key Points:
# - Use ABCs to define interfaces with @abstractmethod.
# - Subclasses must implement all abstract methods.
# - Helps ensure consistent APIs across different implementations.

# 🔹 Mixins are a way to add reusable functionality to classes through multiple inheritance.
# 🔹 They are usually small classes that provide specific behavior.
# 🔹 Mixins don’t stand alone — they’re meant to be combined with other classes.
# 🔹 Help avoid code duplication and keep code modular.

# 📘 Example:

class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class ReprMixin:
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

class Person(JsonMixin, ReprMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)

print(p)           # Person({'name': 'Alice', 'age': 30})
print(p.to_json()) # {"name": "Alice", "age": 30}

# 🔍 Key Points:
# - Mixins provide specific reusable features.
# - Used via multiple inheritance.
# - Keep mixins focused on a single responsibility.
# - Useful to extend functionality without affecting main class hierarchy.

# 🔹 Design patterns are proven solutions to common software design problems.
# 🔹 They improve code maintainability, flexibility, and scalability.
# 🔹 Common design patterns in OOP include:

# 1. Creational Patterns: Deal with object creation.
#    - Singleton: Only one instance of a class exists.
#    - Factory: Creates objects without specifying exact class.
#    - Builder: Step-by-step object construction.

# 2. Structural Patterns: Deal with object composition.
#    - Adapter: Converts interface of one class to another.
#    - Decorator: Adds behavior dynamically to objects.
#    - Composite: Composes objects into tree structures.

# 3. Behavioral Patterns: Deal with object communication.
#    - Observer: Notifies dependents of state changes.
#    - Strategy: Defines a family of algorithms.
#    - Command: Encapsulates requests as objects.

# 📘 Example: Singleton pattern in Python

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True, both are same instance

# 🔍 Key Points:
# - Design patterns provide reusable solutions.
# - Help write cleaner, more manageable code.
# - Choose pattern based on problem context.

# 🔹 Follow SOLID principles for clean, maintainable design:
#   S - Single Responsibility: One class, one reason to change.
#   O - Open/Closed: Open for extension, closed for modification.
#   L - Liskov Substitution: Subtypes must be substitutable for their base types.
#   I - Interface Segregation: Many client-specific interfaces are better than one general.
#   D - Dependency Inversion: Depend on abstractions, not concrete classes.

# 🔹 Keep classes focused and small.
# 🔹 Use meaningful class and method names.
# 🔹 Encapsulate data; prefer private/protected variables.
# 🔹 Use inheritance and composition wisely.
# 🔹 Write clear and simple code; avoid over-engineering.
# 🔹 Document your classes and methods.
# 🔹 Test your classes thoroughly.

# Example of Single Responsibility Principle:

class Invoice:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] * item['qty'] for item in self.items)

class InvoicePrinter:
    def print_invoice(self, invoice):
        print("Invoice Details:")
        for item in invoice.items:
            print(f"{item['name']} - {item['qty']} x {item['price']}")
        print(f"Total: {invoice.calculate_total()}")

items = [
    {'name': 'Pen', 'qty': 10, 'price': 1.5},
    {'name': 'Notebook', 'qty': 5, 'price': 3}
]

invoice = Invoice(items)
printer = InvoicePrinter()
printer.print_invoice(invoice)

# 🔍 Key Points:
# - Follow SOLID principles.
# - Keep separation of concerns.
# - Encapsulate and hide complexity.
# - Test and document your OOP code.
