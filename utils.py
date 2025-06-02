def getCellColor(grid, rowIndex, columnIndex):
    cell = grid[rowIndex][columnIndex]
    if (cell == 0):
        return "white"
    elif (cell == 1):
        return "black"
    elif (cell == 2):
        return "green"
    else:
        return "blue"
    
def getDistance(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])