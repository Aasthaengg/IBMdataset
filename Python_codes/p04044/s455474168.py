N, L = map(int, input().split())
S = [input() for _ in range(N)]
S.sort()
ans = ""
for s in S:
    ans += s
print(ans)
