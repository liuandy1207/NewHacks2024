from matplotlib import pyplot as plt, colors
from matplotlib.animation import FuncAnimation
import numpy as np
from node import Node
from forest import Forest
from road import Road
import random
from simulate import simulate_fire

class Grid:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.forest = Forest()
        self.road = Road()
        self.grid = [[Node(0, random.choice([self.forest]), 30) for _ in range(self.column)]
                     for _ in range(self.row)]

        # Define colormap
        self.cmap = colors.ListedColormap(["lightgrey", "red"])
        self.bounds = [0, 1]
        self.norm = colors.BoundaryNorm(self.bounds, self.cmap.N)

    def update_node(self, row, column, state):
        self.grid[row][column].state = state

    def get_data(self):
        # Create a 2D array with the state of each node
        data = np.zeros((self.row, self.column), dtype=int)
        for i in range(self.row):
            for j in range(self.column):
                data[i][j] = self.grid[i][j].state
        return data

    def display_grid(self):
        # Initial setup of the plot
        fig, ax = plt.subplots()
        data = self.get_data()
        cax = ax.imshow(data, cmap=self.cmap, norm=self.norm, aspect='equal')

        # Customize grid
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
        plt.xticks(np.arange(-0.5, self.column, 1), [])
        plt.yticks(np.arange(-0.5, self.row, 1), [])
        ax.tick_params(axis='both', direction='in', length=5, pad=3, which='major')

        # Create a list to store text objects
        self.texts = []
        for i in range(self.row):
            for j in range(self.column):
                if self.grid[i][j].type == self.forest:
                    text = ax.text(j, i, "F", ha='center', va='center', color='black', fontsize=12,
                                   fontweight='bold')
                else:
                    text = ax.text(j, i, "R", ha='center', va='center', color='black', fontsize=12,
                                   fontweight='bold')
                self.texts.append(text)

        # Animation update function
        def update(frame, burningNodes):
            simulate_fire(self.grid, burningNodes)
            """
            self.grid[5][5].temp = 300
            self.grid[5][5].state = 1
            simulate_fire(self.grid, {(5, 5)})
            """

            # Update the image and the text based on the new data
            cax.set_array(self.get_data())
            for i, text in enumerate(self.texts):
                row = i // self.column
                col = i % self.column
                # Keep letters visible even if the state is burning
                text.set_text("F" if self.grid[row][col].type == self.forest else "R")

            return [cax] + self.texts

        # Set up animation
        ani = FuncAnimation(fig, update, frames=100, interval=200, blit=True)
        plt.show()


# Create and animate the grid
ngrid = Grid(10, 10)
ngrid.display_grid()
