# ----CODE1---- #
# Create a class with properties:
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("Rock",20)
print(p1.name) #output = ishan
print(p1.age) #output = 20

# ----CODE2---- #
# You can access object properties using dot notation:
class car:
    def __init__(self,brand,name):
        self.brand = brand
        self.name = name
car1 = car("Toyata","Fortuner")

# ----CODE3---- #
# You can modify the value of properties on objects:

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("Rock",20)
print(p1.age) #output = 20

p1.age = 26
print(p1.age) #output = 26

# ----CODE4---- #
# You can delete properties from objects using the del keyword:

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("Rock",20)
del p1.age

print(p1.name) #output = Rock
#print(p1.age)  #output = AttributeError: 'person' object has no attribute 'age'

# ----CODE5---- #
# Class property vs instance property:

class Person:
    species = "Human"  # Class property

    def __init__(self,name):
        self.name = name  # Instance property
p1 = Person("Henry")
p2 = Person("Alverd")

print(p1.name)  #output = Henry
print(p2.name)  #output = Alverd
print(p1.species)  #output = Human
print(p2.species)  #output = Human


# ----CODE6---- #
# Change a class property:
 
class per:
    lastname = ""

    def __init__(self,name):
       self.name = name
p1 = per("linus")
p2 = per("Emil")

per.lastname = "Refsnes"
print(p1.lastname)  #output = Refsnes
print(p2.lastname)  #output = Refsnes


# ----CODE7---- #
# Add a new property to an object:

class person:
    def __init__(self,name):
        self.name = name

p1 = person("tobias")

p1.age = 25
p1.city = "New York"

print(p1.name)  #output = tobias
print(p1.age)  #output = 25
print(p1.city)  #output = New York