s = input()

t = []
for c in s:
    if c == "B":
        if len(t) != 0:
            t.pop()
    else:
        t.append(c)
print("".join(t))

