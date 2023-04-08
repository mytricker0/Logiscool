# dictionary = {"cat":"pisica" , "chien": 19 }
# phone_numbers = {'Lucas': 9425791354, 'George': 9475248944 }
# empty = dict()
# print(dictionary["cat"]) 

# words = ["cat", "lion", "horse"]

# for word in words:
#     if word in dictionary:
#         print(word, '->' , dictionary[word])
#     else :
#         print(word, "is not in dictionary")



# animals = {
#             "cat": "Katze",
#             "dog": "Hund",
#             "horse": "Pferd"
#           }

# for key in animals.keys():
#     print(key, "->", animals[key])

# for key,value in animals.items():
#     print(key, '->', value)

# for german in animals.values():
#     print(german)

# animals["cat"] = "pisica"
# animals.update({"duck" : "canard" , "Maria": "Lion"})
# print(animals)

# animals["Patrick"] = "bg"
# print(animals)

# del animals["Maria"]
# print(animals)

# # Task 10 - Practicing dictionaries
# # create one and add a key to it
# # change a value in it

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = {}


# dic4.update(dic1)
# dic4.update(dic2)
# dic4.update(dic3)
# print(dic4)

# for i in (dic1, dic2 , dic3):
#     dic4.update(i)
# print(dic4)



# Task 12 - Complex task alone
# students' test results - names and scores
# add the name then their scores
# print average scores of the students
students = {}
while True:
    name = input("Enter the name: ")
    if name == "":
        break
    score = int(input("enter the age: "))
    if name not in students:
        students[name] = (score,)
    else : 
        students[name] += (score,)
print(students)
for name in sorted(students.keys()):
    add =0
    counter =0
    for score in students[name]:
        add += score
        counter += 1
    print(name, ":" , add/counter)

