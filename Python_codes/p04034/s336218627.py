N, M = map(int, input().split())
xy = []
for _ in range(M):
    xy.append(tuple(map(int, input().split())))

num = [1] * N
red = [False] * N
red[0] = True

for el in xy:
    x, y = el
    x, y = x - 1, y - 1
    if red[x]:
        red[y] = True
    num[x] -= 1
    if num[x] == 0:
        red[x] = False
    num[y] += 1
# print(num, red)
cnt = 0
for el in red:
    if el:
        cnt += 1
print(cnt)
