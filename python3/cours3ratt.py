import math
import random
def ex1():
    print(math.pi)
    print(math.tau)
    print(math.e)
    print(math.inf)
    print(math.nan)


def cercle(rayon):
    print("La circonference du cercle est", round(rayon * math.tau, 3)," cm.")
    print("l'air du cercle est", round(math.pi * rayon**2, 3)," cm.")


# print(math.factorial(10))
# print(math.sqrt(2))


def ex2():
    numbers = []
    for i in range(100):
        numbers.append(random.randrange(90,100)) # dernier argument sert a mettre les multiples de ce nombre
    print(numbers)
    # print(math.fabs(-5))

def ex3():
    chances = 7
    solution = random.randrange(1,101)
    guess = 0
    while guess != solution and chances > 0 :
        guess = int(input("donne moi un nombre entre 1 et 100: "))
        if guess > solution:
            print("le nombre est trop grand")
        elif guess < solution:
            print("Essaye plus grand")
        else :
            print("Bien joué")
            break
        chances -= 1
        print(f"il te reste {chances} chances")
    print(f"le nombre etait {solution} :)")



def bmi(poids,taille):
    m = taille/100
    h = m**2
    bmi = round(poids/h,2)
    return bmi



dices = int(input("How many dices do you need?\n"))
max_value = int(input("What is the maximum value on the dices?\n"))
while True:
    input("Press Enter to roll the dice(s)...")
    dice_values = []
    for i in range(0, dices):
        dice_values.append(random.randint(1,max_value))
    for i in range(0, dices):
        print("The value of dice", i+1, "is", dice_values[i])