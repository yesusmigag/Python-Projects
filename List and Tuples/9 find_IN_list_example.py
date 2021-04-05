"""This program creates a list of five highest mountains and checks another 
well-known mountain, Kilimanjaro, against the list. Fill in the missing if 
statement to display the expected output.      

Expected Output
Kilimanjaro is not on the top five list.
['Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']     """

top_five_mountains = ['Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']

if 'Kilimanjaro' not in top_five_mountains:
     print('Kilimanjaro is not on the top five list.')
else:
     print('Kilimanjaro is one of the top five tallest mountains.')
print(top_five_mountains)