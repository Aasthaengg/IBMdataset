n=int(input())
L=list(map(int,input().split()))
L.sort()
ans=0
for i in range(0,2*n,2):
  ans+=min(L[i], L[i+1])
print(ans)