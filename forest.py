"""
This Python file implements the Forest class, subclass of Terrain.
"""
from terrain import Terrain

class Forest(Terrain):
    """
    Fuel is represented in kg/100m^2. Ignition temperature is represented in degrees Celsius.
    """
    def __init__(self):
        self.fuel = 750
        self.ignitionTemp = 450
