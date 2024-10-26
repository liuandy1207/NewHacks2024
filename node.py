"""
This file defines the Node class for our program.
"""

class Node:
    """
    A class representing a 1km x 1km square of a map.
    """
    state: int
    temp: float
    elevation: int
    type: str
    neighbours = set

    def __init__(self, state, temp, elevation, type, neighbours):
        self.temp = temp
        self.elevation = elevation
        self.type = type
        self.state = state
        self.neighbours = neighbours

    def update(self):
        """
        Update current node based on the state of neighbouring nodes using Game of Life rules.
        """
        burningNeighbours = 0
        for neighbour in self.neighbours:
            if neighbour.state == 1:
                burningNeighbours += 1

        if self.state == 0:
            if burningNeighbours == 3:
                self.state = 1
        else:
            if burningNeighbours < 2 or burningNeighbours > 3:
                self.state = 0
