N, A = map(int, input().split())
X = list(map(int, input().split()))
s = [{} for i in range(N+1)]
s[0][0] = 1

for i in range(N):
  cur = X[i]
  for j in range(N, 0, -1):
    for k, v in s[j-1].items():
      s[j][cur + k] = s[j].get(cur + k, 0) + v

ans = 0
for i in range(1, N+1):
  ans += s[i].get(i*A, 0)
print(ans)