n=int(input())
a=[int(input()) for _ in range(n)]
ans=0
for i in range(n):
    ans+=a[i]//2
    a[i]=a[i]%2
    if i<n-1 and a[i]>0 and a[i+1]>0:
        a[i]=0
        a[i+1]-=1
        ans+=1
print(ans)
