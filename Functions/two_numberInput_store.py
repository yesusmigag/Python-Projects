#This program multiplies two numbers and stores them into a variable named product. 
#Complete the missing code to display the expected output.

# multiply two integers and display the result in a function
def main():
    val_1 = int(input('Enter an integer: '))
    val_2 = int(input('Enter another integer: '))
    multiply(val_1, val_2)
    
def multiply(num_1, num_2):
    product = num_1*num_2 
    print ('The result is', product)

main()