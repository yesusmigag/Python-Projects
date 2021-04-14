import random

random1= random.randint(1,100)
random2= random.randint(1,100)

def askQuestion():

    global random1
    global random2

    #userAnswer = int(input("Enter your resp")
    userAnswer = int (input(f"{random2:3,.2f}\n" + f"{random2:3,.2f}\n" + 
     f"--------"))
    return userAnswer
 


def main():
     userAnswer = askQuestion()



main()


