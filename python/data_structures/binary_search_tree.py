from data_structures.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        pass

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find_max(self):
        pass

class Node():

    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None
