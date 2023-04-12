# print("Welcome", "to", "Logiscool", sep="=== ", end="\n_____________\n")

def ex1():
    a = 42
    b = "apple"
    c = True
    print(a, b, c)
    print(str(a) + " " + b + " " + str(c))


def ex2():
    print(123)
    print(0o123) # octal (base 8)
    print(0x123) # hexadecimal (base 16)
    print(0b101101) # binary (base 2)

 
def ex3():
    a = 0.0002
    b = 2e-4 # 2 * 10^-4
    print(a)
    print(b)
    print(0.0000000000000000000000001)

def ex4():
    print ('c\'est la vie')




import random
def ex5():
    try: 
        for i in range(1, 10):
            a = random.randint(0, 3) # aleatoire entre 0 et 3
            b = random.randrange(0, 3) # aleatoire entre 0 et 2
            print(a, "/", b, "=", a/b)
    except ZeroDivisionError:
        print("Division par 0 impossible")
        



myInteger = 42
myString = "Logiscool"
myFloat = 3.14
myBool = True
myList = ["apple", "orange", "pear", "kiwi"]
myMatrix = [[4, 5, 3], [1, 9, 7], [8, 2, 6]]
myTuple = (55, 120, 200)
myDictionary = {"first": 1, "second": 2, "third": 3} # dictionnaire KEY : VALUE


def iteration():
    for i in myString:
        print(i, end="")
    print("\n")

    for i in myList: # i is string
        print(i, end=", ")

    for i in range(len(myList)): #i is int
        print(myList[i], end=", ")
    print("\n")

    myDictionary['Patrick'] = 4

    for i in myDictionary.keys(): 
        print(i, ": ", myDictionary[i], sep="") 

def wahtid():
    print("id:", id(myList))
    print(myList)
    myList.append(4)
    myList[0] = 999
    print(myList)
    print("id:", id(myList))

# myTupleList = ([1, 2, 3], 4, 5, 6)
# temp = list(myTupleList)
# print(temp)
# temp[2] = 46
# myTupleList = tuple(temp)
# print(myTupleList)

# myTupleList[2] = 46
# print(myTupleList)
def secc():
    seconds = int(input("Enter the seconds passed today:\n"))
    minutes = seconds // 60  # exemple secondes = 70 -> 70 // 60 = 1 minute
    seconds = seconds % 60 # exemple secondes = 70 -> 70 % 60 = 10 secondes

    hours = minutes // 60
    minutes = minutes % 60

    print("It is", hours, ":", minutes, ":", seconds, "now")



def exLists():
    myList = []
    # ajouter tout les nombres divisibles par 7 mais pas par 5  entre 1000 et 2500
    for i in range(1000, 2501):
        if i % 7 == 0 and i % 5 != 0:
            myList.append(i)
    print(myList)


def unAcinqe():
    boolean = True
    i = 0
    while boolean:
        print(i)
        i += 1
        if i == 50000:
            boolean = False


def boucle():
    i = 0
    while i < (len(myList)):
        print(myList[i])
        i += 1


def ex6():
    def is_prime(nombre):
        prime = True
        for ind in range(2,nombre):
            if nombre % ind == 0: # si mon nombre n'est pas divisibre par les nombre entre 2 et nombre-1
                prime =False
                break 
        return prime 
    
    n = int(input("Enter the limit of numbers:\n"))
    primeList = []
    i = 2
    while True:
        if is_prime(i):
            primeList.append(i)
        i += 1
        if i ==n :
            break 
    print("The prime list is:", primeList)



def forelse():
    basket = {'apple': 20, 'banana': 30, 'orange': 10}
    fruit = input('Enter a fruit:')
    index = 0
    for item in basket: # type of item is key -> string 
        if item == fruit: 
            print("The basket has ", basket[item], " ", item,  ".", sep="")
            break 
    else : 
        quantity = int(input(f"Enter the quantity of {fruit}:\n"))
        basket[fruit] = quantity
        for item in basket:
            print(item, ": ", basket[item], sep="")


def makeMatrix():
    rows = int(input("Enter the number of rows:\n"))
    columns = int(input("Enter the number of columns:\n"))

    myMatrix = [[i for i in range(0,columns)] for _ in range(rows)]
    print(myMatrix)
makeMatrix()