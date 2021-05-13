from collections import deque
N, L = map(int, input().split())
c = list(map(int, input().split()))
for i in range(len(c)-1):
  if c[i] + c[i+1] >= L:
    pos = i + 1
    break
else:
  print("Impossible")
  exit()

print("Possible")
for i in range(1,pos):
  print(i)
for i in range(len(c) -1, pos, -1):
  print(i)
print(pos)