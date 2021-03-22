#This program uses the return value of a function.

def main():
    #Get the users age
    first_age = int(input("Enter the age: "))
    second_age = int(input("Enter the age of you fiend: "))

    #get sum of 2 ages
    total= sum(first_age,second_age)

    #display the total age
    print("Together age is ",total, "years old")

   

# The sum function accepts two numeric arguments and returns the sum of those arguments.
def sum(num1, num2):
    result = num1+num2
    return result


# Call  main functions
main()