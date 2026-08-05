# 🐍 Python Object-Oriented Programming (OOP)

Welcome to the **Python OOP** repository! This repository serves as a comprehensive guide and code reference for mastering Object-Oriented Programming principles in Python.

---
### ⚠️ Important Note for Beginners
> 💡 **New to Python?** If you are completely new to coding or don't know the core syntax of Python yet, please stop here and learn basic Python first! Data Structures require a strong grasp of loops, functions, and conditional statement etc.
> 
> I have built a dedicated repository covering all fundamental concepts, syntax, and foundational exercises:
> 🔗 **[Explore the BASIC_PYTHON Repository Here](https://github.com/Alpha1221-gif/BASIC_PYTHON)** 👈

---
## 📚 Table of Contents

- [🐍 Python Classes/Objects](#-python-classesobjects) #CLASSES_OBJECTS
- [⚙️ Python `__init__` Method](#️-python-__init__-method)
- [🎯 Python self Parameter](#-python-self-parameter)
- [💎 Python Class Properties](#-python-class-properties)
- [🛠️ Python Class Methods](#️-python-class-methods)
- [🌿 Python Inheritance](#-python-inheritance)
- [🎭 Python Polymorphism](#-python-polymorphism)
- [🔒 Python Encapsulation](#-python-encapsulation)
- [📦 Python Inner Classes](#-python-inner-classes)

---

## 🔍 Topic Overviews & Code Snippets

### 🐍 Python Classes/Objects
A class is a blueprint or template for creating objects. An object is an instance of a class containing real values.

```python
class Car:
    pass

# Creating an object
my_car = Car()
```

### ⚙️ Python `__init__` Method
The `__init__` method is the constructor in Python. It automatically runs when a new object of a class is instantiated to initialize attributes.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

### 🎯 Python self Parameter
The `self` parameter represents the specific instance of the class currently being modified or accessed. It binds attributes to the given argument.

```python
class Car:
    def display_info(self):
        print(f"This is a {self.brand} {self.model}.")
```

### 💎 Python Class Properties
Properties allow you to define getters, setters, and deleters using the `@property` decorator, enabling controlled access to private variables.

```python
class Car:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
```

### 🛠️ Python Class Methods
Class methods take `cls` as the first argument instead of `self`. They are bound to the class itself rather than individual instances and are defined using the `@classmethod` decorator.

```python
class Car:
    total_cars = 0

    @classmethod
    def increment_count(cls):
        cls.total_cars += 1
```

### 🌿 Python Inheritance
Inheritance allows a new child class to adopt the attributes and methods of an existing parent class, promoting code reusability.

```python
class Vehicle:
    def start(self):
        return "Engine started"

class Car(Vehicle):  # Car inherits from Vehicle
    pass
```

### 🎭 Python Polymorphism
Polymorphism means "many forms." It allows different classes to share the same method names but exhibit unique behaviors during runtime.

```python
class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

def animal_sound(animal_object):
    print(animal_object.speak())
```

### 🔒 Python Encapsulation
Encapsulation restricts direct access to specific object data and methods to prevent accidental modification, typically implemented using single `_` or double `__` underscores.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance
```

### 📦 Python Inner Classes
An inner (or nested) class is a class defined inside another class, logical grouping when a class's existence depends entirely on another.

```python
class Outer:
    def __init__(self):
        self.inner = self.Inner()

    class Inner:
        def display(self):
            print("Inside inner class")
```

---

## 🚀 How to Run the Files

1. Open your terminal or command prompt in your local project folder.
2. Run any specific script using Python:
   ```bash
   python script_name.py
   ```

----
🚀
**Happy Coding!** Practice these concepts by writing your own Python code.
