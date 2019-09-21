#!/usr/bin/python3

# 2019-09-18
#
# Implement regular expression matching with the following special characters:
#
#  . (period) which matches any single character
#  * (asterisk) which matches zero or more of the preceding element
#
# That is, implement a function that takes in a string and a valid regular
# expression and returns whether or not the string matches the regular
# expression.
# 
# For example, given the regular expression "ra." and the string "ray", your
# function should return true. The same regular expression on the string
# "raymond" should return false.
# 
# Given the regular expression ".*at" and the string "chat", your function
# should return true. The same regular expression on the string "chats" should
# return false.

from enum import Enum

class Node(object):
    class Type(Enum):
        ROOT = 0
        LETTER = 1
        DOT = 2
        TERMINATOR = 3
    def __init__(self):
        self.type = Node.Type.ROOT
        self.letter = ''
        self.next = []

def build_tree(re):
    node = root = Node()
    for c in re:
        if c != '*':
            new_node = Node()
            if c == '.':
                new_node.type = Node.Type.DOT
            else:
                new_node.type = Node.Type.LETTER
                new_node.letter = c
            node.next.append(new_node)
            node = new_node
        else:
            node.next.append(node)
    new_node = Node()
    new_node.type = Node.Type.TERMINATOR
    node.next.append(new_node)
    return root.next[0]

def to_string(node):
    out = '<' + str(node.type) + '(' + node.letter + ')' + '[';
    for next in node.next:
        if next == node:
            out += '*,'
        else:
            out += to_string(next) + ','
    if out[-1] == ',': out = out[:-1]
    out += ']>'
    return out

def match(string, node):
    print('match("%s", %s)' % (string, to_string(node)))
    if string == '': return node.type == Node.Type.TERMINATOR
    if (node.type == Node.Type.LETTER and node.letter == string[0] or
        node.type == Node.Type.DOT):
        for next in node.next:
            if match(string[1:], next): return True
    return False

re1 = build_tree('ra.')
re2 = build_tree('.*at')

print(to_string(re1))
print(to_string(re2))

assert match('ray', re1) == True
assert match('raymond', re1) == False

assert match('chat', re2) == True
assert match('chats', re2) == False

re3 = build_tree('st.*en.*ing')

print(to_string(re3))

assert match('steven gerding', re3) == True
assert match('steve gerding', re3) == False
