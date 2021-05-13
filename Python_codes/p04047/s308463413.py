import numpy as np
n = int(input())
L = [int(s) for s in input().split()]
# print(n)
# print(L)
npL = np.array(L)
# print(npL)
npL = np.sort(npL)
npLd = np.reshape(npL, (-1, 2))
# print(npLd)
cnt = 0
for i in npLd:
    cnt += i[0]
print(cnt)