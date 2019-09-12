#!/usr/bin/python3

# 2019-09-11
#
# Given an array of integers and a number k, where 1 <= k <= length of the
# array, compute the maximum values of each subarray of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10,
# 7, 8, 8], since:
#
#    10 = max(10, 5, 2)
#    7 = max(5, 2, 7)
#    8 = max(2, 7, 8)
#    8 = max(7, 8, 7)

# Do this in O(n) time and O(k) space. You can modify the input array in-place
# and you do not need to store the results. You can simply print them out as
# you compute them.

import collections

def add_candidate(candidates, v):
    while candidates and candidates[-1] < v:
        candidates.pop()
    candidates.append(v)

def remove_candidate(candidates, v):
    if v == candidates[0]:
        candidates.popleft()

def subarray_maxes(a, k):
    output = []
    candidates = collections.deque()

    for end in range(k):
        add_candidate(candidates, a[end])
    output.append(candidates[0])

    begin = 0
    for end in range(k, len(a)):
        remove_candidate(candidates, a[begin])
        begin += 1

        add_candidate(candidates, a[end])
        output.append(candidates[0])

    return output

assert subarray_maxes([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
