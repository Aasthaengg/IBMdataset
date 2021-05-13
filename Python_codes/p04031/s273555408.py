n=int(input())
a=list(map(int,input().split()))
m=int(round(sum(a)/n,0))
ans=0
for i in a:
  ans+=(i-m)**2
print(ans)