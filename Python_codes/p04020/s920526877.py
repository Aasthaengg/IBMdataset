R=[0]
L=list()
N=int(input())
for i in range(N):
  k=int(input())
  L.append(k)
  if k==0:
    R.append(len(L))
S=sum(L)
R.append(N)
for i in range(len(R)-1):
  if sum(L[R[i]:R[i+1]])%2==1:
    S=S-1
print(S//2)