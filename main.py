from grid import Grid
from copy import deepcopy


if __name__ == "__main__":
    Gridd = Grid(50, 50)

    startx = 15
    starty = 2

    for i in range(0, 20): 
        for j in range(0, 20):
            Gridd.grid[1][1].temp = 30
            Gridd.grid[1][1].state = 0

    Gridd.grid[startx][starty].temp = 200
    Gridd.grid[startx][starty].state = 1
    Gridd.display_grid(burningNodes={(startx,starty)})