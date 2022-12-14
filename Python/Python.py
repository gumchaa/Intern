# Camel Case
variableName = 'value'
# Pascal Case
VariableName = 'value'
# Snake Case
variable_name = 'value'

# many values to multiple Variables
x, y, z = "This is x", "\nthis is y", "\nthis is z"
print(x, y, z)

#one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpacking Collection
friends = ["Ross", "Chandler", "Joey"]
x, y, z = friends
print(x)
print(y)
print(z)

#global variable
def myfunc():
    global x 
    x = "easy"
    print("Python is "+ x)
    
myfunc()
print(x)

# String Length
a = "This is a String"
print(len(a))

# Check String
txt = "This is also a string"
print("string" in txt)

if "is" in txt :
    print("yes, its present!")
    
# Check if NOT
txt = "Education was supposed to be free"
print("expensive" not in txt)

if "expensive" not in txt:
    print("Yes, its absent!")

# Slicing
txt = "Education was supposed to be free"
print(txt[0:10])

# Upper Case
a = "upper case"
print(a.upper())

# Lower Case
print(a.lower())

# String concatenate
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# F'strings

goal = "125"
league = "ucl"
stringgg = f"Lionel Messi scored {goal} goals in {league}"
print(stringgg)

# Boolean

x = ""
y = 0
print(bool(x))
print(bool(y))

x = "not empty"
y = 1
print(bool(x))
print(bool(y))

def myFun() :
    return True

if myFun() :
    print("YES!")
else:
    print("NO!")

# Lists
thisIsList = ["item1", "item2", "item3"]
print(len(thisIsList))
print(type(thisIsList))

    # list constructor
thisIsList = list(("apple","samsung","oneplus"))
print(thisIsList)

    # range
fruitList = ["apple", "kiwi", "orange", "mango", "berry", "banana"]
print(fruitList[0:3])

if "apple" in fruitList:
    print("Yes, its present")
else:
    print("Nope")
    
    # Changing item value in list
fruitList[2] = "melon"
print(fruitList)

    #  Inserting items
fruitList.insert(2, "Orange")
print(fruitList)

    # Extending List
tropical = ["mango", "pineapple", "papaya"]
fruitList.extend(tropical)
print(fruitList)

    # Removing Items
fruitList.remove("melon")
print(fruitList)

    # Poping Items
fruitList.pop()
print(fruitList)

    # Deleting Items
del fruitList[1]
print(fruitList)

    # Clearing List
print(fruitList.clear())

    # Looping through List
fruitList = ["appple", "orange", "strawberry", "kiwi", "banana"]
for fruit in fruitList:
    print(fruit)

    # Looping through the index Numbers
for i in range(len(fruitList)):
    print(fruitList[i])
    
while i < len(fruitList) :
    print(fruitList[i])
    i = i + 1
    
this_is_list = ["one", "two", "three", "four"]
[print(x) for x in this_is_list]

    # List Comprehension
fruits = ["apple", "orange", "banana", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(newlist)
newlist = []

newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = []

newlist = [x for x in fruits if x != "a"]
print(newlist)

# Tuple
thisIsTuple = ("apple", "banana", "cherry")
print(thisIsTuple)

    # tuple constructor
thistuple = tuple(("apple", "banana", "cherry", "melon"))
print(thistuple)

x = ("apple", "potato")
y = list(x)
y[1] = "kiwi"
del x, y

    # Looping through tuple
for i in range(len(thistuple)):
    print(thistuple[i])
    
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

    # Multiplying Tuples
fruittuple = ("apple", "banana", "cherry", "berry")
ttuppllee = fruittuple * 2

print(ttuppllee)

    # Methods 
print(ttuppllee.count("apple"))

# Set
thisIsSet = {"apple", "orange", "banana", "cherry"}
print(thisIsSet)

print(len(thisIsSet))
print(type(thisIsSet))

    # Set Constructor
thisSet = set(("one", "two", "three", "four"))
print(thisSet)

    # Adding items to set
thisSet.add("five")
print(thisSet)

thisSet.update(thisIsSet)
print(thisSet)

    # Removing items from Set
thisSet.remove("apple")
print(thisSet)

thisSet.discard("two")
print(thisSet)

thisSet.pop()
print(thisSet)

    # Deleting or Clearing a Set
thisSet.clear()
print(thisSet)

thisSet = {"one","two"}
"""del thisSet"""

print(thisSet)

    # Loopig through Set

print(thisIsSet)

for x in thisIsSet:
    print(x)

    # Joining two sets
set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3, 4}

