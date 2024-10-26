from terrain import Terrain

class Road(Terrain):
    fuel: float
    ignitionTemp: float

    def changeTemp(self, temp):
        raise NotImplementedError

    def changeFuel(self, fuel):
        raise NotImplementedError