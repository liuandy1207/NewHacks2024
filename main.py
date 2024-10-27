from grid import Grid
from copy import deepcopy
from forest import Forest
from road import Road
from building import Building
from water import Water


if __name__ == "__main__":
    Gridd = Grid(50, 50)

    for i in range(0, 50):
        for j in range(0, 50):
            if j >= 30 and j <= 30:
                Gridd.grid[i][j].temp = 20
                Gridd.grid[i][j].state = 0
                Gridd.grid[i][j].type = Water()
            elif i == 20: 
                Gridd.grid[i][j].temp = 40
                Gridd.grid[i][j].state = 0
                Gridd.grid[i][j].type = Road()
            elif i == 22 or i == 24 or i == 26:
                Gridd.grid[i][j].temp = 20
                Gridd.grid[i][j].state = 0
                Gridd.grid[i][j].type = Building()
            else: 
                Gridd.grid[i][j].temp = 30
                Gridd.grid[i][j].state = 0
                Gridd.grid[i][j].type = Forest()

    startx = 10
    starty = 10

    Gridd.grid[startx][starty].temp = 500
    Gridd.grid[startx][starty].state = 1
    Gridd.display_grid(burningNodes={(startx,starty)})
