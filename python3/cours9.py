imyList = ["cat", "dog", "lion", "lizard", "kangaroo"]
def ex1():
    #{'cat': 3, 'dog': 3, 'lion': 4, 'lizard': 6, 'kangaroo': 8}
    dictionary = {}
    for i in myList:
        # d['mynewkey'] = 'mynewvalue'
        dictionary[i] = len(i)
    print(dictionary)
    def ex2():
        k = list(dictionary.keys())
        v = list(dictionary.values())
        print(k,v)
        maxi = v[0]
        max_index = 0
        for i in range(len(v)): # i is int 
            if v[i] > maxi :
                maxi = v[i]
                max_index = i
        return k[max_index]
    
    def longest_word_2():
        k = list(dictionary.keys())
        v = list(dictionary.values())
        return k[v.index(max(v))]
    
            
        
def matrices():
    matrix = [[4, 23, 8], [2], [63, 4, 15, 16], [4, 7]]
    max_len = 0 # equivalent a la longueure max
    for row in matrix:
        for i in row:
            print(i,end=" ")
        print("")
    for i in matrix:
        if len(i) > max_len:
            max_len = len(i)
    for k in matrix:
        print(k)
        if len(k) < max_len:
            toApend = max_len - len(k)
            for _ in range(toApend):
                k.append(0)
                
    for row in matrix:
        for i in row:
            print(i,end=" ")
        print("")
             
        
    
        
matrices()