n, m = map(int, input().split())
red = {1, }
l = [1 for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    l[x - 1] -= 1
    l[y - 1] += 1
    if x in red:
        red.add(y)
        if l[x - 1] == 0:
            red.discard(x)
print(len(red))
