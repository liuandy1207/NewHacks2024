from grid import Grid
from copy import deepcopy
from forest import Forest


if __name__ == "__main__":
    Gridd = Grid(50, 50)

    startx = 15
    starty = 2

    for i in range(0, 20):
        for j in range(0, 20):
            Gridd.grid[i][j].temp = 30
            Gridd.grid[i][j].state = 0
            Gridd.grid[i][j].type = Forest
            Gridd.grid[i][j].fuel = Forest.fuel

    Gridd.grid[startx][starty].temp = 1000
    Gridd.grid[startx][starty].state = 1
    Gridd.display_grid(burningNodes={(startx,starty)})
