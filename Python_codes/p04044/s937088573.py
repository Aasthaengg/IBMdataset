N,L=list(map(int,input().split()))
S=[]
B=[]
for n in range(N):
  S.append(input())
  
B=sorted(S)
C=""
for n in range(N):
  C=C+(B[n])
  
print(C)