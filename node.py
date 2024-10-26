"""
This file defines the Node class for our program.
"""

class Node:
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
        raise NotImplementedError
