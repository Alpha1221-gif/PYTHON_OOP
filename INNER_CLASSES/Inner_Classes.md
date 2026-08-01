# 🐍 Python Inner Classes (Object-Oriented Programming)

An **inner class** (or nested class) is a class defined entirely inside the scope of another outer class. This pattern structure is ideal when a secondary class exists solely to serve or support the primary class.

---

## 🛠️ Complete Code Example

This executable script shows how to structure, instantiate, and use inner classes in Python.

```python
class Car:
    """Outer class representing a vehicle."""
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        # 1. Standard approach: Instantiate inner class inside outer constructor
        self.engine = self.Engine(horsepower=250)

    def display_specs(self) -> str:
        return f"{self.brand} {self.model} with a {self.engine.get_specs()} engine."

    class Engine:
        """Inner class serving the Car class."""
        def __init__(self, horsepower: int):
            self.horsepower = horsepower
            self.status = "Stopped"

        def start(self) -> str:
            self.status = "Running"
            return "Engine started... vroom!"

        def get_specs(self) -> str:
            return f"{self.horsepower} HP"


if __name__ == "__main__":
    # Method A: Standard usage via the outer class instantiation
    my_car = Car("Tesla", "Model S")
    print(my_car.display_specs())
    print(my_car.engine.start())

    # Method B: Direct explicit instantiation using Outer class namespace
    standalone_engine = Car.Engine(horsepower=400)
    print(f"Custom engine built: {standalone_engine.get_specs()}")
```

---

## 💡 Key Conceptual Pillars

* 🧩 **Encapsulation:** Groups dependent components together cleanly inside a localized scope.
* 📦 **Namespace Isolation:** Prevents class name collisions in the global file.
* 🏗️ **Logical Relationships:** Ideal for strict Parent-Child configurations (e.g., Head-Brain, Order-Item).
* ⚙️ **Maintainability:** Makes codebases easier to refactor by keeping tightly coupled logic contained.

---

## 🚀 Advanced Concepts

### 1. Accessing Outer Class Attributes
By default, a Python inner class does **not** have access to the outer class instance variables. To bridge this gap, you must explicitly pass the outer class's `self` instance to the inner class initialization method.

```python
class Outer:
    def __init__(self, name):
        self.name = name
        # Pass 'self' (the outer object instance) to the inner class
        self.inner = self.Inner(self)

    class Inner:
        def __init__(self, outer_instance):
            self.outer = outer_instance

        def print_outer_name(self):
            # Accessing the outer class variable successfully
            print(f"Outer name is: {self.outer.name}")
```

### 2. Multiple Levels of Nesting
Python allows you to nest inner classes inside other inner classes deep down the chain, though nesting beyond two layers is generally discouraged to prevent overly complex structures.

```python
class Universe:
    class Galaxy:
        class Star:
            def shine(self):
                return "Twinkle!"
```

---

## ⚠️ Important Implementation Gotchas

* 🚫 **No Automatic Reference:** Inner classes do not implicitly inherit or link to parent attributes without structural mapping.
* 📉 **Inheritance Limits:** Inheriting from an inner class inside other modules requires verbose namespacing (`Outer.Inner`).
* 🧹 **Readability Costs:** Overuse of nested classes can make files bloated and break the "flat is better than nested" guideline of the Zen of Python.

----
🚀
**Happy Coding!** Practice these concepts by writing your own Python code.
