from data_structures.queue import Queue


class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        Traverse the tree in a pro-order fashion
        return list of the values in correct order
        expected order ["a", "b", "d", "e", "c", "f", "g"]
        """
        def climb(root, values):  # arg is root, because every subtree is a tree root = Node or None Recursive
            # Recursive function needs to know when to stop, It needs the Base case
            if not root:
                return
            # add value to list
            values.append(root.value)
            # Go left
            climb(root.left, values)
            # Go right
            climb(root.right, values)
        ordered_values = []
        climb(self.root, ordered_values)

        return ordered_values

    def in_order(self):
        """
        # method returns a list of the values in the tree in appropriate order
        # expected order ["d", "b", "e", "a", "f", "c", "g"]
        # goes left, goes root, goes right
        """
        def climb(root, values):
            if not root:
                return
            # Go left
            climb(root.left, values)
            # add value to list
            values.append(root.value)
            # Go right
            climb(root.right, values)

        ordered_values = []
        climb(self.root, ordered_values)

        return ordered_values

    def post_order(self):
        # method returns a list of the values in the tree in appropriate order
        # Expected order ["d", "e", "b", "f", "g", "c", "a"]
        def climb(root, values):
            if not root:
                return
            # Go left
            climb(root.left, values)
            # Go right
            climb(root.right, values)
            # add value to list
            values.append(root.value)
        ordered_values = []
        climb(self.root, ordered_values)

        return ordered_values

    def find_max(self):

        if self.root is None:
            return None

        def climb(root, max):
            if root is None:
                return max
            if root.value > max:
                max = root.value
            max = climb(root.left, max)
            max = climb(root.right, max)
            return max

        result = climb(self.root, 0)
        return result

    def add(self, value):

        node = Node(value)

        if not self.root:
            self.root = node
            return

        breadth = Queue()

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                breadth.enqueue(front.left)

            if not front.right:
                front.right = node
                return
            else:
                breadth.enqueue(front.right)

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
