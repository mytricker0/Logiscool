def ex1():
    value = int(input('Enter an integer:\n'))
    print("the half of",value,"is",value/2)

def ex2():
    value = input("give me a number: ")
    if value.isdecimal():
        value = int(value)
        print("the half of",value,"is",value/2)
    else : 
        print("The input is not valid")


def ex3():
    try:
        value = int(input("donne moi un nombre: "))
        print("The reciprocal of",value,"is",1/value)
    except:
        print("I can't do this")

def ex4():
    try:
        value = int(input("donne moi un nombre: "))
        print("The reciprocal of",value,"is",1/value)
    except ZeroDivisionError:
        print("you tried to divide by 0. It is impossible")
    except ValueError:
        print("give me a number")
    except:
        print("I can't do this")


def ex5():
    value = int(input("Enter an Integer: "))
    if value > 0:
        print("It is a positive number")
    elif value < 0 : print("It is a negative number")

    else : print("it is 0")

def ex6():
    try:
        value = int(input("Enter an Integer: "))
        print(value/value)
    except ZeroDivisionError:
        print("Very bad input...")
    except ValueError :
        print("give me a number")
    except:
        print("Booo!")

def ex7(a,b):
    try:
        c = a/b
        print("The division of", a, "/", b, "is", c, ".")
    except TypeError:
        print("at least one of the arguments is wrong ")
    except ZeroDivisionError:
        print("Very bad input...")
    else:
        print("well done")

def ex8():
    try:
        f = open("demofile.txt")
        try:
            f.write("Ceci est un test")
        except :
            print("something went wrong when writing ")
        finally:
            print("done")
            f.close()
    except:
        print("something went wrong when opening the file ")


def ex9():
    MyList = [4,8,"paper",15,"code",16," ",23,42]   
    print(type(MyList))
    value = 0
    numbers = 0
    for i in range(len(MyList)):
        try:
            value += MyList[i]
        except TypeError:
            print(f"Cant't add {MyList[i]} to the sum")
            print(f"This value is at index {i} .")
            print("--------------")
        else : numbers +=1
    print("There are", numbers, "numbers in the list.")
    print("The sum of the numbers is", value, ".")
import 