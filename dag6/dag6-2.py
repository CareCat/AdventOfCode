lines = [line.rstrip('\n') for line in open('C:\kod\AdventOfCode\dag6\mestinput.txt')]

def get_center_and_orbiter(line):
    split = line.split(')')
    return split[0] , split[1]

planetsToCenters = {'COM':'ingen'}
planetsToOrbitNumbers = {'COM': 0}

for line in lines:
    (center,orbiter) = get_center_and_orbiter(line)
    planetsToCenters[orbiter] = center        


youPlanet = "YOU"
santaPlanet = "SAN"

youPlanets = [youPlanet]
santaPlanets = [santaPlanet]

youPlanetsContainSantaPlanet = False
santaPlanetsContainsYouPlanet = False

while youPlanet is not santaPlanet and not youPlanetsContainSantaPlanet and not santaPlanetsContainsYouPlanet:
    santaPlanet = planetsToCenters[santaPlanet]
    youPlanet = planetsToCenters[youPlanet]
    
    santaPlanets.append(santaPlanet)
    youPlanets.append(youPlanet)

    youPlanetsContainSantaPlanet = santaPlanet in youPlanets
    santaPlanetsContainsYouPlanet = youPlanet in santaPlanets

if santaPlanetsContainsYouPlanet:
    jumps = len(youPlanets) - 2 + santaPlanets.index(youPlanet) - 1
    print(jumps)

if youPlanetsContainSantaPlanet:
    jumps = len(santaPlanets) - 2 + youPlanets.index(santaPlanet) - 1
    print(jumps)

