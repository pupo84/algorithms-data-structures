# Given 2D list calculate the sum of diagonal elements.


def diagonal_sum(arr):
    lines = len(arr)
    columns = len(arr[0])

    if lines != columns:
        raise Exception("Cannot calculate the matrix diagonal sum!")

    total = 0

    for i in range(lines):
        total += arr[i][i]

    return total


print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(diagonal_sum([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
