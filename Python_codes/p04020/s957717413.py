n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())

ans=0
for i in range(n):
    pea=a[i]//2
    ans+=pea
    if i+1<n:
        if a[i]%2==1 and a[i+1]>=1:
            a[i+1]-=1
            ans+=1

print(ans)