#!/usr/bin/python3

# 2019-08-31
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as
# 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not
# allowed.

def is_valid(s):
    return int(s) <= 26

def encodings(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    if len(s) == 2:
        return [s[0] + '-' + s[1]] + ([s] if is_valid(s) else [])

    return [s[0:2] + '-' + r for r in encodings(s[2:]) if is_valid(s[0:2])] + \
           [s[0]   + '-' + r for r in encodings(s[1:])]

def count_encodings(s):
    if len(s) <= 1: return 1
    return count_encodings(s[1:]) + \
          (count_encodings(s[2:]) if is_valid(s[0:2]) else 0)

inputs = [
    '',
    '1',
    '7',
    '56',
    '567',
    '12',
    '11',
    '111',
    '1111',
    '1234567',
    '2626',
    '2327',
    ]

for input in inputs:
    print(input, encodings(input), count_encodings(input))
