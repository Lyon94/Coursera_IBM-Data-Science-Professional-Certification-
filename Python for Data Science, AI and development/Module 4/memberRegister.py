"""
with open('members.txt', 'r+') as mainReg:

    with open('active.txt', 'a+') as actReg:
        with open('inactive.txt', 'a+') as inActReg:

            regList = mainReg.readlines()[1:]
            print(regList)
            print(len(regList))
            inActReg.seek(0)
            inActregList = inActReg.readlines()[1:]
            print(inActregList)
            print(len(inActregList))

            mainReg.seek(0)
            mainReg.write("Membership No  Date Joined  Active  \n")
            inActReg.write("\n")
            for line in regList:
                if 'no' in line:
                    inActReg.write(line)
                else:
                #    actReg.write(line)
                    mainReg.write(line)

            mainReg.truncate()

            mainReg.seek(0)
            print(mainReg.read())
            inActReg.seek(0)
            inActregList = inActReg.readlines()[1:]
            print(len(inActregList))
            #actReg.seek(0)
            #actRegList = actReg.readlines()[1:]
            #print(len(actRegList))
"""

def cleanFiles(currentMem,exMem):
    with open(currentMem, "r+") as actReg:
        with open(exMem, "a+") as inActReg:
            actRegList = actReg.readlines()
            inActReg.seek(0)
            inActRegList = inActReg.readlines()
            actReg.seek(0)
            if not("\n" in inActRegList[-1]):
                inActReg.write("\n")
            for line in actRegList:
                if "no" in line:
                    inActReg.write(line)
                else:
                    actReg.write(line)

            actReg.truncate()

"""
with open(currentMem, "r+") as actReg:
    with open(exMem, "a+") as inActReg:
        actRegList = actReg.readlines()
        actReg.seek(0)
        # print(actRegList)
        inActReg.seek(0)
        inActRegList = inActReg.readlines()
        # print(inActRegList)
        if not ("\n" in inActRegList[-1]):
            inActReg.write("\n")
        for eachPersonStatus in actRegList:
            if "no" in eachPersonStatus:
                inActReg.write(eachPersonStatus)
            else:
                actReg.write(eachPersonStatus)

        actReg.truncate()
"""

memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg, exReg)