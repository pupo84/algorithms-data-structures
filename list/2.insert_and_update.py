from typing import List

my_list: List[int] = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
my_list[2] = 33
print(my_list)
my_list.insert(2, 22)
print(my_list)
my_list.append(8)
print(my_list)
my_list.extend([9, 10, 11])
print(my_list)
