N, L = map(int, input().split())
S = []
for i in range(N):
  S.append(input())
S.sort()
ans = ""
for s in S:
  ans += s
print(ans)