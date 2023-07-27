from typing import List


def find_linear(arr: List[int], target: int) -> bool:
    return target in arr


def find_recursive(arr: List[int], target: int) -> bool:
    if len(arr) <= 2:
        if target in arr:
            return True
        return False

    arr1: List[int] = arr[: len(arr) // 2]
    arr2: List[int] = arr[len(arr) // 2 :]

    if arr1[len(arr1) - 1] >= target:
        arr = arr1
    elif arr2[0] <= target:
        arr = arr2
    else:
        return False

    return find_recursive(arr, target)


print(find_linear([i for i in range(100)], 20))
print(find_linear([i for i in range(100)], 201))
print(find_recursive([i for i in range(100)], 20))
print(find_recursive([1, 2, 3, 4, 5, 6, 7, 8, 10], 9))
