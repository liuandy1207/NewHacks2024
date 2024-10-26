import matplotlib as mpl
from fontTools.merge import cmap
from matplotlib import pyplot, pyplot as plt, colors
import numpy as np

"Grid of the simulation"

class Grid:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def create_grid(self):
        # Create a row x column grid with all values set to a single level
        data = np.zeros((self.row, self.column))

        # Set up the colormap with a single default color
        cmap = colors.ListedColormap(['lightgray'])
        bounds = [0, 1]  # Boundaries for single color
        norm = colors.BoundaryNorm(bounds, cmap.N)

        # Plot the initial grid with one color
        fig, ax = plt.subplots()
        ax.imshow(data, cmap=cmap, norm=norm)

        # Draw gridlines for clarity
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.5)
        ax.set_xticks(np.arange(0, self.column, 10))
        ax.set_yticks(np.arange(0, self.row, 10))

        ax.set_xticklabels([])
        ax.set_yticklabels([])

        ax.tick_params(axis='both', direction='in', length=1, pad=3, which='major')

        plt.show()

        # Later on, to change colors, you can update `data` with new values
        # and replot with a new colormap or colors for each value.

ngrid = Grid(500,500)
ngrid.create_grid()

