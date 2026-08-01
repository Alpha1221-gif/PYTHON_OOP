# ----CODE1---- #
# Create an inner class:


class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name) #output = Outer Class


# ----CODE2---- #
# Access the inner class and create an object:


class Outer:
  def __init__(self):
    self.name = "Outer class"

  class Inner:
    def __init__(self):
      self.name = "Inner class"

    def display(self):
      print("Hello from this class")

outer = Outer()
inner = outer.Inner()
inner.display() #output = Hello from this class


# ----CODE3---- #
# Pass the outer class instance to the inner class:

class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display() #output = Outer class name: Emil


# ----CODE4---- #
# Use an inner class to represent a car's engine

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine()

  class Engine:
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()
'''Start the engine first!
Engine started
Driving the Toyota Corolla'''
