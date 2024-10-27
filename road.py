from terrain import Terrain

class Road(Terrain):
    fuel = 0
    ignitionTemp = 10000

    @staticmethod
    def updateTempFuel(node):
        node.temp = min(1200, node.temp + 15)
        node.fuel = max(0, node.fuel - 50)

        if node.fuel == 0:
            node.state = 2
