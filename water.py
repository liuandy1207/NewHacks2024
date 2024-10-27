from terrain import Terrain

class Water(Terrain):

    def __init__(self):
        self.fuel = 0
        self.ignitionTemp = 100000

    @staticmethod
    def updateTempFuel(node):
        node.state = 0
