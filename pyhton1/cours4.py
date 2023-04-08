def ex1():
    print(5 + 5)
    print(6 - 4)
    print(9 * 10)
    print(9 / 3)
    print(9 / 2)
    print(7 % 4) # 
    print(3 ** 3) #
    print(99 / 4)
    print(99 // 4) #
    print("")

def operations():
    num = 8
    print(num)
    num += 7 # num = num +7
    print(num) #
    num -= 6
    print(num)
    num *= 5 
    print(num)
    num /= 4
    print(num)
    num **= 2
    print(num)
    print("")


def comparaisons():
    print(5 < 4) # False
    print(32 > 9) #
    print(6 >= 6 ) # 
    print(6 <= 6 ) #dqfdsfqsdfq d qsdfqsd fq dsfqs df
    print(9 == 45)
    print(9 * 5 == 45)
    print()

def bizzare():
    num = 5
    num2 = 5
    print(5 == 5)
    print(num is num2)

    # print(8 is 9)
    # print(6 is "peach")
    x1 = 5
    x2 = 5
    x3 = 8
    y1 = "random name"
    y2 = "random animal"
    print(x1 is x2)
    print(x1 is x3)
    print(x1 is y1)
    print(y1 is y1)
    print(y1 is y2)


def membership():
    z1 = 'H'
    z2 = 'K'
    z3 = "world"
    z4 = "h"
    word = "Hello world"

    print(z1 in word)
    print(z2 in word)
    print(z3 in word)
    print(z4 in word.lower())


def ifstatements():
    a1 =  7# type int
    a2 =  8# type int
    if a1 < a2:
        print(str(a1) + " est plus petit que " + str(a2))
    if a1 ** a2 == a2 ** a1:
        print(a1,"^",a2,"est egal a",a2,"^",a1)
    if a1 ** a2 != a2 ** a1:
        print(f"{a1}^{a2} n'est pas egal a {a2}^{a1}")

def valide(adresse):
    
    if "@" in adresse and (adresse.endswith(".com") or adresse.endswith(".be") or adresse.endswith(".ro")):
        print("adresse mail valide ")
    else:
        print("adresse mail invalide")
# valide("monsieursyt") ctrl + / pour mettre en commentaire

def valeur(nombre):
    if nombre >= 0:
        if nombre == 0:
            print("Zero")
        else : 
            print("nombre positif")
    else : 
        print("c'est un nombre negatif ")

def leplusgrand():
    a = float(input("Enter the first number!\n"))
    b = float(input("Enter the second number!\n"))
    c = float(input("Enter the third number!\n"))
    if a > b:
        if a > c :
            print(f"{a} est le plus grand")
        elif c > a :
            print(f"{c} est le plus grand")
        else : print("il y a plusieurs nombres egaux")
    elif b > a:
        if b > c:
            print(f"{b} est le plus grand")
        elif c > b: 
            print(f"{c} est le plus grand")
        else :  
            print("il y a plusieurs nombres egaux")
    else :
        if c > b: 
            print(f"{c} est le plus grand")
        else : 
            print("il y a plusieurs nombres egaux")

