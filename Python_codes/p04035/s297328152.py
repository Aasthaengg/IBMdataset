N,L=list(map(int, input().split()))
A=list(map(int, input().split()))
for i in range(N-1):
  if A[i]+A[i+1]>=L:
    print('Possible')
    k=i
    break
else:
  print('Impossible')
  exit()
ans=[0]*(N-1)
ans[k]=N-1
for i in range(k):
  ans[i]=i+1
for i in range(N-2-k):
  ans[N-i-2]=k+i+1
for i in range(N-1):
  print(ans[i])