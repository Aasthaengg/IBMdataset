n,l= map(int,input().split())
a= list(map(int,input().split()))
rh=-1
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        rh=i
        break
else:
    print('Impossible')
    exit()
print('Possible')
if rh>0:
    for i in range(rh):print(i+1)
if rh+1<n:
    for i in range(n-1,rh+1,-1):print(i)
print(rh+1)
