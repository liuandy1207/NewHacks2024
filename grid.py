from matplotlib import pyplot as plt, colors
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
import numpy as np
from node import Node
from forest import Forest
from road import Road
from building import Building
from water import Water
import random
from simulate import simulate_fire

class Grid:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.forest = Forest()
        self.road = Road()
        self.grid = [[Node(0, 30, self.forest) for _ in range(self.column)]
                    for _ in range(self.row)]

        # Define colormap
        self.cmap = colors.ListedColormap(["lightgrey", "red", "brown", "orange"])
        self.bounds = [0, 1, 2, 3, 4]
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


    def display_grid(self, burningNodes):
        # Initial setup of the plot
        fig, ax = plt.subplots(figsize=(12, 8))
        data = self.get_data()
        cax = ax.imshow(data, cmap=self.cmap, norm=self.norm, aspect='equal')

        # Customize grid
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.1)
        plt.xticks(np.arange(-0.5, self.column, 1), [])
        plt.yticks(np.arange(-0.5, self.row, 1), [])
        ax.tick_params(axis='both', direction='in', length=0.1, pad=3, which='major')

        color_legend_handles = [
            Patch(color="lightgrey", label="Not Burning"),
            Patch(color="Orange", label="Close to Burning"),
            Patch(color="red", label="Burning"),
            Patch(color="brown", label="Burnt")]
        
        symbol_legend_handles = [
            Line2D([0], [0], marker='None', linestyle='None', color='b', markerfacecolor='black', markersize=10, label='F - Forest'),
            Line2D([0], [0], marker='None', linestyle='None', color='b', markerfacecolor='black', markersize=10, label='B - Building'),
            Line2D([0], [0], marker='None', linestyle='None', color='b', markerfacecolor='black', markersize=10, label='W - Water'),
            Line2D([0], [0], marker='None', linestyle='None', color='w', markerfacecolor='green', markersize=10, label='R - Road')]
        # Add the legend to the plot
        color_legend = ax.legend(handles=color_legend_handles + symbol_legend_handles, title="Legend",
                             loc="upper left", bbox_to_anchor=(1.05, 1), borderaxespad=0.)

        


        # Create a list to store text objects
        self.texts = []
        for i in range(self.row):
            for j in range(self.column):
                letter = ""
                if self.grid[i][j].type == Forest:
                    letter = "F"
                elif self.grid[i][j].type == Water:
                    letter = "W"
                elif self.grid[i][j].type == Building:
                    letter = "B"
                elif self.grid[i][j].type == Road:
                    letter = "R"

                # Create the text object and store it
                text = ax.text(j, i, letter, ha='center', va='center', color='black', fontsize=10, fontweight='bold')
                self.texts.append(text)


        # Animation update function
        def update(frame):
            simulate_fire(self.grid, burningNodes)
            '''
            self.grid[5][5].temp = 300
            self.grid[5][5].state = 1
            simulate_fire(self.grid, {(5, 5)})
            '''
            #print("above node:", self.grid[1][2])
            #print("below node:", self.grid[1][2])

            # Update the image and the text based on the new data
            cax.set_array(self.get_data())
            for i, text in enumerate(self.texts):
                row = i // self.column
                col = i % self.column

                # Keep letters visible even if the state is burning
                #text.set_text("F")
                if isinstance(self.grid[row][col].type, Forest):
                    text.set_text("F")
                elif isinstance(self.grid[row][col].type, Water):
                    text.set_text("W")
                elif isinstance(self.grid[row][col].type, Building):
                    text.set_text("B")
                elif isinstance(self.grid[row][col].type, Road):
                    text.set_text("R")
                    

                text.set_fontsize(5)

            return [cax] + self.texts

        # Set up animation
        ani = FuncAnimation(fig, update, frames=100, interval=1000, blit=False)
        plt.show()
