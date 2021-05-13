n,m = map(int,input().split())
flag = [False]*n
balls = [1]*n
flag[0]= True
for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    balls[x] -=1
    balls[y] += 1
    if flag[x] == True:
        flag[y] =True
    if flag[x] == True and balls[x] == 0:
        flag[x] = False

cnt = 0
for i in range(n):
    if flag[i] == True and balls[i]>=1:
        cnt += 1
print(cnt)