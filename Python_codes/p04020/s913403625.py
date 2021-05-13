n=int(input())
a=[int(input())  for i in range(n)]
ans=0
for i in range(n)[::-1]:
    if i<n-1:
        x=min(a[i+1],a[i])
        ans+=x
        a[i]-=x
    ans+=a[i]//2
    a[i]-=2*(a[i]//2)
print(ans) 