a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(c)

d = a * 2
print(d)

print(len(a))
print(max(a))
print(min(a))
print(sum(a))

n = []
while True:
    inp: str = input("Enter a number: ")
    if inp == "done":
        break
    n.append(int(inp))

print(sum(n) / len(n))
