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
