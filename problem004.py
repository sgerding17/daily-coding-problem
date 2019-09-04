#!/usr/bin/python3

# 2019-08-28
#
# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer
# that does not exist in the array. The array can contain duplicates and
# negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
# should give 3.
#
# You can modify the input array in-place.

tests = [
    ([3, 4, -1, 1], 2),
    ([1, 2, 0],     3),
]

def find_missing(a):
    for n in range(1, max(a)):
        if n not in a: return n
    return max(1, max(a) + 1)

def find_missing_nlogn(a):
    a.sort()
    expected = 1
    for n in a:
        if n < 1: continue
        if n > expected: return expected
        expected = n + 1
    return expected

def find_missing_linear(a):
    found = [False for _ in range(max(a))]
    for n in a:
        if n >= 1: found[n - 1] = True
    for i in range(max(a)):
        if not found[i]: return i + 1
    return max(1, max(a) + 1)

def emplace(a, n):
    if n <= 0 or n >= len(a): return
    if a[n-1] == n: return

    next_n = a[n-1]
    a[n-1] = n
    emplace(a, next_n)

def find_missing_const_space(a):
    for i in range(len(a)):
        emplace(a, a[i])
    for i in range(len(a)):
        if a[i] != i+1: return i+1
    return max(a)+1

algs = [find_missing,
        find_missing_nlogn,
        find_missing_linear,
        find_missing_const_space]

for alg in algs:
    for test in tests:
        assert alg(test[0]) == test[1]

import random
min_val = -10
max_val = 10
max_size = 50
for i in range(1000):
    a = [random.randrange(min_val, max_val) for _ in
            range(random.randrange(1, max_size))]
    expected = find_missing(a)
    for alg in algs[1:]:
        if alg(a) != expected:
            print(alg.__name__, a, alg(a), expected)
