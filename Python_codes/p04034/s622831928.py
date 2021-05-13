N, M = map(int,input().split())
z = [list(map(int,input().split())) for i in range(M)]
box = [[1,1]]
for i in range(N-1):
  box.append([0,1])
for i in range(M):
  box[z[i][0]-1][1] -= 1
  box[z[i][1]-1][1] += 1
  if (box[z[i][0]-1][0] == 1):
    box[z[i][1]-1][0] = 1
  if (box[z[i][0]-1][1] == 0):
    box[z[i][0]-1][0] = 0
ans = 0
for i in range(N):
  if (box[i][0] != 0):
    ans += 1
print(ans)