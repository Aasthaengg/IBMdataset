import sys

N, L = map(int, sys.stdin.readline().split())
S = []
for _ in range(N):
    S.append(sys.stdin.readline().strip())

S.sort()
ans = ""
for s_i in S:
    ans += s_i

print(ans)