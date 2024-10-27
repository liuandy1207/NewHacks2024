"""
This Python file simulates the fire.
"""
# from grid import Grid
# from forest import Forest

def update_self(grid, x, y):
    grid[x][y].type.updateTempFuel(grid[x][y])
    # print(grid[x][y].state)

def update_state(grid, x, y, burningNodes):
    try:
        if grid[x][y].state == 0 and grid[x][y].temp > grid[x][y].type.ignitionTemp:
            grid[x][y].state = 1
            burningNodes.add((x, y))
    except IndexError:
        pass

def update_first_neighbours(grid, x, y):
    try:
        if (x - 1) >= 0 and (y - 1) >= 0:
            grid[x-1][y-1].temp = round((grid[x-1][y-1].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x - 1) >= 0 and (y) >= 0:
            grid[x-1][y].temp = round((grid[x-1][y].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x - 1) >= 0 and (y + 1) >= 0:
            grid[x-1][y+1].temp = round((grid[x-1][y+1].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x >= 0) and (y - 1) >= 0:
            grid[x][y-1].temp = round((grid[x][y-1].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x >= 0) and (y + 1) >= 0:
            grid[x][y+1].temp = round((grid[x][y+1].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x + 1) >= 0 and (y - 1) >= 0:
            grid[x+1][y-1].temp = round((grid[x+1][y-1].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x + 1) >= 0 and y >= 0:
            grid[x+1][y].temp = round((grid[x+1][y].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x + 1) >= 0 and (y + 1) >= 0:
            grid[x+1][y+1].temp = round((grid[x+1][y+1].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass


def update_second_neighbours(grid, x, y):
    try:
        if (x - 2) >= 0 and (y - 2) >= 0:
            grid[x - 2][y - 2].temp = round((grid[x - 2][y - 2].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x - 2) >= 0 and (y) >= 0:
            grid[x - 2][y].temp = round((grid[x - 2][y].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x - 2) >= 0 and (y + 2) >= 0:
            grid[x - 2][y + 2].temp = round((grid[x - 2][y + 2].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x >= 0) and (y - 2) >= 0:
            grid[x][y - 2].temp = round((grid[x][y - 2].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x >= 0) and (y + 2) >= 0:
            grid[x][y + 2].temp = round((grid[x][y + 2].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x + 2) >= 0 and (y - 2) >= 0:
            grid[x + 2][y - 2].temp = round((grid[x + 2][y - 2].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x + 2) >= 0 and (y) >= 0:
            grid[x + 2][y].temp = round((grid[x + 1][y].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass

    try:
        if (x + 2) >= 0 and (y + 2) >= 0:
            grid[x + 2][y + 2].temp = round((grid[x + 2][y + 2].temp + grid[x][y].temp) / 2, 2)
    except IndexError:
        pass


def simulate_fire(grid, burningNodes: set):
    for _ in range(1):
        newBurningNodes = set()
        for x, y in burningNodes:
            # node.fuel = node.type.updateFuel(node.fuel)
            # node.temp = node.type.updateTemp(node.temp)
            update_self(grid, x, y)
            update_first_neighbours(grid, x, y)
            update_second_neighbours(grid, x, y)

            update_state(grid, x - 1, y - 1, newBurningNodes)
            update_state(grid, x - 1, y, newBurningNodes)
            update_state(grid, x - 1, y + 1, newBurningNodes)

            update_state(grid, x, y - 1, newBurningNodes)
            update_state(grid, x, y + 1, newBurningNodes)

            update_state(grid, x + 1, y - 1, newBurningNodes)
            update_state(grid, x + 1, y, newBurningNodes)
            update_state(grid, x + 1, y + 1, newBurningNodes)

            update_state(grid, x - 2, y - 2, newBurningNodes)
            update_state(grid, x - 2, y, newBurningNodes)
            update_state(grid, x - 2, y + 2, newBurningNodes)

            update_state(grid, x, y - 2, newBurningNodes)
            update_state(grid, x, y + 2, newBurningNodes)

            update_state(grid, x + 2, y - 2, newBurningNodes)
            update_state(grid, x + 2, y, newBurningNodes)
            update_state(grid, x + 2, y + 2, newBurningNodes)

        for node in newBurningNodes:
            burningNodes.add(node)
