N, M = map(int, input().split())
ans = [0] * N
ans[0] = 1
w = [1] * N

for i in range(M):
  x, y = map(int, input().split())
  w[x-1] -= 1
  w[y-1] += 1
  if ans[x-1] == 1:
    ans[y-1] = 1
    if w[x-1] == 0:
      ans[x-1] = 0
    
print(sum(ans))