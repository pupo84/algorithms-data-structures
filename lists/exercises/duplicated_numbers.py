"""
Write a function to remove the duplicate numbers on given integer array/list
"""

from typing import List
from collections import Counter


def remove_duplicated(arr: List[int]) -> List[int]:
    return list(set(arr))


def remove_duplicated_with_counter(arr: List[int]) -> List[int]:
    return list(Counter(arr))


print(remove_duplicated([1, 2, 2, 3, 4, 5, 5, 6]))
print(remove_duplicated_with_counter([1, 2, 2, 3, 4, 5, 5, 6]))
