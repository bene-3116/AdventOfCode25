import fileinput



def day1part2Chat():
    password = 0
    position = 50

    for line in fileinput.input('/home/benedikt/development/AdventOfCode25/Input/Day1.txt'):
        RL = str(line[0])
        value = int(line[1:])

        oldPosition = position

        # Treffer während der Rotation zählen
        if RL == 'R':
            # wie viele Klicks bis zum nächsten 0?
            first = (100 - oldPosition) % 100
            if first == 0:
                first = 100
            if first <= value:
                password += 1 + (value - first) // 100

            position += value

        elif RL == 'L':
            first = oldPosition % 100
            if first == 0:
                first = 100
            if first <= value:
                password += 1 + (value - first) // 100

            position -= value

        # Endposition normalisieren
        position %= 100

    print(password)


def day1part2():
    password = 0
    position = 50
    for line in fileinput.input('/home/benedikt/development/AdventOfCode25/Input/Day1.txt'):
        RL = str(line[0])
        value = int(line[1:])        

        oldPosition = position

        if(RL == 'R'):
            position += value
            password += position // 100
        
        elif(RL == 'L'):
            position -= value
            if(position < 0):                
                password += 1 + abs(position) // 100
                if(value + position == 0):
                    password -= 1
                
        
        position %= 100        
    print(password)
    
        
day1part2()

