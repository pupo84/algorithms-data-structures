import numpy as np

arr1 = np.array([[1, 10, 11], [5, 4, 10], [24, 20, 37]])
print(arr1)

arr2 = np.insert(arr1, 0, [1, 2, 3], axis=1)
print(arr2)

arr3 = np.append(arr2, [[4, 5, 6, 7]], axis=0)
print(arr3)
