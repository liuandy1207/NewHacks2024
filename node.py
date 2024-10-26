"""
This file defines the Node class for our program.
"""
from terrain import Terrain

class Node:
    """
    A class representing a 1km x 1km square of a map.
    """
    state: int
    temp: float
    elevation: int
    fuel: float
    type: Terrain
    neighbours = set

    def __init__(self, state, type, temp):
        self.temp = temp
        '''self.elevation = elevation'''
        self.type = type
        self.state = state
        #self.neighbours = neighbours
        '''
        self.setFuel()'''

    '''def setFuel(self):
        self.fuel = Terrain.fuel'''

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
