#Write the definition of a function max that has 
#three integer parameters and returns the largest.


def max (num1,num2,num3):
    if (num1>num2 and num1>num3):
        return num1
    elif (num2>num1 and num2>num3):
        return num2
    else:
       return num3