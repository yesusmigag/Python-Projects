# A slicing expression selects a range of elements from a sequence
#     list_name[start : end]


# Example with range [1:3]
numbers = [1, 2, 3, 4, 5] 
print(numbers) 
#display [1, 2, 3, 4, 5]
print(numbers[1:3])
print('----------------------')
#display [2, 3]


# Example with string
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
print(days)
mid_days = days[2:5]
print(mid_days)
print('----------------------')
#display ['Tuesday', 'Wednesday', 'Thursday']


#Example with range [:3] Starting index was omitted, the slice contains the elements from index 0 up to 3
numbers = [1, 2, 3, 4, 5] 
print(numbers) 
#display [1, 2, 3, 4, 5]
print(numbers[:3]) 
print('----------------------')
#display [1, 2, 3]


# Example with range [2:] Because the ending index was omitted, the slice 
# contains the elements from index 2 through the end of the list.
numbers = [1, 2, 3, 4, 5] 
print(numbers) 
#display [1, 2, 3, 4, 5]
print(numbers[2:]) 
print('----------------------')
#display [3, 4, 5]


# Example [:] Because the ending index was omitted, the slice 
# contains the elements from index 2 through the end of the list.
numbers = [1, 2, 3, 4, 5] 
print(numbers) 
#display [1, 2, 3, 4, 5]
print(numbers[:])
print('----------------------')
#display [1, 2, 3, 4, 5]


# Example [1:8:2] Slicing expressions can also have step 
# value, which can cause elements to be skipped in the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(numbers) 
#display [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1:8:2]) 
print('----------------------')
#display [2, 4, 6, 8]


#You can also use negative numbers as indexes in slicing expressions to 
#reference positions relative to the end of the list. Python adds a negative
#index to the length of a list to get the position referenced by that index.(last 5 position)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(numbers) 
#display [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(numbers[−5:])
print('----------------------')
#display [6, 7, 8, 9, 10]



"""
#Complete the program below display the following output.
#Expected Output
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[2, 4, 6, 8, 10]
[12, 14, 16, 18, 20]
[2] [20]
"""
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 
print(evens) 
print(evens[:5]) 
print(evens[5:]) 
print(evens[:1], evens[9:])
print('----------------------')

"""
Ejercice
This program lists a series of even numbers and 
then selects the number 12 to display. Fill in the 
last statement with the missing code to display the expected output.
Expected Output
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[12]
"""
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 
print(evens) 
print(evens[5:6:1])