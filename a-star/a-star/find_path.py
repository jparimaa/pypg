import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import random
import astar

def generate_10x10_test_grid():
    grid = np.zeros(100)
    for i in range(16, 57, 10):
        grid[i] = 1
    for i in range(52, 57):
        grid[i] = 1
    return grid.reshape((10, 10))

def generate_grid(row_count, column_count):
    random.seed(5)
    total_count = row_count * column_count
    grid = np.zeros(total_count)
    for i in range(total_count):
        value = 0
        if random.randrange(100) < 30:
            value = 1
        grid[i] = value
    return grid.reshape((row_count, column_count))

width = 10
height = 10
grid = generate_10x10_test_grid()
#grid = generate_grid(width, height)
print(grid)
#color_map = ListedColormap([[1, 1, 1], [0, 0, 0]])
#plt.matshow(grid, cmap = color_map)
#plt.show()
path = astar.find_path(grid, width, height, [0,0], [width - 1, height - 1])
for p in path:
    grid[p[0]][p[1]] = 8
if len(path) > 0:
    print(path)
    print(grid)
else:
    print("Path not found")