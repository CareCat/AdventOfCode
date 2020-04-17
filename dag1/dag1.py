import math

lines = [line.rstrip('\n') for line in open('C:\kod\AdventOfCode\dag1\input.txt')]

fuel = 0

for line in lines:
    moduleFuel = (math.floor(int(line) / 3) - 2)
    fuel4fuel = (math.floor(moduleFuel / 3) - 2)
    
    temp = fuel4fuel
    while temp > 0:
        temp = (math.floor(temp / 3) - 2)
        if(temp>0):
            fuel4fuel += temp    
    
    fuel += moduleFuel + fuel4fuel

print(fuel)