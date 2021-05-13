n=int(input())
a=[int(input()) for i in range(n)]
a+=[0]

ans=0
for i in range(n):
    pair=a[i]//2
    ans+=pair
    a[i]-=2*pair
    if a[i]>0 and a[i+1]>0:
        ans+=1
        a[i]-=1
        a[i+1]-=1

print(ans)

