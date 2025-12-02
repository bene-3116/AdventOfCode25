import fileinput
import select

def repeatsSumPart1(pair):
    output = set()
    current = pair[0] - 1
      
    while (True):
        current += 1
        digitNum = len(str(current))
        if(digitNum % 2 != 0):
            current = int("1" + "0" * (digitNum))
            digitNum += 1
        digits = [int(x) for x in str(current)]
        if(current > pair[1]):
            break
        
        checkNum = digitNum // 2
        checkRepeatSeq = digits[0:checkNum]
        if(checkRepeatSeq == digits[checkNum:]):
            output.add(current)    
    return output

def repeatsSumPart2(pair):
    output = set()
    current = pair[0]
    digitNum = len(str(current)) % 2 != 0

    for current in range(pair[0], pair[1]):
        digits = [int(x) for x in str(current)]        
        hasRepeat = True
        for checkNum in range(1, len(digits) // 2 + 1):
            hasRepeat = True            
            i = 1
            checkRepeatSeq = digits[0:checkNum]
            while (i*checkNum) < len(digits):
                if(checkRepeatSeq != digits[i*checkNum:(i+1)*checkNum]):
                    hasRepeat = False
                    break
                i += 1
            if hasRepeat:
                output.add(current)
                break
    return output


def Day2():
    input = fileinput.input("/home/benedikt/development/AdventOfCode25/Input/Day2.txt").readline()
    input = list(map(lambda x: 
                        (int(x.split("-")[0]), int(x.split("-")[1])), input.split(",")))
    output = set()
    for pair in input:
        for match in list(repeatsSumPart2(pair)):
            output.add(match)
    
    print(sum([int(x) for x in list(output)]))
Day2()