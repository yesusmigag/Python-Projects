#Define a function called signOf that takes a parameter containing 
#an integer value and returns a 1 if the parameter is positive, 0 if the parameter is 0, and -1 if the parameter is negative.

def main():
    display = signOf(-7)
    print(display)

def signOf(int):
  if int>0:
    return 1
  elif int==0:
    return 0
  else:
    return -1

main()