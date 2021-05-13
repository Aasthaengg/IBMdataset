n = int(input())
a = [int(input()) for _ in range(n)]

ans = 0
for i in range(n - 1):
    pair1 = a[i] // 2
    a[i] -= pair1 * 2
    pair2 = min(a[i], a[i+1])
    ans += pair1 + pair2
    a[i+1] -= pair2

ans += a[-1] // 2
print(ans)
