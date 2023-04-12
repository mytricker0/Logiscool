# Task 1 - Modulo 3
myNum = int(input("Enter an integer:\n"))
while myNum > 1:
    if myNum % 3 == 0:
        myNum /= 3
    else:
        myNum += 1
    print(myNum)
print(myNum)

# Task 2 - While true
boolean = True
i = 0
while boolean:
    print(i)
    i += 1
    if i == 50000:
        boolean = False

# Task 3 - While list
myList = ["dog", "cat", "lizard", "hamster", "guinea pig", "parrot", "cameleon"]
i = 0
while i < len(myList):
    print(myList[i])
    i += 1

# Task 4-5 - For loop
for i in range(0, len(myList)):
    print(myList[i])
for i in myList:
    print(i)

# Task 6 - Letters in string
myString = input("Input a string\n")
digits = 0
letters = 0
for char in myString:
    if char.isdigit():
        digits = digits + 1
    elif char.isalpha():
        letters = letters + 1
    else:
        pass
print("Letters:", letters)
print("Digits:", digits)


# Task 7 - Break, continue
def is_prime(p):
    prime = True
    for ind in range(2, p):
        if p % ind == 0:
            prime = False
            break
    return prime


n = int(input("Enter the limit of numbers:\n"))
primeList = []
i = 2
while True:
    if is_prime(i):
        primeList.append(i)
    i += 1
    if i == n:
        break
print("The prime list is:", primeList)


# Task 8 - Loop-else
basket = {'apple': 20, 'banana': 30, 'orange': 10}
fruit = input('Enter a fruit:')
index = 0
for item in basket:
    if item == fruit:
        print("The basket has ", basket[item], " ", item,  ".", sep="")
        break
else:
    quantity = int(input(f"Enter the quantity of {fruit}:\n"))
    basket[fruit] = quantity
    for item in basket:
        print(item, ": ", basket[item], sep="")

# Task 9 - Reverse a number
num = int(input("Enter an integer:\n"))
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)

# Task 10 - Matrix generator
rows = int(input("Enter the number of rows:\n"))
columns = int(input("Enter the number of columns:\n"))
myMatrix = [[0 for col in range(columns)] for row in range(rows)]
for i in range(len(myMatrix)):
    print(myMatrix[i])

# Task 11 - Valid password
import string
password = input("Enter a new password:\n")
length = False
spec_char = False
letter_char = False
digit_char = False
low = False
cap = False
for i in password:
    if i.isalpha():
        letter_char = True
    if i.isdigit():
        digit_char = True
    if i.islower():
        low = True
    if i.isupper():
        cap = True
    if string.punctuation.__contains__(i):
        spec_char = True
    if 6 <= len(password) <= 16:
        length = True
if length and spec_char and cap and low and digit_char and letter_char:
    print("This is a valid password")
else:
    print("This is not a good password")





def unAcinqe():
    while i < 50000:
        print(i)
        i += 1

unAcinqe()