# https://atcoder.jp/contests/agc002/tasks/agc002_b

n, m = map(int, input().split())

xy = []
for _ in range(m):
    x, y = map(int, input().split())
    xy.append((x - 1, y - 1))

box = [0] * n
box[0] = 1
num = [1] * n
for x, y in xy:
    if box[x]:
        box[y] |= 1
    num[x] -= 1
    num[y] += 1
    if not num[x]:
        box[x] = 0
ans = 0
for i in range(n):
    if box[i] and num[i]:
        ans += 1
print(ans)