def ex1():
    d = {'x':10, 'y':20 , 'z':30}
    for dict_key , dict_value in d.items():
        print(dict_key, '->',dict_value)

def ex2():
    nums = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    for dict_key , dict_value in nums.items():
        if dict_key % 2 == 0:
            print(dict_key, '->',dict_value)
def ex3():
    d = dict()
    for x in range(1,21):
        d[x] = x**2
    return d

def ex4():
    my_dict = {'data1': 1, 'data2': 2, 'data3': 3, 'data4': 4, 'data5': 5}
    result = 1
    for key in my_dict:
        result = result * my_dict[key]
    print(result)

#ex5"
# def fact(a):
#     r = 1
#     for i in range(a,1,-1):
#         r = r*i
#     return r 
# print(fact(5))

def ex6():
    # Task 6 - Min and max of values in dictionary
    my_dict = {'x': 500, 'y': 5874, 'z': 560}
    print("Maxvalue:", max(my_dict.values()))
    print("Minvalue:", min(my_dict.values()))


def ex7():
    d = {'1': ['a', 'b'], '2': ['c', 'd']}
    print(d.values())
    a,b = d.values()
    print(a)
    print(b)
    for i in a: # vaut a au debut 
        for j in b: # vaut c
            print(i+j)

# Task 8 - Information about people
def ex8():
    people = dict()
    while True:
        person = input("What is the name of the next person?\n->")
        if person == '':
            break
        else : 
            person_list = []
            age = int(input(f"How old is {person} ? \n->"))
            gender = input("Is " + person + " a female or a male?\n\n->") 
            job = input(f"What is {person}'s job\n->")
            person_list.append(age)
            person_list.append(gender)
            person_list.append(job)
            people[person] =person_list
    for person in people.keys():
        print(person, '->', people[person])

def ex9():
    test_results = {'physics': 80, 'math': 90, 'chemistry': 86}
    key = list(test_results)
    print(key)
    for i in range(len(key)):
        print(key[i])
    del test_results['math']
    test_results['algebra'] = 7
    test_results['statistics'] = 75
    test_results['analyse'] = 89
    print(test_results)


def ex10():
    my_dict = dict()
    if len(my_dict) == 0:
        print("dict is empty")
    else: 
        print("dict isn't empty")
    




