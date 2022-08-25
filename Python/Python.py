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
    
