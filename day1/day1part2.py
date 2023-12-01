def getFirstDigit(line):
    for x in line:
        if x.isnumeric():
            return x
    return "0"

def firstNumberString(line, digits):
    partLine = ""
    for char in line:
        partLine += char
        for digit in digits.keys():
            partLine = partLine.replace(digit, digits[digit])
        first = getFirstDigit(partLine)
        if first != "0":
            return first

    return "0"

def getLastDigit(line):
    for x in reversed(line):
        if x.isnumeric():
            return x
    return "0"

def lastNumberString(line, digits):
    partLine = ""
    for char in reversed(line):
        partLine = char + partLine
        for digit in digits.keys():
            partLine = partLine.replace(digit, digits[digit])
        last = getLastDigit(partLine)
        if last != "0":
            return last

    return "0"

def getLineTotal(line, digits):
    return int(firstNumberString(line, digits) + lastNumberString(line, digits))

def getCalibrationValue():
    total = 0
    firstFound = False
    digits = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    with open('input.txt') as f:
        for line in f:
            line.strip()
            print(getLineTotal(line, digits))
            total += getLineTotal(line, digits)

    return total

print("Calibration Value: " + str(getCalibrationValue()))
