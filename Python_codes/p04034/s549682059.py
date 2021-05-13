N,M = list(map(int,input().split()))
XY = [list(map(int,input().split())) for _ in range(M)]
L1 = [1]*N
L2 = [0]*N
L2[0] = 1
for xy in XY:
    if L2[xy[0]-1] == 1:
        L2[xy[1]-1] = 1
    L1[xy[0]-1] -= 1
    L1[xy[1]-1] += 1
    if L1[xy[0]-1] == 0:
        L2[xy[0]-1] = 0
print(sum(L2))