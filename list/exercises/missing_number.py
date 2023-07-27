# Write a function to find the missing number in a given integer array of 1 to 100.

from typing import List


def missing_number(arr: List[int], n: int) -> int:
    total: int = n * (n + 1) // 2
    sum_arr: int = sum(arr)
    missing: int = total - sum_arr
    return missing


print(missing_number([1, 2, 3, 4], 5))
