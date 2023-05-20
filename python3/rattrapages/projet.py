cours = ["sciences","math","histoire"]
import os 
from datetime import datetime, date, time


def verif():
    if not os.path.exists('Matières'):
        os.makedirs("Matières") # create directory
    for matiere in cours:
        with open(f'Matières/{matiere}', 'w'):
            pass

def addNote(matiere,note):
    now = datetime.now()
    fdate = now.strftime('%d-%m-%Y')
    if matiere.lower() in cours:
        with open(f'Matières/{matiere.lower()}', 'a') as f:
            f.write(f"{fdate} {note}")
            f.close()
    else : print("Tu as mal Ecrit un cour jpense")
def moyenne(matiere):
    if matiere.lower() in cours:
        with open(f'Matières/{matiere.lower()}', 'r') as f:
            everything = f.readlines()
            print(everything)
            f.close()
    else : print("Tu as mal Ecrit un cour jpense")
    moyenne = 0
    for i in everything:
        note = int(i.split()[1][:-3])
        # print(note)
        moyenne += note
    moyenne = moyenne/len(everything)
    print(moyenne)

if __name__ == '__main__':
    # addNote("math","12/20\n")
    moyenne("math")




