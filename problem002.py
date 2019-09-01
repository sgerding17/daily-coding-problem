#!/usr/bin/python

# 2019-08-26
#
# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original
# array except the one at i.
# 
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
# be [2, 3, 6].
# 
# Follow-up: what if you can't use division?

inputs = [[1, 2, 3, 4, 5],
          [3, 2, 1]]

# First cut
for input in inputs:
    product = 1
    for element in input:
        product *= element
    output = []
    for element in input:
        output.append(product / element)
    print input, output

# Simplified
for input in inputs:
    product = reduce((lambda x,y:x*y), input)
    print input, [product / element for element in input]

# Np division
for input in inputs:
    output = []
    for i in range(len(input)):
        product = 1
        for j in range(len(input)):
            if j != i: product *= input[j]
        output.append(product)
    print input, output
