import numpy as np
import numpy.typing as npt

arr1 = np.array([[1, 10, 11], [5, 4, 10], [24, 20, 37]])
print(arr1)


def access(arr: npt.NDArray[np.int64], row: int, column: int) -> int:
    print(row, len(arr), column, len(arr[0]))
    if row >= len(arr) or column >= len(arr[0]):
        raise Exception("Incorrect index or column")
    return int(arr[row][column])


n = access(arr1, 1, 20)
print(n)
