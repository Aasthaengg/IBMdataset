n,m = map(int,input().split())
ans = [False]*n
cnt = [1]*n
ans[0] = True
for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    cnt[y] += 1
    if ans[x]:
        ans[y] = True
    cnt[x] -= 1
    if cnt[x]==0:
        ans[x] = False
c = 0
for i in ans:
    if i:
        c += 1

print(c)
        
