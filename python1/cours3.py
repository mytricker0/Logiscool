def ex1():
    my_name = "Patrick"
    my_age = 19
    print("My name is " + my_name)
    print("My name is",my_name)
    print(f"My name is {my_name}")
    print("My name is %s" %my_name)
    print("My name is %s and I am %d years old" %(my_name,my_age))


def ex2():
    my_age = 11
    print("My age is " + str(my_age) + " years old")


def ex3():
    pet_name = "Mr.hamster"
    pet_age = 3
    pet_species = "Hamster"
    print("My first pet called: " + pet_name + " and he is " + str(pet_age) + " years old. He is a " + pet_species)
    # print( sous cette forme: mon premier animal de compagnie s'appelle pet_name, 
    # il a pet_age ans et c'est un pet_species)

def ex4():
    num = 5
    word = "cat"
    is_boy = True
    is_animal = False

    if num :
        print("it's a number")
    if word:
        print('it\'s a word ')
    if is_boy: 
        print("it's a boy")
    if is_animal:
        print("it's an animal")
    else: 
        print('It is not an animal')
import random
def ex5():
    num1 = random.randrange(0,100)
    num2 = random.randrange(0,100)
    if  num1 == num2 :
        print("they are equal")
    elif num1 > num2:
        print(f"{num1} is bigger than {num2}")
    else:
        print(f"{num1} is lower than {num2}")

def ex6():
    point = int(input("donne moi une note: "))
    if int(point) >= 90:
        print("You got an A")
    elif int(point) >= 75:
        print("You got an B")
    elif int(point) >= 60:
        print("You got an C")
    elif int(point) >= 45:
        print("You got an D")
    else : print("You got an E")
    

def exuseless():
    thing_1 = input("Give me a thing:\n")  # card
    thing_2 = input("Give me another thing:\n")  # desk
    adjective = input("Give me an adjective:\n")  # beautiful
    song_title = input("Give me a song title:\n")  # Thunderstruck
    celebrity = input("Give me a celebrity name:\n")  # Tom Holland
    feeling = input("Give me an emotion:\n")  # sad
    verb = input("Give me a verb:\n")  # cook
    place = input("Give me a place:\n")  # home
    food = input("Give me a food:\n")  # burger
    person = input("Give me person/name:\n")  # Anna

    print("""
    I just got back from a pizza party with %s. 
    Can you believe we got to eat %s pizza in %s?! 
    Everyone got to choose their own toppings. 
    I made '%s and %s' pizza, which is my favorite! 
    They even stuffed the crust with %s. How %s! 
    If that wasn't good enough already, %s was there singing %s. 
    I was so inspired by the music, I had to get up out of my seat and %s.

    """ %(person, adjective, place, food, thing_1, thing_2, feeling, celebrity, song_title, verb))

    # a little more time, but you can definitely find the variables easier in the story
    print("I just got back from a pizza party with " + person +". Can you believe we got to eat " + adjective +
        "\npizza in " + place + "?! Everyone got to choose their own toppings. I made '" + food + " and " + thing_1 +
        "'\npizza, which is my favorite! They even stuffed the crust with " + thing_2 + ". How " + feeling +
        "!\nIf that wasn't good enough already, " + celebrity + " was there singing " + song_title +
        ".\nI was so inspired by the music, I had to get up out of my seat and " + verb + ".")