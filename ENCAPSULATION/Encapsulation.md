# 🐍 Encapsulation in Object-Oriented Programming (OOP) using Python

Encapsulation restricts direct access to specific components of an object. It bundles data (attributes) and methods into a single unit (a class) and hides the internal state using access modifiers.

## 🔓 1. Public Members
By default, all attributes and methods in Python are public. They can be accessed from anywhere inside or outside the class.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name      # Public attribute
        self.salary = salary  # Public attribute

# Usage
emp = Employee("Alice", 50000)
print(emp.name)    # Output: Alice
print(emp.salary)  # Output: 50000
```

## ⚠️ 2. Protected Members
Protected attributes are prefixed with a single underscore `_`. This is a convention telling developers that the member should not be accessed outside the class or its subclasses, though Python does not strictly enforce it.

```python
class Company:
    def __init__(self):
        # Protected attribute
        self._project = "Internal AI Tool"

class Department(Company):
    def show_project(self):
        # Accessing protected attribute in subclass
        return f"Working on: {self._project}"

# Usage
dept = Department()
print(dept.show_project())  # Output: Working on: Internal AI Tool
# print(dept._project)      # Allowed, but strongly discouraged by convention
```

## 🚫 3. Private Members
Private attributes are prefixed with a double underscore `__`. Python strictly restricts direct external access to these members through a mechanism called **Name Mangling**.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

# Usage
account = BankAccount("Bob", 1000)
print(account.owner)  # Output: Bob
# print(account.__balance)  # Throws AttributeError
```

## 🛠️ 4. Getters and Setters
To safely view or modify private data, you use getter and setter methods. This controls how data is updated and validated.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    # Getter method
    def get_age(self):
        return self.__age

    # Setter method with validation
    def set_age(self, new_age):
        if 0 < new_age < 120:
            self.__age = new_age
        else:
            print("Invalid age values!")

# Usage
stud = Student("Sam", 20)
stud.set_age(21)
print(stud.get_age())  # Output: 21
stud.set_age(-5)       # Output: Invalid age values!
```

## 💎 5. The `@property` Decorator
Python provides a cleaner, more Pythonic way to use getters and setters without calling functions explicitly, using the `@property` decorator.

```python
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price cannot be negative.")

# Usage
item = Product(100)
item.price = 120      # Triggers the setter implicitly
print(item.price)     # Triggers the getter implicitly. Output: 120
```

## 🕵️ 6. Accessing Private Members (Name Mangling)
Behind the scenes, Python renames private attributes to `_ClassName__attributeName`. You can technically still access them using this syntax, though it is highly discouraged.

```python
class Secret:
    def __init__(self):
        self.__password = "Admin123"

# Usage
obj = Secret()
# Accessing via name mangling bypass
print(obj._Secret__password)  # Output: Admin123
```

----
🚀
**Happy Coding!** Practice these concepts by writing your own Python code.

