import math
import queue
from itertools import permutations

inputData = [3,8,1001,8,10,8,105,1,0,0,21,38,59,84,93,110,191,272,353,434,99999,3,9,101,5,9,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,102,5,9,9,1001,9,4,9,1002,9,2,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99]


def GetValueByMode(parameter, mode, data):
    
    if mode == 0:
        return data[data[parameter]]
    if mode == 1:
        return data[parameter]

def SetValueByMode(parameter,mode, value ,data):

    if mode == 0:
        data[data[parameter]] = value
    if mode == 1:
        data[parameter] = value

def GetOperation(opCode):
    operation = opCode % 10
    if operation == 9:
        return 99
    return operation

def GetModes(opCode):
    opCode = opCode // 100
    if opCode is 0:
        return(0,0)

    mode1 = opCode % 10
    opCode = opCode // 10
    mode2 = opCode % 10
    return(mode1,mode2)


phasePermutations = list(permutations([5,6,7,8,9]))
maxThrust = 0
    
for permutation in phasePermutations:

    inputQueue = queue.Queue(maxsize=20)
    errorCodes = []

    inputVariable = 0
    

    for amplifierNr in range(5):

        instructionPointer = 0
        data = inputData.copy()
        inputPhase = True      

        for instruction in data:
            opCode = data[instructionPointer]
           
            mode1 , mode2 = GetModes(opCode)
            operation = GetOperation(opCode)

            if operation == 1:
                data[data[instructionPointer + 3]]  = GetValueByMode(instructionPointer + 1,mode1 ,data) + GetValueByMode(instructionPointer + 2 ,mode2 , data)       
                instructionPointer += 4

            if operation == 2:
                data[data[instructionPointer + 3]]  = GetValueByMode(instructionPointer + 1,mode1 ,data) * GetValueByMode(instructionPointer + 2 ,mode2 , data)
                instructionPointer += 4

            if operation == 3:
                if(inputPhase):
                    data[data[instructionPointer + 1]] = permutation[amplifierNr]
                    inputPhase = False        
                else:
                    data[data[instructionPointer + 1]] = inputVariable
                instructionPointer += 2
                
            if operation == 4:
                inputVariable = data[data[instructionPointer + 1]]
                if(amplifierNr == 4):
                    if(inputVariable > maxThrust):
                        maxThrust = inputVariable
                instructionPointer += 2

            if operation == 5:
                jump = GetValueByMode(instructionPointer + 1 , mode1, data) is not 0
                if jump:
                    instructionPointer = GetValueByMode(instructionPointer + 2, mode2, data)
                else:
                    instructionPointer += 3

            if operation == 6:
                jump = GetValueByMode(instructionPointer + 1 , mode1, data) is 0
                if jump:
                    instructionPointer = GetValueByMode(instructionPointer + 2, mode2, data)
                else:
                    instructionPointer += 3

            if operation == 7:
                lessThan = GetValueByMode(instructionPointer + 1, mode1, data) < GetValueByMode(instructionPointer + 2 ,mode2 , data)
                if lessThan:
                    data[data[instructionPointer + 3]] = 1
                else:
                    data[data[instructionPointer + 3]] = 0
                instructionPointer += 4       
            
            if operation == 8:
                equals = GetValueByMode(instructionPointer + 1, mode1, data) == GetValueByMode(instructionPointer + 2 ,mode2 , data)
                if equals:
                    data[data[instructionPointer + 3]] = 1
                else:
                    data[data[instructionPointer + 3]] = 0
                instructionPointer += 4 
            
            if operation == 99:

                data  = inputData.copy()
                break

print(maxThrust)
            
            