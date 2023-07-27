my_dict = {"name": "Edy", "age": 26}
my_dict["address"] = "London"
print(my_dict)


def traverse(dict):
    for key in dict:
        print(key, dict[key])


traverse(my_dict)


def search(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "The value does not exist"


print(search(my_dict, 27))

my_dict.pop("name")


my_dict = {"eooooa": 1, "aas": 2, "udd": 3, "sseo": 4, "werwi": 5}

print(sorted(my_dict, key=len))
