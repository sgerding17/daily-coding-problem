#!/usr/bin/python3

# 2019-09-19
#
# Given a singly linked list and an integer k, remove the kth last element from
# the list. k is guaranteed to be smaller than the length of the list.
#
# The list is very long, so making more than one pass is prohibitively
# expensive.
#
# Do this in constant space and in one pass.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def build_list(string):
    root = Node(string[0])
    p = root
    for c in string[1:]:
        p.next = Node(c)
        p = p.next
    return root

def to_string(root):
    string = ''
    while root:
        string += root.value
        root = root.next
    return string

def remove_kth_last(root, k):
    p1 = root
    for i in range(k):
        p1 = p1.next

    p2 = root
    while p1.next:
        p1 = p1.next
        p2 = p2.next

    temp = p2.next
    p2.next = p2.next.next
    del temp

    return root

assert to_string(remove_kth_last(build_list('hello'), 4)) == 'hllo'
assert to_string(remove_kth_last(build_list('hello'), 3)) == 'helo'
assert to_string(remove_kth_last(build_list('hello'), 2)) == 'helo'
assert to_string(remove_kth_last(build_list('hello'), 1)) == 'hell'
