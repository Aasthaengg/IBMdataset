# diff 693
n, m = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(m)]
# indに気を付ける
ans = 0

# judについて0:red 1:white
jud = [0] + [1] * (n - 1)
num = [1] * n

for i in xy:
    if num[i[0] - 1] >= 2 and jud[i[0] - 1] == 0:
        jud[i[1] - 1] = 0
        num[i[0] - 1] -= 1
        num[i[1] - 1] += 1
    elif num[i[0] - 1] < 2 and jud[i[0] - 1] == 0:
        jud[i[1] - 1] = 0
        jud[i[0] - 1] = 1
        num[i[0] - 1] -= 1
        num[i[1] - 1] += 1
    else:
        num[i[0] - 1] -= 1
        num[i[1] - 1] += 1

print(jud.count(0))