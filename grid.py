import matplotlib as mpl
from fontTools.merge import cmap
from matplotlib import pyplot, pyplot as plt
import numpy as np

"Grid of the simulation"

class Grid:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def create_grid(self):
        cmap = plt.cm.binary
        grid = np.random.choice([0,1], size=(self.row, self.column))
        plt.figure(figsize=(6, 6))
        plt.imshow(grid, cmap=cmap)
        plt.grid(which='both', color='gray', linestyle='-', linewidth=1)
        plt.xticks(range(self.column))
        plt.yticks(range(self.row))
        plt.gca().set_xticks(np.arange(-0.5, self.column, 1), minor=True)
        plt.gca().set_yticks(np.arange(-0.5, self.row, 1), minor=True)
        plt.gca().grid(which="minor", color="gray", linestyle='-', linewidth=1)
        plt.show()

ngrid = Grid(2,2)
ngrid.create_grid()

