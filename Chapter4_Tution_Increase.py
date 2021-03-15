'''At one college, the tuition for a full-time student is $8,000 per semester. 
It has been announced that the tuition will increase by 3 percent each year 
for the next 5 years. Write a program with a loop that displays the projected 
semester tuition amount for the next 5 year'''

tuit = 8000
for years in range(1,6):
    tuit*=1.03
    if years ==1:
     print('In ',years,' year, the tuition will be $',tuit,".",sep="")
    else:
     print('In ',years,' years, the tuition will be $',tuit,".",sep="")