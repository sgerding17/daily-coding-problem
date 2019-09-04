#!/usr/bin/python3

# 2019-08-29
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first
# and last element of that pair. For example, car(cons(3, 4)) returns 3, and
# cdr(cons(3, 4)) returns 4.
# 
# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

# def first(a, b): return a
# def last(a, b): return b
# def car(pair): return pair(first)
# def cdr(pair): return pair(last)

car = lambda p:p(lambda a,b:a)
cdr = lambda p:p(lambda a,b:b)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))

print(car(cons(3, cons(4, 5))))
print(car(cdr(cons(3, cons(4, 5)))))
print(cdr(cdr(cons(3, cons(4, 5)))))
