import fileinput

def impInput():
  data = [line.replace("\n", "") for line in fileinput.input("/home/benedikt/development/AdventOfCode25/Input/Day7.txt")]
  return data

def Day7Part1():
  data = impInput()
  beams = set()
  splits = 0
  i = 2

  beams.add(data[0].index("S"))
  while i < len(data):
    j = 0
    newbeams = set(beams)
    while j < len(beams):
      beam = list(beams)[j]      
      if(data[i][beam] != "^"):
        j += 1
        continue
      newbeams.remove(beam)
      newbeams.add(beam+1)
      newbeams.add(beam-1)      
      splits += 1
      j += 1
    beams = set(newbeams)
    i += 2
  return splits

def Day7Part2():
  data = impInput()
  beams = dict()
  splits = 0
  i = 2

  beams[data[0].index("S")] = 1
  while i < len(data):
    j = 0
    newbeams = dict(beams)
    beamsKeys = [x[0] for x in beams.items()]
    for beam in beamsKeys:  
      newbeamsKeys = [x[0] for x in newbeams.items()]
      if(data[i][beam] != "^"):
        j += 1
        continue      
      
      if(newbeamsKeys.__contains__(beam+1)):
        newbeams[beam+1] += beams[beam]
      else:
        newbeams[beam+1] = beams[beam]
      if(newbeamsKeys.__contains__(beam-1)):
        newbeams[beam-1] += beams[beam]
      else:
        newbeams[beam-1] = beams[beam] 
      newbeams.pop(beam)  
      splits += 1
      j += 1
    beams = dict(newbeams)
    i += 2
  return sum([x[1] for x in beams.items()])
        

print(Day7Part2())