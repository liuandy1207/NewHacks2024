"""
This Python file simulates the fire.
"""
from grid import Grid

def simulate_fire(grid: Grid, burningNodes: set, N: int):
    for _ in range(N):
        for node in burningNodes:
            # node.fuel = node.type.updateFuel(node.fuel)
            # node.temp = node.type.updateTemp(node.temp)

            for neighbour in node.neighbours:
                neighbour.temp = round((node.temp + neighbour.temp) / 2, 2)

                for second_neighbour in neighbour.neighbours:
                    if second_neighbour == node:
                        continue
                    second_neighbour.temp = round((neighbour.temp + second_neighbour.temp) / 2, 2)
