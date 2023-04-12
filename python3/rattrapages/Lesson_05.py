# Task 1 - Data types
myInteger = 42
myString = "Logiscool"
myFloat = 3.14
myBool = True
myList = ["apple", "orange", "pear", "kiwi"]
myMatrix = [[4, 5, 3], [1, 9, 7], [8, 2, 6]]
myTuple = (55, 120, 200)
myDictionary = {"first": 1, "second": 2, "third": 3}

# Task 2 - Print data
# string
for i in myString:
    print(i, end="")
print("\n")
# list
for i in myList:
    print(i, end=", ")
print("\n")
# matrix
for i in myMatrix:
    for j in i:
        print(j, end=" ")
    print("\n", end="")
# tuple
print("\n", end="")
for i in myTuple:
    print(i, end=", ")
print("\n")
# dictionary
for i in myDictionary.keys():
    print(i, ": ", myDictionary[i], sep="")

# Task 3 - Mutable vs immutable
myList[0] = 10
print(myList)
# The following line will cause an error
# myTuple[0] = 10
# print(myTuple)

# Task 4 - Immutable integer variable
print(myInteger)
print("id:", id(myInteger))
myInteger = 100
print(myInteger)
print("id:", id(myInteger))

# Task 5 - Id of list
print("id:", id(myList))
myList.append(4)
myList[0] = 999
print("id:", id(myList))

# Task 6 - Mutable or immutable
myTupleList = ([1, 2, 3], 4, 5, 6)
print(myTupleList)
print(id(myTupleList))
myTupleList[0][0] = 10
print(myTupleList)
print(id(myTupleList))


# Task 7 - List to string
myNewList = [4, 3, 2, 1]
myNewList = str(myNewList)
print(myNewList)
print(type(myNewList))
# Second test
for i in myNewList:
    print(i)

# Task 8 - Variable
try:
    x = float(input("Enter a number:\n"))
    y = -2*x**4 + 3*x**3 + 2*x**2 - 7*x + 4
    print("y =", y)
except ValueError:
    print("It is not a valid input.")

# Task 9 - Clock time
seconds = int(input("Enter the seconds passed today:\n"))
if seconds > 86399:
    seconds = seconds % (24*60*60)
minutes = seconds // 60
seconds = seconds % 60
hours = minutes // 60
minutes = minutes % 60
print("The exact time is: ", hours, ":", minutes, ":", seconds, sep="")


# Task 10 - Appending lists
# Solution 1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
for i in list1:
    list2.append(i**2)
print(list1)
print(list2)
# Solution 2
list2 = []
for i in range(0, len(list1)):
    list2.append(list1[i]**2)
print(list1)
print(list2)

# Task 11 - Divisibility
myList = []
for i in range(1000, 2500):
    if (i % 7 == 0) and (i % 5 != 0):
        myList.append(i)
for i in myList:
    print(i, end=", ")
