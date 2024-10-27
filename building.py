from terrain import Terrain

class Building(Terrain):
    fuel = 1500
    ignitionTemp = 1100

    @staticmethod
    def updateTempFuel(node):
        node.temp = min(1200, node.temp + 15)
        node.fuel = max(0, node.fuel - 50)

        if node.fuel == 0:
            node.state = 2
