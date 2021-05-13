n, l = map(int, input().split())
S = sorted([input() for _ in range(n)])

ans = ''
for s in S:
    ans += s
print(ans)