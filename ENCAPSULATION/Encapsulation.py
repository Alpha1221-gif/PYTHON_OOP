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