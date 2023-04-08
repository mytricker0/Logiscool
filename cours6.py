def ex1():
    names = ["Anna", "Elizabeth", "George", "Tom", "Adam", "Chris"]
    matrix = [[1,2,3], [4,5,6],[7,8,9]]
    print("matrix ->",matrix, '\n'+ "names ->", names )

    print(f"le 4eme element de ma liste \"names\" est {names[3]}")

def printall():
    names = ["Anna", "Elizabeth", "George", "Tom", "Adam", "Chris"]
    for i in range(0,len(names)):
        #Grace à len(names) on peut parcourir TOUTE LA LISTE 
        print(f"le {i + 1} eme element de ma liste \"names\" est {names[i]}")

def ajouter():
    numbers = [] # ou list()
    # print(numbers)
    i = 0
    while i <= 80:
        numbers.append(i)
        i+= 1 
   
    # creer un autre liste avec que des nombres pair ou impair 
    listPair =[]
    listImpair = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0: # si pair
            listPair.append(numbers[i])
        else : 
            listImpair.append(numbers[i]) # append ajoute un element dans la liste 
    print(f"la liste pair est : {listPair} \n\net ma liste impair est {listImpair}")


def print_matrix(matrix):
    for line in matrix:
        print(line)
def dev_matrix():
    first_line = [0,1,2]
    second_line = [1,0,4]
    third_line = [2,4,0]
    matrix = [first_line,second_line,third_line]
    #print_matrix(matrix)

    V1_Vlast_distance = matrix[0][-2]
    print(f"V1_Vlast_distance : {V1_Vlast_distance}")

    V1_distances = matrix[0] #On récupère la premiere LISTE de la matrice
    print(f"V1_distances : {V1_distances}")
    print(f"type(V1_distances) : {type(V1_distances)}")
    print(f"type(V1_distances[2]) : {type(V1_distances[2])}")

    summ_distances = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"matrix[{i}][{j}] {matrix[i][j]}")
            summ_distances += matrix[i][j]
        print("Une ligne a ete parcourue")
    print(f"La somme des elements de la matrice : {summ_distances}")
#EXO BONUS : determiner la transposé MANUELLEMENT de la matrix