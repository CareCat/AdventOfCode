import math

inputData = [3,225,1,225,6,6,1100,1,238,225,104,0,1002,114,19,224,1001,224,-646,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,40,62,225,1101,60,38,225,1101,30,29,225,2,195,148,224,1001,224,-40,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1001,143,40,224,101,-125,224,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,101,29,139,224,1001,224,-99,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,14,34,225,102,57,39,224,101,-3420,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,70,40,225,1102,85,69,225,1102,94,5,225,1,36,43,224,101,-92,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,94,24,224,1001,224,-2256,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,8,13,225,1101,36,65,224,1001,224,-101,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,677,226,224,1002,223,2,223,1006,224,329,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,344,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,359,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,389,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,404,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,108,677,226,224,1002,223,2,223,1006,224,434,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,449,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,7,677,677,224,102,2,223,223,1005,224,494,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,524,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,554,1001,223,1,223,8,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,599,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,614,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,629,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226]
testdata = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
testdata = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
testdata = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]


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
    

data = inputData.copy()
instructionPointer = 0
inputVariable = 5
errorCodes = []
lastOpCode = 0

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
        data[data[instructionPointer + 1]] = inputVariable        
        instructionPointer += 2

    if operation == 4:
        print(data[instructionPointer + 1])
        errorCodes.append(data[data[instructionPointer + 1]])
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
    
    lastOpCode = opCode

print(errorCodes)