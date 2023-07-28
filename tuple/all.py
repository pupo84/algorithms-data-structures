new_tuple = ("a", "b", "c", "d", "e")
new_tuple1 = tuple("abcde")

print(new_tuple1)

# Access Tuple elements

print(new_tuple[0])


#  Traverse through tuple

for i in new_tuple:
    print(i)


for index in range(len(new_tuple)):
    print(new_tuple[index])


#  How to search for an element in Tuple?

print("a" in new_tuple)


def search(p_tuple, element):
    for i in p_tuple:
        if i == element:
            return p_tuple.index(i)
    return "The element does not exist"


print(search(new_tuple, "a"))

# Tuple Operations / Functions
my_tuple = (1, 4, 3, 2, 5)
my_tuple1 = (1, 2, 6, 9, 8, 7)

print(my_tuple + my_tuple1)
print(my_tuple * 4)
print(2 in my_tuple1)

my_tuple1.count(2)
my_tuple1.index(2)
