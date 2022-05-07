from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def add(self, value):

        def climb(root, new_node):  # root(10) new (5)
            # Base case
            if not root:
                return

            #  we have [5] to add to tree with root of 10
            if new_node.value < root.value:
                # go left
                if root.left:
                    climb(root.left, new_node)
                else:
                    root.left = new_node
            else:
                #  go right
                if root.right:
                    climb(root.right, new_node)
                else:
                    root.right = new_node
        node_to_add = Node(value)
        if not self.root:
            self.root = node_to_add
            return

        climb(self.root, node_to_add)

    def contains(self, value):
        # Log(N)
        def climb(root, search_value):  # 10, 15

            if root.value == search_value:  # we've found the search val, return true
                print("catch")
                return True
            elif search_value > root.value and root.right is None:
                return False
            elif search_value < root.value and root.left is None:
                return False

            if root.value < search_value:
                return climb(root.right, search_value)
            elif root.value > search_value:
                return climb(root.left, search_value)

        return climb(self.root, value)
