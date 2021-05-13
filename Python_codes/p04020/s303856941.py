N = int(input())
tmp = 0
ans = 0
for _ in range(N):
    a = int(input())
    if a != 0:
        tmp += a
    else:
        ans += tmp // 2
        tmp = 0
ans += tmp // 2
print(ans)
