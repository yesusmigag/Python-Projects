'''
Mode	            Description
'r'	-----------Open a file for reading only. The file cannot be changed or written to.
'w'	-----------Open a file for writing. If the file already exists, erase its contents. 
               If it does not exist, create it.
'a'	-----------Open a file to be written to. All data written to the file will be 
               appended to its end. If the file does not exist, create it.'''


#1 OPEN
#the file hostdata.txt for reading
hostdata_file = open('hostdata.txt','r')
 
#2 Write a statement to open the file yearsummary.txt in a way 
#that erases any existing data in the file.
open('yearsummary.txt','w')

#3 Write a statement to open the file priceList.txt for writing
open('priceList.txt','w')

#4 Given four files named asiasales2009.txt, europesales2009.txt, 
#africasales2009.txt, and latinamericasales2009.txt, define four file 
#objects named asia, europe, africa, and latin, and use them, respectively, 
#to open the four files for writing.
asia = open('asiasales2009.txt', 'w')
europe = open('europesales2009.txt', 'w')
africa = open('africasales2009.txt','w')
latin = open('latinamericasales2009.txt', 'w')

#5 Given a file named execution.log write the necessary code to add the line "Program 
#Execution Successful" to the end of the file (add the statement on a new line).
thefile =open('execution.log','a')
thefile.write("\nProgram Execution Successful")
thefile.close()

#6 Assume that corpdata is a file object that has been used to read data from a file.
# Write the necessary statement to close the file.
''' corpdata.close() '''