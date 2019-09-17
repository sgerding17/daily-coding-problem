#!/usr/bin/python3

# 2019-09-12
#
# A builder is looking to build a row of N houses that can be of K different
# colors. He has a goal of minimizing cost while ensuring that no two
# neighboring houses are of the same color.
#
# Given an N by K matrix where the nth row and kth column represents the cost
# to build the nth house with kth color, return the minimum cost which achieves
# this goal.

import sys

def min_total_cost(cost):
    total_cost = [[sys.maxsize for _ in col] for col in cost]
    total_cost[0] = cost[0]

    for house in range(1, len(cost)):
        for color1 in range(0, len(cost[house])):
            for color2 in range(0, len(cost[house])):
                if color2 == color1: continue
                total_cost[house][color2] = min(total_cost[house][color2],
                                                total_cost[house - 1][color1] + cost[house][color2])

    return min(total_cost[-1])

cost = [
    [1, 2, 3, 4],
    [4, 2, 1, 5],
    [5, 4, 1, 2],
    [5, 4, 1, 2],
]

print(min_total_cost(cost))
