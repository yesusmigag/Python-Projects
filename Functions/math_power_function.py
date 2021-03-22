#This program uses the power function in the math library on two numbers and stores 
# the result in a variable amed powered. Provide the line with the calculation.
import math

def main():

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter a number: '))

    # Calculate num_1 to the power of num_2. 
    powered = pow(num1,num2)

    print('The result of', num1, 'raised to the power of', num2, 'is', powered)

main()