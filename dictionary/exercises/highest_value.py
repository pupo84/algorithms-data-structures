"""
Define a function which takes a dictionary as a parameter and 
returns the key with the highest value in a dictionary.

Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output:

b
"""


def max_value_key_a(dict1):
    return list({k: v for k, v in sorted(dict1.items(), key=lambda i: i[1])}.keys())[-1]


def max_value_key_b(dict1):
    return max(dict1, key=dict1.get)


print(max_value_key_a({"a": 5, "b": 9, "c": 2}))
print(max_value_key_b({"a": 5, "b": 9, "c": 2}))
