import kd_tree

def find(values, tree):
    found = tree.find(values)
    if found == None:
        print("Not found {}".format(values))
    else:
        print("Found {} with id {}".format(values, found.id))

my_2d_tree = kd_tree.KdTree(2)
my_2d_tree.add([25,40])
my_2d_tree.add([70,70])
my_2d_tree.add([50,30])
my_2d_tree.add([35,25])
my_2d_tree.add([30,20])
my_2d_tree.add([45,40])

#find([100,100], my_2d_tree)
#find([0,100], my_2d_tree)

#print("Smalles node values d=0: {}".format(my_2d_tree.find_min(0).values))
#print("Smalles node values d=1: {}".format(my_2d_tree.find_min(1).values))
my_2d_tree.visualize()
n = my_2d_tree.remove([70,70])
print(n.values)
my_2d_tree.visualize("deleted.gv")