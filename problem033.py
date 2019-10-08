#!/usr/bin/python3

# 2019-09-26
#
# Compute the running median of a sequence of numbers. That is, given a stream
# of numbers, print out the median of the list so far on each new element.
#
# Recall that the median of an even-numbered list is the average of the two
# middle numbers.
#
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should
# print out:
#
#    2
#    1.5
#    2
#    3.5
#    2
#    2
#    2

def running_median(iterator):
    history = []
    def insert_history(n):
        history.append(n)
        i = len(history) - 1
        while i > 0 and history[i] < history[i - 1]:
            (history[i], history[i - 1]) = (history[i - 1], history[i])
            i -= 1
    for n in iterator:
        insert_history(n)
        midpoint = int(len(history) / 2)
        if len(history) % 2 == 1:
            print(history[midpoint])
        else:
            print((history[midpoint] +
                   history[midpoint - 1]) / 2)

running_median(iter([2, 1, 5, 7, 2, 0, 5]))
