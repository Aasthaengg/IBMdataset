n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
for i in range(n - 1):
    if a[i] & 1 and a[i + 1] > 0:
        a[i] -= 1
        a[i + 1] -= 1
        ans += 1
for i in range(n):
    ans += a[i] // 2


print(ans)
