"""
This program creates three lists, each by adding on the prior one in some way.
Fill in the statement to create list3 where indicated to match the expected output.

Expected Output
[9, 11, 13, 15]
[9, 11, 13, 15, 17, 19, 21, 23]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]   """

# Create a list with values.
list1 = [9, 11, 13, 15]
print(list1)
# Add list1 to the beginning of list2.
list2 = list1 + [17, 19, 21, 23]
print(list2)
# Add list2 to the end of list3 below. 
list3 = [1, 3, 5, 7] + list2
print (list3)