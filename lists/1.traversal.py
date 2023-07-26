from typing import List

shopping_list: List[str] = ["Milk", "Cheese", "Butter"]
print(shopping_list[0])
print("Milk" in shopping_list)
print(shopping_list[::-1])
[print(item) for item in shopping_list]
[print(key, item) for key, item in enumerate(shopping_list)]
