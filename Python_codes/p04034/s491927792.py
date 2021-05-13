n,m = map(int,input().split())
n += 1
p = [1]*n
r = [0]*n
r[1] = 1
for i in range(m):
    x,y = map(int,input().split())
    if r[x]:
        r[y] = 1
        if p[x] == 1:
            r[x] = 0
    p[x] -= 1
    p[y] += 1
    
print(sum(r))