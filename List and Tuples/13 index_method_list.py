"""The index Method
Earlier, you saw how the in operator can be used to determine whether an item is in a list. Sometimes you need 
to know not only whether an item is in a list, but where it is located. The index method is useful in these cases.
 You pass an argument to the index method, and it returns the index of the first element in the list containing 
 that item. If the item is not found in the list, the method raises a ValueError exception """


# This program demonstrates how to get the
# index of an item in a list and then replace
# that item with a new item.
 
def main():
   # Create a list with some items.
   food = ['Pizza', 'Burgers', 'Chips']
   # Display the list.
   print('Here are the items in the food list:')
   print(food)
   # Get the item to change.
   item = input('Which item should I change? ')
   try:
      # Get the item's index in the list.
      item_index = food.index(item)

      # Get the value to replace it with.
      new_item = input('Enter the new value: ')

      # Replace the old item with the new item.
      food[item_index] = new_item
      # Display the list.
      print('Here is the revised list:')
      print(food)
   except ValueError:
      print('That item was not found in the list.')

# Call the main function.
main()