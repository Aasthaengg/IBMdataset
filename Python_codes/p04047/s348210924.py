N=int(input())
L=list(map(int,input().split()))
L=sorted(L)
ans=0
for l in L[0::2]:
  ans+=l
print(ans)