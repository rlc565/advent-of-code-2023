def getIdTotal():
    total = 0
    with open('input.txt') as f:
        for line in f:
            redMin = 0
            greenMin = 0
            blueMin = 0
            games = line.strip().split(":")[1].strip().split(";")
            for game in games:
                for cubes in game.strip().split(","):
                    cubesList = cubes.strip().split(" ")
                    print(cubesList)
                    cubesList[0] = int(cubesList[0])
                    if cubesList[1] == "red":
                        if cubesList[0] > redMin:
                            redMin = cubesList[0]
                    elif cubesList[1] == "green":
                        if cubesList[0] > greenMin:
                            greenMin = cubesList[0]
                    elif cubesList[1] == "blue":
                        if cubesList[0] > blueMin:
                            blueMin = cubesList[0]
            print("red: " + str(redMin) + " green: " + str(greenMin) + " blue: " + str(blueMin))
            total += (redMin * greenMin * blueMin)
    return total

print(getIdTotal())
