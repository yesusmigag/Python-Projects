"""	Jesus M 		      	
	Chapter #2,Problem #6 Sales Tax	

	This program will calculate the  Sales Tax
	-------------------------------------------------------
	INPUT							OUTPUT
	-----							------
	Amount of Purchase				Amount of Purchasee
						            Country Sales Tax
	                                State Sales Tax
                                    Total Sales Tax
	-------------------------------------------------------
"""
#****Module\Libraries
import os
#*** Program modules, functions, constants, and variables
#*** Declaration and initialization of variables
state_tax = 0.05
country_tax = 0.025

#*** BEGINNING OF THE PROGRAM LOGIC ****

#*** Description of the program
os.system("clear")          #*** Clear screen
print("This program will calculate the Sales Tax.\n")

#*** Request data
purchase = float(input("Plase enter the amount of your purchase: "))

#*** Process data
total_state_tax = purchase * state_tax
total_country_tax= purchase * country_tax
total_sales_tax = total_state_tax + total_country_tax

#*** Display results

print()
print(f"Amount of Purchase : ${purchase:7,.2f}")
print(f"Country Sales Tax  : ${total_country_tax:7,.2f}")
print(f"State Sales Taxe   : ${total_state_tax:7,.2f}")
print(f"Total Sales Tax    : ${total_sales_tax:7,.2f}")


#***** Ending program
print("\n")   
#***** END executions of the program    