lines = [line.rstrip('\n') for line in open('C:\kod\AdventOfCode\dag6\input.txt')]


def get_center_and_orbiter(line):
    split = line.split(')')
    return split[0] , split[1]

planetsToCenters = {'COM':'ingen'}
planetsToOrbitNumbers = {'COM': 0}

for line in lines:
    (center,orbiter) = get_center_and_orbiter(line)
    planetsToCenters[orbiter] = center        
    

for planet, center in planetsToCenters.items():
    orbits = 0
    
    while center is not 'ingen':
        orbits += 1
        center = planetsToCenters[center]
        
    
    planetsToOrbitNumbers[planet] = orbits    

totalOrbits = 0
for planet, orbitNumber in planetsToOrbitNumbers.items():
    totalOrbits += orbitNumber

print(totalOrbits)

    