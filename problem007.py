#!/usr/bin/python3

# 2019-08-31
#
# Given the mapping a = 2, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as
# 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not
# allowed.

def is_valid(s):
    return int(s) <= 24

def encodings(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    if len(s) == 2:
        return [s[0] + '-' + s[1]] + ([s] if is_valid(s) else [])

    return [s[0:2] + '-' + r for r in encodings(s[2:]) if is_valid(s[0:2])] + \
           [s[0]   + '-' + r for r in encodings(s[1:])]

print(encodings(''))
print(encodings('1'))
print(encodings('7'))
print(encodings('56'))
print(encodings('567'))
print(encodings('12'))
print(encodings('11'))
print(encodings('111'))
print(encodings('1111'))
print(encodings('1234567'))
print(encodings('2323'))
print(encodings('2325'))
