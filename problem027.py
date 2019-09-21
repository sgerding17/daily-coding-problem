#!/usr/bin/python3

# 2019-09-20
#
# Given a string of round, curly, and square open and closing brackets, return
# whether the brackets are balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false..

BRACKET_MAPPING = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
}
OPEN_SET = set(BRACKET_MAPPING.values())
CLOSE_SET = set(BRACKET_MAPPING.keys())

def counterpart(b):
    return BRACKET_MAPPING[b]

def is_balanced(string):
    stack = []
    for b in string:
        if b in OPEN_SET:
            stack.append(b)
        elif b in CLOSE_SET:
            if not stack or stack[-1] != counterpart(b):
                return False
            stack.pop()
        else:
            assert False
    return not stack

assert is_balanced('([])[]({})') == True
assert is_balanced('([)]') == False
assert is_balanced('((()') == False
