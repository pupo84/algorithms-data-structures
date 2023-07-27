# Find all pairs of integers whose sum is equal to a given number
from typing import List, Tuple, Set


def two_sum(numbers: List[int], target: int) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = list()
    seen: Set[int] = set()

    for value in numbers:
        complement = target - value

        if complement in seen:
            result.append((value, complement))

        seen.add(value)

    return result


print(two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
