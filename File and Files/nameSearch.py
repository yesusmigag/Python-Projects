def readBoysNameFile (filename):
    boysNameFile = open(filename,'r')
    boysNameList = []

    boyName = boysNameFile.readline()

    while boyName != "":
        boyName= boyName.rstrip("\n")
        boysNameList.append(boyName)
        boyName = boysNameFile.readline()

    return boysNameFile

def readGirlsNameFile (filename):
    girlsNameFile = open(filename,'r')
    girlsNameList = []

    girlName = girlsNameFile.readline()

    while girlName != "":
        girlName= girlName.rstrip("\n")
        girlsNameList.append(girlName)
        girlName = girlsNameFile.readline()

    return girlsNameList


def getUserSearchNames():
    userSearchName= input('')

def main():
    girlsFileName = "GirlNames.txt"
    girlsNameList = readGirlsNameFile(girlsFileName)

    print(girlsNameList)

main()

