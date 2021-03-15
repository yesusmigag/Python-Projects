import os
os.system("clear")           #*** Clear screen

limit = 5
count = 1
grade = 0
sumOfGrade = 0

for count in range (1,6):    
    grade = int(input(f"Enter grade #{count}: "))
    while (grade < 0 or grade >100):
        print("Error: Invalid grade")
        grade = int(input(f"Enter grade #{count}: "))

   
    sumOfGrade += grade
    count += 1
    

count -= 1
if count > 0:
      average = sumOfGrade/count

    
print("------>", count, sumOfGrade, average)
