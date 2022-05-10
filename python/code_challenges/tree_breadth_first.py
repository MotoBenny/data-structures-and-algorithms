from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):

    breadth = Queue()
    values = []

    if not tree:
        return values
    if not tree.root:
        return values
    if not breadth.front:
        breadth.enqueue(tree.root)
    while breadth.front:
        root = breadth.dequeue()
        values.append(root.value)
        if root.left:
            breadth.enqueue(root.left)
        if root.right:
            breadth.enqueue(root.right)

    return values
