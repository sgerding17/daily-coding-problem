#!/usr/bin/python3

# 2019-09-02
#
# Given a list of integers, write a function that returns the largest sum of
# non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?

test_cases = [
    ([2, 4, 6, 2, 5], 13),
    ([5, 1, 1, 5],    10)
]

def nonadj_sum(l):
    odd = 0
    even = 0
    parity = 1
    for n in l:
        if parity:
            odd = max(n + odd, even)
        else:
            even = max(n + even, odd)
        parity = 1 - parity
    return max(odd, even)

def nonadj_sum2(l):
    last_last = 0
    last = 0
    for n in l:
        cur = max(last, n + last_last)
        last_last = last
        last = cur
    return max(last, last_last)

algs = [nonadj_sum, nonadj_sum2]

for case in test_cases:
    for alg in algs:
        print(alg.__name__, case[0], case[1], alg(case[0]))
        assert alg(case[0]) == case[1]
