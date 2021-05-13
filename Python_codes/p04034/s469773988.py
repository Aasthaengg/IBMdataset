def solve():
  N, M = map(int, input().split())
  lis = [False]*N
  cnt = [1]*N
  lis[0] = True
  for i in range(M):
    x,y = map(int, input().split())
    x -= 1
    y -= 1
    if lis[x]==True:
      lis[y]=True
      if cnt[x]==1:
        lis[x]=False
    cnt[x] -= 1
    cnt[y] += 1
  ans = lis.count(True)
  return ans
print(solve())