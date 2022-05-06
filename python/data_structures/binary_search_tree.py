from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """
    #
    # def __init__(self):
    #     pass

    def add(self, value):

        def climb(root, new_node): # root(10) new (5)
            # Base case
            if not root:
                return

            # we have [5] to add to tree with root of 10
            if new_node.value < root.value:
                # go left
                if root.left:
                    climb(root.left, new_node)
                else:
                    root.left = new_node

            else:
                # go right
                if root.rightt:
                    climb(root.right, new_node)
                else:
                    root.right = new_node
        if not self.root:
            self.root = Node(value)
            return

        node_to_add = Node(value)

        if not self.root:
            self.root = node_to_add
            return

        climb(self.root, value)







    # def __init__(self, data):
    #     self.data = data
    #     pass
    #
    # def insert(self, data):
    #     if self.data:
    #         if data < self.data:
    #             if self.left is None:
    #                 self.left = Node(data)
    #             else:
    #                 self.left.insert(data)
    #         elif data > self.data:
    #             if self.right is None:
    #                 self.right = Node(data)
    #             else:
    #                 self.right.insert(data)
    #     else:
    #         self.data = data
    #
    # def find_max(self):
    #     pass

