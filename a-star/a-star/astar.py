from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
  
# 0 = free to move
# 1 = blocked
# 2 = closed
# 3 = open
# 4 = current
def find_path(grid, width, height, start, end, visualize=True):
    start_node = Node(None, start)
    end_node = Node(None, end)
    open_list = []
    closed_list = []
    open_list.append(start_node)
    total_loop_counter = 0
    grid_copies = []

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
                
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] < 0 or node_position[1] < 0 or node_position[0] > width - 1 or node_position[1] > height - 1:
                continue
            
            # Make sure not blocked
            if grid[node_position[0]][node_position[1]] == 1:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:            
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)
        
        if visualize:
            color_map = ListedColormap([[1, 1, 1], [0, 0, 0], [0.6, 0.6, 1], [0, 1, 0], [1, 0, 0]])
            max_columns = 10
            row_count = max(2, (total_loop_counter // max_columns) + 1)
            column_count = max(2, min(total_loop_counter + 1, max_columns))
            fig, axs = plt.subplots(row_count, column_count)
            fig.set_figwidth(20)
            visualize_grid = grid.copy()
            for n in open_list:
                visualize_grid[n.position[0]][n.position[1]] = 3
            for n in closed_list:
                visualize_grid[n.position[0]][n.position[1]] = 2          
            visualize_grid[current_node.position[0]][current_node.position[1]] = 4
            grid_copies.append(visualize_grid)
            last_index = 0
            for index, grid in enumerate(grid_copies):
                r = index // column_count
                c = index % column_count
                axs[r, c].get_xaxis().set_visible(False)
                axs[r, c].get_yaxis().set_visible(False)
                axs[r, c].set_title("%s" % (index + 1))
                axs[r, c].matshow(grid, cmap=color_map)
                last_index = index
            for index in range(last_index + 1, column_count * row_count):
                r = index // column_count
                c = index % column_count
                axs[r, c].axis("off")
            plt.show()

        total_loop_counter += 1

    # Path not found
    return []
