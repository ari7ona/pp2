#Python booleans
##Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)
##Example 2
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
##Example 3
print(bool("Hello"))
print(bool(15))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
##Example 4
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
##Example 5
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))
##Example 6
def myFunction() :
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")
##Example 7
x = 200
print(isinstance(x, int))

#Python operators
##Example 1
x = 5
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
##Example 2
x = 5
x += 3
x -= 3
x *= 3
x /= 3
x %= 3
x //= 3
x **= 3
x &= 3
x |= 3
x ^= 3
x >>= 3
x <<= 3
print(x)

#Python lists
##Example 1
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
##Example 2
thislist = list(("apple", "banana", "cherry"))
print(thislist)
##Example 3
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])
print(thislist[1:2])
print(thislist[:2])
##Example 4
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
##Example 5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1] = "blackcurrant"
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
##Example 6
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
##Example 7
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
##Example 8
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
##Example 9
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
##Example 10
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
##Example 11
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
##Example 12
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
##Example 13
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #The most shortest syntax
##Example 14
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
##Example 15
newlist = [x for x in range(10)]
print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
##Example 16
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)
##Example 15
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
##Example 16
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
for x in list2:
    list1.append(x)
print(list1)
list1.extend(list2)
print(list1)

#Python tuples
##Example 1
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
##Example 2
thistuple = ("apple",)
print(type(thistuple))
thistuple = ("apple") #Not a tuple, need coma to make one item tuple
print(type(thistuple))
##Example 3
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
##xample 4
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
##Example 5
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
##Example 6
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
##Example 7
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
##Example 8
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
##Example 9
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
for i in range(len(thistuple)):
    print(thistuple[i])
##Example 10
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
##Example 11
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
##Example 12
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
##Example 13
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
x = thistuple.index(8)
print(x)

#Python sets
##Example 1
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
##Example 2
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
##Example 3
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
##Example 4
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
##Example 5
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
##Example 6
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
##Example 7
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)
##Example 8
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
##Example 9
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)
##Example 10
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
##Example 11
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
##Example 12
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#Python dictionaries
##Example 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
##Example 2
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
##Example 3
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
x = thisdict.keys()
x = thisdict.values()
x = thisdict.items()
##Example 4
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
##Example 5
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
##Example 6
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
##Example 7
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
##Example 8
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
##Example 9
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)
##Example 10
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(thisdict[x])

thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict.values():
    print(x)
for x in thisdict.keys():
    print(x)
##Example 11
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x, y in thisdict.items():
    print(x, y)
##Example 12
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)
##Example 13
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)

child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily["child2"]["name"])

#Python if..else
##Example 1
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
##Example 2
if a > b: print("a is greater than b")
print("A") if a > b else print("=") if a == b else print("B")
##Example 3
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
if a > b or a > c:
    print("At least one of the conditions is True")
##Example 4
if not a > b:
    print("a is NOT greater than b")
##Example 5
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#Python while loops
##Example 1
i = 1
while i < 6:
    print(i)
    i += 1
##Example 2
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
##Example 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
##Example 4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#Python for loops
##Example 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
##Example 2
for x in "banana":
    print(x)
##Example 3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
##Example 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
##Example 5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
##Example 6
for x in range(6):
    print(x)
for x in range(2, 6):
    print(x)
for x in range(2, 30, 3):
    print(x)
##Example 7
for x in range(6):
    print(x)
else:
    print("Finally finished!")
##Example 8
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)