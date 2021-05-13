n = int(input())
A = [int(input()) for _ in range(n)]
ans = 0
tmp = 0
for a in A:
    if tmp > a:
        ans += a
        tmp = 0
        continue
    else:
        ans += tmp
        a -= tmp
        ans += a // 2
        tmp = a - (a // 2) * 2
print(ans)