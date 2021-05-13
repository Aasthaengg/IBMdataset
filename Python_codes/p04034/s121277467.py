N,M = map(int,input().split())
rboxes = [False]*N
rboxes[0] = True
ballC = [1]*N
for i in range(M):
    x, y = map(int, input().split())
    if rboxes[x-1]:
        rboxes[y-1] = True
    ballC[x-1] -= 1
    ballC[y-1] += 1
    if ballC[x-1] == 0:
        rboxes[x-1] = False
c = 0
for i in range(N):
    if rboxes[i]:
        c+=1
print(c)


