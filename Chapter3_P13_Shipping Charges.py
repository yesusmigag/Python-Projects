"""			      	
	Chapter #3,Problem #13 Shipping Charges	

	This program will calculate the Shipping Charges
	-------------------------------------------------------
	INPUT							OUTPUT
	-----							------
	Weight of a package				Shipping charges.
	------------------------------------------------------
"""
#****Module\Libraries
import os

#*** BEGINNING OF THE PROGRAM LOGIC ****
os.system("clear")          #*** Clear screen

#*** Request data
weigth = float(input("Enter the weight of a package: "))
#*** Process data

if weigth <= 2:
    shipping_charges = weigth *1.5
elif  weigth > 2 and weigth <=6:
    shipping_charges = weigth * 3.0
elif weigth > 6 and weigth <= 10.0:
    shipping_charges = weigth * 4.0
elif  weigth > 10.0:
    shipping_charges = weigth * 4.75


#*** Display results
print(f"The shipping charges: ${shipping_charges:7,.2f}")

#***** Ending program
print("\n")   
#***** END  executions of the program    


