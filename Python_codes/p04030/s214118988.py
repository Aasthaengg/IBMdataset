S = input()
l = []
for i in S:
    if i == "0":
        l.append("0")
    if i == "1":
        l.append("1")
    if i == "B" and len(l) > 0:
        del l[len(l) - 1]

for i in l:
    print(f"{i}", end="")
print()
