# Find the maximum product of two integers in an array where all elements are positive.
from typing import List


def max_product(arr: List[int]) -> int:
    arr.sort(reverse=True)
    return arr[0] * arr[1]


print(max_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
