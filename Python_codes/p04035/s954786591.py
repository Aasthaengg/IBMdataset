n,l=map(int,input().split())
a=list(map(int,input().split()))
ok=False
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        ok=True
        idx=i
if ok:
    print("Possible")
    for i in range(1,idx+1):
        print(i)
    for i in reversed(range(idx+2,n)):
        print(i)
    print(idx+1)
else:
    print("Impossible")