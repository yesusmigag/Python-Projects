'''Write a program that reads the records from the golf.txt file written in the 
    previous exercise and prints them in the following format:

Name: Emily
Score: 30

Name: Mike
Score: 20

Name: Jonathan
Score: 23'''
#Solution 1
file = open("golf.txt", "r")
name = True
for line in file:
    if name:
        print("Name:" + line, end="")
    else:
        print("Score:" + line)
    name = not name
    
file.close()


#SOLUTION 2
golf_file = open('golf.txt','r')
line=golf_file.readlines()
#score=''

for i in range(0,len(line),2):
  print('Name:'+line[i].strip('\n'))
  print('Score:'+line[i+1].strip('\n'))
  print()
golf_file.close()