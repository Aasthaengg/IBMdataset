import numpy as np

N, M = map(int,input().split())

box = np.array([1]*N)#個数
pos = np.array([0]*N)#ありえるか
pos[0] = 1

for i in range(M):
    x, y = map(lambda x:int(x)-1,input().split())
    box[x] -= 1
    box[y] += 1
    if pos[x]:
        pos[y] = 1
        if box[x] == 0:
            pos[x] = 0

#print(box)
#print(pos)

box = np.where(box > 0, 1, 0)
print(sum(pos*box))