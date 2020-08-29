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

    def visualize(self):
        g = graphviz.Graph('g', filename='kdtree.gv', format = "png")
        g.graph_attr['rankdir'] = 'BT'
        self.visualize_recursive(self.root, None, g)
        g.view()
                
    def visualize_recursive(self, current, parent, g):
        list_str = ', '.join([str(elem) for elem in current.values]) 
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

    def set_values(self, values, id):
        self.values = values
        self.id = str(id)
        self.empty = False
        self.left = Node()
        self.right = Node()