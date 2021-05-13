N, M = map(int, input().split())

Red = [0]*N
Red[0] = 1
Num = [1]*N

for i in range(M):
  In, Out = map(int, input().split())
  In -= 1
  Out -= 1
  Num[In] -= 1
  Num[Out] += 1
  if Red[In]:
    Red[Out] = 1
  if Num[In] == 0:
    Red[In] = 0

print(sum(Red))