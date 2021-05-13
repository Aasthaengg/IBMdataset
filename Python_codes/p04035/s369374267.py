N,L=map(int,input().split())
A=[int(x) for x in input().split()]

psbl=False
ans=0
for i in range(1,N):
  if A[i-1]+A[i]>=L:
    psbl=True
    ans=i-1
    break
if psbl==False:
  print("Impossible")
else:
  print("Possible")
  for i in range(ans):
    print(i+1)
  for j in range(N-1-ans):
    print(N-j-1)