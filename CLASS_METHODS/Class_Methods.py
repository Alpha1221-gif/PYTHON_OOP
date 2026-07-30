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
# A method that changes a property value:
class person:
   def __init__(self,name,age):
      self.name = name
      self.age = age

   def celebrate_birthday(self):
      self.age += 1
      print(f"Happy birthday! You are now {self.age}")   

p1 = person("emil",25)
p1.celebrate_birthday()  #output = Happy birthday! You are now 26
p1.celebrate_birthday()  #output = Happy birthday! You are now 27

#---The __str__() method is a special method that controls what is returned when the object is printed:---#

# ----CODE5---- #
#Without the __str__() method:

class Person:
   def __init__(self,name,age):
      self.name = name
      self.age = age
p1 = Person("Emil",25)
print(p1)  #output = <__main__.Person object at 0x000001C7FCD98980>

# ----CODE5---- #
# With the __str__() method:

class Person:
   def __init__(self,name,age):
      self.name = name
      self.age = age

   def __str__(self):
      return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)  #output = Tobias (36)


# ----CODE6---- #
#Create multiple methods in a class:

class playlist:
   def __init__(self,name):
      self.name = name
      self.songs = []

   def add_song(self,song):
      self.songs.append(song)
      print (f"Added: {song}")

   def remove_song(self,song):
      if song in self.songs:
         self.songs.remove(song)
         print(f"Removed: {song}")

   def show_song(self):
      print(f"Playlist '{self.name}:")
      for song in self.songs:
         print(f"- {song}")

my_playlist = playlist("Favourites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_song()
'''Playlist 'Favourites:
- Bohemian Rhapsody
- Stairway to Heaven'''

# ----CODE7---- #
#Delete a method from a class:

class Person:
   def __init__(self,name):
      self.name = name

   def greet(self):
      print("hello")

p1 = Person("Emil")

del Person.greet

p1.greet() ## This will cause an error