import graphviz

class KdTree():
    def __init__(self, d):
        self.d = d
        self.root = Node()
        self.counter = 0

    def add_node(self, values):        
        return self.add_node_recursive(self.root, values, 0)
        
    def add_node_recursive(self, current, values, depth):
        if current.empty:
            current.set_values(values, self.counter)
            self.counter += 1
            return current
        dimension = depth % self.d
        if values[dimension] < current.values[dimension]:
            current.left = self.add_node_recursive(current.left, values, depth + 1)
        else:
            current.right = self.add_node_recursive(current.right, values, depth + 1)
        return current

    def find(self, values):
        return self.find_recursive(self.root, values, 0)

    def find_recursive(self, current, values, depth):

        if values == current.values:
            return current
        dimension = depth % self.d
        if values[dimension] < current.values[dimension]:
            if current.left.empty:
                return None
            else:
                return self.find_recursive(current.left, values, depth + 1)
        else:
            if current.right.empty:
                return None
            else:
                return self.find_recursive(current.right, values, depth + 1)

    def find_min(self, dimension):
        return self.find_min_recursive(self.root, dimension, 0)

    def find_min_recursive(self, current, dimension, depth):
        if current.empty:
            return current
        current_dimension = depth % self.d
        if current_dimension == dimension:
            if current.left.empty:
                return current
            else:
                return get_smaller_node(current, 
                                        self.find_min_recursive(current.left, dimension, depth + 1), 
                                        dimension)

        smallest_child = get_smaller_node(self.find_min_recursive(current.left, dimension, depth + 1), 
                                          self.find_min_recursive(current.right, dimension, depth + 1), 
                                          dimension)
        return get_smaller_node(current, smallest_child, dimension)

    def visualize(self):
        g = graphviz.Graph('g', filename='kdtree.gv', format = "png")
        g.graph_attr['rankdir'] = 'BT'
        self.visualize_recursive(self.root, None, g)
        g.view()
                
    def visualize_recursive(self, current, parent, g):
        list_str = current.id + "\n"
        list_str += ', '.join([str(elem) for elem in current.values])
        g.node(current.id, list_str)
        if parent != None:
            g.edge(current.id, parent.id)
        if not current.left.empty:
            self.visualize_recursive(current.left, current, g)
        if not current.right.empty:
            self.visualize_recursive(current.right, current, g)

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

def get_smaller_node(n1, n2, d):
    if n1.empty:
        return n2
    if n2.empty:
        return n1
    if n1.values[d] < n2.values[d]:
        return n1
    else:
        return n2