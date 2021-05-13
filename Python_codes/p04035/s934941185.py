N,L=map(int, input().split())
A=list(map(int, input().split()))
x=0
for i in range(N-1):
  d=A[i]+A[i+1]
  if d>=L:
    x=1
    knot=i+1
    break
    
if x==0:
  print('Impossible')
  exit()

print('Possible')
for i in range(1,knot):
  print(i)
for i in range(N-1,knot-1,-1):
  print(i)