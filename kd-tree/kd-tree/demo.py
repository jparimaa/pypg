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

def create_test_tree_3():
    tree = kd_tree.KdTree(2)
    tree.add([200,200])
    tree.add([250,250])
    tree.add([300,300])
    tree.add([350,350])
    tree.add([400,400])
    tree.add([450,450])
    return tree

def create_test_tree_4():
    tree = kd_tree.KdTree(2)
    tree.add([450,450])
    tree.add([400,400])
    tree.add([350,350])
    tree.add([300,300])
    tree.add([250,250])
    tree.add([200,200])
    return tree

def create_test_tree_1():
    tree = kd_tree.KdTree(2)
    tree.add([300,300])
    tree.add([200,200])
    tree.add([100,100])
    tree.add([50,50])
    tree.add([150,500])
    tree.add([250,250])
    tree.add([400,400])
    tree.add([350,350])
    tree.add([500,500])
    tree.add([425,425])
    return tree

#find([100,100], my_2d_tree)
#find([0,100], my_2d_tree)

#print("Smalles node values d=0: {}".format(my_2d_tree.find_min(0).values))
#print("Smalles node values d=1: {}".format(my_2d_tree.find_min(1).values))
my_2d_tree = create_test_tree_1()
#my_2d_tree.visualize()
nearest = my_2d_tree.find_nearest([426,426])
print(nearest)
#removed = my_2d_tree.remove([450,450])
#print(removed)
#my_2d_tree.visualize("deleted.gv")