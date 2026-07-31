# 🐍 Polymorphism in Object-Oriented Programming (OOP) using Python

Polymorphism means "many forms." It allows different classes to have methods with the same name but different implementations, letting you treat different objects through a common interface.

## 👥 1. Polymorphism with Class Methods
Different classes can have methods with identical names. You can iterate through a tuple or list of these objects and call the same method on each.

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} says Meow!"

class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} says Woof!"

# Usage
animals = [Cat("Whiskers"), Dog("Rex")]

for animal in animals:
    print(animal.make_sound())
# Output:
# Whiskers says Meow!
# Rex says Woof!
```

## ⚙️ 2. Polymorphism with Functions
You can create a standalone function that accepts any object with a specific method, enabling polymorphic behavior.

```python
def animal_sound_function(animal_object):
    print(animal_object.make_sound())

# Using the classes from the previous example
kitty = Cat("Lily")
puppy = Dog("Max")

animal_sound_function(kitty)  # Output: Lily says Meow!
animal_sound_function(puppy)  # Output: Max says Woof!
```

## 🔄 3. Method Overriding (Runtime Polymorphism)
A child class rewrites a method inherited from a parent class to change its behavior.

```python
class Bird:
    def fly(self):
        return "Most birds can fly."

class Sparrow(Bird):
    def fly(self):
        return "Sparrows fly high."

class Ostrich(Bird):
    def fly(self):
        return "Ostriches cannot fly."

# Usage
birds = [Sparrow(), Ostrich()]
for bird in birds:
    print(bird.fly())
# Output:
# Sparrows fly high.
# Ostriches cannot fly.
```

## 🧩 4. Operator Overloading
You can change how operators (like `+`, `*`, `<`, etc.) behave with custom objects by defining special "dunder" (double underscore) methods.

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading the + operator
    def __add__(self, other):
        return self.pages + other.pages

# Usage
book1 = Book(200)
book2 = Book(150)
print(book1 + book2)  # Output: 350
```

## 🦆 5. Duck Typing
Python uses dynamic typing. If an object has the required method at runtime, Python executes it, regardless of the object's actual class type ("If it walks like a duck and quacks like a duck, it's a duck").

```python
class Pterodactyl:
    def fly(self):
        return "Pterodactyl soaring through the sky!"

class Airplane:
    def fly(self):
        return "Airplane flying with jet engines!"

def lift_off(flyable_obj):
    print(flyable_obj.fly())

# Both objects work even though they share no common parent class
lift_off(Pterodactyl())  # Output: Pterodactyl soaring through the sky!
lift_off(Airplane())     # Output: Airplane flying with jet engines!
```


----
🚀
**Happy Coding!** Practice these concepts by writing your own Python code.
