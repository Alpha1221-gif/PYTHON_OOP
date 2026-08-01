# ----CODE1---- #
# Create a private class property named __age:

class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  # Private property
 
p1 = person("emil",25)
print(p1.name)  #emil
#print(p1.__age)  # This will cause an error


# ----CODE2---- #
# Use a getter method to access a private property:

class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  # Private property
    def get_age(self):
        return self.__age
    
p1 = person("emil",25) #output = emil
print(p1.get_age())  #output = 25


# ----CODE3---- #
#use setter method to change a private property:

class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  # Private property

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if (age > 0):
            self.__age = age
        else:
            print("Age must be positive")

p1 = person("emil",25) #output = emil
print(p1.get_age())  #output = 25

p1.set_age(30)
print(p1.get_age()) #output = 30


# ----CODE4---- #
# Use encapsulation to protect and validate data:

class Student:
    def  __init__(self,name):
        self.name = name
        self.__grade = 0

    def set_grade(self,grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 1 to 100")

    def get_grade(self):
        return self.__grade

    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade()) #output = 85
print(student.get_status()) #output = Passed


# ----CODE5---- #
# Create a protected property:

class person:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary

p1 = person("Emil",25000)
print(p1.name)  #output = Emil
print(p1._salary) # Can access, but shouldn't
#output = 25000


# ----CODE6---- #
# Create a private method:

class calculator:
    def __init__(self):
        self.result = 0

    def __validate(self,num):
        if not isinstance(num,(int,float)):
            return False
        return True

    def add(self,num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid no.")

calc = calculator()
calc.add(10)
calc.add(50)
print(calc.result)  #output = 60

# ----CODE7---- #
# See how Python mangles the name:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!
#output = 30