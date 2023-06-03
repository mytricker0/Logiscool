def new_file():
    my_file = open("task1.tax", "w+") # w = overwrite, w+
    # https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
    my_file.write("Try not! Do, or do not. There is no try. - Yoda\n")
    my_file.seek(0)
    print(my_file.read())
    my_file.close()
    
def new_line():
    my_file = open("task1.tax", "a+", encoding='utf-8')
    my_file.write("\Ђ")
    my_file.seek(0)
    allLines = my_file.readlines()
    for line in allLines:
        print(line)
        
def letter_count(p=' '):
    my_file = open("task1.tax", "r", encoding='utf-8')
    counter = 0 
    for i in my_file.read(): # file.read() -> contenu du fichier | i is character
        
        if i.lower() == p : 
            counter +=1 
    if p == ' ':
        print(f"there are {counter} words in the file")
    else :
        print(f"there are {counter} {p} in the file")

def list_file():
    shopping_list = ["bread\n", "milk\n", "cheese\n", "apple\n"]
    my_file = open("task1.tax", "w+", encoding='utf-8')
    my_file.writelines(shopping_list) # at the end of writelines, the stream is placed at the 
    # end of the file
    my_file.seek(0)
    print(my_file.read())

def remove_items(p=' '):
    my_file = open("task1.tax", "r+", encoding='utf-8')
    lines = my_file.readlines()
    my_file.seek(0)
    for line in lines:
        if line.strip("\n") != p:
            my_file.write(line)
        my_file.truncate() #Optional argument. The size of the file (in bytes) after the truncate. 
                            #Default None, which means the current file stream position.
    my_file.seek(0)
    print(my_file.read())
    
def drawing():
    draw = open("Drawfile.ro", "w+")
    for i in range(10):
        j = 0
        while j <10:
            for k in range(j):
                draw.write("-")
            
            for k in range(10-j):
                draw.write("+")
            draw.write('\n')
            j+=1
        while j > 0:
            for k in range(j):
                draw.write("-")
            
            for k in range(10-j):
                draw.write("+")
            draw.write('\n')
            j -=1
    draw.seek(0)
    print(draw.read())
    
    

if __name__ == '__main__':
    drawing()
    
#  ``r''   Open text file for reading.  The stream is positioned at the
#          beginning of the file.

#  ``r+''  Open for reading and writing.  The stream is positioned at the
#          beginning of the file.

#  ``w''   Truncate file to zero length or create text file for writing.
#          The stream is positioned at the beginning of the file.

#  ``w+''  Open for reading and writing.  The file is created if it does not
#          exist, otherwise it is truncated.  The stream is positioned at
#          the beginning of the file.

#  ``a''   Open for writing.  The file is created if it does not exist.  The
#          stream is positioned at the end of the file.  Subsequent writes
#          to the file will always end up at the then current end of file,
#          irrespective of any intervening fseek(3) or similar.

#  ``a+''  Open for reading and writing.  The file is created if it does not
#          exist.  The stream is positioned at the end of the file.  Subse-
#          quent writes to the file will always end up at the then current
#          end of file, irrespective of any intervening fseek(3) or similar.