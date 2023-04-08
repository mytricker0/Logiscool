def ex2():
    var = "ceci est une phrase"
    print(len(var))
    print(var.split())
    inp = int(input("donne moi un nombre: "))
    print(inp)
    print(var.count("e"))
    print(var.find("une"))

    # If it returns True, then the text starts/ends with that character, 
    # if not then it returns False
    print(input("Give me a poem:\n").startswith('M'))
    print(input("Give me a poem:\n").endswith('w'))
    print(input("Give me a poem:\n").isdecimal())
    print(input("Give me a poem:\n").isnumeric())
    print(input("Give me a poem:\n").isalpha())
    print(input("Give me a poem:\n").isupper())
    print(input("Give me a poem:\n").islower())



    age = 19
    age = 20 
    print(age)
    age = 32
def ex1():
    pet_1_age = 3
    pet_1_weight = 32.2
    age = 6
    jobtype = "Senior programmer"
    weight = 48.9


    print(age) # 6
    print(float(age)) # 6.0


    print(weight)
    print(int(round(weight)))


def main(arg):
    print(arg*2)
main("123456")




def test():
    pass