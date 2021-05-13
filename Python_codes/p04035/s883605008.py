n,l = map(int,input().split())
a = [0]+list(map(int,input().split()))
ll = None
for i in range(1,n):
    if a[i]+a[i+1] >= l:
        ll = i
        break

if not ll:
    print('Impossible')
else:
    print('Possible')
    for i in range(1,ll):
        print(i)
    for i in range(n-1,ll,-1):
        print(i)
    print(ll)