def ex():
    myInteger = 42
    myString = "Logiscool"
    myFloat = 3.14
    myBool = True
    myList = ["apple", "orange", "pear", "kiwi"]
    myMatrix = [[4, 5, 3], [1, 9, 7], [8, 2, 6]]
    myTuple = (55, 120, 200)
    myDictionary = {"first": 1, "second": 2, "third": 3}

    def ex1():
        for i in myString:

            print(i,end= "-")
    def ex2():
        for i in myList:

            print(i,end= "-")   
    def ex3():
        for i in myDictionary.keys():
            print(i, ": ", myDictionary[i], sep="") 
    def ex4():
        myInteger = 42
        print(id(myInteger))
        myInteger = 100
        print(id(myInteger))


        print("id:", id(myList))
        myList.append(4)
        myList[0] = 999
        print("id:", id(myList))

    ex4()



def seconds_to_time():
    seconds = int(input("give me seconds: ")) # convert seconds to hours-minutes-seconds
    # no imports accepted
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    print("The exact time is: ", hours, ":", minutes, ":", seconds, sep="")


import random
def appendingList():
    list1 = [random.randint(0,100) for _ in range(random.randint(0,100))]
    print(list1)
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i]**2)
    return list2
    # return a list where every element is squared




def FonctionAvecYield():
    list1 = [random.randint(0,100) for _ in range(random.randint(0,100))]
    print ( list1)
    for i in list1:
        if i %2== 0 :
            yield i

for num in FonctionAvecYield():
    print(num, end = " ")