import kd_tree

def find(values, tree):
    found = tree.find(values)
    if found == None:
        print("Not found {}".format(values))
    else:
        print("Found {} with id {}".format(values, found.id))

def create_test_tree_1():
    tree = kd_tree.KdTree(2)
    tree.add([200,200])
    tree.add([150,150])
    tree.add([160,140])
    tree.add([160,160])
    tree.add([170,170])
    return tree

def create_test_tree_2():
    tree = kd_tree.KdTree(2)
    tree.add([200,200])
    tree.add([150,150])
    tree.add([100,100])
    return tree

#find([100,100], my_2d_tree)
#find([0,100], my_2d_tree)

#print("Smalles node values d=0: {}".format(my_2d_tree.find_min(0).values))
#print("Smalles node values d=1: {}".format(my_2d_tree.find_min(1).values))
my_2d_tree = create_test_tree_1()
my_2d_tree.visualize()
removed = my_2d_tree.remove([200,200])
print(removed)
my_2d_tree.visualize("deleted.gv")