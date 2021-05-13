n, l = map(int, input().split())
slst = [input() for _ in range(n)]
slst.sort()
ans = ""
for s in slst:
    ans += s
print(ans)