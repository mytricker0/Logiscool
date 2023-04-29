def Hangman():
    puzzle = "ComputerScience".lower()
    my_solution = "".join("_" for i in range(len(puzzle)))
    print(my_solution)
    life = 10
    correct_letters = []
    incorrect_letters = []
    while life > 0 and puzzle != my_solution:
        print(my_solution)
        lettre = input("Donne moi une nouvelle lettre:\n->").lower()
        if len(lettre) == len(puzzle):
            print("tu essayes donc de deviner ...")
            if lettre == puzzle:
                print("Correct.")
                break
            else:
                print("Wrong guess fool")
                life -= 1
                print(f"il te reste {life} vies")
        else:
            if lettre in puzzle:  # si la lettre est dans le mot a trouver
                correct_letters.append(lettre)
                for i in range(len(puzzle)):  # on itere a travers chaque lettre de la solution finale
                    if puzzle[i] == lettre:  #
                        my_list = list(my_solution)
                        my_list[i] = lettre  # on remplace la lettre trouvee dans notre guess
                        my_solution = ''.join(my_list)  # Convert the list back to a string and update my_solution
            
            else:
                incorrect_letters.append(lettre)
                print("Wrong guess fool")
                life -= 1
                print(f"il te reste {life} vies")

Hangman()