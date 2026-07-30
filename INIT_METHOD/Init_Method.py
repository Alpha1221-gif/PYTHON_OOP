# ----CODE1---- #
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("tommy",32)
print(p1.name)  #output = tommy
print(p1.age)   #output = 32 

# ----CODE2---- #
# Set a default value for the age parameter:
class person:
    def __init__(self,name,age=20):  
        self.name = name
        self.age = age
p1 = person("Emil")
p2 = person("Romeo",25)

print(p1.name,p1.age) #output = Emil 20
print(p2.name,p2.age) #output = Romeo 25

# ----CODE3---- #
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Tokyo", "Japan")

print(p1.name)  #output = Linus
print(p1.age)   #output = 30
print(p1.city)  #output = Tokyo
print(p1.country)  #output = Japan


# ----CODE3---- #
# Set a default value for the name and age that name is str type and age is int type:
class person:
    def __init__(self,name:str,age:int):  
        self.name = name
        self.age = age
p1 = person("Emil",18)
p2 = person("Romeo",25)

print(p1.name,p1.age) #output = Emil 18
print(p2.name,p2.age) #output = Romeo 25