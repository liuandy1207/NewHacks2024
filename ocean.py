from terrain import Terrain

class Ocean(Terrain):
    fuel = 0
    ignitionTemp = 1300

    @staticmethod
    def updateTempFuel(node):
        node.state = 0
