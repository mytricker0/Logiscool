import emoji # pip install emoji
import pyjokes as pj # c'est un alias
from art import * # pip install art
import random



def ex1():
    a = 5
    print(emoji.emojize(f'Python is a {a} :star2: language.', language='alias'))
    print(emoji.emojize(':lion: :crown:', language='alias'))
    print(emoji.emojize(':monkey: :genie: :princess: :heart: :man:', language='alias'))
    print(emoji.emojize(':girl: :heart: :ogre: :rose: :prince:', language='alias'))
    print(emoji.emojize(':princess: :pick: :pick: :pick: :pick: :pick: :pick: :pick: :apple:', language='alias'))
    print(emoji.emojize(f'Python is a {a} :star2: language.', language='alias'))

def w():
    tprint("Patrick The best")
w()

# python -m pip install freegames
#python -m freegames list
#python -m freegames.{gamename}





def combinaisons():
    import time 
    seconds = time.time()
    lst = [0] * 100
    for i in range(len(lst)): # i is int
         
        for j in range(len(lst)):
            if i < j :
                print(f"{lst[i]} avec {lst[j]}")
    print("Seconds since epoch =", time.time() - seconds )	

combinaisons()