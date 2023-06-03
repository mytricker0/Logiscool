# Task 1 - Create, open, write, read files
def new_file():
    my_file = open("task1_file.txt", "w+")
    my_file.write("Try not! Do, or do not. There is no try. - Yoda\n")
    my_file.seek(0)
    print(my_file.read())
    my_file.close()


new_file()


# Task 2 - Add new line, read lines
def new_line():
    my_file = open("task1_file.txt", "a+", encoding="utf-8")  # encoding for the ' sign
    my_file.write("Who’s the more foolish: the fool or the fool who follows him? - Obi-Wan Kenobi")
    my_file.seek(0)
    for line in my_file.readlines():
        print(line)
    my_file.close()


new_line()


# Task 3 - Counting specific characters in the file
def letter_count(p):
    my_file = open("task1_file.txt", "r+")
    letter_counter = 0
    for i in my_file.read():
        if i.lower() == p:
            letter_counter += 1
    if p == " ":
        print("There are", letter_counter, "words in the text file.")
    else:
        print("There are", letter_counter, p, "in the text file.")
    my_file.close()


letter_count("w")


# Task 4 - Add list to new file
def list_file():
    shopping_list = ["bread\n", "milk\n", "cheese\n", "apple\n"]
    shopping_file = open("myShoppingFile.txt", "w+")
    shopping_file.writelines(shopping_list)
    shopping_file.seek(0)
    print(shopping_file.read())


list_file()


# Task 5 - Remove rows from shopping list
def remove_items(p):
    shopping_file = open("myShoppingFile.txt", "r+")
    lines = shopping_file.readlines()
    shopping_file.seek(0)
    for line in lines:
        if line.strip("\n") != p:
            shopping_file.write(line)
        shopping_file.truncate()
    shopping_file.seek(0)
    print(shopping_file.read())


remove_items("cheese")


# Task 6 - Draw in file
def drawing():
    draw = open("drawFile.txt", "w+")
    for i in range(10):
        j = 0
        while j < 10:
            for k in range(j):
                draw.write("-")
            draw.write("  ")
            for k in range(10-j):
                draw.write("-")
            draw.write("\n")
            j += 1
        while j > 0:
            for k in range(j):
                draw.write("-")
            draw.write("  ")
            for k in range(10-j):
                draw.write("-")
            draw.write("\n")
            j -= 1
    draw.seek(0)
    print(draw.read())


drawing()


# Task 7 - Concat multiple files into dictionary
def ages_of_people():
    names = open("names.txt", "r")
    ages = open("ages.txt", "r")
    pairs = {}
    my_names = names.readlines()
    my_ages = ages.readlines()
    for i in range(len(my_ages)):
        pairs[my_names[i].strip("\n")] = int(my_ages[i].strip("\n"))
    print(pairs)


ages_of_people()


# Task 8 - Concat multiple files into new file
def ages_of_people_2():
    names = open("names.txt", "r")
    ages = open("ages.txt", "r")
    pairs = open("pairs.txt", "w+")
    my_names = names.readlines()
    my_ages = ages.readlines()
    for i in range(len(my_ages)):
        pairs.write(my_names[i].strip("\n"))
        pairs.write(": ")
        pairs.write(my_ages[i].strip("\n"))
        pairs.write("\n")
    pairs.seek(0)
    print(pairs.read())


ages_of_people_2()


# Task 9 - Short words in file
def poem_words():
    my_poem = open("poem.txt", "r")
    my_text = my_poem.read()
    words = my_text.split()
    for word in words:
        if len(word) < 4:
            print(word, end=", ")


poem_words()