n, m = [int(i) for i in input().split()]
data = [0] * n
cnt = [1] * n
data[0] = 1
for i in range(m):
    x, y = [int(i) for i in input().split()]
    if data[x-1] == 1: data[y-1] = 1
    if cnt[x-1] == 1: data[x-1] = 0
    cnt[x-1] -= 1
    cnt[y-1] += 1
print(data.count(1))