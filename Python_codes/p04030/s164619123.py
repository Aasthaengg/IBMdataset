x = input()
li = []
sz = 0
for i in x:
    if (i == '0') or (i == '1'):
        li.append(i)
        sz += 1
    else:
        if sz > 0:
            li.pop()
            sz -= 1

for i in li:
    print(i, end="")
