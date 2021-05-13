import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
B = [1] * N
possible = {0}
for i in range(M):
  x,y = map(int,readline().split())
  x,y = x - 1,y - 1
  B[x] -= 1
  B[y] += 1
  if x in possible:
    possible.add(y)
  if x in possible and B[x] == 0:
    possible.remove(x)

print(len(possible))