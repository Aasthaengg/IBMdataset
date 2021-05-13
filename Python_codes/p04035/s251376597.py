n,l=map(int, input().split())
*a,=map(int, input().split())
mx=0
ind=-1
for i in range(n-1):
    if mx<=a[i+1]+a[i]:
        ind=i
        mx=a[i+1]+a[i]
if mx>=l:
    print("Possible")
    for i in range(ind):
        print(i+1)
    for i in range(n-1,ind,-1):
        print(i)
else:
    print("Impossible")