"""Given:
 * a variable current_members that refers to a list, and
 * a variable member_id that has been assigned a value.
Write some code that assigns True to the variable is_a_member if the value assigned 
to member_id can be found in the current_members list. Otherwise, assign False to 
is_a_member. In your code, use only the variables current_members, member_id, and 
is_a_member.     """

current_members = [2, 3, 5, 6, 7, 10]
member_id = 5

if member_id in current_members:
    is_a_member = True
else:
    is_a_member = False
print(is_a_member)
