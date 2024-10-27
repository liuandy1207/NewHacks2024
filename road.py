from terrain import Terrain

class Road(Terrain):

    def __init__(self):
        self.fuel = 0
        self.ignitionTemp = 1200

    @staticmethod
    def updateTempFuel(node):
        node.state = 2
