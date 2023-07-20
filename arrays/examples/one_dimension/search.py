from array import array
from collections.abc import MutableSequence


def linear_search(array: MutableSequence[int], target: int) -> int:
    for idx, element in enumerate(array):
        if element == target:
            return idx
    return -1


my_array = array("i", [1, 2, 3, 4])
print(linear_search(my_array, 2))
