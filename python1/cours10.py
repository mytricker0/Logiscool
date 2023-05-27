def ex1():
    MyList = []
    for i in range(5):
        MyList.append(input())
    for j in MyList:
        print(j, end=' ') # end = ('\n')
        



def ex2():
    a = input()
    b = input()
    c = input()
    print(a,b,c)
    print(a,b,c,sep="*") # replace les virgules par la valeure de sep
import inquirer
import time

def ex():
    # Define the menu questions
    questions = [
        inquirer.List('menu_choice',
                    message='Select an option:',
                    choices=[
                        'Kg to lbs',
                        'lbs to KG',
                        'Celcius to Fahrenheit',
                        'Fahrenheit to Celcius'
                    ],
                    ),
    ]

    # Prompt the user with the menu questions
    answers = inquirer.prompt(questions)

    # Process the user's selection
    selected_option = answers['menu_choice']
    if selected_option == "Kg to lbs":
        value = float(input("enter the value here: "))
        print(value)
        print(f"{value} kg to lsb is : {value * 2.204623}")
        
    if  selected_option == 'lbs to KG':
        value = float(input("enter the value here: "))
        print(f"{value} lbs into Kg is : {value/2.204623}")
        
    if  selected_option == 'Celcius to Fahrenheit':
        celsius = float(input("enter the Celcius value here: "))
        print(f"{celsius} Celcius into fahrenheit is : {celsius * 1.8 + 32}")
        
    if  selected_option == 'Fahrenheit to Celcius':
        Fahrenheit = float(input("enter the Celcius value here: "))
        print(f"{Fahrenheit} Fahrenheit into Celcius is : {(Fahrenheit - 32) / 1.8}")
    
def pita(a,b):
    c = (a**2 + b **2)**(1/2)
    print(f" l'aire du triangle est {(a*b/2)}")
    print(f"les perimetre du triangle est {a + b+ c}")    
if __name__ == "__main__": # vérité absolue 
    
    while True:
        ex()
        time.sleep(3) # attendre 3 sencondes




    
    
            