#!/usr/bin/python3

def stack_sort(s):
    t = []
    while s:
        v = s.pop()
        while t and t[-1] < v: s.append(t.pop())
        t.append(v)
    while t: s.append(t.pop())

s = [i for i in range(100)]

import random
for i in range(1000):
    random.shuffle(s)
    stack_sort(s)
    assert s == sorted(s)
