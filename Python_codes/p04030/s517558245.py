s = input()
t = []

for x in s:
    if x == "0":
        t.append("0")
    elif x == "1":
        t.append("1")
    else:
        if len(t) > 0:
            t.pop()
print(*t,sep='')