import fileinput

def ImportInput():
    data = []
    input = fileinput.input("/home/benedikt/development/AdventOfCode25/Input/Day4.txt")
    line = input.readline().strip()    
    while line:
        data.append(line)
        line = input.readline().strip()
    return data

def IsReachableRoll(data, rowIndex, columnIndex, columnCount, rowCount):
    if(data[rowIndex][columnIndex] != "@"):
                return False
    adjactentRolls = 0         
    onLeftEdge = columnIndex == 0
    onUpperEdge = rowIndex == 0
    onRightEdge = columnIndex == columnCount - 1
    onBottomEdge = rowIndex == rowCount - 1       
    if(not onLeftEdge):
        # Check Left
        if(data[rowIndex][columnIndex - 1] == "@"):
            adjactentRolls += 1
        if(not onUpperEdge):
            # Check Top-Left
            if(data[rowIndex - 1][columnIndex - 1] == "@"):
                adjactentRolls += 1
        if(not onBottomEdge):
            # Check Bottom-Left
            if(data[rowIndex + 1][columnIndex - 1] == "@"):
                adjactentRolls += 1
    if(not onRightEdge):
        # Check Right
        if(data[rowIndex][columnIndex + 1] == "@"):
            adjactentRolls += 1
            if(adjactentRolls >= 4):
                return False
        if(not onUpperEdge):
            # Check Top-Right
            if(data[rowIndex - 1][columnIndex + 1] == "@"):
                adjactentRolls += 1
                if(adjactentRolls >= 4):
                    return False
        if(not onBottomEdge):
            # Check Bottom-Right
            if(data[rowIndex + 1][columnIndex + 1] == "@"):
                adjactentRolls += 1
                if(adjactentRolls >= 4):
                    return False
    if(not onUpperEdge):
        # Check Top
        if(data[rowIndex - 1][columnIndex] == "@"):
            adjactentRolls += 1
            if(adjactentRolls >= 4):
                return False
    if(not onBottomEdge):
        # Check Bottom                
        if(data[rowIndex + 1][columnIndex] == "@"):
            adjactentRolls += 1
            if(adjactentRolls >= 4):
                return False
    return adjactentRolls < 4
    

def Day4Part1():
    data = ImportInput()
    columnCount = len(data[0])
    rowCount = len(data)
    reachableCount = 0
    for(rowIndex) in range(0, rowCount):
        for(columnIndex) in range(0, columnCount):
            if(IsReachableRoll(data, rowIndex, columnIndex, columnCount, rowCount)):
                reachableCount += 1
    print(reachableCount)
    


def Day4Part2():
    data = ImportInput()
    columnCount = len(data[0])
    rowCount = len(data)
    deletableCount = 0    
    reachableFound = True
    while(reachableFound):
        reachableFound = False
        rowIndex = 0
        while(rowIndex < rowCount):
            columnIndex = 0
            while(columnIndex < columnCount):
                if(not IsReachableRoll(data, rowIndex, columnIndex, columnCount, rowCount)):
                    columnIndex += 1
                    continue
                deletableCount += 1
                reachableFound = True
                data[rowIndex] = data[rowIndex][:columnIndex] + "." + data[rowIndex][columnIndex + 1:]
                columnIndex += 1
            rowIndex += 1
    print(deletableCount)

Day4Part2()