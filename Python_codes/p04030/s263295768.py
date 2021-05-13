# -*- coding: utf-8 -*-
# B - バイナリハックイージー

s = input()
listAns = []

set1 = ['0', '1']
set2 = ['B']

listS = list(s)

# print(listS)

for i in listS:
    if i in set1:
        listAns.append(i)

    elif i in set2:
        if len(listAns) != 0:
            listAns.pop()

ans = "".join(listAns)

print(ans)