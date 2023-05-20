def ex1():
    myNum = int(input("Enter an integer:\n"))
    while myNum > 1:

        if myNum % 3 == 0:
            myNum /= 3
        else : myNum += 1
        print(myNum)

def vous(): # avec une boucle while, affichez dans le termial tt les nombres de 1 a 1000
    boolean = True
    i = 0
    while boolean:
        print(i)
        i += 1
        if i == 1000 :
            boolean = False


def ex3 () :
    myList = ["dog", "cat", "lizard", "hamster", "guinea pig", "parrot", "cameleon"]
    # print tt les elements de la liste 1 par 1 avec une boucle while 
    i = 0
    while i < len(myList):
        print(myList[i])
        i += 1
def avecfor():
    for i in range(len(myList)):
        print(myList[i])    
    for i in myList:
        print(i)


def ex4():
    basket = {'apple': 20, 'banana': 30, 'orange': 10} # Key:value
    fruit = str(input("Enter a fruit: "))
    index = 0
    for item in basket: # item est la Key
        if item == fruit: 
            print("The basket has ", basket[item], " ", item,  ".", sep="")
            break
    else:
        quantity = int(input(f"Enter the quantity of {fruit}:\n"))
        basket[fruit] = quantity # ajouter fuit:quantitée
        for item in basket:
            print(item, ": ", basket[item], sep="")


def ex5():
    def is_prime(n):
        prime = True
        for i in range(2,n):
            if n % i == 0 :
                prime = False 
        return prime
    n = int(input("tu veux les nombres premiers jusqu'a combien ? "))
    primeList = []
    i = 2
    while True:
        if is_prime(i):
            primeList.append(i)
        i += 1
        if i == n:
            break
    print(primeList)
ex5()
    
    