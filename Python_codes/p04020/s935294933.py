n = int(input())
a = [int(input()) for i in range(n)]
ans = 0
ans += a[0]//2
a[0] %= 2
for i in range(1,n):
    if a[i-1] == 1 and a[i] > 0:
        ans += 1
        a[i] -= 1
    ans += a[i]//2
    a[i] %= 2
print(ans)