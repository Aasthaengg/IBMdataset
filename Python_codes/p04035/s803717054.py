K=10**10
import sys
N,L=map(int,input().split())
T=list(map(int,input().split()))
for i in range(N-1):
  if T[i]+T[i+1]>=L:
    K=i
    print("Possible")
    break
if K==10**10:
  print("Impossible")
  sys.exit()
K=K+1
R=list(range(1,K))
M=list(range(K+1,N))
M.reverse()
R.extend(M)
R.append(K)
for i in range(N-1):
  print(R[i])