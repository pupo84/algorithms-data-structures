"""
Write a function that calculates the sum and 
product of all elements in a tuple of numbers.

Example

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24
"""
from functools import reduce


def sum_product(input_tuple):
    return (sum(input_tuple), reduce(lambda x, y: x * y, input_tuple))


input_tuple = (1, 2, 3, 4)
print(sum_product(input_tuple))
