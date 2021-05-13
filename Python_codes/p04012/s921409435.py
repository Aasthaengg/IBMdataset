s = input()
d = {}
flag = 1
for i in s:
    if i in d:
        d[i] += 1
    else:
        d.setdefault(i, 1)
    
for j in d.values():
    if j % 2 != 0:
        flag = 0
if flag == 0:
    print("No")
else:
    print("Yes")