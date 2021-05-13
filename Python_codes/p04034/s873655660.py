import copy
N,M = [int(hoge) for hoge in input().split()]
Ball = [False]*N
BallNum = [1] * N
Ball[0] = True
for i in range(M):
    x,y = [int(hoge) - 1  for hoge in input().split()]
    BallNum[x] -= 1
    BallNum[y] += 1
    if Ball[x]:
        Ball[y] = True 
    if BallNum[x] == 0:
        Ball[x] = False
print(sum(Ball))