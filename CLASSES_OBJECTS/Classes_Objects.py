# ----CODE1---- #
class my_class:
    x = 10
print(my_class)  #output = <class '__main__.my_class'>

# ----CODE2---- #
class my_class:
    x = 10
a = my_class()
print(a.x)  #output = 10

# ----CODE3---- #
class my_class:
    x = 10
a = my_class()
del a  # Used for delete

# ----CODE4---- #
class my_class:
    x = 10
a = my_class()
b = my_class()
c = my_class()
d = my_class()
print(a.x)  #output = 10
print(b.x)  #output = 10
print(c.x)  #output = 10
print(d.x)  #output = 10