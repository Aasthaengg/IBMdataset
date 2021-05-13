n,m = map(int,input().split(" "))
ar = [[0,1] for i in range(n)]
ar[0] = [1,1]
r = 0
for i in range(m):
    a,b = map(int,input().split(" "))
    a -= 1
    b -= 1
    if ar[a][0] == 1 and ar[a][1] >= 1:
        ar[b][0] = 1
    ar[b][1] += 1
    ar[a][1] -= 1
    if ar[a][1] == 0:
        ar[a][0] = 0
count = 0
for r in ar:
    if r[0] == 1:
        count += 1
print(count)