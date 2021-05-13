n, m = (int(x) for x in input().split())
ab = []
for _ in range(m):
    a, b = (int(x) for x in input().split())
    ab.append([a-1, b-1])

box = [1]*n

red = [0]*n

red[0] = 1

for x,y in ab:
    if 0 < red[x]:
        red[y] = 1
    box[x] -= 1
    box[y] += 1

    if box[x] == 0:
        red[x] = 0
print(sum(red))