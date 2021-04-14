"""			      	
The program should display a menu allowing the user to select addition, 
subtraction, multiplication, or division. The final selection on the menu 
should let the user quit the program. 
Arithmetic Menu
==============
1 – Addition
2 – Subtraction
3 – Multiplication
4 – Division
5 – Quit
=================
Enter your selection? 
	
"""
#****Module\Libraries
import os
import random
import math

#*** BEGINNING OF THE PROGRAM LOGIC ****
os.system("clear")          #*** Clear screen

#Constants for the menu choices
 
addition = 1
subtraction = 2
multiplication = 3
division = 4
QUIT_CHOICE = 5


# The main function.
def main():

    #Call function 
    choiceInput()

          

def choiceInput(): 
    # The choice variable controls the loop
    choice =0

    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()
        # Get the user's choice.
        choice = int(input(f"Enter your selection? "))
        # Perform the selected action.
        if choice == addition:
           additionCalc()

        elif choice == subtraction:
           subtractionCalc()

        elif choice == multiplication:
           multiplicationCalc()

        elif choice == division:
           divisionCalc()

        elif choice ==QUIT_CHOICE:
            print(f"Exit program") 
        else:
            print(f"Error: invalid selection.")
            wait = input("")   


#The display_menu function displays a menu.
def display_menu():
    print(f"Arithmetic Menu")
    print(f"==============")
    print(f"1 – Addition")
    print(f"2 – Subtraction")
    print(f"3 – Multiplication")
    print(f"4 – Division")
    print(f"5 – Quit")
    print(f"=================")


#The function to calculate addition
def additionCalc():
  randomNumer1 = random.randint(1, 100)
  randomNumer2 = random.randint(1, 100)
  print(f"Addition")
  print(f"{randomNumer1:6,.2f}")
  print(f"+{randomNumer2:3,.2f}")
  print(f"--------")
  result = float(input(f"Enter an answer to the problem "))
  sum = randomNumer1+randomNumer2
  validationAnswer(result,sum)


#The function to calculate subtraction
def subtractionCalc():
  randomNumer1 = random.randint(1, 100)
  randomNumer2 = random.randint(1, 100)
  print(f"Subtraction")
  print(f"{randomNumer1:6,.2f}")
  print(f"-{randomNumer2:3,.2f}")
  print(f"--------")
  result = float(input(f"Enter an answer to the problem "))
  sub = randomNumer1-randomNumer2
  validationAnswer(result,sub)


#The function to calculate nultiplication
def multiplicationCalc():
  randomNumer1 = random.randint(1, 100)
  randomNumer2 = random.randint(1, 100)
  print(f"Multiplication")
  print(f"{randomNumer1:6,.2f}")
  print(f"*{randomNumer2:3,.2f}")
  print(f"--------")
  result = float(input(f"Enter an answer to the problem "))
  mult = randomNumer1*randomNumer2
  validationAnswer(result,mult)


#The function to calculate division
def divisionCalc():
  randomNumer1 = random.randint(1, 100)
  randomNumer2 = random.randint(1, 100)
  print(f"Division")
  print(f"{randomNumer1:6,.2f}")
  print(f"/{randomNumer2:3,.2f}")
  print(f"--------")
  result = float(input(f"Enter an answer to the problem "))
  divi = randomNumer1/randomNumer2
  validationAnswer(result,divi)
  

#The function to validate data
def validationAnswer(resultUser,resultOk):
  if (resultUser == resultOk):
    print(f"The answer is correct")
    wait = input("")
  else:
    print(f"The answer is incorrect")
    print(f"The corret answer is {resultOk:6,.2f}")
    wait = input("")

    
  

# Call the main function.
main()


#***** Ending program
print("\n")   
#***** END executions of the program 


