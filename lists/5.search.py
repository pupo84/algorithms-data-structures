my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def search(element: int) -> bool:
    return element in my_list


def linear_search(element: int) -> bool:
    for item in my_list:
        if item == element:
            return True
    return False


print(linear_search(50))
print(linear_search(5))
