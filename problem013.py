#!/usr/bin/python3

# 2019-09-06
#
# Given an integer k and a string s, find the length of the longest substring
# that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k
# distinct characters is "bcb".

import collections

def ldss_quadratic(s, k):
    max_len = 0
    for end in range(len(s)):
        begin = end
        unique = {s[begin]: True}
        while len(unique) <= k and begin >= 0:
            begin -= 1
            unique[s[begin]] = True
        begin += 1
        max_len = max(max_len, end - begin + 1)
    return max_len

def ldss_quadratic2(s, k):
    max_len = 0
    for begin in range(len(s)):
        end = begin
        unique = {s[end]: True}
        while len(unique) <= k and end < len(s) - 1:
            end += 1
            unique[s[end]] = True
        # 'end' points to one beyond the last character in the substring.
        max_len = max(max_len, end - begin)
    return max_len

def ldss_linear(s, k):
    max_len = 0
    letters = collections.defaultdict(int)
    unique_count = 0
    begin = 0
    for end in range(len(s)):
        letters[s[end]] += 1
        if letters[s[end]] == 1: unique_count += 1
        while unique_count > k:
            letters[s[begin]] -= 1
            if letters[s[begin]] == 0: unique_count -= 1
            begin += 1
        max_len = max(max_len, end - begin + 1)
    return max_len
    
tests = [
    ('abcba',       2, 3),
    ('abcccdccabc', 2, 6)
]

algs = (ldss_quadratic, ldss_quadratic2, ldss_linear)
for test in tests:
    for alg in algs:
        assert alg(test[0], test[1]) == test[2]
