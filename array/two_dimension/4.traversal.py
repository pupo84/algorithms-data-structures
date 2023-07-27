import numpy as np
import numpy.typing as npt

arr1 = np.array([[1, 10, 11], [5, 4, 10], [24, 20, 37]])
print(arr1)


def traverse(arr: npt.NDArray[np.int64]) -> None:
    for d1 in arr1:
        for d2 in d1:
            print(d2)


traverse(arr1)
