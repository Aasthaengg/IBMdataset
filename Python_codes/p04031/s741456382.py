n = int(input())
a = list(map(int, input().split()))

mn = min(a)
mx = max(a)

ans = 10000000
for i in range(mn, mx+1):
    p = 0
    for j in a:
        p += (j-i) * (j-i)
    if ans > p:
        ans = p
print(ans)
