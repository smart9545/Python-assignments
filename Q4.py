#############################################
#	COMPSCI 105 SS C, 2018              #
#	Assignment 2                        #
#                                           #
#	@author  	FanYu and fyu914    #
#	@version	10/2/2018           #
#############################################
"""
Description：
Define a function, convert_flat_to_nested_list() that will take a list input representing
a flat list binary tree. This function should output a list of the same tree in nested list format.
Define a function,convert_flat_to_tree() that take a flat list as parameter, output a BinaryTree object.
Define a function,convert_tree_to_nested() that take a BinaryTree object as parameter,output a nested list.
"""
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_left(self):
         return self.left

    def get_right(self):
         return self.right

    def get_data(self):
         return self.data

    def set_data(self, data):
         self.data = data

    ##You may choose to implement this function which adds a
    ##BinaryTree to the left instead of any data
    def insert_tree_left(self, left_tree):
        if self.left == None:
            self.left = left_tree
      

    ##You may choose to implement this function which adds a
    ##BinaryTree to the right instead of any data
    def insert_tree_right(self, right_tree):
        if self.right == None:
            self.right = right_tree

    
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.left = self.left
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data)
            t.right = self.right
            self.right = t


##This function should take in a list in flat list format and
##return a list in nested list format
def convert_flat_to_nested_list(flat_list):
    tree_object= convert_flat_to_tree(flat_list, 1)
    nested_list= convert_tree_to_nested(tree_object)
    return nested_list


##You may choose to implement the following recursive method to
##turn a flat list into a BinaryTree structure
def convert_flat_to_tree(flat_list, index):
    if index>= len (flat_list) or flat_list[index]== None:
        return None
    else:
         root= BinaryTree(None)
         root.set_data(flat_list[index])
         root.insert_tree_left(convert_flat_to_tree(flat_list, 2*index))
         root.insert_tree_right(convert_flat_to_tree(flat_list, 2*index+1))
         return root


          
            
##You may choose to implement the following recursive method to
##turn a BinaryTree into a nested list format
def convert_tree_to_nested(tree):
    nested_list = [None]*3
    if tree.get_data() == None:
        return None
    else:
            nested_list[0]= tree.get_data()
            if tree.get_left()!=None:
                nested_list[1] = convert_tree_to_nested(tree.get_left())
            if tree.get_right()!= None:
                nested_list[2]= convert_tree_to_nested(tree.get_right())
            return nested_list

##test implementation
flat_list = [None, 10, 5, 15, None, None, 11, 22]
nested_list = convert_flat_to_nested_list(flat_list)
print(nested_list)



