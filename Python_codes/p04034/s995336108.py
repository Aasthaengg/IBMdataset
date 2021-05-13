n, m = list(map(int, input().split()))
cnt = [1] * n
has_red = [False] * n
has_red[0] = True
for i in range(m):
    a, b = list(map(int, input().split()))
    has_red[b - 1] = has_red[b - 1] or has_red[a - 1]
    if cnt[a - 1] == 1:
        has_red[a - 1] = False
    cnt[a - 1] -= 1
    cnt[b - 1] += 1
print(has_red.count(True))
