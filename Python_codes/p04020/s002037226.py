n = int(input())
a = [int(input()) for i in range(n)]
ans = 0
flag = 0
for i in range(n):
    if flag and a[i] >= 1:
        ans += 1
        a[i] -= 1
    flag = a[i] % 2
    ans += a[i] // 2
print(ans)