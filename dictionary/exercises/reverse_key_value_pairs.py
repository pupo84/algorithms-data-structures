"""
Define a function which takes as a parameter dictionary and returns a 
dictionary in which everse the key-value pairs are reversed.

Example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)
Output:

{1: 'a', 2: 'b', 3: 'c'}
"""


def reverse_dict(dict1):
    return {v: k for k, v in dict1.items()}


print(reverse_dict({"a": 1, "b": 2, "c": 3}))
