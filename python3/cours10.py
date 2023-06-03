# def noParameters():
#     return [2,5]


# myList = noParameters()
# print(myList)


# def avecPar(p,q):
#     print(f"p is {p} and q is {q}")
#     return p*q

# print(avecPar(2,3))
# print(avecPar(q=8,p=5))
# print(avecPar(2,q=3))



def ex1(lst): # remove second smalest element from list 
    srt = sorted(lst)
    print(srt)
    srt.pop(1)
    print(srt)

def removeEven(lst):
    for i in lst:
        if i % 2 == 0 :
            lst.remove(i)
    print(lst)
testlist= [1,5,9,3,6,5,7,2,4,5]
removeEven(testlist)

def matrixSum(mtx):
    summ = 0
    for i in mtx: # i is list 
        for j in i: # j is int 
            summ += j  
    return summ


ml = [[1, 2], 
      [3, 4], 
      [5, 6], 
      [7, 8]]


mynumber = 45946231978646453210123456789

# def sum_digits(number):
#     summ = 0
#     number = str(number)
#     for i in number:
#         summ += int(i)
#     print(summ)
    
def f(number):
    print(number)
    if number == 0:
        return 0
    else:
        return number % 10 + f(int(number / 10)) # 2 + 1 + 0 + 0
print(f(12))
    
    


def unique_character(string): # return {key : character, valueur: nb} d'occurences dans le string 
    frequency = {}
    string = string.lower()
    for i in string: # i is character 
        if i not in frequency:
            # frequency[key] = value
            frequency[i] = 1
        else : 
            frequency[i] += 1
    print(frequency)
    user = input("give me a character : ")
    print(f"{user} is present {frequency[user]} times in the dictionnary")
            
        
ex = "Patrick,Emma,Maria,iyqrgfliREGQEFRGKJhjgfuyfkuevflzjkgflizfb"
unique_character(ex)