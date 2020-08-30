import graphviz
import copy

class KdTree():
    def __init__(self, d):
        self.d = d
        self.root = Node()
        self.counter = 0
        self.dummyID = -1

    def add(self, values):        
        return self.__add_recursive(self.root, values, 0)
        
    def __add_recursive(self, current, values, depth):
        if current.empty:
            current.set_values(values, self.counter)
            self.counter += 1
            return current
        dimension = depth % self.d
        if values[dimension] < current.values[dimension]:
            current.left = self.__add_recursive(current.left, values, depth + 1)
        else:
            current.right = self.__add_recursive(current.right, values, depth + 1)
        return current

    def remove(self, values):
        return self.__remove_recursive(self.root, values, 0)

    def __remove_recursive(self, current, values, depth):
        if current.empty:
            return []
        dimension = depth % self.d
        if current.values == values:
            if not current.right.empty:
                min_node = self.__find_min_recursive(current.right, dimension, depth + 1)
                replace_node = copy.deepcopy(min_node)
                replace_node.right = self.__remove_recursive(current.right, min_node.values, depth + 1)
                current = replace_node
            elif not current.left.empty:
                min_node = self.__find_min_recursive(current.left, dimension, depth + 1)
                replace_node = copy.deepcopy(min_node)
                replace_node.right = self.__remove_recursive(current.left, min_node.values, depth + 1)
                current = replace_node
            else:
                current.reset()
            return current
        if values[dimension] < current.values[dimension]:
            current.left = self.__remove_recursive(current.left, values, depth + 1)
        else:
            current.right = self.__remove_recursive(current.right, values, depth + 1)
        return current

    def find(self, values):
        return self.__find_recursive(self.root, values, 0)

    def __find_recursive(self, current, values, depth):
        if values == current.values:
            return current
        dimension = depth % self.d
        if values[dimension] < current.values[dimension]:
            if current.left.empty:
                return None
            else:
                return self.__find_recursive(current.left, values, depth + 1)
        else:
            if current.right.empty:
                return None
            else:
                return self.__find_recursive(current.right, values, depth + 1)

    def find_min(self, dimension):
        return self.__find_min_recursive(self.root, dimension, 0)

    def __find_min_recursive(self, current, dimension, depth):
        if current.empty:
            return current
        current_dimension = depth % self.d
        if current_dimension == dimension:
            if current.left.empty:
                return current
            else:
                return get_smaller_node(current, 
                                        self.__find_min_recursive(current.left, dimension, depth + 1), 
                                        dimension)

        smallest_child = get_smaller_node(self.__find_min_recursive(current.left, dimension, depth + 1), 
                                          self.__find_min_recursive(current.right, dimension, depth + 1), 
                                          dimension)
        return get_smaller_node(current, smallest_child, dimension)

    def visualize(self, filename="kdtree.gv"):
        g = graphviz.Graph("g", filename=filename, format = "png")
        g.graph_attr["rankdir"] = "BT"
        self.dummyID = -1
        self.__visualize_recursive(self.root, None, g)
        g.view()
                
    def __visualize_recursive(self, current, parent, g):                
        if current.empty:
            dummyID = str(self.dummyID)
            dummyNode = g.node(dummyID, "", style="invis")
            if parent != None:
                g.edge(dummyID, parent.id)
            self.dummyID -= 1
            return
        list_str = ', '.join([str(elem) for elem in current.values])
        g.node(current.id, list_str)
        if parent != None:
            g.edge(current.id, parent.id)
        self.__visualize_recursive(current.left, current, g)
        self.__visualize_recursive(current.right, current, g)

class Node():
    def __init__(self):
        self.empty = True
        self.values = []

    def set_values(self, values, id):
        self.values = values
        self.id = str(id)
        self.empty = False
        self.left = Node()
        self.right = Node()

    def reset(self):
        self.empty = True
        self.id = ""
        self.values = []
        
def get_smaller_node(n1, n2, d):
    if n1.empty:
        return n2
    if n2.empty:
        return n1
    if n1.values[d] < n2.values[d]:
        return n1
    else:
        return n2