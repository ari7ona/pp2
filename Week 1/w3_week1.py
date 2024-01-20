#Python syntax
##Exercise 1
print("Hello world!")
##Exercise 2
if 5 > 2:
    print("YES")

#Python comments
##Exercise 1
#This is a comment
##Exercise 2
"""
This is a comment
written in 
more than just one line
"""

#Python Variables
##Exercise 1
carname = "Volvo"
##Exercise 2
x = 50
##Exercise 3
x = 5
y = 10
print(x + y)
##Exercise 4
x = 5
y = 10
z = x + y
print(z)
##Exercise 5
x, y, z = "Orange", "Banana", "Cherry"
##Exercise 6
x = y = z = "Orange"
##Exercise 7
def myfunc():
    global x
    x = "fantastic"

#Python data types
##Exercise 1
x = 5
print(type(x)) #int
##Exercise 2
x = "Hello World"
print(type(x)) #str
##Exercise 3
x = 20.5
print(type(x)) #float
##Exercise 4
x = ["apple", "banana", "cherry"]
print(type(x)) #list
##Exercise 5
x = ("apple", "banana", "cherry")
print(type(x)) #tuple
##Exercise 6
x = {"name" : "John", "age" : 36}
print(type(x)) #dict
##Exercise 7
x = True
print(type(x)) #bool

#Python numbers
##Exercise 1
x = 5
x = float(x)
##Exercise 2
x = 5.5
x = int(x)
##Exercise 3
x = 5
x = complex(x)

#Python strings
##Exercise 1
x = "Hello World"
print(len(x))
##Exercise 2
txt = "Hello World"
x = txt[0]
##Exercise 3
txt = "Hello World"
x = txt[2:5]
##Exercise 4
txt = " Hello World "
x = txt.strip()
##Exercise 5
txt = "Hello World"
txt = txt.upper()
##Exercise 6
txt = "Hello World"
txt = txt.lower()
##Exercise 7
txt = "Hello World"
txt = txt.replace("H","J")
##Exercise 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))




