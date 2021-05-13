N = int(input())
ans = 0
now = 0
for i in range(N):
    a = int(input())
    if a != 0:
        now += a
    else:
        ans += now // 2
        now = 0
ans += now // 2
print(ans)
