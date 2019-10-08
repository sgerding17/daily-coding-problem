#!/usr/bin/python3

# 2019-09-25
#
# Suppose you are given a table of currency exchange rates, represented as a 2D
# array. Determine whether there is a possible arbitrage: that is, whether
# there is some sequence of trades you can make, starting with some amount A of
# any currency, so that you can end up with some amount greater than A of that
# currency.
#
# There are no transaction costs and you can trade fractional quantities.

rates = [
    [ 1.0, 0.4, 0.5, 0.9],
    [ 0.4, 1.0, 0.3, 0.8],
    [ 0.2, 2.0, 1.0, 0.7],
    [ 1.1, 1.2, 1.1, 1.0],
]

import collections

def arbitrage(rate):
    for start in range(len(rate)):
        quantity = {start : 1.0}
        path = {start: []}
        candidates = collections.deque()
        candidates.append(start)
        while candidates:
            candidate = candidates.popleft()
            for next in range(len(rate)):
                next_quant = quantity[candidate] * rate[candidate][next]
                if next not in quantity or quantity[next] < next_quant:
                    quantity[next] = next_quant
                    path[next] = path[candidate] + [candidate]
                    if next == start: return (path[next], quantity[next])
                    candidates.append(next)
        return []

print(arbitrage(rates))
