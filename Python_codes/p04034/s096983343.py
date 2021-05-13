n, m = map(int, input().split())

a = [[1, False] for _ in range(n+1)]
a[1] = [1, True]

for _ in range(m):
    x, y = map(int, input().split())
    if a[x][1]:
        a[y][1] = True
    
    a[x][0] -= 1
    if a[x][0] == 0:
        a[x][1] = False
    a[y][0] += 1

print(sum(x[1] for x in a))