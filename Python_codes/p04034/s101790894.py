N, M = map(int, input().split())
s = [0]*N
t = [1]*N
s[0] = 1
res = 1
for _ in range(M):
    x, y = map(int, input().split())
    x-=1
    y-=1
    t[x] -= 1
    t[y] += 1
    if s[x] == 1:
        if t[x]==0:
            s[x] = 0
            if s[y]==1:
                res -= 1
        else:
            if s[y]!=1:
                res += 1
        s[y] = 1
print(res)