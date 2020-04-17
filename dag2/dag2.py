import math

inputData = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,5,19,23,2,10,23,27,1,27,5,31,2,9,31,35,1,35,5,39,2,6,39,43,1,43,5,47,2,47,10,51,2,51,6,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,1,71,5,75,1,13,75,79,1,6,79,83,2,83,13,87,1,87,6,91,1,10,91,95,1,95,9,99,2,99,13,103,1,103,6,107,2,107,6,111,1,111,2,115,1,115,13,0,99,2,0,14,0]
index = 0

for i in range(0,100):
    for j in range(0,100):
        
        data = inputData.copy()
        index = 0
        data[1] = i
        data[2] = j

        for instruction in data:
            operation = data[index]

            if operation == 1:
                data[data[index + 3]]  = data[data[index + 1]] + data[data[index + 2]]

            if operation == 2:
                data[data[index + 3]]  = data[data[index + 1]] * data[data[index + 2]]
            
            if operation == 99:
                if i == 12 and j == 2:
                    print(data[0])

                if data[0] == 19690720:
                    print("I = " + str(i) + " J = " + str(j))

                data  = inputData.copy()
                break            

            index += 4
