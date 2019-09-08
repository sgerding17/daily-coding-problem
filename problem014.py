#!/usr/bin/python3

# 2019-09-07
#
# The area of a circle is defined as pi*r^2. Estimate pito 3 decimal places
# using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x2 + y2 = r2.

import random

def estimate_pi(num_steps):
    count = 0
    for i in range(num_steps):
        x = random.uniform(-1., 1.)
        y = random.uniform(-1., 1.)
        if x**2 + y**2 < 1.: count += 1
    return 4. * count / num_steps

stable_value = 0
stable_count = 0
num_steps = 1
while stable_count < 5:
    estimate = round(100 * estimate_pi(num_steps))
    if stable_value == round(100 * estimate):
        stable_count += 1
    else:
        stable_value = round(100 * estimate)
        stable_count = 0
    num_steps *= 2
    print(num_steps, stable_value, stable_count)
print('pi = ', stable_value / 100)
