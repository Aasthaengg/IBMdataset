import numpy as np

n, l = map(int, input().split())
knot = list(map(int, input().split()))

flg = 0
li = []
for i in range(0, int(n) - 1):
    if(knot[i] + knot[i + 1] >= l):
        flg = 1
        print("Possible")
        li.append(i + 1)

        for j in range(i + 2, n):
            li.append(j)
        for j in reversed(range(1, i + 1)):
            li.append(j)
        break

if flg == 0:
    print("Impossible")

for i in reversed(li):
    print(i)
