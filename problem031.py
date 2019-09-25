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

def masks(partial, count, length):
    if len(partial) == count: return [partial]
    last = partial[-1] if partial else -1
    outputs = []
    for i in range(last + 1, length):
        outputs += masks(partial + [i], count, length)
    return outputs

def dist(short, long, mask):
    assert len(long) == len(short) + len(mask)
    diffs = 0
    for i in range(len(long)):
        if mask and i == mask[0]:
            mask = mask[1:]
            continue
        if short[0] != long[i]: diffs += 1
        short = short[1:]
    return diffs

def edit_distance(short, long):
    (short, long) = (short, long) if len(short) <= len(long) else (long, short)
    min_dist = len(long)
    for mask in masks([], len(long) - len(short), len(long)):
        min_dist = min(min_dist, dist(short, long, mask) + len(mask))
    return min_dist

print(edit_distance('kitten', 'sitting'))
print(edit_distance('sitting', 'kitten'))

print(edit_distance('kitten', 'kitten'))
print(edit_distance('kitten', 'xxxxkitten'))
print(edit_distance('kitten', 'kittenxxxx'))
print(edit_distance('kitten', 'xxkittenxx'))
print(edit_distance('kitten', 'kitxxxxten'))

print(edit_distance('mommy', 'daddy'))
print(edit_distance('log', 'dog'))

print(edit_distance('the quick brown fox', 'jumped over the lazy dogs'))
