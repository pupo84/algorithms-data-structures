from array import array
from collections.abc import MutableSequence


def traverse(array: MutableSequence[int]) -> None:
    for arr in array:
        print(arr)


my_array = array("i", [1, 2, 3, 4])
traverse(my_array)
