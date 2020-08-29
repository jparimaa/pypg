import kd_tree

my_2d_tree = kd_tree.KdTree(2)
my_2d_tree.add_node([20,20])
my_2d_tree.add_node([10,10])
my_2d_tree.add_node([30,10])
my_2d_tree.add_node([5,15])
my_2d_tree.add_node([40,5])
#my_2d_tree.visualize()
my_2d_tree.print()