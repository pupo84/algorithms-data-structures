"""
Create a function that takes a tuple of tuples and returns a
tuple containing the diagonal elements of the input.

Example

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)
"""


def get_diagonal(input_tuple):
    rows = len(input_tuple)
    columns = len(input_tuple[0])

    if rows != columns:
        raise Exception("Can't calculate the diagonal of the specified tuple!")

    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))


input_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
output_tuple = get_diagonal(input_tuple)
print(output_tuple)
