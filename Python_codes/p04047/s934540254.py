input()
A=list(map(int,input().split()))
A.sort()
r = 0
for i in range(0,len(A),2):
  r+=A[i]
  
print(r)