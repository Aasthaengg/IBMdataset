N, M = map(int, input().split())
num = [1] * N
possible = [False] * N
possible[0] = True

for i in range(M):
  x, y = map(int, input().split())
  x -= 1; y -= 1
  nx, ny = num[x], num[y]
  if possible[x]:
    possible[y] = True
    if nx == 1:
      possible[x] = False
  
  num[x] -= 1; num[y] += 1

print(sum(possible))