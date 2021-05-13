n = int(input())
lst = list(map(int, input().split()))

M = max(lst)
m = min(lst)
ans = float("INF")

for i in range(m,M+1):
    num = 0
    for j in lst:
        num += (i-j)**2
    ans = min(ans, num)

print(ans)
