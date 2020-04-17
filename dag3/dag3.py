
wires = [line.rstrip('\n').split(',') for line in open('C:\kod\AdventOfCode\dag3\pestinput.txt')]
intersections = []



for wire in wires:
    maxX = 0
    minX = 0
    maxY = 0
    minY = 0

    x = 0
    y = 0


    for section in wire:

        direction = section[0]
        nrSteps = int(section[1:])
        
        if direction == "U":
            y += nrSteps
            if y > maxY:
                maxY = y
        
        if direction == "D":
            y -= nrSteps
            if y < minY:
                minY = y
        if direction == "R":
            x += nrSteps
            if x > maxX:
                maxX = x
        if direction == "L":
            x -= nrSteps
            if x < maxX:
                minX = x

print("Max X: " + str(maxX))
print("Max Y: " + str(maxY))
print("Min X: " + str(minX))
print("Min Y: " + str(minY))

grid = [[0 for j in range(1000)] for i in range(1000)]
crossings = []
wireNr = 18


print("done making grid")

print("grid X: " + str(len(grid)))
print("grid Y: " + str(len(grid[0])))


for wire in wires:
    startX = 500
    startY = 500
    
    wireNr = 18

    for section in wire:

        direction = section[0]
        nrSteps = int(section[1:])

        if direction == "U":
            for i in range(nrSteps):
                if(grid[startX][startY + i] is not 0 and not wireNr):
                    crossings.append((startX,startY +i))
                grid[startX][startY + i] = wireNr
                startY += 1

        if direction == "D":
            for i in range(nrSteps):
                if(grid[startX][startY -i] is not 0 and not wireNr):
                    crossings.append((startX,startY - i))
                grid[startX][startY - i] = wireNr
                startY -= 1

        if direction == "R":
             for i in range(nrSteps):
                if(grid[startX + i][startY] is not 0 and not wireNr):
                    crossings.append((startX + i,startY))
                grid[startX + i][startY] = wireNr
                startX += 1

        if direction == "L":
             for i in range(nrSteps):
                if(grid[startX -i][startY] is not 0 and not wireNr):
                    crossings.append((startX - i,startY))
                grid[startX - i][startY] = wireNr
                startY -= 1
        
    wireNr = 57

print(crossings)  