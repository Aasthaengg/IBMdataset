N = int(input())
A = [int(input()) for i in range(N)]

ans = 0
tmp = 0
for a in A:
    if a == 0:
        tmp = 0
    a += tmp
    ans += a // 2
    tmp = a % 2

print(ans)
