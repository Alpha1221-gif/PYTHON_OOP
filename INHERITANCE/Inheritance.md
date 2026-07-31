# 🐍 Inheritance in Object-Oriented Programming (OOP) using Python

Inheritance allows a new class (Child/Derived) to adopt attributes and methods from an existing class (Parent/Base). It promotes code reusability and establishes a hierarchy.

## 🔗 1. Single Inheritance
A child class inherits from a single parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} is barking."

# Usage
my_dog = Dog("Buddy")
print(my_dog.eat())   # Output: Buddy is eating.
print(my_dog.bark())  # Output: Buddy is barking.
```

## 🚀 2. The `super()` Function
The `super()` function allows the child class to call the parent class's `__init__` method or other methods to extend their functionality.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        # Call parent constructor
        super().__init__(name, age)
        self.employee_id = employee_id

# Usage
emp = Employee("Alice", 30, "E101")
print(emp.name, emp.employee_id) # Output: Alice E101
```

## 🧬 3. Multiple Inheritance
A child class inherits directly from more than one parent class.

```python
class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming deep!"

# Child class inherits from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    pass

# Usage
donald = Duck()
print(donald.fly())   # Output: Flying high!
print(donald.swim())  # Output: Swimming deep!
```

## 🪜 4. Multilevel Inheritance
A child class inherits from a parent class, which in turn inherits from another parent class.

```python
class Vehicle:
    def start(self):
        return "Vehicle started."

class Car(Vehicle):
    def drive(self):
        return "Car driving."

class ElectricCar(Car):
    def charge(self):
        return "Battery charging."

# Usage
tesla = ElectricCar()
print(tesla.start())   # From Vehicle
print(tesla.drive())   # From Car
print(tesla.charge())  # From ElectricCar
```

## 🌿 5. Hierarchical Inheritance
Multiple child classes inherit from a single parent class.

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def draw_circle(self):
        return "Drawing a circle."

class Square(Shape):
    def draw_square(self):
        return "Drawing a square."
```

## 🔄 6. Method Overriding
A child class can provide a specific implementation of a method that is already provided by its parent class.

```python
class Parent:
    def show(self):
        return "Parent's method"

class Child(Parent):
    def show(self):
        return "Child's overridden method"

# Usage
obj = Child()
print(obj.show())  # Output: Child's overridden method
```

----
🚀
**Happy Coding!** Practice these concepts by writing your own Python code.
