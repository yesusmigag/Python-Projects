""" A Python list is mutable.

#  even_numbers = [2, 4, 6, 8, 10]
#  names = ['Molly', 'Steven', 'Will', 'Alicia', 'Adriana']

# A  list can hold items of different types
# info = ['Alicia', 27, 1550.87]"""


#Print function to display an entire list
numbers = [5, 10, 15, 20]
print(numbers)

#Repetition of operator with list
#   list * n    
numbers = [1]* 5
print(numbers)
# Other example
numbers = [1,2,3]* 5
print(numbers)


# List are Mutable, which means their elements can be changed

numbers = [1, 2, 3, 4, 5]
print(numbers)
#result  [1, 2, 3, 4, 5]

numbers[0] = 99
print(numbers)
#result [99, 2, 3, 4, 5]
