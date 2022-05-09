import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_max()
    expected = 30

    assert actual == expected


def test_larger_tree():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(50)
    tree.root.right.left = Node(7)

    actual = tree.find_max()
    expected = 50

    assert actual == expected

