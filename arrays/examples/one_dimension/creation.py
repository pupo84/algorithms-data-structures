import array
import numpy as np

my_array = array.array("i")
print(my_array)

my_array_with_items = array.array("i", [1, 2, 3, 4, 5])
print(my_array_with_items)

np_array = np.array([], dtype=int)
print(np_array)

np_array_with_items = np.array([1, 2, 3, 4])
print(np_array_with_items)
