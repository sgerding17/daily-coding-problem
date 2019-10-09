#!/usr/bin/python3

# 2019-09-29
#
# Given the root to a binary search tree, find the second largest node in the
# tree.

class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def second_largest_node(root):
    # The second largest element isn't defined for a zero- or one-node tree.
    assert root and (root.left or root.right)

    # Step 1: Find the maximum node and its parent.
    p = root
    parent = None
    while p.right:
        parent = p
        p = p.right

    # Step 2: If the maximum is a leaf, return the parent.
    if not p.left: return parent

    # Step 3: Otherwise, return the maximum of the maximum node's left subtree.
    p = p.left
    while p.right:
        p = p.right
    return p

def make_bst(a):
    assert len(a)
    root = node(a[0])
    for e in a[1:]:
        p = root
        while True:
            if e > p.value:
                if p.right:
                    p = p.right
                else:
                    p.right = node(e)
                    break
            else:
                if p.left:
                    p = p.left
                else:
                    p.left = node(e)
                    break
    return root

def second_largest(a): return sorted(a)[-2]

print(second_largest_node(make_bst([30, 10, 31, 4, 17, 40, 3, 16, 22, 34, 47])).value)
print(second_largest_node(make_bst([30, 10, 31, 4, 17, 40, 3, 16, 22, 34])).value)
print(second_largest_node(make_bst([30, 10, 31, 4, 17, 3, 16, 22])).value)
print(second_largest_node(make_bst([30, 10, 4, 17, 3, 16, 22])).value)

import random
for i in range(1000):
    a = [random.randrange(-1000, 1000) for _ in
             range(random.randrange(2, 1000))]
    assert second_largest_node(make_bst(a)).value == second_largest(a)
