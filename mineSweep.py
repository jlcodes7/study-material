# Helper Functions #

# uses the mine string to create a matrix of the mine field
def createMineField(mineStr, mineCols):
    tmp = [mineStr[i: i + mineCols] for i in range(0, len(mineStr) - 1, mineCols)]
    
    mineBoard = [list(n) for n in tmp]

    return mineBoard

# finds the number of mines adjacent to current coordinate
def getAdjacentMines(mineField, x, y):
    numMines = 0
    for row in range(x - 1, x + 2):
        for col in range(y - 1, y + 2):
            if row >= 0 and row < len(mineField) and col >= 0 and col < len(mineField[row]) and mineField[row][col] == "*":
                numMines += 1
    return numMines

# dfs recursive function to reveal the minefield
def mineSweep(mineField, coords):
    row, col = coords

    for row in range(len(mineField)):
        for col in range(len(mineField[row])):
            if mineField[row][col] == "*":
                    continue
            mineField[row][col] = str(getAdjacentMines(mineField, row, col))

    return mineField

# accepts minefield info in template "minefield rows, minefield columns; minefield string"
userInput = input("Input Mine Field: ")

mineInfo = userInput.split(";")

mineSize = mineInfo[0].split(",")
mineRows = int(mineSize[0])
mineCols = int(mineSize[1])

mineStr = str(mineInfo[1])

mineField = createMineField(mineStr, mineCols)

coords = [0, 0]
 
revealedMineField = mineSweep(mineField, coords)

flatMineField = sum(revealedMineField, [])

output = ""

for n in flatMineField:
    output += n

print(output)