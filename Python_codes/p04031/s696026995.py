n = int(input())
A = list(map(int, input().split()))

ans = float("INF")
for i in range(min(A), max(A)+1):
    tmp = 0
    for a in A:
        tmp += (i - a) ** 2
    ans = min(tmp, ans)

print(ans)