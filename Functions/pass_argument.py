#This program demostrates an argument being
#passed to a function

def main():
     value = 5
     show_double(value)

#The show double function accepts an arguments
#and display double its value

def show_double(argument1):
    result = argument1 * 100
    print (result)

#Call funcstion main
main()
