"""
This Python file defines the Terrain super class.
"""

class Terrain:
    """
    Fuel is represented in kg/100m^2. Ignition temperature is represented in degrees Celsius.
    """
    fuel: float
    ignitionTemp: float

    def updateTemp(self, temp):
        raise NotImplementedError

    def updateFuel(self, fuel):
        raise NotImplementedError
