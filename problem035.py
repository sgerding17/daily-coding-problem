#!/usr/bin/python3

# 2019-09-28
#
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the
# values of the array so that all the Rs come first, the Gs come second, and
# the Bs come last. You can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
# become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def binary_segregate(a, left_set, right_set):
    l = 0
    r = len(a) - 1
    while True:
        while a[l] in left_set: l += 1
        while a[r] in right_set: r -= 1
        if l >= r: break
        (a[l], a[r]) = (a[r], a[l])

def segregate(a):
    binary_segregate(a, ['R'], ['G', 'B'])
    binary_segregate(a, ['R', 'G'], ['B'])

a = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(a)
segregate(a)
print(a)

import random
import copy
for _ in range(1000):
    a = (['R'] * random.randrange(1, 100) +
         ['G'] * random.randrange(1, 100) +
         ['B'] * random.randrange(1, 100))
    orig_a = copy.deepcopy(a)
    random.shuffle(a)
    segregate(a)
    assert a == orig_a
