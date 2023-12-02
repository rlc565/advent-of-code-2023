def getIdTotal():
    total = 0
    with open('input.txt') as f:
        for line in f:
            redMax = 0
            greenMax = 0
            blueMax = 0
            id = int(line.strip().split(":")[0].strip().split(" ")[1])
            games = line.strip().split(":")[1].strip().split(";")
            for game in games:
                for cubes in game.strip().split(","):
                    cubesList = cubes.strip().split(" ")
                    print(cubesList)
                    cubesList[0] = int(cubesList[0])
                    if cubesList[1] == "red":
                        if cubesList[0] > redMax:
                            redMax = cubesList[0]
                    elif cubesList[1] == "green":
                        if cubesList[0] > greenMax:
                            greenMax = cubesList[0]
                    elif cubesList[1] == "blue":
                        if cubesList[0] > blueMax:
                            blueMax = cubesList[0]
            print("red: " + str(redMax) + " green: " + str(greenMax) + " blue: " + str(blueMax))
            if (redMax <= 12) and (greenMax <= 13) and (blueMax <= 14):
                total += id
    return total

print(getIdTotal())
