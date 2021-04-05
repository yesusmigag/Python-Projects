'''The Springfork Amateur Golf Club has a tournament every weekend. The club president has 
asked you to write a program that will read each player's name and score as keyboard input, 
and then save these as records in a file named golf.txt.First, have the program ask the user 
how many players they want to add to their record. Then, ask the user for each name and score 
individually.golf.txt should be structured so that there is a line with the player's name, 
followed by their score on the next line.
Example
Emily
30
Mike
20
Jonathan
23 '''

#Ask the user how many records they would like to add
num = int(input("Enter number of players:"))

#Open golf.txt for writing
file = open("golf.txt", "w")

#Go through and ask the user for name and score of each player
for i in range(1, num+1):
    name = input("Enter name of player number " + str(i) + ":")
    score = input("Enter score of player number " + str(i) + ":")

    #Write to a file
    file.write(name)
    file.write('\n')
    file.write(score)
    file.write('\n')


#close the file
file.close()
