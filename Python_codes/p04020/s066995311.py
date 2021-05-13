n = int(input())
a = [int(input()) for i in range(n)]

ans = 0
c = a[0]
for i in range(n - 1):
    b = c
    c = a[i + 1]
    use = b // 2 * 2
    ans += use // 2
    b -= use
    if b and c >= 1:
        ans += 1
        c -= 1
ans += c // 2

print(ans)
