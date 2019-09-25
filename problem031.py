#!/usr/bin/python3

# 2019-09-24
#
# The edit distance between two strings refers to the minimum number of
# character insertions, deletions, and substitutions required to change one
# string to the other. For example, the edit distance between "kitten" and
# "sitting" is three: substitute the "k" for "s", substitute the "e" for "i",
# and append a "g".
#
# Given two strings, compute the edit distance between them.

def masks(partial, positions, length):
    if len(partial) == positions: return [partial]
    last = partial[-1] if partial else -1
    outputs = []
    for i in range(last + 1, length):
        outputs += masks(partial + [i], positions, length)
    return outputs

def dist(short, long, mask):
    diffs = 0
    for i in range(len(long)):
        if i == mask:
            mask = mask[1:]
            continue
        if short[0] != long(i): diffs += 1
        short = short[1:]
    return diffs

def edit_distance(short, long):
    min_dist = len(long)
    for mask in masks([], len(long) - len(short), len(long)):
        min_dist = min(min_dist, dist(short, long, mask))
    return min_dist

for mask in masks([], 3, 8):
    print(mask)

print(edit_distance('mommy', 'daddy'))