set3 = set1.union(set2)
print(set3)
set4 = {"p" ,"q", "r", "s"}
set4.update(set3)
print(set4)

    # intersection and others
x = {"axe", "sword", "knife", "hammer"}
y = {"axe", "archer", "bow", "knife"}
z = x.intersection(y)

x.intersection_update(y)

print(x)
print(z)

q = {"box", "letter", "pen"}
p = {"pen", "ballpen", "fountain pen"}
r = q.symmetric_difference(p)
q.symmetric_difference_update(p)

print(q)
print(r)

# Dictionary
thisDict = {
    "brand": "apple",
    "series": "iPhone",
    "model": "12",
    "year": 2020
}
print(thisDict)
print(len(thisDict))
print(type(thisDict))

    # Accessing Dictionary Items
x = thisDict["model"]
print(x)
y = thisDict.get("year")
print(y)
print(thisDict.keys())
print(thisDict.values())
if "model" in thisDict:
    print("yes, its present")

    # Changing & Updating Dict
thisDict["model"] = "13"
thisDict.update({"year": 2021})
print(thisDict)

thisDict["color"] = "red"
thisDict.update({"storage": "128gb"})
print(thisDict)

    # Removing Items from Dict
thisDict.pop("storage")
thisDict.popitem()
del thisDict["model"]
print(thisDict)

    # Clearing and Deleting a dict
thisDict.clear()
print(thisDict)
del thisDict

    #Looping through Dict
thisDict = {
    "brand": "Volkswagen",
    "model": "Polo",
    "edition": "Gt"
}
for x in thisDict:
    print(x)

for x in thisDict:
    print(thisDict[x])

for x in thisDict.values():
    print(x)

for x, y in thisDict.items():
    print(x,": ", y)

    # Dict Methods
v_Dict = thisDict.copy()
print(v_Dict)

    # Nested Dict
maleFriends = {
    "friend1" : {
        "name": "Joey",
        "job": "Actor"
    },
    "friend2" : {
        "name": "Chandler",
        "job" : "transponster"
    },
    "friend3" : {
        "name": "Ross",
        "job" : "Paleontologist"
    }
}
print(maleFriends)
friend1 = {
    "name": "Monica",
    "job": "Chef"
}
friend2 = {
    "name": "Rachel",
    "job": "fashion"
}
friend3 = {
    "name": "Pheobe",
    "job": "masseuse"
}

femaleFriends = {
    "friend1" : friend1,
    "friend2" : friend2,
    "friend3" : friend3
}
print(femaleFriends)

# Conditions & if Statements

a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b :
    print("a and b are equal")
else:
    print("a is grater than b")

    # short hand method
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a==b else print("B")

    #Using Logical Operators
a = 200
b = 33
c = 500

print("Both condtions are True") if a>b and c>b else 0

print("At least one of the condition is true") if a>b or a>c else 0

    # Nested if 
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

a = 33
b = 200

if a > b:
    pass

# While Loops
i = 1
while i < 6:
    print(i)
    i += 1
    
    # Break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

    # Continue statement
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
    
# For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        continue
    print(x)
    
    # Looping through range
for x in range(2, 10, 2):
    print(x)
    
for x in range(3, 30, 3):
    print(x)
else:
    print("finally Finished")
    
for x in range(6):
    if x == 3: break
    print(x)
else: 
    print("Finally Finished!")
    
    # Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
        
for x in [0, 1, 2]:
    pass

# Functions

def thisFunction():
    print("\" hello From the other side \"")
    
thisFunction()

def thisfunction(fname):
    print(fname + " Uchiha")
    
thisfunction("Sasuke")
thisfunction("Ithachi")

def thisIsfunction(ninja):
    for i in range(0, 3):
        print("the best ninja is " + ninja[i])
    
ninjas = ["kakashi", "naruto", "guy"]
thisIsfunction(ninjas)

    # Returning Values
def multiplesOf5(x):
    return 5 * x

print(multiplesOf5(10))