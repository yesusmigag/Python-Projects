"""Python has a built-in function named len that 
returns the length of a sequence, such as a list"""

my_list = [10, 20, 30, 40]
size = len(my_list)

my_list = [10, 20, 30, 40]
index = 0
while index < len(my_list):
  print(my_list[index])
  index += 1

""" Result
10
20
30
40
"""