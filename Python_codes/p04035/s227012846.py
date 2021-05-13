N,L = map(int,input().split())
A = list(map(int,input().split()))

last = 0
for i in range(N-1):
  if A[i] + A[i+1] >= L:
    last = i+1
    break
if last == 0:
  print('Impossible')
else:
  print('Possible')
  for i in range(1,last):
    print(i)
  for i in range(N-1,last-1,-1):
    print(i)
