n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
    if i > 0:
        if a[i-1] == 1 and a[i] > 0:
            ans += 1
            a[i] -= 1

    ans += a[i] // 2
    a[i] %= 2

print(ans)