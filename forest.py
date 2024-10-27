"""
This Python file implements the Forest class, subclass of Terrain.
"""
from terrain import Terrain

class Forest(Terrain):
    """
    Fuel is represented in kg per 100m^2 (the size of one node).
    Ignition temperature is represented in degrees Celsius.
    """
    fuel = 750
    ignitionTemp = 450

    @staticmethod
    def updateTempFuel(node):
        node.temp = min(1200, node.temp + 15)
        node.fuel = max(0, node.fuel - 50)

        if node.fuel == 0:
            node.state = 2
