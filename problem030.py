#!/usr/bin/python3

# 2019-09-23
#
# You are given an array of non-negative integers that represents a
# two-dimensional elevation map where each element is unit-width wall and the
# integer is the height. Suppose it will rain and all spots between two walls
# get filled up.
# 
# Compute how many units of water remain trapped on the map in O(N) time and
# O(1) space.
# 
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the
# middle.
# 
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2
# in the second, and 3 in the fourth index (we cannot hold 5 since it would run
# off to the left), so we can trap 8 units of water.

def compute_water_lin_space(elevation):
    max_left = [0] * len(elevation)
    max_right = [0] * len(elevation)
    for i in range(1, len(elevation)):
        max_left[i] = max(max_left[i-1], elevation[i-1])
    for i in range(len(elevation) - 2, -1, -1):
        max_right[i] = max(max_right[i+1], elevation[i+1])
    water = 0
    for (el, ml, mr) in zip(elevation, max_left, max_right):
        water += max(min(ml, mr) - el, 0)
    return water

def compute_water_on_side(elevation, start, end, direction):
    water = 0

    i1 = i2 = start
    ullage = 0
    while i1 != end:
        i2 += direction
        if elevation[i2] >= elevation[i1]:
            water += max((abs(i2 - i1) - 1) * elevation[i1] - ullage, 0)
            i1 = i2
            ullage = 0
        else:
            ullage += elevation[i2]
    assert i1 == i2 == end
    
    return water

def compute_water_const_space(elevation):
    top_index = elevation.index(max(elevation))
    return (compute_water_on_side(elevation, 0, top_index, +1) +
            compute_water_on_side(elevation, len(elevation) - 1, top_index, -1))

assert compute_water_lin_space([1, 3, 2, 5, 1]) == 1
assert compute_water_lin_space([3, 0, 1, 3, 0, 5]) == 8
assert compute_water_lin_space([3, 0, 1, 3, 0, 5, 2, 3, 2]) == 9

assert compute_water_const_space([1, 3, 2, 5, 1]) == 1
assert compute_water_const_space([3, 0, 1, 3, 0, 5]) == 8
assert compute_water_const_space([3, 0, 1, 3, 0, 5, 2, 3, 2]) == 9

import random
max_val = 100
max_size = 100
for i in range(1000):
    a = [random.randrange(0, max_val) for _ in
             range(random.randrange(1, max_size))]
    if compute_water_const_space(a) != compute_water_lin_space(a):
        print(a, compute_water_const_space(a), compute_water_lin_space(a))
        assert False
