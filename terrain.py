"""
This Python file defines the Terrain super class.
"""

class Terrain:
    """
    Fuel is represented in kg per 100m^2 (the size of one node). 
    Ignition temperature is represented in degrees Celsius.
    """
    fuel: float
    ignitionTemp: float

    def updateTempFuel(self, temp, fuel):
        raise NotImplementedError
