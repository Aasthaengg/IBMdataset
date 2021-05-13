N,L=map(int,input().split())
A=list(map(int,input().split()))
if N==2:
  if sum(A)>=L:
    print('Possible')
    print(1)
  else:
    print('Impossible')
  exit(0)
lasti=-1
for i in range(N-1):
  if A[i]+A[i+1]>=L:
    lasti=i+1
    break
if lasti==-1:
  print('Impossible')
else:
  print('Possible')
  for i in range(1,lasti):
    print(i)
  for i in range(N-1,lasti-1,-1):
    print(i)