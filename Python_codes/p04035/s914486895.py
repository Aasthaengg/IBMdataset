n,l=map(int, input().split())
a=list(map(int, input().split()))
ans=-1
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        ans=i+1
        break
if ans==-1:print('Impossible')
else:
    print('Possible')
    for i in range(1,ans):print(i)
    for i in range(n-1,i,-1):print(i)