#!/usr/bin/python3

# 2019-09-22
#
# Run-length encoding is a fast and simple method of encoding strings. The
# basic idea is to represent repeated successive characters as a single count
# and character. For example, the string "AAAABBBCCDAA" would be encoded as
# "4A3B2C1D2A".
#
# Implement run-length encoding and decoding. You can assume the string to be
# encoded have no digits and consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.

def encode(string):
    output = ''
    i = 0
    while i < len(string):
        c = string[i]
        count = 1
        while i < len(string) - 1 and string[i + 1] == c:
            count += 1
            i += 1
        output += str(count) + c
        i += 1
    return output

def decode(string):
    output = ''
    i = 0
    while i < len(string):
        count_str = ''
        while i < len(string) and string[i].isdigit():
            count_str += string[i]
            i += 1
        output += string[i] * int(count_str)
        i += 1
    return output

print(encode('AAAABBBCCDAA'))
print(decode(encode('AAAABBBCCDAA')))
