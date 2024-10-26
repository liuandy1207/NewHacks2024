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

        zvals = np.random.rand(self.row, self.column) * -2

        # make a color map of fixed colors
        cmap = mpl.colors.ListedColormap(['white', 'black', 'red'])
        bounds = [-6, -2, 2, 6]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

        # tell imshow about color map so that only set colors are used
        img = pyplot.imshow(zvals, interpolation='nearest',
                            cmap="Blues", norm=norm)

        pyplot.show()
ngrid = Grid(1000,1000)
ngrid.create_grid()

