n, m = map(int, input().split())
l = [True if i == 0 else False for i in range(n)]
k = [1 for i in range(n)]
for i in range(m):
    xy = list(map(int, input().split()))
    if l[xy[0]-1]:
        if k[xy[0]-1] > 1:
            l[xy[1]-1] = True
        else:
            l[xy[1]-1] = True
            l[xy[0]-1] = False
    k[xy[0]-1] -= 1
    k[xy[1]-1] += 1
print(l.count(True))