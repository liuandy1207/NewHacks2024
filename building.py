from terrain import Terrain
import random

class Building(Terrain):

    def __init__(self):
        self.fuel = random.randint(1300, 1700)
        self.ignitionTemp = random.randint(1000, 1200)

    @staticmethod
    def updateTempFuel(node):
        node.temp = min(1300, node.temp + 30)
        node.fuel = max(0, node.fuel - 50)

        if node.fuel == 0:
            node.state = 2
