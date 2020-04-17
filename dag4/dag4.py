lowerLimit = 264360
upperLimit = 746325

passwordRange = range(lowerLimit,upperLimit)

print(passwordRange)
validPasswords = 0

for password in passwordRange:
    passwordDigits = [int(x) for x in str(password)]
    previousDigit = 0
    index = 0
    for passwordDigit in passwordDigits:
        if passwordDigit < previousDigit:
            break
        if index == 5:

            if len(passwordDigits) != len(set(passwordDigits)):
                previousDigit = 12
                ranges = []
                rangeCount = 1
                passwordDigits.append(0)
                for passwordDigit in passwordDigits:

                    if passwordDigit == previousDigit:
                        rangeCount += 1
                    if passwordDigit is not previousDigit:
                        ranges.append(rangeCount)
                        rangeCount = 1
                    previousDigit = passwordDigit

                if ranges.count(2) is not 0:
                    validPasswords += 1
        
        previousDigit = passwordDigit
        index += 1


    
print(validPasswords)