"""
The remove method removes an item from the list. You pass an item to the method as an argument, 
and the first element containing that item is removed. This reduces the size of the list by one
element. All of the elements after the removed element are shifted one position toward the beginning 
of the list. A ValueError exception is raised if the item is not found in the list """


# This program demonstrates how to use the remove
# method to remove an item from a list.

def main():
    # Create a list with some items.
    food = ['Pizza', 'Burgers', 'Chips']

    # Display the list.
    print('Here are the items in the food list:')
    print(food)

    # Get the item to change.
    item = input('Which item should I remove? ')
    try:
    # Remove the item.
       food.remove(item)
       # Display the list.
       print('Here is the revised list:')
       print(food)
    except ValueError:
       print('That item was not found in the list.')

# Call the main function.
main()



print('--------------------------')

"""The del Statement the remove method you saw earlier removes a specific item from a list,
   if that item is in the list. Some situations might require you remove an element from a 
   specific index, regardless of the item that is stored at that index """


my_list = [1, 2, 3, 4, 5]
print('Before deletion:', my_list)
del my_list[2]
print('After deletion:', my_list)

#display  Before deletion: [1, 2, 3, 4, 5]
#display  After deletion: [1, 2, 4, 5]