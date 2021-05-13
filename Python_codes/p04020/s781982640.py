n=int(input())
a=[]
ans=0
for _ in range(n):
    a.append(int(input()))

for i in range(n-1):
    if a[i]==a[i+1]:
        ans+=a[i]
        a[i],a[i+1]=0,0
    elif a[i]>a[i+1]:
        if a[i]%2==0:
            ans+=a[i]//2
            a[i]=0
        else:
            ans+=(a[i]-1)//2
            a[i]=1
        if a[i]<a[i+1]:
            ans+=a[i]
            a[i+1]-=a[i]
            a[i]=0
    elif a[i]<a[i+1]:
        ans+=a[i]
        a[i+1]-=a[i]
        a[i]=0
if a[-1]%2==0:
    ans+=a[-1]//2
else:
    ans+=(a[-1]-1)//2

print(ans)