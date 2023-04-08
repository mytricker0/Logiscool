def ex1():
    """
        Cette fonction permet de prendre en main les input().
    """
    promp = input("ecrit moi un truc \n-> ")
    print(len(promp)) # len donne la longueure d'un input

    print(input("ecrit une phrase: ").split()) # argument de split peut etre n'importe quoi. 
    par defaut  c'est les espaces
    print(input("ecrit une phrase: ").count("a"))
    e = input("Give me a poem:\n")
    print(e.find('e'))

    exemple = "ah c'est bon monsieur"

    print(exemple.islower()) # isupper 
    print("is decimal: " , e.isdecimal())
    print("is numeric: " , e.isnumeric())

def ex2():
    nom_de_variable = 3
    test = "une phrase"
    avec_virgule = 0.6
    tableau = [0,1]
    di = {"key":"value"}
    print(type(di))

def print_truc():

    print("Plein de ")
    print("trucs!")
print_truc()

def ma_fonction(premier,deuxieme):
    #a,b sont des nombres
    result = (premier+deuxieme)/2
    print("result :", result)
    result+=1
    print("Fin!")
    return result #Voici ma réponse!
mon_resultat = ma_fonction(premier=1886,deuxieme=1624)
print("Voici ma valeur :", mon_resultat)