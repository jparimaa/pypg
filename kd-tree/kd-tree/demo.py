import kd_tree

def find(values, tree):
    found = tree.find(values)
    if found == None:
        print("Not found")
    else:
        print("Found {} with id {}".format(values, found.id))

my_2d_tree = kd_tree.KdTree(2)
my_2d_tree.add_node([20,20])
my_2d_tree.add_node([10,10])
my_2d_tree.add_node([30,10])
my_2d_tree.add_node([0,15])
my_2d_tree.add_node([40,5])
my_2d_tree.add_node([5,5])
my_2d_tree.add_node([100,100])

find([100,100], my_2d_tree)
find([0,100], my_2d_tree)

print(my_2d_tree.find_min(0).values)
print(my_2d_tree.find_min(1).values)

my_2d_tree.visualize()