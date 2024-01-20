#Python syntax
##Example 1
if 5 > 2:
    print("Five is greater than two!")
##Example 2
x = 5
y = "Hello, World!"

#Python comments
##Example 1
print("Hello, World!") #This is a comment
##Exampple 2
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#Python Variables
##Example 1
x = 4
x = "Sally"
print(x)
##Example 2
x = str(3)
y = int(3)
z = float(3)
##Example 3
x = 5
y = "John"
print(type(x))
print(type(y))
##Example 4
myvar = "John"
my_var = "John" #This is correct according to PEP
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
##Example 5
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
##Example 6
x = y = z = "Orange"
print(x)
print(y)
print(z)
##Example 7
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
##Example 8
x = "Python is awesome"
print(x)
##Example 9
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)
##Example 10
x = 5
y = 10
z = "John"
print(x + y)
print (x, y)
##Example 11
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
##Example 11
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
##Example 12
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

#Python data types
##Example 1
x = "Hello World"
x = 20
x = 20.5
x = 1j
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name" : "John", "age" : 36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
x = None
##Example 2
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

#Python numbers
##Example 1
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))
##Example 2
x = 1
y = 2.8
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
##Example 3
import random
print(random.randrange(1, 10))

#Python casting
##Example 1
y = int(2.8)
x = float(1)
z = str(3.0)

#Python strings
##Example 1
a = "Hello"
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print(b)
##Example 2
a = "Hello, World!"
print(a[1])
print(len(a))
for x in "banana":
    print(x)
##Example 3
txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")
##Example 4
txt = "The best things in life are free!"
print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
##Example 5
b = "Hello, World!"
print(b[:5])
print(b[2:])
print(b[-5:-2])
##Example 6
a = "Hello, World!"
b = " Hello, World! "
print(a.upper())
print(a.lower())
print(b.strip())
print(a.replace("H", "J"))
print(a.split(","))
##Example 7
a = "Hello"
b = "World"
c = a + b
d = a + " " + b
print(c)
print(d)
##Example 8
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
##Example 9
txt = "We are the so-called \"Vikings\" from the north." #Escape character for double quotes
