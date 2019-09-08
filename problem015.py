#!/usr/bin/python3

# 2019-09-08
#
# Given a stream of elements too large to store in memory, pick a random
# element from the stream with uniform probability.

import collections
import random

def sequence(num_values):
    for i in range(num_values):
        yield i * 100

def stream_sample(gen):
    candidate = 0
    count = 0
    for value in gen:
        count += 1
        retain_prob = 1. / count
        if random.uniform(0, 1) < retain_prob:
            candidate = value
    return candidate

samples = collections.defaultdict(int)
for i in range(100000):
    samples[stream_sample(sequence(10))] += 1

for value in sorted(samples):
    print(value, samples[value])
