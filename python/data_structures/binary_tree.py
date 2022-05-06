class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

        pass

    def pre_order(self):
        # method returns a list of the values in the tree in appropriate order
        # expected order ["a", "b", "d", "e", "c", "f", "g"]
        pass

    def in_order(self):
        # method returns a list of the values in the tree in appropriate order
        # expected order ["d", "b", "e", "a", "f", "c", "g"]
        pass

    def post_order(self):
        # method returns a list of the values in the tree in appropriate order
        # Expected order ["d", "e", "b", "f", "g", "c", "a"]
        pass


class Node:

    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None
