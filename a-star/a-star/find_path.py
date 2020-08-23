import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import random
import astar

def generate_grid(row_count, column_count):
    random.seed(3)
    total_count = row_count * column_count
    grid = np.zeros(total_count)
    for i in range(total_count):
        value = 0
        if random.randrange(100) < 10:
            value = 1
        grid[i] = value
    return grid.reshape((row_count, column_count))

width = 10
height = 10
grid = generate_grid(width, height)
#color_map = ListedColormap([[1, 1, 1], [0, 0, 0]])
#plt.matshow(grid, cmap = color_map)
#plt.show()
path = astar.find_path(grid, width, height, [0,0], [width - 1, height - 1])
