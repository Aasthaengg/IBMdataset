N,L=map(int,input().split())
S=[]
for i in range(0,N):
  S.append(input())
  
S.sort()

for i in range(0,N):
  print(S[i],end='')
print()