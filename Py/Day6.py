import fileinput

def impInput():
    data = [line.replace("\n", "") for line in fileinput.input("/home/benedikt/development/AdventOfCode25/Input/Day6.txt")]
    return data

def Day6Part1():
    data = impInput()
    nums = [x.split(" ") for x in data[:len(data)-1]]
    ops = data[len(data)-1].split(" ")
    for i in range(0,len(nums)):
        while '' in nums[i]:
            nums[i].remove('')
    while '' in ops:
        ops.remove('')
    result = 0
    for col in range(0,len(ops)):
        colResult = 0
        add = ops[col] == "+"
        multiply = ops[col] == "*"
        if add:
            for row in range(0,len(nums)):
                colResult += int(nums[row][col])
        elif multiply:
            colResult = 1
            for row in range(0,len(nums)):
                colResult *= int(nums[row][col])
        result += colResult
    return result

def Day6Part2():
    data = impInput()
    nums = data[:len(data)-1]
    transformedNums = []
    ops = data[len(data)-1].split(" ")
    col = 0
    while(col < len(nums[0])):
        transformedNumsCol = []        
        while(col < len(nums[0])):
            transformedNum = ""
            for row in range(0,len(nums)):
                transformedNum += nums[row][col]
            transformedNum = transformedNum.replace(" ","")
            if(transformedNum == ""):
                break
            transformedNumsCol.append(transformedNum)
            col += 1        
        transformedNums.append(transformedNumsCol)
        col += 1

    while '' in ops:
        ops.remove('')
    
    result = 0
    for i in range(0,len(ops)):
        colResult = 0
        add = ops[i] == "+"
        multiply = ops[i] == "*"
        if add:
            for j in range(0,len(transformedNums[i])):
                colResult += int(transformedNums[i][j])
        elif multiply:
            colResult = 1
            for j in range(0,len(transformedNums[i])):
                colResult *= int(transformedNums[i][j])
        result += colResult
    return result

print(Day6Part2())



