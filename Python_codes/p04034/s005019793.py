n,m = map(int,input().split())
l = [1] * n
d = set()
d.add(1)

for i in range(m):
    x,y = map(int,input().split())
    l[x-1] -= 1
    l[y-1] += 1
    if(x in d):
        d.add(y)
        if(l[x-1] == 0):
            d.remove(x)

s = 0
for i in d:
    if(l[i-1] != 0):s += 1
print(s)
