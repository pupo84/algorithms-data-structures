my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[1:5])

my_list[0:2] = [11, 12]
print(my_list)

my_list.pop()
print(my_list)

del my_list[2]
print(my_list)

my_list.remove(9)
print(my_list)
