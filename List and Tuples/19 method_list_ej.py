"""This program creates a list of popular programming/scripting languages. Fill in the missing line for the first insert statement.

Expected Output
The list before the insert:
['Python', 'Java', 'R']
The list after the insert:
['Python', 'Java', 'c', 'R']
The list after another insert:
['Python', 'Java', 'c', 'R', 'Javascript']     """


# This program demonstrates the insert method.

def main():
    # Create a list with some programming languages.
    languages = ['Python', 'Java', 'R']

    # Display the list.
    print('The list before the insert:')
    print(languages)

    # Insert a new element.
    languages.insert(2, 'c')

    # Display the list again.
    print('The list after the insert:')
    print(languages)

    # Insert a new element.
    languages.insert(5, 'Javascript')

    # Display the list again.
    print('The list after another insert:')
    print(languages)
    
# Call the main function.
main()