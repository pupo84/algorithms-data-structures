from typing import List
from array import array
from collections.abc import MutableSequence
import random

# 1. create an array and traverse
arr = array("i", [1, 2, 3, 4, 5])


def traverse(arr: MutableSequence[int]) -> None:
    [print(f"Array index {idx}") for idx in arr]


traverse(arr)


# 2. Access individual elements throught indexes
def get(arr: MutableSequence[int], index: int) -> int:
    return arr[index]


num: int = random.randrange(0, 5)
print(f"Array element number {num} is {get(arr, num)}")

# 3. Append any value to the array using append()
arr.append(num)
print(f"Appending {num} to the end of array {arr}")

# 4. Add any value to the array using insert()
val: int = random.randrange(0, 100)
arr.insert(num, val)
print(f"Inserting value {val} in position {num} to {arr}")

# 5. Extend array
new_items: List[int] = [-1, -2, -3]
arr.extend([-1, -2, -3])
print(f"Extended array {arr}")

# 6. Add items using fromList
arr.fromlist(new_items)
print(f"Added items using fromList {arr}")

# 7. Remove element using remove()
arr.remove(num)
print(f"Removed item {num} using remove {arr}")

# 8. Remove last element using pop()
element: int = arr.pop()
print(f"Removed item {element} using pop {arr}")

# 9. Fetch element using index()
idx: int = arr.index(-1)
print(f"Got number -1 in position {idx}")

# 10. Reverse array using reverse()
reversed_list: MutableSequence[int] = list(reversed(arr))
print(f"This is the reversed list {reversed_list}")

# 11. Get array buffer info using buffer_info()
address_memory, array_length = arr.buffer_info()
print(f"The address memory is {address_memory} with length {array_length}")

# 12. Check number of occurrences using count()
count: int = arr.count(-1)
print(f"The number of occurrences of -1 is {count}")

# 13. Convert array to list using tolist()
print(f"Array to list {arr.tolist()}")

# 14. Slice elements of array
print(f"Slicing arrau {arr[2:5]}")
