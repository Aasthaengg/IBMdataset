n = int(input())
ans = 0
a = [int(input()) for _ in range(n)]
for i in range(n-1):
    if a[i] >= 2:
        ans += a[i]//2
        a[i+1] += a[i] % 2
print(ans+a[-1]//2)
