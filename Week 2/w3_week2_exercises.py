#Python booleans
##Exercise 1
print(10 > 9) #Output will be True
##Exercise 2
print(10 == 9) #Output will be False
##Exercise 3
print(10 < 9) #Output will be False
##Exercise 4
print(bool("abc")) #Output will be True
##Exercise 5
print(bool(0)) #Output will be False

#Python operators
##Exercise 1
print(10 * 5)
##Exercise 2
print(10 / 2)
##Exercise 3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")
##Exercise 4
if 5 != 10:
    print("5 and 10 is not equal")
##Exercise 5
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

#Python lists
##Exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
##Exercise 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
##Exercise 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
##Exercise 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
##Exercise 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
##Exercise 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
##Exercise 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
##Exercise 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Python lists
##Exercise 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
##Exercise 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
##Exercise 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
##Exercise 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Python sets
##Exercise 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")
##Exercise 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
##Exercise 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
##Exercise 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
##Exercise 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Python disctionaries
##Exercies 1
car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))
##Exercise 2
car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020
##Exercise 3
car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"
##Exercise 4
car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")
##Exercise 5
car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()

#Python if..else
##Exercise 1
a = 50
b = 10
if a > b:
    print("Hello World")
##Exercise 2
a = 50
b = 10
if a != b:
    print("Hello World")
##Exercise 3
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")
##Exercise 4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")
##Exercise 5
if a == b and c == d:
print("Hello")
##Exercise 6
if a == b or c == d:
print("Hello")
##Exercise 7
if 5 > 2:
    print("YES")
##Exercise 8
a = 2
b = 5
print("YES") if a == b else print("NO")
##Exercise 9
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")

#Python while loops
##Exercise 1
i = 1
while i < 6:
    print(i)
    i += 1
##Exercise 2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1
##Exercise 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
##Exercise 4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#Python for loops
##Exercise 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
##Exercise 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
##Exercise 3
for x in range(6):
    print(x)
##Exercise 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)