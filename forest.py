"""
This Python file implements the Forest class, subclass of Terrain.
"""
from terrain import Terrain
import random

class Forest(Terrain):
    """
    Fuel is represented in kg per 100m^2 (the size of one node).
    Ignition temperature is represented in degrees Celsius.
    """
    def __init__(self):
        self.fuel = random.randint(500, 1000)
        self.ignitionTemp = random.randint(250, 700)

    @staticmethod
    def updateTempFuel(node):
        node.temp = min(1200, node.temp + 15)
        node.fuel = max(0, node.fuel - 25)

        if node.fuel == 0:
            node.state = 2
