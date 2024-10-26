"""
This Python file defines the Terrain super class.
"""

class Terrain:
    fuel: float
    ignitionTemp: float

    def changeTemp(self, temp):
        raise NotImplementedError

    def changeFuel(self, fuel):
        raise NotImplementedError
