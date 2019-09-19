#!/usr/bin/python3

# 2019-09-14
#
# Given an array of time intervals (start, end) for classroom lectures
# (possibly overlapping), find the minimum number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

from heapq import heappush, heappop

def min_rooms(lectures):
    lectures.sort(key=lambda l: l[0])
    rooms = []
    max_rooms = 0
    for (start, end) in lectures:
        if rooms and rooms[0] <= start:
            heappop(rooms)
        heappush(rooms, end)
        max_rooms = max(max_rooms, len(rooms))
    return max_rooms

def min_rooms2(lectures):
    starts = sorted([l[0] for l in lectures])
    ends = sorted([l[1] for l in lectures])
    max_rooms = 0
    num_rooms = 0
    si = 0
    ei = 0
    while si < len(starts) and ei < len(ends):
        if starts[si] < ends[ei]:
            si += 1
            num_rooms += 1
        else:
            ei += 1
            num_rooms -= 1
        max_rooms = max(max_rooms, num_rooms)
    return max_rooms

def min_rooms3(lectures):
    starts = [l[0] for l in lectures]
    ends = [l[1] for l in lectures]
    last_time = max(ends)

    schedule = [0] * (last_time + 1)
    for start in starts: schedule[start] += 1
    for end in ends:     schedule[end] -= 1

    max_rooms = 0
    num_rooms = 0
    for time in schedule:
        num_rooms += time
        max_rooms = max(max_rooms, num_rooms)
    return max_rooms


print(min_rooms([(30, 75), (0, 50), (60, 150)]))
print(min_rooms([(30, 75), (0, 50), (1, 31), (60, 150)]))

print(min_rooms2([(30, 75), (0, 50), (60, 150)]))
print(min_rooms2([(30, 75), (0, 50), (1, 31), (60, 150)]))

print(min_rooms3([(30, 75), (0, 50), (60, 150)]))
print(min_rooms3([(30, 75), (0, 50), (1, 31), (60, 150)]))
