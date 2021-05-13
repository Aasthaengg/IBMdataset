n,m = map(int, input().split())
r = [0]*(n+1)
r[1] = 1
b0 = [1]*(n+1)
for i in range(m):
    x,y = map(int, input().split())
    b0[x] -= 1
    b0[y] += 1
    if r[x]:
        r[y] = 1
    if b0[x]==0:
        r[x]=0
ans = 0
for j in range(n+1):
    if r[j]:
        ans += 1
print(ans)
