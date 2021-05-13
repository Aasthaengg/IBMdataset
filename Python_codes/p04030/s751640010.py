s = input()
temp = []
for c in s:
    if c == "B":
        if temp:
            temp.pop()
    else:
        temp.append(c)
print("".join(temp))