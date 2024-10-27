from terrain import Terrain

class Road(Terrain):

    def __init__(self):
        self.fuel = 10
        self.ignitionTemp = 1200

    @staticmethod
    def updateTempFuel(node):
        node.temp = min(1300, node.temp + 5)
        node.fuel = max(0, node.fuel - 1)

        if node.fuel == 0:
            node.state = 2
