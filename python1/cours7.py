# for i in range(0,5,1): # dernier argument optionel 
#     print(i)

# for i in range(5):
#     print(i)


# pritez moi tout les nombres paires de 30 a 100
def boucles():
    for i in range(30,101,2):
        print(i)
    texte = "Bonjour a tous"
    for i in texte:
        print(i,end=" ")
def multiplicationTable():
    num = int(input("Give me a number and i'll show you its multiplication table: "))
    for i in range(1,11):
        print(f"{i} * {num} = {num*i}")

def exList():
    list_1 = []
    for i in range(1,51):
        list_1.append(i)
    print(list_1)
def slicing():
    template = "123456789"
    print(template[1:6])

# Task 10 - Generate numbers with for loop from 7 to -20
# for i in range(7,-21,-1):
#     print(i)
def namess():
    names = ["Anna", "David", "George", "Alex", "Felix", "Mike"]
    nomUtilisateur = input("Give me a name:\n")
    if nomUtilisateur not in names:
        names.append(nomUtilisateur)
        print(names)
    else :
        print("deja dedans \n",names)


def mat():
    numbers = []
    for i in range(1,11):
        for j in range(1,11):
            numbers.append(i*j)
    print(numbers)
    
    for i in range(11):
        print(numbers[i*10:(i*10)+10])
mat()
