s = input()
a = []
for i in s:
    if i != "B":
        a.append(i)
    else:
        if a:
            a.pop()
print(*a, sep = "")