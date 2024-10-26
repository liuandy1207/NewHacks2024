"""
This Python file defines the Terrain super class.
"""

class Terrain:
    fuel: float
    ignitionTemp: float

    def updateTemp(self, temp):
        raise NotImplementedError

    def updateFuel(self, fuel):
        raise NotImplementedError
