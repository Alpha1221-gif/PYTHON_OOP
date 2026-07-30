# ----CODE1---- #
# Create a method in a class:

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Witard")
p1.greet()  #output = Hello, my name is Witard


# ----CODE2---- #
# Create a method with parameters:

class calculator:
  
  def add(self,a,b):
    return a+b
  
  def multiply(self,a,b):
    return a*b
calc = calculator()
print(calc.add(2,3))  #output = 5
print(calc.multiply(2,3))  #output = 6


# ----CODE3---- #
# A method that accesses object properties:
 
class person:
      def __init__(self,name,age):
         self.name = name
         self.age = age
      def info(self):
         return f"{self.name} is {self.age} years old."
p1 = person("Tobias", 28)     
print(p1.info())  #output = Tobias is 28 years old.


# ----CODE4---- #
