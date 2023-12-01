def getFirstDigit(line):
    for x in line:
        if x.isnumeric():
            return x
    return "0"

def getLastDigit(line):
    for x in reversed(line):
        if x.isnumeric():
            return x
    return "0"

def getLineTotal(line):
    return int(getFirstDigit(line) + getLastDigit(line))

def getCalibrationValue():
    total = 0
    with open('input.txt') as f:
        for line in f:
            line.strip()
            print(getLineTotal(line))
            total += getLineTotal(line)

    return total

print("Calibration Value: " + str(getCalibrationValue()))
