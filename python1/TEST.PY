hauteur = int(input("Entrez la hauteur de la pyramide : ")) # Demande la hauteur de la pyramide à l'utilisateur

for i in range(1, hauteur+1): # Boucle pour parcourir les lignes de la pyramide
    print(" "*(hauteur-i), end="") # Affiche des espaces pour centrer la ligne
    print("*"*(2*i-1)) # Affiche les étoiles de la ligne
