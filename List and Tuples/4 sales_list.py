# The NUM_DAYS constant holds the number of
# days that we will gather sales data for.
NUM_DAYS = 5

def main():
    # Create a list to hold the sales for each day.
    sales = [0] * NUM_DAYS
    # Create a variable to hold an index.
    index = 0
    print('Enter the sales for each day.')

    # Get the sales for each day.
    while index < NUM_DAYS:
        print('Day #', index + 1, ': ', sep='', end='')
        sales[index] = float(input())
        index += 1

    # Display the values entered.
    print('Here are the values you entered:')
    for value in sales:
        print(value)

# Call the main function.
main()


"""The statement in line 3 creates the variable NUM_DAYS, which is used as a 
constant for the number of days. The statement in line 8 creates a list with 
five elements, with each element assigned the value 0. Line 11 creates a 
variable named index and assigns the value 0 to it.

The loop in lines 16 through 19 iterates 5 times. The first time it iterates, 
index references the value 0, so the statement in line 18 assigns the user’s 
input to sales[0]. The second time the loop iterates, index references the value 1,
 so the statement in line 18 assigns the user’s input to sales[1]. This continues
until input values have been assigned to all the elements in the list"""