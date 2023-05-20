myList = ["cat", "dog", "lion", "lizard", "kangaroo","654987465416"]
dictionary = {}
for i in myList: # pour chaque element dans myList
    
    #pour rajouter un élément dans un dictionnaire on utilise la syntaxe suivante : dictionnaire[clé] = valeur
    dictionary[i] = len(i)


# {'cat': 3, 'dog': 3, 'lion': 4, 'lizard': 6, 'kangaroo': 8}
def longest_word():
    k = list(dictionary.keys())
    v = list(dictionary.values())
    
    maximum = v[0]
    max_index = 0
    for i in range(len(v)): # i is int 
        if v[i] > maximum:
            maximum = v[i]
            max_index = i 
    return k[max_index]

def longest_word_2():
    k = list(dictionary.keys())
    v = list(dictionary.values())
    return k[v.index(max(v))]


# Task 3 - Uneven matrix
def matrix():
    matrix = [[4, 23, 8], [2], [63, 4, 15, 16], [4, 7]]
   
    max_value = 0
    for row in matrix:
        if len(row) > max_value:
            max_value = len(row)
    print(max_value)





    for row in matrix:
        while len(row) < max_value:
            row.append(0)
    print(matrix)



    for row in matrix: # i is list
        for item in row:
            print(item,end=" ")
        print("")
matrix()