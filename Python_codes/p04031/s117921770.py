n=int(input())
a=list(map(int,input().split()))
mi=min(a)
ma=max(a)
i=mi
ans=10**10
while i<=ma:
    x=sum((a[j]-i)**2 for j in range(n))
    ans=min(ans,x)
    i+=1
print(ans)

