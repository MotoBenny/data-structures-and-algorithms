from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree_one, tree_two):
    """
    For each node in tree_a traverse through tree_b, If node in tree_a == node in tree_b, add node. Value to set.
    at end of method return set.

    """
    match_values = set()

    ht = Hashtable()

    tree_one_values = BinaryTree.pre_order(tree_one)
    tree_two_values = BinaryTree.pre_order(tree_two)

    for num in tree_one_values:
        ht.set(num, num)

    for num in tree_two_values:

        if ht.contains(num):
            match_values.add(num)

    return match_values
