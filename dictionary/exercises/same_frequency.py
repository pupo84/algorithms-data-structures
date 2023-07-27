"""
Define a function which takes two lists as parameters and check 
if two given lists have the same frequency of elements.

Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
Output:

False
"""
from collections import Counter


def check_same_frequency(list1, list2):
    return Counter(list1) == Counter(list2)


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 2]

print(check_same_frequency(list1, list2))
