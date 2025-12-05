import fileinput

def impInput():
    dataString = ""
    for line in fileinput.input("/home/benedikt/development/AdventOfCode25/Input/Day5.txt"):
        dataString += line
    return dataString

def Day5Part1():
    dataString = impInput()
    dataStringSplit = dataString.split("\n\n")
    freshRanges = dataStringSplit[0].split("\n")
    freshRangesSplit = [x.split("-") for x in freshRanges]
    availableIDs = dataStringSplit[1].split("\n")
    freshCount = 0
    for ID in availableIDs:
        IDint = int(ID)
        for i in range(0, len(freshRangesSplit)):
            if IDint >= int(freshRangesSplit[i][0]) and IDint <= int(freshRangesSplit[i][1]):
                freshCount += 1
                break
    return freshCount

def Day5Part2():
    dataString = impInput()
    dataStringSplit = dataString.split("\n\n")
    freshRanges = dataStringSplit[0].split("\n")
    freshRangesSplit = [x.split("-") for x in freshRanges]
    sortedFreshRanges = sorted(freshRangesSplit, key=lambda x: int(x[0]))
    freshCount = 0

    i = 0
    while i < len(sortedFreshRanges) - 1:
        curRightBorder = int(sortedFreshRanges[i][1])
        if(curRightBorder >= int(sortedFreshRanges[i+1][1])):
            sortedFreshRanges.pop(i+1)
            continue
        if curRightBorder >= int(sortedFreshRanges[i+1][0]):
            sortedFreshRanges[i][1] = sortedFreshRanges[i+1][1]
            sortedFreshRanges.pop(i+1)
            continue
        i += 1
    
    for i in range(0, len(sortedFreshRanges)):
        freshCount += (int(sortedFreshRanges[i][1]) - int(sortedFreshRanges[i][0])) + 1
    return freshCount
print(Day5Part2())

