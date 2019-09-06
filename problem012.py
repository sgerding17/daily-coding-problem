#!/usr/bin/python3

# 2019-09-05
#
# There exists a staircase with N steps, and you can climb up either 1 or 2
# steps at a time. Given N, write a function that returns the number of unique
# ways you can climb the staircase. The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
#    1, 1, 1, 1
#    2, 1, 1
#    1, 2, 1
#    1, 1, 2
#    2, 2
#
# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example, if X = {1,
# 3, 5}, you could climb 1, 3, or 5 steps at a time.

def unique_climbs(N, X):
    history = [0] * max(X)
    for i in range(N + 1):
        current = 0
        if i in [0, 1]:
            current = 1
        else:
            for step in X:
                current += history[step - 1]
        history = [current] + history[:-1]
    return history[0]

tests = [
    (10, [1]),
    (1,  [1, 2]),
    (2,  [1, 2]),
    (3,  [1, 2]),
    (4,  [1, 2]),
    (5,  [1, 2]),
    (6,  [1, 2]),
    (7,  [1, 2]),
    (8,  [1, 2]),
    (9,  [1, 2]),
    (10, [1, 2]),
    (1,  [1, 3, 5]),
    (2,  [1, 3, 5]),
    (3,  [1, 3, 5]),
    (4,  [1, 3, 5]),
    (5,  [1, 3, 5]),
    (6,  [1, 3, 5]),
    (7,  [1, 3, 5]),
    (8,  [1, 3, 5]),
    (9,  [1, 3, 5]),
    (10, [1, 3, 5]),
]

for test in tests:
    print(test[0], test[1], unique_climbs(test[0], test[1]))

