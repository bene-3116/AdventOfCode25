import fileinput

def impInput():
    banks = []
    for line in fileinput.input("/home/benedikt/development/AdventOfCode25/Input/Day3.txt"):
        banks.append([int(x) for x in line.replace("\n","")])
    return banks

def Day3Part1():
    banks = impInput()
    joltages = []
    for bank in banks:
        max1 = bank[0]
        max2 = bank[1]
        for i in range(1, len(bank)-1):
            if(bank[i+1] > max2):
                max2 = bank[i+1]
            if bank[i] > max1:
                max1 = bank[i]
                max2 = bank[i+1]
        joltages.append(int(str(max1) + str(max2)))
    print(sum(joltages))

def Day3Part2():
    banks = impInput()
    joltages = []
    for bank in banks:
        maxes = [0 for x in range(0,12)]
        for i in range(0, len(bank)-11):
            for j in range(-11,1):
                if(bank[i-j] <= maxes[-j]):
                    continue
                for k in range(-j,len(maxes)):
                    maxes[k] = bank[i+k]
        joltages.append(int("".join([str(x) for x in maxes])))
    print(sum(joltages))

Day3Part2()