def ex1():
    myNum = int(input("Enter an integer: "))
    while myNum > 1 :
        if myNum % 3 == 0 :
            myNum /= 3
        else : 
            myNum += 1
    print(myNum)

def ex2(): # print moi tout les elements dans le terminal
    myList = ["dog", "cat", "lizard", "hamster", "guinea pig", "parrot", "cameleon"]
    i = 0
    while i < len(myList) :
        
        print(myList[i])
        i +=1
def ex3():
    myList = ["dog", "cat", "lizard", "hamster", "guinea pig", "parrot", "cameleon"]
    for i in range(0, len(myList)): # i is int 
        print(myList[i])

    for i in myList: # i is str 
        print(i)

def ex4():
    def is_prime(p):
        prime = True
        for ind in range(2,p):
            if p % ind == 0:
                prime = False 
                break
        return prime # booleen
    n = int(input("Enter the limit of a number:\n-> "))
    primeList = []
    i = 2
    while True:
        if is_prime(i):
            primeList.append(i)
        i += 1
        if i == n:
            break
    print(primeList) 



def ex5():
    basket = {'apple': 20, 'banana': 30, 'orange': 10}
    fruit = input('Enter a fruit:')
    index = 0
    for item in basket: # for all keys in basket 
        if item == fruit:
            print("The basket has ", basket[item], " ", item,  ".", sep="") 
            break
        # value : basket[item] && key: item
    else : 
        quantity = int(input(f"Enter the quantity of {fruit}:\n"))
        basket[fruit] = quantity
        for item in basket:
            print(item, ": ", basket[item], sep="")

ex5()