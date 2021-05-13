N,M = map(int,input().split())
xy = [list(map(int,input().split())) for _ in range(M)]

ball_count = [1]*N
visited = [0]*N
visited[0] = 1

for x,y in xy:
  ball_count[x-1] -= 1
  ball_count[y-1] += 1
  if visited[x-1] == 1:
    visited[y-1] = 1
  if ball_count[x-1] == 0:
    visited[x-1] = 0

print(sum(visited))