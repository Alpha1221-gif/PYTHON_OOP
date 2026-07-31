'''Create a Parent Class
# Parent class is the class being inherited from, also called base class.'''

# ----CODE1---- #
# Create a class named Person, with firstname and lastname properties, and a printname method:

class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def print(self):
        print(self.fname , self.lname)
#Use the Person class to create an object, and then execute the printname method:
x = person("John", "Doe")
x.print() #output = John Doe


'''Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:'''

# ----CODE2---- #
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def print(self):
        print(self.fname , self.lname)

class student(person):
    pass

y = student("John", "Doe")
y.print() #output = John Doe


# Add the __init__() function to the Student class:
# ----CODE3---- #
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def print(self):
        print(self.fname , self.lname)

class student(person):
    def __init__(self, fname, lname):
        person.__init__(self,fname, lname)

z = student("John", "Doe")
z.print() #output = John Doe


# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# ----CODE4---- #
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def print(self):
        print(self.fname , self.lname)

class student(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

a = student("John", "Doe")
a.print() #output = John Doe


# Add a property called graduationyear to the Student class:
# ----CODE5---- #
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def print(self):
        print(self.fname , self.lname)

class student(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year

a = student("John", "Doe",2020)
print(a.graduationyear) #output = 2020


# Add a method called welcome to the Student class:
# ----CODE6---- #

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

f = Student("Mike", "Olsen", 2024)
f.welcome()
# Welcome Mike Olsen to the class of 2024