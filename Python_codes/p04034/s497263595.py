n,m = map(int,input().split())
ball = [1]*n
ans = [0]*n
ans[0] = 1

for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    ball[x] -= 1
    ball[y] += 1
    if ans[x] == 1:
        ans[y] = 1
    if ball[x] == 0:
        ans[x] = 0

a = 0
for an in ans:
    if an == 1:
        a += 1

print(a)