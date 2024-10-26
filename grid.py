import matplotlib as mpl
from fontTools.merge import cmap
from matplotlib import pyplot, pyplot as plt, colors
import numpy as np
from node import Node

class Grid:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.grid = [[Node(0) for _ in range(self.column)] for _ in range(self.row)]
        #lightgrey 0 = not burning, black 1 = burnt
        self.cmap = colors.ListedColormap(["lightgrey", "black"])
        self.bounds = [0,1]
        self.norm = colors.BoundaryNorm(self.bounds, self.cmap.N)

    def update_node(self, row, column, state):
        self.grid[row][column].state = state

    def display_grid(self):
        data = np.zeros((self.row, self.column), dtype=int)
        for i in range(self.row):
            for j in range(self.column):
                data[i][j] = self.grid[i][j].state
        fig, ax = plt.subplots()
        cax = ax.imshow(data, cmap=self.cmap, norm=self.norm,aspect='equal')
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
        plt.xticks(np.arange(-.5, self.column, 1), [])
        plt.yticks(np.arange(-.5, self.row, 1), [])


        plt.show()

ngrid = Grid(10,10)
ngrid.update_node(5, 5, 1)  # Set state to 1 (active)
ngrid.update_node(5, 6, 1)  # Set state to 2 (burning)
ngrid.update_node(5, 7, 0)


ngrid.display_grid()
