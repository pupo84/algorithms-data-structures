import numpy as np

arr1 = np.array([[1, 10, 11], [5, 4, 10], [24, 20, 37]])
print(arr1)

arr2 = np.delete(arr1, 0, axis=0)
print(arr2)
