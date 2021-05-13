n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())
ans=0
for i in range(n):
    if i==0:
        ans+=a[i]//2
        a[i]=a[i]-(a[i]//2)*2
    else:
        if a[i-1]==0:
            ans+=a[i]//2
            a[i]=a[i]-(a[i]//2)*2
        else:
            if a[i]>=1:
                ans+=1
                a[i-1]-=1
                a[i]-=1
            ans+=a[i]//2
            a[i]=a[i]-(a[i]//2)*2
print(ans)
