n,m = map(int,input().split())
x = [0 for _ in range(m)]
y = [0 for _ in range(m)]
for i in range(m):
    x[i],y[i] = map(int,input().split())
    x[i] -= 1
    y[i] -= 1

box = [1 for _ in range(n)]
red = [0 for _ in range(n)]
red[0] = 1
for i in range(m):
    red[y[i]] = 1 if red[x[i]] else red[y[i]]
    red[x[i]] = red[x[i]] if box[x[i]]-1 else 0
    box[x[i]] -= 1
    box[y[i]] += 1
print(sum(red))