# To make a copy of a list, you must copy the list’s elements.

#Create a list.
list1 = [1, 2, 3, 4]
# Assign the list to the list2 variable.
list2 = list1

print('--------------------------')

list1 = [1, 2, 3, 4] 
list2 = list1 
print(list1) 
#display [1, 2, 3, 4]
print(list2) 
#display [1, 2, 3, 4]
list1[0] = 99 
print(list1) 
#display [99, 2, 3, 4]
print(list2) 
#display [99, 2, 3, 4]

print('--------------------------')


# Create a list with values.
list1 = [1, 2, 3, 4]
# Create an empty list.
list2 = []
# Copy the elements of list1 to list2.
for item in list1:
   list2.append(item)


print('--------------------------')

# Create a list with values.
list1 = [1, 2, 3, 4]
# Create a copy of list1.
list2 = [] + list1

print('--------------------------')
#By the end of a snippet of code, list1 and list2 will reference two separate but identical lists.
#Replace the last line in the code below to use the concatenation operator.

# Create a list with values.
list1 = [1, 2, 3, 4]
# Create a copy of list1.
list2 = [] + list1

print('--------------------------')
