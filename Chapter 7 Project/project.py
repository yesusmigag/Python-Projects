gender = input("Enter 'boy', 'girl', or 'both':")

if (gender == 'boy'):
    f = open('BoyNames.txt', 'r')
    boyName = input("Enter a boy's name:")
    boyNames = f.read().splitlines()
    if (boyName in boyNames):
        print(boyName + " was a popular boy's name between 2000 and 2009.")
    else:
        print(boyName + " was not a popular boy's name between 2000 and 2009.")
elif (gender == 'girl'):
    f = open('GirlNames.txt', 'r')
    girlName = input("Enter a girl's name:")
    girlNames = f.read().splitlines()
    if (girlName in girlNames):
        print(girlName + " was a popular girl's name between 2000 and 2009.")
    else:
        print(girlName + " was not a popular girl's name between 2000 and 2009.")
elif (gender == 'both'):
    boy = open('BoyNames.txt', 'r')
    girl = open('GirlNames.txt', 'r')
    boyName = input("Enter a boy's name:")
    girlName = input("Enter a girl's name:")
    boyNames = boy.read().splitlines()
    girlNames = girl.read().splitlines()

    if (boyName in boyNames):
        print(boyName + " was a popular boy's name between 2000 and 2009.")
    else:
        print(boyName + " was not a popular boy's name between 2000 and 2009.")
    if (girlName in girlNames):
        print(girlName + " was a popular girl's name between 2000 and 2009.")
    else:
        print(girlName + " was not a popular girl's name between 2000 and 2009.")
else:
    print('Please enter a valid choice')
