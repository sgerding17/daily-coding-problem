#!/usr/bin/python3

# 2019-09-16
#
# You are given an M by N matrix consisting of booleans that represents a
# board. Each True boolean represents a wall. Each False boolean represents a
# tile you can walk on.
#
# Given this matrix, a start coordinate, and an end coordinate, return the
# minimum number of steps required to reach the end coordinate from the start.
# If there is no possible path, then return null. You can move up, left, down,
# and right. You cannot move through walls. You cannot wrap around the edges of
# the board.
#
# For example, given the following board:
#
#    [[f, f, f, f],
#     [t, t, f, t],
#     [f, f, f, f],
#     [f, f, f, f]]
#
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
# number of steps required to reach the end is 7, since we would need to go
# through (1, 2) because there is a wall everywhere else on the second row.

from heapq import heappush, heappop

def min_steps(board, start, end):
    visited = {start : 0}
    queue = [(0, start)]

    while end not in visited and queue:
        (steps, current) = heappop(queue)
        for next in get_next(current, board, visited):
            visited[next] = steps + 1
            heappush(queue, (steps + 1, next))

    return visited[end] if end in visited else None

def get_next(current, board, visited):
    (cur_row, cur_col) = current
    for (next_row, next_col) in [(cur_row + 1, cur_col),
                                 (cur_row - 1, cur_col),
                                 (cur_row,     cur_col + 1),
                                 (cur_row,     cur_col - 1)]:
        if (next_row >= 0 and next_row < len(board) and
            next_col >= 0 and next_col < len(board[next_row]) and
            not board[next_row][next_col] and
            (next_row, next_col) not in visited):
            yield (next_row, next_col)

board = [[False, False, False, False],
         [True,  True,  False, True],
         [False, False, False, False],
         [False, False, False, False]]

print(min_steps(board, (3,0), (0,0)))
