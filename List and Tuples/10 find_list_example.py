"""This program aks the user to enter a grocery item and checks it against a grocery code list. Fill in the missing if statement to display the expected output.

Expected Output
Enter an item: ice cream
The item ice cream was not found in the list."""

def main():
    # Create a list of grocery items.
    grocery_list = ['apples', 'peanut butter', 'eggs', 'spinach', 'coffee', 'avocado']
    # Search for a grocery item.
    search = input('Enter an item: ')
    # Determine whether the item is in the list.
    if search in grocery_list:
         print('The item', search, 'was found in the list.')
    else:
         print('The item', search, 'was not found in the list.')

# Call the main function.
main()