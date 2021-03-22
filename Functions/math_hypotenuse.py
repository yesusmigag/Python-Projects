#This program uses the hypotenuse function in the math library on two
#numbers and stores the result in a variable named hypotenuse.
#Provide the line with the calculation.
import math

def main():

# Get the length of the triangle's two sides.
   a = float(input('Enter the side A: '))
   b = float(input('Enter the side B: '))

# Calculate the length of the hypotenuse.
   hypotenuse = math.hypot(a, b)

# Display the length of the hypotenuse.
   print('The hypotenuse of', a, 'and', b, 'is', hypotenuse)

# Call the main function.
main()