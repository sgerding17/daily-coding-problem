#!/usr/bin/python

# 2019-08-27
#
# Given the root to a binary tree, implement serialize(root), which serializes
# the tree into a string, and deserialize(s), which deserializes the string
# back into the tree.
#
# For example, given the following Node class:

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

SEP = " "
TERM = "$"

def serialize(node):
    if not node: return TERM
    return node.val + SEP + serialize(node.left) + SEP + serialize(node.right)

def deserialize_aux(s):
    if s == TERM: return (None, "")
    (first, rest) = s.split(SEP, 1)
    if first == TERM: return (None, rest)
    (left, rest) = deserialize_aux(rest)
    (right, rest) = deserialize_aux(rest)
    return (Node(first, left, right), rest)

def deserialize(s):
    return deserialize_aux(s)[0]

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

print serialize(node)
print serialize(deserialize(serialize(node)))
