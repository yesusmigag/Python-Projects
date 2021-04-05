"""			      	
	Chapter #4,Problem #4 Distance Traveled	

	This program will calculate the distance a vehicle travels
	-------------------------------------------------------
	INPUT							OUTPUT
	-----							------
	speed				            hour
    time                        distance_traveled  
	------------------------------------------------------
"""
#****Module\Libraries
import os

#*** BEGINNING OF THE PROGRAM LOGIC ****
os.system("clear")          #*** Clear screen

#*** Request data
speed = int(input("What is the speed of the vehicle in mph? "))
while speed<=0:      #***Input Validation***
    print("Do not accept a negative number for speed")
    speed = int(input("What is the speed of the vehicle in mph? "))

time = int(input("How many hours has it traveled? "))
while time<=1:      #***Input Validation***
    print("Do not accept any value less than 1 for time traveled")
    time = int(input("How many hours has it traveled? "))

#*** Process data

print("\nHour","\tDistance Traveled" )
print("--------------------------" )
for count in range(1,time + 1):
   distance_traveled = speed * count
#*** Display results
   print(format(count,'2d'),format(distance_traveled,'15d'))

#***** Ending program
print("\n")   
#***** END  executions of the program    


