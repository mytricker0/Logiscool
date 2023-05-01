def ex1():
    myList = ["cat", "dog", "lion", "lizard", "kangaroo","ergerg","egergerg","iywegfwe","hgsdfkujshgfdv"]
    # {cat:3, dog:3, lion:4, lizard:6, kangaroo:8}
    d = {} # d est un dictionnaire vide
    for i in myList:
        d[i] = len(i)
    print(d)

    def longestWord():
        k = list(d.keys())
        v = list(d.values())
        maximum = v[0]
        max_index = 0
        for i in range(len(v)): # pour chaque valeur dans v, i est un int 
            if v[i] > maximum:
                maximum = v[i]
                max_index = i
        return k[max_index]
    def longestWord2():
        k = list(d.keys())
        v = list(d.values())
        return k[v.index(max(v))]
    print(longestWord())
    print(longestWord2())



def ex2():
    matrix = [[4, 23, 8], [2], [63, 4, 15, 16], [4, 7]]
    max_len = 0
    # for row in matrix:
    #     for item in row:
    #         print(item, end=" ")
    #     print("")
    for i in matrix:
        if len(i) > max_len:
            max_len = len(i)
    # print(max_len)
    # max_len = 4
    for j in matrix:
        k = max_len - len(j)
        
        while k > 0:
            j.append(0)
            k -= 1
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print("")
ex2()