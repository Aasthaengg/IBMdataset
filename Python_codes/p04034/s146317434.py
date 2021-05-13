N, M = map(int, input().split())
Z = [list(map(int,input().split())) for i in range(M)]
kosuu = [1 for _ in range(N)]
red = [False for _ in range(N)]
red[0] = True

for i in range(M):
  x = Z[i][0] - 1
  y = Z[i][1] - 1
  if (kosuu[x] != 0 and red[x] == True):
    red[y] = True
  if (kosuu[x] == 1 and red[x] == True):
    red[x] = False
  kosuu[x] -= 1
  kosuu[y] += 1

ans = 0
for i in range(N):
  if red[i] == True:
    ans+=1

print(ans)