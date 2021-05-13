n,m = [int(x) for x in input().split()]
xy = []
for _ in range(m):
    tmp = [int(x)-1 for x in input().split()]
    xy.append(tmp)

box = {x: 1 for x in range(n)}
red = {x: False for x in range(n)}
red[0] = True

for x,y in xy:
    box[x] -= 1
    box[y] += 1
    if red[x]:
        red[y] = True
    if box[x] == 0:
        red[x] = False

print(len([1 for x in red.values() if x]))