import numpy as np
import numpy.typing as npt

arr1 = np.array([[1, 10, 11], [5, 4, 10], [24, 20, 37]])


def linear_search(arr: npt.NDArray[np.int64], value: int) -> bool:
    for d1 in arr1:
        for d2 in d1:
            if d2 == value:
                return True
    return False


print(linear_search(arr1, 20))
