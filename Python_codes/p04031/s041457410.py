n=int(input())
a=list(map(int,input().split()))
a.sort()

l=a[0]
r=a[-1]

ans=float('inf')
for pin in range(l,r+1):
  cnt=0
  for i in range(n):
    cnt+=(a[i]-pin)**2
    
  ans=min(ans,cnt)
  
print(ans)