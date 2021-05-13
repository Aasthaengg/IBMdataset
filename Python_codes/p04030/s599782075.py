# -*- coding: utf-8 -*-

s = list(str(input()))
c = []

for x in s:
    if x != 'B':
        c.append(x)
    elif x == 'B' and c != []:
        c.pop()
    else:
        continue


print(*c, sep='')