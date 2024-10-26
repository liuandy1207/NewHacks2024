"""
This Python file simulates the fire.
"""
#from grid import Grid

def update_state(node):
    if node.temp > node.type.ignitionTemp:
        node.state = 1

#def simulate_fire(grid: Grid, burningNodes: set, N: int):
def update_first_neighbours(grid, x, y):
    try:
        grid[x-1][y-1].temp = round((grid[x-1][y-1].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x-1][y-1])
    except IndexError:
        pass

    try:
        grid[x-1][y].temp = round((grid[x-1][y].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x-1][y])
    except IndexError:
        pass

    try:
        grid[x-1][y+1].temp = round((grid[x-1][y+1].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x-1][y+1])
    except IndexError:
        pass

    try:
        grid[x][y-1].temp = round((grid[x][y-1].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x][y-1])
    except IndexError:
        print("lollll")

    try:
        grid[x][y+1].temp = round((grid[x][y+1].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x][y+1])
    except IndexError:
        pass

    try:
        grid[x+1][y-1].temp = round((grid[x+1][y-1].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x+1][y-1])
    except IndexError:
        pass

    try:
        grid[x+1][y].temp = round((grid[x+1][y].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x+1][y])
    except IndexError:
        pass

    try:
        grid[x+1][y+1].temp = round((grid[x+1][y+1].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x+1][y+1])
    except IndexError:
        pass


def update_second_neighbours(grid, x, y):
    try:
        grid[x - 2][y - 2].temp = round((grid[x - 2][y - 2].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x-2][y-2])
    except IndexError:
        pass

    try:
        grid[x - 2][y].temp = round((grid[x - 2][y].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x-2][y])
    except IndexError:
        pass

    try:
        grid[x - 2][y + 2].temp = round((grid[x - 2][y + 2].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x-2][y+2])
    except IndexError:
        pass

    try:
        grid[x][y - 2].temp = round((grid[x][y - 2].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x][y-2])
    except IndexError:
        pass

    try:
        grid[x][y + 2].temp = round((grid[x][y + 2].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x][y+2])
    except IndexError:
        pass

    try:
        grid[x + 2][y - 2].temp = round((grid[x + 2][y - 2].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x+2][y-2])
    except IndexError:
        pass

    try:
        grid[x + 2][y].temp = round((grid[x + 1][y].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x+2][y])
    except IndexError:
        pass

    try:
        grid[x + 2][y + 2].temp = round((grid[x + 2][y + 2].temp + grid[x][y].temp) / 2, 2)
        update_state(grid[x+2][y+2])
    except IndexError:
        pass


def simulate_fire(grid, burningNodes: set):
    for _ in range(1):
        for x, y in burningNodes:
            # node.fuel = node.type.updateFuel(node.fuel)
            # node.temp = node.type.updateTemp(node.temp)

            update_first_neighbours(grid, x, y)
            update_second_neighbours(grid, x, y)



            # for neighbour in node.neighbours:
            #     neighbour.temp = round((node.temp + neighbour.temp) / 2, 2)
            # 
            #     for second_neighbour in neighbour.neighbours:
            #         if second_neighbour == node:
            #             continue
            #         second_neighbour.temp = round((neighbour.temp + second_neighbour.temp) / 2, 2)
        