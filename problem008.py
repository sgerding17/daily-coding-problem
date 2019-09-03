#!/usr/bin/python3

# 2019-09-01
#
# A unival tree (which stands for "universal value") is a tree where all nodes
# under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
# 
# For example, the following tree has 5 unival subtrees:
#
#     0
#    / \
#   1   0
#      / \
#     1   0
#    / \
#   1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_leaf(node): return not node.left and not node.right

class unival_info:
    def __init__(self, count, is_unival):
        self.count = count
        self.is_unival = is_unival

def compute_unival(node):
    if not node: return unival_info(0, False)
    if is_leaf(node): return unival_info(1, True)

    left = compute_unival(node.left)
    right = compute_unival(node.right)

    # Note that short-circuit prevents accessing a null child's value because
    # its is_unival will be false.
    is_unival = (left.is_unival and right.is_unival and
                 node.left.val == node.right.val == node.val)

    return unival_info(left.count + right.count + (1 if is_unival else 0),
                       is_unival)

def count_unival(node):
    return compute_unival(node).count

tree = Node(0,
            Node(1),
            Node(0,
                 Node(1,
                      Node(1),
                      Node(1)),
                 Node(0)))

assert count_unival(tree) == 5
